# Jormungandr - Onboarding
from ..domain.exceptions import ErrorOnFindUser, ErrorOnUpdateUser, NoSuitabilityAnswersFound, SuitabilityEmptyValues
from ..domain.suitability.model import SuitabilityModel
from ..repositories.mongo_db.suitability_answers.repository import SuitabilityRepository
from ..repositories.mongo_db.user.repository import UserRepository
from ..transports.audit.transport import Audit

# Standards
from typing import Tuple


class SuitabilityService:

    @staticmethod
    async def create(unique_id: str):
        answers, score, version = await SuitabilityService._get_suitability_answers()
        suitability_model = SuitabilityModel(
            answers=answers,
            score=score,
            unique_id=unique_id,
            version=version
        )
        audit_template_msg = suitability_model.get_audit_suitability_template()
        await Audit.suitability_answer_log(audit_template_msg=audit_template_msg)
        suitability_doc = suitability_model.get_mongo_suitability_template()
        await SuitabilityService._update_suitability_in_user_db(unique_id=unique_id, suitability_doc=suitability_doc)
        return True

    @staticmethod
    async def _get_suitability_answers() -> Tuple[list, float, int]:
        suitability_answers = await SuitabilityRepository.find_one_most_recent_suitability_answers()
        if not suitability_answers:
            raise NoSuitabilityAnswersFound
        answers = suitability_answers.get("answers")
        score = suitability_answers.get("score")
        version = suitability_answers.get("suitability_version")
        if not all([answers, score, version]):
            raise SuitabilityEmptyValues
        return answers, score, version

    @staticmethod
    async def _update_suitability_in_user_db(unique_id: str, suitability_doc: dict):
        user = await UserRepository.find_one_by_unique_id(unique_id=unique_id)
        if not user:
            raise ErrorOnFindUser
        user_updated = await UserRepository.update_one_with_suitability_data(
            user=user,
            suitability=suitability_doc
        )
        if not user_updated.acknowledged:
            raise ErrorOnUpdateUser

