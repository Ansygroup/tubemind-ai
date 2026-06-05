"""SEO Optimizer Agent - Optimizes YouTube metadata"""
import os, json
import anthropic

class SEOOptimizer:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    async def optimize(self, topic: str, description: str, niche: str, language: str) -> dict:
        """Generate SEO-optimized title, description, and tags"""
        prompt = f"""
        Create SEO-optimized YouTube metadata for:
        - Topic: {topic}
        - Niche: {niche}
        - Language: {language}

        Return JSON:
        {{
            "title": "Clickbait but honest title (max 60 chars)",
            "description": "Full description with keywords (500-1000 chars)",
            "tags": ["tag1", "tag2", ... up to 15 tags]
        }}
        """
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        text = response.content[0].text.strip()
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        return json.loads(text)
