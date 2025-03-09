#!/usr/bin/env python3

from pymongo import MongoClient

def log_stats():
    """Provides stats about Nginx logs stored in MongoDB."""
    client = MongoClient()
    db = client.logs
    collection = db.nginx
    
    # Count total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")
    
    # Count GET requests to /status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()

