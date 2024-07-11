import uuid
from typing import Dict


class ParticipantCreator:
    def __init__(self, participants_repository, emails_repository):
        self.__participants_repository = participants_repository
        self.__emails_repository = emails_repository

    def create(self, body, trip_id) -> Dict:
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            emails_infos = {
                "email": body["email"],
                "id": email_id,
                "trip_id": trip_id,
            }
            participants_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"],
            }
            self.__emails_repository.registry_email(emails_infos)
            self.__participants_repository.registry_participant(participants_infos)
            return {
                "body": {"participant_id": participant_id},
                "status": 201,
            }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status": 400,
            }
