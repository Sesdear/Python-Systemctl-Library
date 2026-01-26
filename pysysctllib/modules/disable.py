def disable(name) -> bool:
    import subprocess
    import os
    
    if os.geteuid() != 0:
        raise PermissionError("Root privileges are required to disable a service.")
    
    try:
        subprocess.run(['systemctl', 'disable', name], check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except Exception:
        return False