from motor.motor_asyncio import AsyncIOMotorClient

from ..base_repository.base import MongoDbBaseRepository

from etria_logger import Gladsheim
from decouple import config


class SuitabilityRepository(MongoDbBaseRepository):

    database = config("MONGODB_DATABASE_NAME")
    collection = config("MONGODB_SUITABILITY_ANSWERS_COLLECTION")

    @classmethod
    async def find_one_most_recent_suitability_answers(cls) -> dict:
        try:
            collection = await cls._get_collection()
            result = await collection.find_one({"$query": {}, "$orderby": {"$natural": -1}})
            return result
        except Exception as ex:
            message = f"SuitabilityRepository::find_last_suitability_answer:: error on trying to" \
                      f" get suitability answers"
            Gladsheim.error(error=ex, message=message)
            raise ex
