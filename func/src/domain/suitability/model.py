from datetime import datetime

from khonshu import CustomerAnswers, CustomerSuitability
from pytz import timezone

from src.domain.models.device_info import DeviceInfo


class SuitabilityModel:
    def __init__(
        self,
        customer_suitability: CustomerSuitability,
        unique_id: str,
        customer_answers: CustomerAnswers,
        device_info: DeviceInfo,
    ):
        self.customer_questions_with_answers = customer_answers.dict().get("answers")
        self.profile = customer_suitability.profile
        self.score = customer_suitability.score
        self.unique_id = unique_id
        self.version = customer_suitability.version
        self.submission_date = datetime.now(tz=timezone("America/Sao_Paulo"))
        self.device_info = device_info

    async def get_audit_suitability_template(self) -> dict:
        audit_msg = {
            "unique_id": self.unique_id,
            "form": self.customer_questions_with_answers,
            "version": self.version,
            "score": self.score,
            "profile": self.profile,
            "ip": self.device_info.ip,
            "latitude": self.device_info.latitude,
            "longitude": self.device_info.longitude,
            "precision": self.device_info.precision,
        }
        return audit_msg

    async def get_mongo_suitability_template(self):
        suitability_template = {
            "suitability": {
                "score": self.score,
                "profile": self.profile,
                "submission_date": self.submission_date,
                "suitability_version": self.version,
            }
        }
        return suitability_template
