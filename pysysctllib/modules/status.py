
class _Loaded:
    def __init__(self):
        self.status: str = ""
        self.service_path: str = ""
        self.enabled: str = ""
        self.preset: str = ""
    
class _DropIn:
    def __init__(self):
        self.path: str = ""
    
class _Active:
    def __init__(self):
        self.status: str = ""
        self.substatus: str = ""
        self.datetime: str = ""
        self.time_ago: str = ""
    
class _Invocation:
    def __init__(self):
        self.inv_id: str = ""
    
class _Process:
    def __init__(self):
        self.pid: int = 0
        self.exec_path: str = ""
        self.exec_args: str = ""
        self.code: str = ""
        self.status: str = ""
    
class _Tasks:
    def __init__(self):
        self.active: str = ""
        self.limit: str = ""
    
class _Memory:
    def __init__(self):
        self.now_memory: str = ""
        self.peak_memory: str = ""
    
class _CPU:
    def __init__(self):
        self.startup_time: str = ""
    
class _Logs:
    def __init__(self):
        self.logs: str = ""
    
class StatusModel:
    def __init__(self):
        self.service_name: str = ""
        self.description: str = ""
        self.loaded: _Loaded = _Loaded()
        self.dropin: _DropIn = _DropIn()
        self.active: _Active = _Active()
        self.invocation: _Invocation = _Invocation()
        self.process: _Process = _Process()
        self.tasks: _Tasks = _Tasks()
        self.memory: _Memory = _Memory()
        self.cpu: _CPU = _CPU()
        self.logs: _Logs = _Logs()

def status(name) -> StatusModel:
    import subprocess
    import re
    
    
    try:
        status_model: StatusModel = StatusModel()
        
        result = subprocess.run(
            ['systemctl', 'status', name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        log = result.stdout
        pattern = r"^[○●.x]?\s*([\w.-]+)(?:\s+-\s+(.*))?"

        match = re.search(pattern, log.splitlines()[0].strip())
        if match:
            status_model.service_name = match.group(1)
            status_model.description = match.group(2) if match.group(2) else ""

        for line in log.splitlines():
            if "Loaded" in line:
                pattern = r"Loaded:\s+(\w+)\s+\(([^;]+);\s+(\w+);(?:\s+preset:\s+(\w+))?"
                match = re.search(pattern, line)
                if match:
                    status_model.loaded.status = match.group(1)
                    status_model.loaded.service_path = match.group(2)
                    status_model.loaded.enabled = match.group(3)
                    status_model.loaded.preset = match.group(4)

            elif "Drop-In" in line:
                status_model.dropin.path = line.split(":", 1)[1].strip()
            elif "Active" in line:
                pattern = r"Active:\s+(\w+)\s+\(([^)]+)\)(?:\s+since\s+([^;]+))?(?:;\s+(.*))?"
                match = re.search(pattern, line)
                if match:
                    status_model.active.status = match.group(1) if match.group(1) else ""
                    status_model.active.substatus = match.group(2) if match.group(2) else ""
                    status_model.active.datetime = match.group(3).strip() if match.group(3) else ""
                    status_model.active.time_ago = match.group(4).strip() if match.group(4) else ""
            elif "Invocation" in line:
                pattern = r"Invocation:\s+([a-f0-9\-]+)"
                match = re.search(pattern, line)
                if match:
                    status_model.invocation.inv_id = match.group(1) if match.group(1) else ""
            elif "Process" in line:
                pattern = (
                r"Process:\s+(\d+)\s+ExecStart=([^\s]+)"
                r"(?:\s+(.*?))?\s+\(code=(\w+),\s+status=([\w/]+)\)"
                )
                match = re.search(pattern, line)
                if match:
                    status_model.process.pid = int(match.group(1)) if match.group(1) else 0
                    status_model.process.exec_path = match.group(2) if match.group(2) else ""
                    status_model.process.exec_args = match.group(3) if match.group(3) else ""
                    status_model.process.code = match.group(4) if match.group(4) else ""
                    status_model.process.status = match.group(5) if match.group(5) else ""
            elif "Tasks" in line:
                pattern = r"\s*Tasks:\s+(\d+)\s+\(limit:\s*(\d+)\)"
                match = re.match(pattern, line)
                if match:
                    status_model.tasks.active = match.group(1) if match.group(1) else ""
                    status_model.tasks.limit = match.group(2) if match.group(2) else ""
                    
            elif "Memory" in line:
                pattern = r"Memory:\s+([^\s]+)\s+\(peak:\s+([^\s]+)\)"
                match = re.search(pattern, line)
                if match:
                    status_model.memory.now_memory = match.group(1) if match.group(1) else ""
                    status_model.memory.peak_memory = match.group(2) if match.group(2) else ""
            
            elif "CPU" in line:
                pattern = r"CPU:\s+(.+)"
                match = re.search(pattern, line)
                if match:
                    status_model.cpu.startup_time = match.group(1) if match.group(1) else ""

        return status_model
    except subprocess.CalledProcessError as e:
        return StatusModel()
    except Exception:
        return StatusModel()