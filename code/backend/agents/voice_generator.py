"""Voice Generator Agent - Creates AI voiceover using HF Space"""
import os, httpx, json

class VoiceGenerator:
    def __init__(self):
        self.hf_space_url = os.getenv("HF_SPACE_VOICE", "")
        self.hf_token = os.getenv("HF_TOKEN", "")

    async def generate(self, text: str, language: str = "ar") -> str:
        """Generate voiceover audio"""
        if not self.hf_space_url:
            return "https://placeholder-audio-url.com/audio.wav"
        try:
            async with httpx.AsyncClient(timeout=120) as client:
                response = await client.post(
                    f"{self.hf_space_url}/api/predict",
                    json={"data": [text, language, "default"]},
                    headers={"Authorization": f"Bearer {self.hf_token}"}
                )
                result = response.json()
                return result.get("data", [""])[0] or "placeholder_audio_url"
        except Exception as e:
            print(f"Voice generation error: {e}")
            return "placeholder_audio_url"
