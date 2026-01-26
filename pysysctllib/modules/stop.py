def stop(name) -> bool:
        import subprocess
        import os
        
        if os.geteuid() != 0:
            raise PermissionError("Root privileges are required to stop a service.")
        
        try:
            subprocess.run(['systemctl', 'stop', name], check=True)
            return True
        except subprocess.CalledProcessError:
            return False
        except Exception:
            return False
        