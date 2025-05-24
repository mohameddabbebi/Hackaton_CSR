import requests

url = "https://api.elevenlabs.io/v1/text-to-speech/TxGEqnHWrfWFTfGW9XjX"  # ID de voix par défaut

headers = {
    "xi-api-key": "xxxxxxx",
    "Content-Type": "application/json"
}

data = {
    "text": "بالنسبة للرصيد، تنجم تعرفو ببعث *122# في مكالمة، أو عن طريق تطبيق MyTT. إذا الرصيد ما طلعلكش، نجّم تعمل إعادة تشغيل للتليفون ونجربو مرّة أخرى. إذا بقى نفس المشكل، نجم نعملو شكاية تقنيّة ونتابعوها معاك.",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
}

response = requests.post(url, json=data, headers=headers)
with open("tunisian_tts.mp3", "wb") as f:
    f.write(response.content)




#code modulaire:

import requests

def generate_tts(text, output_file="tunisian_tts.mp3", api_key="YOUR_API_KEY"):
    """
    Génère un fichier audio MP3 à partir de texte en arabe tunisien
    via l'API ElevenLabs.

    :param text: Texte à lire
    :param output_file: Nom du fichier MP3 de sortie
    :param api_key: Clé API ElevenLabs
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech/TxGEqnHWrfWFTfGW9XjX"  # Voix par défaut

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"✅ Audio enregistré dans : {output_file}")
    else:
        print(f"❌ Erreur {response.status_code} : {response.text}")




