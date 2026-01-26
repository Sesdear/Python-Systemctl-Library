def get_unit_file_state(name) -> str:
    import subprocess
    
    try:
        result = subprocess.run(['systemctl', 'show', name, '--property', 'UnitFileState'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout.strip()
        _, state = output.split('=', 1)
        return state
    except Exception:
        return ""