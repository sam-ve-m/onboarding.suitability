from ...domain.enums.types import ProfileTypes
from datetime import datetime


class SuitabilityModel:
    def __init__(self, answers: list, score: int, unique_id: str, version: int):
        self.answers = answers
        self.score = score
        self.unique_id = unique_id
        self.version = version
        self.submission_date = datetime.utcnow()

    def get_audit_suitability_template(self) -> dict:
        normalized_answers = [
            {
                "question_id": item.get("question_id"),
                "answer": item.get("answer"),
            }
            for item in self.answers
        ]
        audit_msg = {
                "unique_id": self.unique_id,
                "form": normalized_answers,
                "version": self.version,
                "score": self.score,
                "profile": ProfileTypes.AGGRESSIVE,
                "create_suitability_time_stamp": self.submission_date,
            }
        return audit_msg

    def get_mongo_suitability_template(self):
        suitability_doc = {
            "suitability": {
                "score": self.score,
                "submission_date": self.submission_date,
                "suitability_version": self.version,
            }
        }
        return suitability_doc
