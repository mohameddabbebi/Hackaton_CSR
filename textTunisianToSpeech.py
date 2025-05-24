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
