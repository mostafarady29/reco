# Azure SQL Database Firewall Configuration for Railway

## Current Issue

✅ **Railway deployment is working** - Server starts successfully  
✅ **PORT configuration fixed** - Root endpoint responds correctly  
❌ **Database connection failing** - Error: `"Database connection failed"`

## Root Cause

Azure SQL Database has a firewall that blocks connections by default. Railway's servers need to be whitelisted.

## Solution: Configure Azure SQL Firewall

### Option 1: Allow Azure Services (Recommended for Testing)

1. Go to **Azure Portal** (https://portal.azure.com)
2. Navigate to your SQL Database: **insight123**
3. Click on **Set server firewall** or **Networking**
4. Under **Firewall rules**, toggle **Allow Azure services and resources to access this server** to **ON**
5. Click **Save**

This allows all Azure and cloud services (including Railway) to connect.

---

### Option 2: Add Railway IP Ranges (More Secure)

Railway uses dynamic IPs, so you need to allow Railway's IP ranges:

1. Go to **Azure Portal** → **insight123** → **Networking**
2. Click **+ Add client IP** or **+ Add firewall rule**
3. Add these Railway IP ranges:

```
Name: Railway-US-West
Start IP: 35.184.0.0
End IP: 35.184.255.255

Name: Railway-US-East
Start IP: 34.23.0.0
End IP: 34.23.255.255
```

**Note:** Railway's exact IP ranges may vary. For the most secure setup, you can:
- Enable Azure Services temporarily
- Check Railway deployment logs for the actual IP being used
- Add that specific IP to the firewall

---

### Option 3: Allow All IPs (NOT Recommended for Production)

**⚠️ Only use for testing/debugging:**

1. Azure Portal → **insight123** → **Networking**
2. Add firewall rule:
   - Name: `AllowAll-TemporaryTesting`
   - Start IP: `0.0.0.0`
   - End IP: `255.255.255.255`
3. **Remember to remove this rule after testing!**

---

## Verification Steps

After updating the firewall:

1. **Wait 1-2 minutes** for changes to propagate
2. **Test the health endpoint:**
   ```bash
   curl https://reco-production-0b1e.up.railway.app/api/health
   ```
   
   Expected successful response:
   ```json
   {
     "status": "healthy",
     "database": "connected",
     "timestamp": "2025-12-15T..."
   }
   ```

3. **Test recommendations:**
   ```bash
   curl "https://reco-production-0b1e.up.railway.app/api/recommend?user_id=1&top_n=5"
   ```

4. **Or run the test script:**
   ```bash
   python test_deployment.py
   ```

---

## Current Working Endpoints

✅ **Root:** https://reco-production-0b1e.up.railway.app/  
Response:
```json
{
  "message": "Research Paper Recommender API - Optimized",
  "version": "2.0.0",
  "endpoints": {...}
}
```

⚠️ **Health:** https://reco-production-0b1e.up.railway.app/api/health  
Current: `{"detail":"Database connection failed"}`  
After fix: Should show `{"status":"healthy","database":"connected"}`

⚠️ **Recommendations:** https://reco-production-0b1e.up.railway.app/api/recommend  
Current: 500 error  
After fix: Should return recommendation data

---

## Summary

**Problem:** Azure SQL firewall blocking Railway's IP addresses  
**Solution:** Enable "Allow Azure services" or add Railway IP ranges  
**Expected Result:** All endpoints return 200 OK with proper data

Once you update the Azure SQL firewall settings, the deployment will be fully functional! 🎉
