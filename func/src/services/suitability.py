from khonshu import Khonshu, KhonshuStatus, CustomerSuitability, CustomerAnswers
from pymongo.results import UpdateResult

from ..domain.enums.types import UserOnboardingStep
from ..domain.exceptions.repositories.exception import ErrorOnUpdateUser
from ..domain.exceptions.services.exception import ErrorCalculatingCustomerSuitability
from ..domain.exceptions.transports.exception import InvalidOnboardingCurrentStep
from ..domain.models.device_info import DeviceInfo
from ..domain.suitability.model import SuitabilityModel
from ..repositories.mongo_db.user.repository import UserRepository
from ..transports.audit.transport import Audit
from ..transports.onboarding_steps.transport import OnboardingSteps


class SuitabilityService:
    @staticmethod
    async def validate_current_onboarding_step(jwt: str) -> bool:
        user_current_step = await OnboardingSteps.get_user_current_step(jwt=jwt)
        if not user_current_step == UserOnboardingStep.SUITABILITY:
            raise InvalidOnboardingCurrentStep()
        return True

    @classmethod
    async def set_in_customer(
        cls, unique_id: str, customer_answers: CustomerAnswers, device_info: DeviceInfo
    ) -> bool:
        customer_suitability = await cls.__get_customer_suitability_from_khonshu(
            customer_answers=customer_answers
        )
        suitability_model = SuitabilityModel(
            unique_id=unique_id,
            customer_suitability=customer_suitability,
            customer_answers=customer_answers,
            device_info=device_info,
        )
        await Audit.record_message_log(suitability_model=suitability_model)
        suitability = await suitability_model.get_mongo_suitability_template()
        await SuitabilityService.__save_customer_suitability_data(
            unique_id=unique_id, suitability=suitability
        )
        return True

    @staticmethod
    async def __get_customer_suitability_from_khonshu(
        customer_answers: CustomerAnswers,
    ) -> CustomerSuitability:
        (
            success,
            khonshu_status,
            customer_suitability,
        ) = await Khonshu.get_suitability_score(customer_answers=customer_answers)
        if khonshu_status == KhonshuStatus.SUCCESS:
            return customer_suitability
        raise ErrorCalculatingCustomerSuitability()

    @staticmethod
    async def __save_customer_suitability_data(
        unique_id: str, suitability: dict
    ) -> bool:
        user_updated: UpdateResult = (
            await UserRepository.update_customer_suitability_data(
                unique_id=unique_id, suitability=suitability
            )
        )
        if not user_updated.matched_count:
            raise ErrorOnUpdateUser()
        return True
