# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_ETH_STAKES = "/v1/eth/stakes"
    V1_ETH_REWARDS = "/v1/eth/rewards"
    V1_ETH_OPERATIONS = "/v1/eth/operations"
    V1_ETH_NETWORKSTATS = "/v1/eth/network-stats"
    V1_ETH_TRANSACTION_STAKE = "/v1/eth/transaction/stake"
    V1_ETH_TRANSACTION_BROADCAST = "/v1/eth/transaction/broadcast"
    V1_ETH_TRANSACTION_STATUS = "/v1/eth/transaction/status"
    V1_ETH_REPORTS = "/v1/eth/reports"
