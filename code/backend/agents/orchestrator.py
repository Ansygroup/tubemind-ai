"""Video Production Orchestrator - Coordinates all AI agents"""
import os, asyncio
from supabase import create_client
from agents.trend_hunter import TrendHunter
from agents.scriptwriter import Scriptwriter
from agents.voice_generator import VoiceGenerator
from agents.image_generator import ImageGenerator
from agents.seo_optimizer import SEOOptimizer
from agents.publisher import Publisher

class VideoOrchestrator:
    def __init__(self):
        self.db = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

    def _update_job(self, job_id, status, metadata=None):
        update = {"status": status}
        if metadata:
            update["metadata"] = metadata
        self.db.table("jobs").update(update).eq("id", job_id).execute()

    async def run(self, job_id: str, params: dict):
        try:
            channel_id = params["channel_id"]
            video_type = params.get("video_type", "long_form")
            topic = params.get("topic")
            language = params.get("language", "ar")

            # Get channel info
            channel = self.db.table("channels").select("*").eq("id", channel_id).single().execute().data

            # Step 1: Find trending topic
            self._update_job(job_id, "finding_trend")
            if not topic:
                hunter = TrendHunter()
                topic = await hunter.find_trending_topic(channel["niche"], language)

            # Step 2: Write script
            self._update_job(job_id, "writing_script")
            writer = Scriptwriter()
            script = await writer.write_script(topic, video_type, channel, language)

            # Step 3: Generate voiceover
            self._update_job(job_id, "generating_voice")
            voice_gen = VoiceGenerator()
            audio_url = await voice_gen.generate(script["voiceover"], language)

            # Step 4: Generate visuals
            self._update_job(job_id, "generating_visuals")
            img_gen = ImageGenerator()
            thumbnail_url = await img_gen.generate_thumbnail(topic, channel["niche"])

            # Step 5: SEO optimization
            self._update_job(job_id, "optimizing_seo")
            seo = SEOOptimizer()
            seo_data = await seo.optimize(topic, script["description"], channel["niche"], language)

            # Step 6: Save video record
            video_record = {
                "channel_id": channel_id,
                "title": seo_data["title"],
                "description": seo_data["description"],
                "tags": seo_data["tags"],
                "script": script["full_script"],
                "audio_url": audio_url,
                "thumbnail_url": thumbnail_url,
                "status": "ready_to_publish",
                "video_type": video_type,
                "job_id": job_id
            }
            result = self.db.table("videos").insert(video_record).execute()
            video_id = result.data[0]["id"]

            self._update_job(job_id, "completed", {"video_id": video_id})
            print(f"✅ Video pipeline completed: {video_id}")

        except Exception as e:
            self._update_job(job_id, "failed", {"error": str(e)})
            print(f"❌ Pipeline failed: {e}")
