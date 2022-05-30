# Jormungandr-Onboarding
from ...domain.enums.types import QueueTypes
from ...domain.exceptions import ErrorOnSendAuditLog

# Third party
from decouple import config
from etria_logger import Gladsheim
from persephone_client import Persephone


class Audit:
    audit_client = Persephone
    partition = QueueTypes.SUITABILITY.value
    topic = config("PERSEPHONE_TOPIC_USER")
    schema_name = config("PERSEPHONE_SUITABILITY_SCHEMA")

    @classmethod
    async def suitability_answer_log(cls, audit_template_msg: dict):
        (
            success,
            status_sent_to_persephone
        ) = await cls.audit_client.send_to_persephone(
            topic=cls.topic,
            partition=cls.partition,
            message=audit_template_msg,
            schema_name=cls.schema_name,
        )
        if not success:
            Gladsheim.error(message="Audit::register_user_log::Error on trying to register log")
            raise ErrorOnSendAuditLog
