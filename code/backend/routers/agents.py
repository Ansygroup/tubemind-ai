"""Agent Control Routes"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class AgentTask(BaseModel):
    agent_name: str
    channel_id: str
    params: Optional[dict] = {}

@router.get("/")
async def list_agents():
    """List all available agents"""
    agents = [
        {"name": "trend_hunter", "description": "Finds trending topics", "status": "ready"},
        {"name": "scriptwriter", "description": "Writes video scripts", "status": "ready"},
        {"name": "voice_generator", "description": "Generates AI voiceover", "status": "ready"},
        {"name": "image_generator", "description": "Creates thumbnail & visuals", "status": "ready"},
        {"name": "video_editor", "description": "Assembles final video", "status": "ready"},
        {"name": "seo_optimizer", "description": "Optimizes title, desc, tags", "status": "ready"},
        {"name": "publisher", "description": "Uploads to YouTube", "status": "ready"},
        {"name": "analytics", "description": "Tracks performance", "status": "ready"},
        {"name": "comment_manager", "description": "Manages comments", "status": "ready"},
        {"name": "scheduler", "description": "Plans content calendar", "status": "ready"},
        {"name": "memory", "description": "Channel memory & learning", "status": "ready"},
    ]
    return {"agents": agents}

@router.post("/run")
async def run_agent(task: AgentTask):
    """Run a specific agent"""
    return {"success": True, "agent": task.agent_name, "status": "started"}
