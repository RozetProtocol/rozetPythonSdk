# Rozet Python SDK

[Javascript](https://github.com/RozetProtocol/rozetJavascriptSdk) | [Java](https://github.com/RozetProtocol/rozetJavaSdk)

The Rozet Python SDK implements the python server-side libraries used by
applications using the Rozet protocols. This SDK is distributed via:

- [pip package](https://pypi.org/project/rozet/)

## Getting Started

### Installation

To use Rozet in your project, run:

```bash
pip install rozet
```

### Usage

Before you can start working on the Rozet Py SDK, you need to have Python
`3.6.0` or greater installed on your machine.

**Example** - Issue a badge:

Save file as **issueBadge.py**

```py
from rozet import Rozet, Badge

mnemonic = 'example example example example example example example example example example example example'
r = Rozet(mnemonic=mnemonic)

badge = Badge(
    'Great guy!',
    'Great doing business with you!',
    5,
    'john_b',
    '0x1111111111111111111111111111111111111111',
    'nathan!',
    '0x1111111111111111111111111111111111111111'
)


tx_hash = r.issueBadge(badge)

print(f'Issue badge in tx {tx_hash}')
```

Execute script on the command line

```bash
python issueBadge.py
```
or
```bash
python3.6 issueBadge.py
```

**Example** - Listen for new badges:

Save file as **listenForBadges.py**

```py
from rozet import Rozet

r = Rozet()

previousBlocks = 1000000

events = r.events(previousBlocks)

for event in events:
    sender = event['args']['sender']
    tx_hash = event['transactionHash'].hex()
    print(f'{sender} sent a badge with txHash {tx_hash}!')
```

Execute script on the command line

```bash
python listenForBadges.py
```
or
```bash
python3.6 listenForBadges.py
```

## License
You can view our [license here](https://github.com/RozetProtocol/rozetPythonSdk/blob/master/LICENSE).
