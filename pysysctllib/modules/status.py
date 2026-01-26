def status(name) -> str:
    import subprocess
        
    try:
        result = subprocess.run(['systemctl', 'is-active', name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stdout.strip() if e.stdout else "unknown"
    except Exception:
        return "unknown"