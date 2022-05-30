class ErrorOnFindUser(Exception):
    msg = "Jormungandr-Onboarding::create_suitability_profile::Error on trying to get user in mongo_db::" \
          "User not exists, or unique_id invalid"


class ErrorOnUpdateUser(Exception):
    msg = "Jormungandr-Onboarding::create_suitability_profile::Error on trying to update user in mongo_db::" \
          "User not exists, or unique_id invalid"


class ErrorOnSendAuditLog(Exception):
    msg = "Jormungandr-Onboarding::create_suitability_profile::Error when trying to send log audit on Persephone"


class ErrorOnDecodeJwt(Exception):
    msg = "Jormungandr-Onboarding::create_suitability_profile::Fail when trying to get unique id," \
          " jwt not decoded successfully"


class NoSuitabilityAnswersFound(Exception):
    msg = "Jormungandr-Onboarding::create_suitability_profile::Error on get suitability answers"


class SuitabilityEmptyValues(Exception):
    msg = "Jormungandr-Onboarding::create_suitability_profile::Empty values in suitability answers"
