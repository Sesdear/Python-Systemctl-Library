def get_main_pid(name) -> int:
    import subprocess
    
    try:
        result = subprocess.run(['systemctl', 'show', name, '--property', 'MainPID'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout.strip()
        _, pid_str = output.split('=')
        pid = int(pid_str)
        return pid if pid != 0 else -1
    except Exception:
        return -1