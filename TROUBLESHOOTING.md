# Railway Deployment Troubleshooting

## Current Status

The Railway deployment logs show:
- ✅ Database pool initialized
- ✅ API started - Environment: production  
- ✅ Application startup complete
- ⚠️ Uvicorn running on http://0.0.0.0:**8000**

## Issue

The server is binding to port 8000 instead of using Railway's PORT environment variable.

## Why This Happens

Railway expects the application to bind to the port specified in the `PORT` environment variable, not a hardcoded port. The logs show "Uvicorn running on http://0.0.0.0:8000" which means the PORT variable might not be set or being read correctly.

## Verification Steps

1. **Check Railway Environment Variables:**
   - Go to Railway Dashboard → reco service → Variables
   - Verify that Railway automatically sets the `PORT` variable (it should)
   - The PORT is typically a random high port like 3000, 8000, etc.

2. **Check Dockerfile CMD:**
   The Dockerfile uses: `${PORT:-8000}` which means:
   - If PORT is set, use it
   - If PORT is not set, default to 8000
   
   Since it's showing 8000, it might be using the default.

3. **Test if Railway is assigning a different port:**
   Railway automatically assigns a PORT and expects your app to use it.

## Possible Solutions

### Solution 1: Check Railway Settings
The issue might be that Railway is assigning a PORT but the app is showing 8000 in logs (which could be correct if Railway assigned 8000).

Try accessing the health endpoint through Railway's public domain to see if it's actually working.

### Solution 2: Verify railway.json
Check if `railway.json` has any port configuration that might conflict.

### Solution 3: Check Railway Service Settings
In Railway Dashboard:
- Settings → Deploy → Check if there's a custom start command override
- Settings → Networking → Verify the service has a public domain assigned

## Quick Test

The 502 errors could mean:
1. Railway hasn't fully deployed yet (wait 1-2 minutes)
2. Railway's networking hasn't connected yet
3. The health check is failing

Try accessing the URL in your browser:
- https://reco-production-6919.up.railway.app/
- https://reco-production-6919.up.railway.app/api/health

If you see JSON responses, the deployment is working!
