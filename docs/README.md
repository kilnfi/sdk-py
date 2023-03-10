# Kiln Connect SDK

## Overview

Welcome to the Python Kiln Connect SDK which provides facilities
around Staking using the Kiln API. It is composed of three parts:

- [API layer](https://github.com/kilnfi/sdk-py/tree/main/kiln_connect/openapi_client) which facilities usage of the Kiln API,
- [Integration layer](https://github.com/kilnfi/sdk-py/tree/main/kiln_connect/)  which provides facilities around the Kiln API,
- [CLI](https://github.com/kilnfi/sdk-py/tree/main/cli/) which showcases the two previous parts.

The SDK is typically used as follows: a `KilnConnect` instance is
created from a `KilnConfig`, the SDK then provides access to different
parts:

- `accounts` for Kiln Accounts facilities
- `eth` for Ethereum facilities

Optionally, the SDK can be configured with multiple integrations
(similar to the concept of modules), which can be referred later via
their name.

For example, here we create a KilnConnect object from a config
initialized from the environment. This config has a Fireblocks
integration called `fireblocks` (configured with a specific vault
account and API key), we then stake on Ethereum using the fireblocks
integration.

```python
import kiln_connect

config = kiln_connect.KilnConfig.from_env()
kc = kiln_connect.KilnConnect(config)

kc.eth.stake(integration='fireblocks', account_id='...', wallet='...', amount_wei=32000000000000000000)
```

The following integrations are currently supported:

- [Fireblocks](#Fireblocks)

## Configuration

There are two ways to configure the SDK, either manually by creating a
`KilnConfig` object or by using the environment. For simplicity, we
recommend using the environment to start with, and then switch to
`KilnConfig` as your usage becomes more specific.

### Via Environment

Kiln Connect can be configured from the environment by using the
helper `KilnConfig.from_env()`, as follows:

```python
import kiln_connect

def example():
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
       pass
```

This helper builds a `KilnConfig` by looking at the following
environment variables:

| Variable Name                 | Description                                 | Example                                | Misc     |
|-------------------------------|---------------------------------------------|----------------------------------------|----------|
| `KILN_ENV`                    | Environment to use                          | `devnet`, `testnet`, `mainnet`         | Required |
| `KILN_API_URL`                | Kiln Endpoint to target                     | `https://api.testnet.kiln.fi`          | Required |
| `KILN_API_TOKEN`              | Kiln API token                              | `kiln_...`                             | Required |
| `FIREBLOCKS_API_KEY`          | API key for Fireblocks Integration          | `123e4567-e89b-12d3-a456-426614174000` | Optional |
| `FIREBLOCKS_RAW_KEY_PATH`     | Path to PEM key for Fireblocks Integration  | `~/.fireblocks.pem`                    | Optional |
| `FIREBLOCKS_VAULT_ACCOUNT_ID` | Vault Account ID for Fireblocks Integration | `7`                                    | Optional |

### Via KilnConfig

The `KilnConfig` required to initialize the API is defined
as follows:

```python
class KilnConfig:
    """Configuration of the Kiln Connect SDK.
    """
    kiln_base_url: str                     # https://api.testnet.kiln.fi/
    kiln_api_token: str                    # kiln_...
    integrations: list[IntegrationConfig]  # optional list of integration configs

class IntegrationConfig:
    """Configuration of a Kiln integration.
    """
    name: str                              # user-defined name of the integration (i.e: "")
    provider: str                          # type of the integration (i.e: "fireblocks")
    parameters: dict                       # python dict
```

For example:

```python
import kiln_connect

config = kiln_connect.KilnConfig(
    kiln_base_url='https://api.testnet.kiln.fi',
    kiln_api_token='kiln_...',

    integrations=[
       # Fireblocks Integration to stake on ETH_TEST3 (goerli)
       # from vault account 7 using raw key present in file
       # ~/.fireblocks.pem.
       kiln_connect.IntegrationConfig(
         name='fireblocks-testnet',
         provider='fireblocks',
         parameters={
           'api_token': '...',
           'raw_key_path': '~/.fireblocks.pem',
           'vault_account_id': 7,
           'assets': {
              'eth': 'ETH_TEST3',
           }
         }
       )
    ]
)
```

#### Fireblocks

Here is the expected configuration for the optional Fireblocks
integration:

```python
{
   'api_token': '<Fireblocks API token>',
   'raw_key_path': '<Fireblocks raw key path>',
   'vault_account_id': <Fireblocks Vault Account ID>,
   'assets': {
      'eth': 'ETH_TEST3',
   },
}
```

Where assets is a dictionnary used to know which asset to use whenever
staking on a given protocol. The following protocols are supported:

- `eth` (available via `KilnConnect.eth.stake`)

## Usage

The simplest way to start using the SDK is to look at examples
implemented in the [CLI](https://github.com/kilnfi/sdk-py/tree/main/cli/); it is kept simple to showcase the SDK.

API facilities:

- [Accounts](AccountsApi.md)
- [Ethereum](EthApi.md)
- [Tezos](XtzApi.md)

Integrations facilities:

- [Fireblocks](https://github.com/kilnfi/sdk-py/tree/main/docs/README.md#fireblocks)
