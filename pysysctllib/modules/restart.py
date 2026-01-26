def restart(name) -> bool:
    import subprocess
    import os
    
    if os.geteuid() != 0:
        raise PermissionError("Root privileges are required to restart a service.")
    
    try:
        subprocess.run(['systemctl', 'restart', name], check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except Exception:
        return False