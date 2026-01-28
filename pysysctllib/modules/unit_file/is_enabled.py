def is_enabled(name) -> bool:
    import subprocess
    
    try:
        result = subprocess.run(['systemctl', 'is-enabled', name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip() == 'enabled'
    except subprocess.CalledProcessError:
        return False
    except Exception:
        return False