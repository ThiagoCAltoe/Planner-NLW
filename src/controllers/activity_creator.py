import uuid
from typing import Dict

class ActivityCreator:
    def __init__(self, activities_repository):
        self.__activities_repository = activities_repository

    def create(self, body, trip_id) -> Dict:
        try:
            id = str(uuid.uuid4())
            activities_infos = {
                "id": id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"],
            }
            self.__activities_repository.registry_activity(activities_infos)
            return {
                "body": {"activity_id": id},
                "status_code": 201,
            }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400,
            }
