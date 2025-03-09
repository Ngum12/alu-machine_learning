#!/usr/bin/env python3
"""
Nginx logs stored in MongoDB analysis script.

This script connects to a MongoDB instance and retrieves statistics for Nginx logs stored in the "logs.nginx" collection.
It counts the total number of logs, counts per HTTP method (GET, POST, PUT, PATCH, DELETE), and counts status checks (GET requests to "/status").
"""

from pymongo import MongoClient, errors

def main():
    try:
        # Use a context manager to ensure the connection is closed properly
        with MongoClient('mongodb://127.0.0.1:27017') as client:
            collection = client.logs.nginx

            # Get the total number of documents
            total_logs = collection.count_documents({})

            # Define the HTTP methods to count
            methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
            method_counts = {method: collection.count_documents({"method": method}) for method in methods}

            # Get the count of status checks (GET requests with path "/status")
            status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

            # Print the stats
            print(f"{total_logs} logs")
            print("Methods:")
            for method, count in method_counts.items():
                print(f"\tmethod {method}: {count}")
            print(f"{status_check_count} status check")
    except errors.ConnectionFailure as e:
        print("Could not connect to MongoDB:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    main()

