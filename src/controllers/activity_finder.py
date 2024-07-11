from typing import Dict


class ActivityFinder:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def find_from_trip(self, trip_id) -> Dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(trip_id)

            activities_infos = []
            for activity in activities:
                activities_infos.append(
                    {
                        "id": activity[0],
                        "title": activity[2],
                        "occurs_at": activity[3],
                    }
                )
            return {
                "body": {"activities": activities_infos},
                "status": 200,
            }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status": 400,
            }
