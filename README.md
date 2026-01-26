# Python-Systemctl-Libary

Python library providing a direct interface to **systemd** via `systemctl` for service management and inspection.

The library exposes a single high-level class, `Systemctl`, mapping one-to-one to common `systemctl` operations and queries.

---

## Installation

From PyPI:

```bash
pip install python-systemctl-libary
```

From source:

```bash
git clone https://github.com/Sesdear/Python-Systemctl-Libary.git
cd Python-Systemctl-Libary
pip install .
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

svc.start()
svc.stop()
svc.restart()
svc.reload()

svc.enable()
svc.disable()

svc.mask()
svc.unmask()

svc.is_active()
svc.is_enabled()
svc.is_masked()

svc.status()
svc.get_main_pid()
svc.get_description()
svc.get_unit_file_state()
svc.list_dependencies()

svc.reload_daemon()
```

---

## API

### `Systemctl(name: str)`

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

* `status() -> str`
* `is_active() -> bool`
* `get_main_pid() -> int`
* `get_description() -> str`
* `get_unit_file_state() -> str`
* `list_dependencies() -> list`

---

### systemd Manager

* `reload_daemon() -> bool`

---

## License

GPL-2.0

---

## Author

[Sesdear](https://github.com/sesdear)
