import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.v1_eth_stakes import V1EthStakes
from openapi_client.apis.paths.v1_eth_rewards import V1EthRewards
from openapi_client.apis.paths.v1_eth_operations import V1EthOperations
from openapi_client.apis.paths.v1_eth_network_stats import V1EthNetworkStats
from openapi_client.apis.paths.v1_eth_transaction_stake import V1EthTransactionStake
from openapi_client.apis.paths.v1_eth_transaction_broadcast import V1EthTransactionBroadcast
from openapi_client.apis.paths.v1_eth_transaction_status import V1EthTransactionStatus
from openapi_client.apis.paths.v1_eth_reports import V1EthReports

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ETH_STAKES: V1EthStakes,
        PathValues.V1_ETH_REWARDS: V1EthRewards,
        PathValues.V1_ETH_OPERATIONS: V1EthOperations,
        PathValues.V1_ETH_NETWORKSTATS: V1EthNetworkStats,
        PathValues.V1_ETH_TRANSACTION_STAKE: V1EthTransactionStake,
        PathValues.V1_ETH_TRANSACTION_BROADCAST: V1EthTransactionBroadcast,
        PathValues.V1_ETH_TRANSACTION_STATUS: V1EthTransactionStatus,
        PathValues.V1_ETH_REPORTS: V1EthReports,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ETH_STAKES: V1EthStakes,
        PathValues.V1_ETH_REWARDS: V1EthRewards,
        PathValues.V1_ETH_OPERATIONS: V1EthOperations,
        PathValues.V1_ETH_NETWORKSTATS: V1EthNetworkStats,
        PathValues.V1_ETH_TRANSACTION_STAKE: V1EthTransactionStake,
        PathValues.V1_ETH_TRANSACTION_BROADCAST: V1EthTransactionBroadcast,
        PathValues.V1_ETH_TRANSACTION_STATUS: V1EthTransactionStatus,
        PathValues.V1_ETH_REPORTS: V1EthReports,
    }
)
