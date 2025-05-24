!wget -q https://alphacephei.com/vosk/models/vosk-model-small-fr-0.22.zip

# Décompresser
!unzip -q vosk-model-small-fr-0.22.zip


import os
import wave
import json
from vosk import Model, KaldiRecognizer

def convert_mp3_to_wav(mp3_path: str, wav_path: str = "converted.wav") -> str:
    """Convertit un fichier mp3 en wav compatible Vosk"""
    os.system(f"ffmpeg -i \"{mp3_path}\" -ar 16000 -ac 1 -acodec pcm_s16le {wav_path}")
    return wav_path

def transcribe_audio(wav_path: str, model_path: str = "vosk-model-small-fr-0.22") -> str:
    """Transcrit un fichier WAV en texte avec Vosk"""
    wf = wave.open(wav_path, "rb")
    model = Model(model_path)
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
    return result_text.strip()


# 1. Upload du fichier MP3
from google.colab import files
uploaded = files.upload()
mp3_file = list(uploaded.keys())[0]

# 2. Importer le module (dans le même fichier ou copier le code ci-dessus)
from speech_to_text import convert_mp3_to_wav, transcribe_audio

# 3. Conversion
wav_file = convert_mp3_to_wav(mp3_file)

# 4. Transcription
texte = transcribe_audio(wav_file)

# 5. Affichage
print("✅ Texte reconnu :", texte)
