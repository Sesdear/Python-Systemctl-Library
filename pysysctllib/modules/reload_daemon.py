def reload_daemon() -> bool:
    import subprocess
    import os
    
    if os.geteuid() != 0:
        return False
    try:
        subprocess.run(['systemctl', 'daemon-reload'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return True
    except Exception:
        return False