def show(name: str, parameter: str) -> str:
    import subprocess
    try:
        result = subprocess.run(
                ['systemctl', 'show', '-p', parameter, '--value', name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"CalledProcessError: {e}"
    except Exception as e:
        return f"Exception: {e}"