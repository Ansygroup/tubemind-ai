"""Analytics Routes"""
from fastapi import APIRouter, HTTPException
from typing import Optional
import os
from supabase import create_client

router = APIRouter()

def get_db():
    return create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

@router.get("/dashboard")
async def get_dashboard(channel_id: Optional[str] = None):
    """Get dashboard stats"""
    try:
        db = get_db()
        channels_count = len(db.table("channels").select("id").execute().data)
        videos_count = len(db.table("videos").select("id").execute().data)
        jobs_count = len(db.table("jobs").select("id").execute().data)
        return {
            "channels": channels_count,
            "videos": videos_count,
            "jobs": jobs_count,
            "status": "operational"
        }
    except Exception as e:
        return {"channels": 0, "videos": 0, "jobs": 0, "error": str(e)}

@router.get("/channels/{channel_id}")
async def get_channel_analytics(channel_id: str):
    """Get analytics for a channel"""
    return {"channel_id": channel_id, "views": 0, "subscribers": 0, "videos": 0}
