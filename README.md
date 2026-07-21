# Python-Systemctl-Library

Python library providing a direct interface to **systemd** via `systemctl` for service management and inspection.

The library exposes a single high-level class, `Systemctl`, mapping one-to-one to common `systemctl` operations and queries.

---

## Installation

From PyPI:

```bash
pip install pysysctllib
```

From source:

```bash
git clone https://github.com/Sesdear/Python-Systemctl-Libary.git
cd Python-Systemctl-Libary
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry build
cd dist
pip install pysysctllib-*.whl
```

---

## Environment

* Python >= 3.7
* Linux with systemd
* `systemctl` available
* Appropriate privileges for service control

---

## Basic Usage

```python
from pysysctllib import Systemctl

svc = Systemctl("nginx.service")

if svc.reload_daemon():
    print("Daemon reload success!")

```

---

## API

### `Systemctl(service_name: str)`

Service unit controller bound to a specific systemd unit name.

---

### Lifecycle Operations

* `start() -> bool`
* `stop() -> bool`
* `restart() -> bool`
* `reload() -> bool`

---

### Enablement

* `enable() -> bool`
* `disable() -> bool`
* `is_enabled() -> bool`

---

### Masking

* `mask() -> bool`
* `unmask() -> bool`
* `is_masked() -> bool`

---

### State and Metadata

* `properites() -> dict` 
* `status() -> StatusModel`
* `is_active() -> bool`
* `main_pid() -> int`
* `unit_file_state() -> str`
* `list_dependencies() -> list`

---

### systemd Manager

* `reload_daemon() -> bool`

---

## License

Library use [GPL-2.0 License](LICENSE).

---

## Author

[Sesdear](https://github.com/sesdear)
