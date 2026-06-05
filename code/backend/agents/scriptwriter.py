"""Scriptwriter Agent - Creates video scripts using Claude"""
import os, json
import anthropic

class Scriptwriter:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    async def write_script(self, topic: str, video_type: str, channel: dict, language: str) -> dict:
        """Generate full video script"""
        durations = {"long_form": "10-15 minutes", "short": "60 seconds", "ugc": "3-5 minutes"}
        duration = durations.get(video_type, "10 minutes")
        brand_voice = channel.get("brand_voice", "educational, engaging, friendly")

        prompt = f"""
        Write a complete YouTube video script about: "{topic}"
        - Duration: {duration}
        - Language: {language}
        - Brand Voice: {brand_voice}
        - Channel Niche: {channel.get("niche", "general")}

        Return JSON with:
        {{
            "full_script": "complete narration script",
            "voiceover": "clean text for TTS (no stage directions)",
            "description": "YouTube description (2-3 paragraphs)",
            "hooks": ["hook1", "hook2", "hook3"]
        }}
        """
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4000,
            messages=[{"role": "user", "content": prompt}]
        )
        text = response.content[0].text.strip()
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        return json.loads(text)
