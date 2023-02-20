# Kiln Connect

This is Kiln Connect Python edition.

## Overview

This repository is organized as follows:

```
.
├── cli            # Kiln Connect CLI tool -- showcases of the SDK
├── docs           # SDK documentation -- partially generated from OpenAPI
├── kiln_connect   # SDK code -- partially generated from OpenAPI
├── specs          # OpenAPI specs -- config & templates of the generator
└── tests          # SDK unit tests -- SDK unit tests
```

## SDK Documentation

Kiln Connect's SDK can be instantiated from an API token and API URL
as follows:

```
import kiln_connect
import os

host = os.getenv('KILN_API_URL')
access_token = os.getenv('KILN_API_TOKEN')
with kiln_connect.KilnConnect(host, access_token) as kc:
  network_stats = kc.eth.get_eth_network_stats()
```

Detailed documentation about available operations can be found here:

- [Ethereum](docs/EthApi.md)

## CLI

The `kiln-connect` tool allows to interact with Kiln Connect's API
from the command line. This tool is built using the SDK and can be
used as an example of SDK's usage.

```
 Usage: kiln-connect [OPTIONS] COMMAND [ARGS]...
                                                                  
 all-in-one SDK for staking
                                                                  
╭─ Options ──────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                    │
╰────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────╮
│ eth      Staking utilities for Ethereum                        │
╰────────────────────────────────────────────────────────────────
```
