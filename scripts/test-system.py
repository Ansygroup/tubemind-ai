#!/usr/bin/env python3
"""TubeMind AI - System Health Check"""
import os, sys, requests

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def check(name, fn):
    try:
        result = fn()
        print(f"✅ {name}: {result}")
        return True
    except Exception as e:
        print(f"❌ {name}: {e}")
        return False

print("🔍 TubeMind AI System Health Check")
print("=" * 40)

results = [
    check("Backend Health", lambda: requests.get(f"{BACKEND_URL}/health", timeout=5).json()["status"]),
    check("Channels API", lambda: f"{len(requests.get(f'{BACKEND_URL}/channels/', timeout=5).json().get('channels', []))} channels"),
    check("Agents API", lambda: f"{len(requests.get(f'{BACKEND_URL}/agents/', timeout=5).json().get('agents', []))} agents"),
]

print("=" * 40)
passed = sum(results)
print(f"Result: {passed}/{len(results)} checks passed")
sys.exit(0 if passed == len(results) else 1)
