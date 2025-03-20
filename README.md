# gate-python
Python SDK (sync and async) for Gate with Rest and WS capabilities.

You can check Gate's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/gate)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install gate-io-api
```

## Usage

### Async

```Python
from gate_io_api import GateAsync

async def main():
    instance = GateAsync({})
    order = await instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Sync

```Python
from gate_io_api import GateSync

def main():
    instance = GateSync({})
    order =  instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Websockets

```Python
from gate_io_api import GateWs

async def main():
    instance = GateWs({})
    while True:
        orders = await instance.watch_orders(__EXAMPLE_SYMBOL__)
```

