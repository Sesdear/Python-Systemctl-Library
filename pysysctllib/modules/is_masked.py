def is_masked(name) -> bool:
    import subprocess
    
    try:
        result = subprocess.run(['systemctl', 'is-enabled', name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip() == 'masked'
    except subprocess.CalledProcessError:
        return False
    except Exception:
        return False