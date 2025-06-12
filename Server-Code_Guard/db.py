from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["project_db"]
collection = db["versions"]

def save_version(issue_count: int):
    version_data = {
        "date": datetime.now(),
        "issue_count": issue_count
    }
    collection.insert_one(version_data)
    print("✅ גרסה נשמרה:", version_data)