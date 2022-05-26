# Jormungandr - Onboarding
from ..domain.exceptions import ErrorOnFindUser, ErrorOnUpdateUser
from ..domain.suitability.model import SuitabilityModel
from ..repositories.mongo_db.suitability_answers.repository import SuitabilityRepository
from ..repositories.mongo_db.user.repository import UserRepository
from ..transports.audit.transport import Audit


class SuitabilityService:

    async def create(self, unique_id: str):
        answers, score, version = await self._get_suitability_answers()
        suitability_model = SuitabilityModel(
            answers=answers,
            score=score,
            unique_id=unique_id,
            version=version
        )
        audit_template_msg = suitability_model.get_audit_suitability_template()
        await Audit.suitability_answer_log(audit_template_msg=audit_template_msg)
        suitability_doc = suitability_model.get_mongo_suitability_template()
        await self._update_suitability_in_user_db(unique_id=unique_id, suitability_doc=suitability_doc)
        return True

    @staticmethod
    async def _get_suitability_answers() -> tuple:
        results = await SuitabilityRepository.find_most_recent_suitability_answers()
        suitability_answers = results[0]
        answers = suitability_answers.get("answers")
        score = suitability_answers.get("score")
        version = suitability_answers.get("suitability_version")
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
        if not user_updated:
            raise ErrorOnUpdateUser

