"""
Test script for Railway deployment
Run this to verify the recommender API is working
"""
import requests
import json

# Railway deployment URL
BASE_URL = "https://reco-production-0b1e.up.railway.app"

def test_root():
    """Test root endpoint"""
    print("\n=== Testing Root Endpoint ===")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_health():
    """Test health check endpoint"""
    print("\n=== Testing Health Endpoint ===")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"Error Response: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_recommend(user_id=1, top_n=5):
    """Test recommendations endpoint"""
    print(f"\n=== Testing Recommendations (user_id={user_id}, top_n={top_n}) ===")
    try:
        response = requests.get(f"{BASE_URL}/api/recommend", params={"user_id": user_id, "top_n": top_n})
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"User Type: {data.get('user_type')}")
            print(f"Total Recommendations: {data.get('total_recommendations')}")
            print(f"Accuracy Score: {data.get('accuracy_score')}")
            
            if data.get('recommendations'):
                print(f"\nFirst recommendation:")
                rec = data['recommendations'][0]
                print(f"  Title: {rec.get('title')}")
                print(f"  Authors: {rec.get('authors')}")
                print(f"  Score: {rec.get('hybrid_score')}")
        else:
            print(f"Error Response: {response.text[:500]}")
        
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    """Run all tests"""
    print("="*60)
    print("Railway Deployment Test Suite")
    print("="*60)
    print(f"Testing BASE_URL: {BASE_URL}")
    
    results = {
        "Root Endpoint": test_root(),
        "Health Check": test_health(),
        "Recommendations": test_recommend()
    }
    
    print("\n" + "="*60)
    print("Test Results:")
    print("="*60)
    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    print("\n" + "="*60)
    if all_passed:
        print("✅ All tests PASSED! Deployment is working correctly.")
    else:
        print("⚠️ Some tests FAILED. Check error details above.")
        print("   - Root endpoint working = PORT issue fixed ✅")
        print("   - Database endpoints failing = Database connection issue ⚠️")
    print("="*60)

if __name__ == "__main__":
    main()
