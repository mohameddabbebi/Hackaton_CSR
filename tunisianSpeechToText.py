from vosk import Model, KaldiRecognizer
import wave
import json

# Chemin vers le modèle extrait
model_dir = "C:\\Users\\ramib\\OneDrive\\Bureau\\Hackaton Telecom\\vosk-model"  # vérifie le nom exact dans dir_for_zip_extract

# Chemin vers ton fichier audio mono PCM wav
audio_file = "C:\\Users\\ramib\\OneDrive\\Bureau\\Hackaton Telecom\\enregistrement.wav"  # upload ton fichier via l’interface Colab ou modifie ce chemin

# Charger le modèle
model = Model(model_dir)

# Ouvrir le fichier audio
with wave.open(audio_file, "rb") as wf:
    # Vérifier le format audio
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        raise ValueError("Audio file must be WAV format mono PCM.")
    
    rec = KaldiRecognizer(model, wf.getframerate())
    
    # Lire les frames audio
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)
    
    # Récupérer le résultat final
    res = rec.FinalResult()
    transcript = json.loads(res).get("text", "")
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(transcript)

