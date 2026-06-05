"""YouTube OAuth Authentication"""
from fastapi import APIRouter, HTTPException
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
import os, json

router = APIRouter()

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/youtube.readonly",
]

@router.get("/youtube")
async def youtube_auth(channel_id: str):
    """Start YouTube OAuth flow"""
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
                "redirect_uris": [f"{os.getenv('BACKEND_URL', 'http://localhost:8000')}/auth/youtube/callback"],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token"
            }
        },
        scopes=SCOPES,
        redirect_uri=f"{os.getenv('BACKEND_URL', 'http://localhost:8000')}/auth/youtube/callback"
    )
    auth_url, state = flow.authorization_url(access_type="offline", state=channel_id)
    return {"auth_url": auth_url}

@router.get("/youtube/callback")
async def youtube_callback(code: str, state: str):
    """Handle YouTube OAuth callback"""
    return {"status": "success", "channel_id": state, "message": "Channel connected!"}
