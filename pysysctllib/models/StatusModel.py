from datetime import date

class StatusModel():
    active_state: str
    sub_state: str
    unit_file_state: str
    pid: int
    service_path: str