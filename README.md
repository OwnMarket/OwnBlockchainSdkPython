# OwnBlockchainSdkPython

Own Blockchain SDK for Python

## Quick Start

```bash
$ git clone https://github.com/OwnMarket/OwnBlockchainSdkPython.git
$ cd own_blockchain_sdk
```

Run tests:
```bash
$ pytest -v
```

## Usage

Own Blockchain SDK can be used as a pip package.

```bash
$ pip install own-blockchain-sdk
```

or 

``` bash
$ python -m pip install own-blockchain-sdk
```

Use the package in Python code

```python
from own_blockchain_sdk import Wallet, Tx
    
# Create a new wallet
wallet = Wallet()
print('PK =', wallet.private_key, ', Address = ', wallet.address)

# Compose a transaction with nonce = 1 and action fee 0.1
tx = Tx(wallet.address, 1, 0.1)
tx.add_transfer_chx_action('CHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 100) # Transfer 100 CHX to CHxxx... address.

# Look at the raw transaction in JSON format
print(tx.to_json())

# Sign the transaction for submission to node API on TestNet
network_code = 'OWN_PUBLIC_BLOCKCHAIN_TESTNET'
print(tx.sign(network_code, wallet.private_key))
```
