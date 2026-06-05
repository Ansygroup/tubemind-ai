"""Publisher Agent - Uploads videos to YouTube"""
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

class Publisher:
    def __init__(self, credentials: dict):
        creds = Credentials(
            token=credentials.get("access_token"),
            refresh_token=credentials.get("refresh_token"),
            client_id=os.getenv("GOOGLE_CLIENT_ID"),
            client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
            token_uri="https://oauth2.googleapis.com/token"
        )
        self.youtube = build("youtube", "v3", credentials=creds)

    async def upload_video(self, video_path: str, metadata: dict) -> str:
        """Upload video to YouTube"""
        body = {
            "snippet": {
                "title": metadata["title"][:100],
                "description": metadata["description"],
                "tags": metadata.get("tags", [])[:500],
                "categoryId": "22"
            },
            "status": {
                "privacyStatus": metadata.get("privacy", "public"),
                "selfDeclaredMadeForKids": False,
                "containsSyntheticMedia": True
            }
        }
        media = MediaFileUpload(video_path, chunksize=-1, resumable=True, mimetype="video/mp4")
        request = self.youtube.videos().insert(part="snippet,status", body=body, media_body=media)
        response = request.execute()
        return response.get("id", "")
