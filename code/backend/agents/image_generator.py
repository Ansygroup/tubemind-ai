"""Image Generator Agent - Creates thumbnails using Fal.ai / Flux"""
import os, httpx

class ImageGenerator:
    def __init__(self):
        self.fal_key = os.getenv("FAL_KEY", "")

    async def generate_thumbnail(self, topic: str, niche: str) -> str:
        """Generate YouTube thumbnail"""
        if not self.fal_key:
            return "https://via.placeholder.com/1280x720"
        try:
            import fal_client
            prompt = f"YouTube thumbnail for: {topic}, {niche} channel, vibrant colors, eye-catching, professional, 16:9"
            result = await fal_client.run_async(
                "fal-ai/flux/schnell",
                arguments={
                    "prompt": prompt,
                    "image_size": "landscape_16_9",
                    "num_images": 1
                }
            )
            return result["images"][0]["url"]
        except Exception as e:
            print(f"Image generation error: {e}")
            return "https://via.placeholder.com/1280x720"
