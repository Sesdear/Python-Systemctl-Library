def get_description(name) -> str:
    import subprocess
    
    try:
        result = subprocess.run(['systemctl', 'show', name, '--property', 'Description'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout.strip()
        _, description = output.split('=', 1)
        return description
    except Exception:
        return ""