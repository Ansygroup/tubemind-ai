"""Background Task Scheduler"""
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import os, logging

logger = logging.getLogger(__name__)
scheduler = AsyncIOScheduler()

def start_scheduler():
    """Start background scheduler"""
    # Daily video generation at 6 AM UTC
    scheduler.add_job(
        daily_video_task,
        CronTrigger(hour=6, minute=0),
        id="daily_video",
        replace_existing=True
    )
    # Analytics update every 6 hours
    scheduler.add_job(
        update_analytics_task,
        CronTrigger(hour="*/6"),
        id="analytics_update",
        replace_existing=True
    )
    scheduler.start()
    logger.info("✅ Scheduler started")

async def daily_video_task():
    """Auto-generate daily videos for all active channels"""
    try:
        from supabase import create_client
        db = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
        channels = db.table("channels").select("*").eq("auto_generate", True).execute().data
        for channel in channels:
            db.table("jobs").insert({
                "channel_id": channel["id"],
                "type": "video_generation",
                "status": "queued",
                "metadata": {"channel_id": channel["id"], "language": channel.get("language", "ar")}
            }).execute()
        logger.info(f"✅ Queued {len(channels)} daily video jobs")
    except Exception as e:
        logger.error(f"❌ Daily task error: {e}")

async def update_analytics_task():
    """Update analytics from YouTube API"""
    logger.info("📊 Analytics update triggered")
