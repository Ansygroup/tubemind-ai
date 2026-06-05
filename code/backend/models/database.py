"""Database Models"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ChannelModel(BaseModel):
    id: Optional[str] = None
    name: str
    youtube_channel_id: str
    niche: str
    language: str = "ar"
    brand_voice: Optional[str] = None
    auto_generate: bool = False
    created_at: Optional[datetime] = None

class VideoModel(BaseModel):
    id: Optional[str] = None
    channel_id: str
    title: str
    description: Optional[str] = None
    script: Optional[str] = None
    audio_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    video_url: Optional[str] = None
    youtube_video_id: Optional[str] = None
    status: str = "draft"
    video_type: str = "long_form"
    created_at: Optional[datetime] = None

class JobModel(BaseModel):
    id: Optional[str] = None
    channel_id: str
    type: str
    status: str = "queued"
    metadata: Optional[dict] = {}
    created_at: Optional[datetime] = None
