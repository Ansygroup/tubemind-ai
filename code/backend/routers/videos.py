"""Video Management Routes"""
from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional
import os
from supabase import create_client

router = APIRouter()

def get_db():
    return create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

class VideoRequest(BaseModel):
    channel_id: str
    topic: Optional[str] = None
    video_type: str = "long_form"  # long_form, short, ugc
    language: str = "ar"

@router.get("/")
async def list_videos(channel_id: Optional[str] = None):
    """Get all videos"""
    try:
        db = get_db()
        query = db.table("videos").select("*")
        if channel_id:
            query = query.eq("channel_id", channel_id)
        result = query.order("created_at", desc=True).execute()
        return {"videos": result.data}
    except Exception as e:
        return {"videos": [], "error": str(e)}

@router.post("/generate")
async def generate_video(request: VideoRequest, background_tasks: BackgroundTasks):
    """Start video generation pipeline"""
    try:
        db = get_db()
        job = db.table("jobs").insert({
            "channel_id": request.channel_id,
            "type": "video_generation",
            "status": "queued",
            "metadata": request.dict()
        }).execute()
        job_id = job.data[0]["id"]
        background_tasks.add_task(run_video_pipeline, job_id, request.dict())
        return {"success": True, "job_id": job_id, "status": "queued"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def run_video_pipeline(job_id: str, params: dict):
    """Run full video generation pipeline"""
    from agents.orchestrator import VideoOrchestrator
    orchestrator = VideoOrchestrator()
    await orchestrator.run(job_id, params)

@router.get("/jobs/{job_id}")
async def get_job_status(job_id: str):
    """Get job status"""
    try:
        db = get_db()
        result = db.table("jobs").select("*").eq("id", job_id).single().execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=404, detail="Job not found")
