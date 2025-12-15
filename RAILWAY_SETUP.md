# Railway Deployment Setup Guide

## Step 1: Set Environment Variables in Railway

Go to your Railway project dashboard and add these environment variables:

### Database Configuration
```
DB_NAME=Insight
DB_USER=amasoud
DB_PASSWORD=Ahmed@Masoud
DB_HOST=insight123.database.windows.net
DB_PORT=1433
DB_DRIVER=ODBC Driver 18 for SQL Server
```

### API Configuration
```
API_TITLE=Research Paper Recommender API
API_VERSION=2.0.0
ENVIRONMENT=production
```

### CORS Configuration
```
ALLOWED_ORIGINS=https://front-end1-zeta.vercel.app,https://backend-production-139d.up.railway.app
```

### Performance Settings
```
CONNECTION_POOL_SIZE=10
CACHE_TTL=3600
REQUIRE_DB=True
```

## Step 2: How to Add Environment Variables in Railway

1. Go to https://railway.app
2. Select your `reco` service
3. Click on the **Variables** tab
4. Click **+ New Variable**
5. Add each variable one by one
6. After adding all variables, Railway will automatically redeploy

## Step 3: Verify Deployment

After Railway redeploys:

1. Check the **Logs** tab for any errors
2. Test the health endpoint: `https://your-railway-url.railway.app/api/health`
3. Test the recommendation endpoint: `https://your-railway-url.railway.app/api/recommend?user_id=1`

## Troubleshooting

### If you see "Database connection failed":
- Verify Azure SQL firewall allows Railway IPs
- Check that the database credentials are correct
- Ensure the database is running

### If you see 502 errors:
- Check the Deploy Logs for Python errors
- Verify all environment variables are set correctly
- Check that the PORT variable is available (Railway sets this automatically)

## Current Status

✅ Fixed logging configuration  
✅ Fixed Procfile module reference  
✅ Fixed Dockerfile PORT handling  
🔧 Need to set environment variables in Railway dashboard
