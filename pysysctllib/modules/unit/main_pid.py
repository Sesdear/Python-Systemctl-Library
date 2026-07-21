def main_pid(service_name: str):
    import subprocess
    
    try:
        result = subprocess.run([
            'systemctl', 'show', service_name,
            '-p', 'MainPID'
            ], check=True, capture_output=True, text=True)
        data = {}
        
        for line in result.stdout.splitlines():
            key, value = line.split("=", 1)
            data[key] = value
        
        
        return data["MainPID"]
    except subprocess.CalledProcessError:
        return None
    except Exception:
        return None