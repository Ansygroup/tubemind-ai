"""Trend Hunter Agent - Finds trending YouTube topics"""
import os, httpx, json
import anthropic

class TrendHunter:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    async def find_trending_topic(self, niche: str, language: str = "ar") -> str:
        """Use Claude to identify trending topics for the niche"""
        prompt = f"""
        You are a YouTube trend expert. Find the most trending topic right now for:
        - Niche: {niche}
        - Language: {language}
        - Target: YouTube viewers

        Return ONLY a single topic title (max 10 words), no explanation.
        Make it viral and engaging.
        """
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=100,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()
