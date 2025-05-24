!wget -q https://alphacephei.com/vosk/models/vosk-model-small-fr-0.22.zip

# Décompresser
!unzip -q vosk-model-small-fr-0.22.zip


from google.colab import files

uploaded = files.upload()  # Choisis ton .mp3 ici
import os

mp3_file = list(uploaded.keys())[0]
wav_file = "converted.wav"

# Convertir le fichier en WAV PCM 16kHz mono
os.system(f"ffmpeg -i \"{mp3_file}\" -ar 16000 -ac 1 -acodec pcm_s16le {wav_file}")

from vosk import Model, KaldiRecognizer
import wave
import json

model = Model("/content/vosk-model-small-fr-0.22")  # télécharger depuis https://alphacephei.com/vosk/models

wf = wave.open("converted.wav", "rb")
rec = KaldiRecognizer(model, wf.getframerate())

result_text = ""
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())
        result_text += " " + res.get("text", "")
res = json.loads(rec.FinalResult())
result_text += " " + res.get("text", "")

print("Texte reconnu :", result_text.strip())
