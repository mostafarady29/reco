# How to Get Railway's IP Address for Azure SQL Firewall

## Quick Answer: Use the Debug Endpoint

I've added a debug endpoint to your API. After Railway redeploys (wait 1-2 minutes), visit:

**https://reco-production-0b1e.up.railway.app/debug/ip**

This will show Railway's IP address and deployment information.

---

## Better Solution: Enable Azure Services (Recommended)

Instead of whitelisting specific IPs, it's much easier to enable Azure services:

### Steps:
1. Go to **Azure Portal**: https://portal.azure.com
2. Navigate to **SQL Server** → **insight123** (your server, not the database)
3. Click **Networking** (in the left sidebar under Security)
4. Under **Firewall rules**, find the option:
   - **"Allow Azure services and resources to access this server"**
5. Toggle it to **ON**
6. Click **Save**

**Why this is better:**
- ✅ Works immediately
- ✅ No need to track Railway's changing IPs
- ✅ Railway can connect from any of its servers
- ✅ Still secure (only authenticated connections work)

---

## Alternative: Find IP from Error Logs

Sometimes Azure SQL error messages include the blocked IP address:

1. Go to **Azure Portal** → **SQL Database** → **insight123**
2. Click **Query editor** or **Metrics**
3. Look for failed connection attempts
4. The blocked IP will be shown in the error message

---

## After Enabling Azure Services

Wait 1-2 minutes, then test:

```bash
# Test health endpoint
curl https://reco-production-0b1e.up.railway.app/api/health
```

Expected response after fix:
```json
{
  "status": "healthy",
  "database": "connected",
  "timestamp": "2025-12-15T..."
}
```

---

## Summary

**Easiest method:** Enable "Allow Azure services" in Azure SQL firewall settings ✅

**If you need the specific IP:** Visit `/debug/ip` endpoint after Railway redeploys
