def mask(name) -> bool:
    import subprocess
    import os
    
    if os.geteuid() != 0:
        raise PermissionError("Root privileges are required to mask a service.")
    
    try:
        subprocess.run(['systemctl', 'mask', name], check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except Exception:
        return False