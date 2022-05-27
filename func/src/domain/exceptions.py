class ErrorOnFindUser(Exception):
    msg = "User not exists, or unique_id invalid"


class ErrorOnUpdateUser(Exception):
    msg = "User not exists, or unique_id invalid"


class ErrorOnSendAuditLog(Exception):
    msg = "Error when trying to send log audit on Persephone"
