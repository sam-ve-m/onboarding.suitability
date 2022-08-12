class ErrorOnFindUser(Exception):
    msg = (
        "Jormungandr-Onboarding::create_suitability_profile::Error on trying to get user in mongo_db::"
        "User not exists, or unique_id invalid"
    )


class ErrorOnUpdateUser(Exception):
    msg = (
        "Jormungandr-Onboarding::create_suitability_profile::Error on trying to update user in mongo_db::"
        "User not exists, or unique_id invalid"
    )


class ErrorOnSendAuditLog(Exception):
    msg = "Jormungandr-Onboarding::create_suitability_profile::Error when trying to send log audit on Persephone"


class ErrorOnDecodeJwt(Exception):
    msg = (
        "Jormungandr-Onboarding::create_suitability_profile::Fail when trying to get unique id,"
        " jwt not decoded successfully"
    )


class NoSuitabilityAnswersFound(Exception):
    msg = "Jormungandr-Onboarding::create_suitability_profile::Error on get suitability answers"


class SuitabilityEmptyValues(Exception):
    msg = "Jormungandr-Onboarding::create_suitability_profile::Empty values in suitability answers"


class OnboardingStepsStatusCodeNotOk(Exception):
    msg = "Jormungandr-Onboarding::get_user_current_step::Error when trying to get onboarding steps br"


class InvalidOnboardingCurrentStep(Exception):
    msg = "Jormungandr-Onboarding::validate_current_onboarding_step::User is not in the electronic signature step"


class ErrorOnGetUniqueId(Exception):
    msg = "Jormungandr-Onboarding::get_unique_id::Fail when trying to get unique_id"
