#!/usr/bin/env python3
"""TubeMind AI - FastAPI Backend Server"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import os
from routers import channels, videos, agents, analytics, auth
from services.scheduler import start_scheduler

app = FastAPI(
    title="TubeMind AI",
    description="Automated YouTube Channel Management Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(channels.router, prefix="/channels", tags=["channels"])
app.include_router(videos.router, prefix="/videos", tags=["videos"])
app.include_router(agents.router, prefix="/agents", tags=["agents"])
app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])

@app.on_event("startup")
async def startup_event():
    start_scheduler()

@app.get("/")
async def root():
    return {"status": "ok", "service": "TubeMind AI", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
