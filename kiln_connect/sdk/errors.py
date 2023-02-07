"""
Errors raised by the SDK.
"""


class KilnError(Exception):
    pass


class KilnInvalidRequestError(KilnError):
    pass


class KilnInternalError(KilnError):
    pass


class KilnInvalidEnvError(KilnError):
    pass
