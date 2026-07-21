def unit_file_state(service_name) -> (str | None):
    import subprocess
    
    try:
        result = subprocess.run([
            'systemctl', 'show', service_name,
            '-p', 'UnitFileState'
            ], check=True, capture_output=True, text=True)
        data = {}
        
        for line in result.stdout.splitlines():
            key, value = line.split("=", 1)
            data[key] = value
        
        
        return data["UnitFileState"]
    except subprocess.CalledProcessError:
        return None
    except Exception:
        return None