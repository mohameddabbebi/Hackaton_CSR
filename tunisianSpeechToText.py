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
from google.colab import files
import os

# Upload fichier audio MP3 ou autre
print("Upload your audio file (MP3 or WAV):")
uploaded = files.upload()

input_audio = list(uploaded.keys())[0]

# Convertir en WAV mono 16kHz obligatoire pour Vosk
wav_file = "converted1.wav"
convert_command = f'ffmpeg -y -i "{input_audio}" -ar 16000 -ac 1 -f wav "{wav_file}"'
os.system(convert_command)
# Charger modèle Vosk
model_dir = "/content/vosk-model/vosk-model"
model = Model(model_dir)

# Ouvrir le fichier WAV converti
wf = wave.open(wav_file, "rb")

# Vérifier format audio
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    raise ValueError("Le fichier audio doit être WAV mono PCM 16 bits.")

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
