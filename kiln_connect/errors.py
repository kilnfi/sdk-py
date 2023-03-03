class KilnError(Exception):
    """Base class for Kiln errors.
    """


class KilnInvalidEnvError(KilnError):
    """Invalid environment config.
    """


class KilnIntegrationConfigError(KilnError):
    """Invalid integration config.
    """


class KilnFireblocksFailedToSignError(KilnError):
    """Failed to sign the fireblocks transaction.
    """
