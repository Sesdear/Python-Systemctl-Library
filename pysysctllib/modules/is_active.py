def is_active(name) -> bool:
    import subprocess
    
    try:
        result = subprocess.run(['systemctl', 'is-active', name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip() == 'active'
    except subprocess.CalledProcessError:
        return False
    except Exception:
        return False