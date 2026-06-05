"""Channel Management Routes"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import os
from supabase import create_client

router = APIRouter()

def get_db():
    return create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

class Channel(BaseModel):
    name: str
    youtube_channel_id: str
    niche: str
    language: str = "ar"
    target_audience: Optional[str] = None
    brand_voice: Optional[str] = None

@router.get("/")
async def list_channels():
    """Get all channels"""
    try:
        db = get_db()
        result = db.table("channels").select("*").execute()
        return {"channels": result.data}
    except Exception as e:
        return {"channels": [], "error": str(e)}

@router.post("/")
async def create_channel(channel: Channel):
    """Create new channel"""
    try:
        db = get_db()
        result = db.table("channels").insert(channel.dict()).execute()
        return {"success": True, "channel": result.data[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{channel_id}")
async def get_channel(channel_id: str):
    """Get channel details"""
    try:
        db = get_db()
        result = db.table("channels").select("*").eq("id", channel_id).single().execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=404, detail="Channel not found")

@router.delete("/{channel_id}")
async def delete_channel(channel_id: str):
    """Delete channel"""
    try:
        db = get_db()
        db.table("channels").delete().eq("id", channel_id).execute()
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
