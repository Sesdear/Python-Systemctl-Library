def reload(name) -> bool:
    import subprocess
    import os
    
    if os.geteuid() != 0:
        raise PermissionError("Root privileges are required to reload a service.")
    
    try:
        subprocess.run(['systemctl', 'reload', name], check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except Exception:
        return False