
class Service:
    def __init__(self, name):
        self.name = name

    def start(self) -> bool:
        """
        
        Start service by its name.

        Returns:
            bool: Returns True if the service started successfully, False otherwise.
            
        """
        from .modules.start import start
        return start(self.name)
        
    def stop(self) -> bool:
        """
        
        Stop service by its name.

        Returns:
            bool: Returns True if the service stopped successfully, False otherwise.
            
        """
        from .modules.stop import stop
        return stop(self.name)
    
    def status(self) -> str:
        """
        
        Get the current status of the service.

        Returns:
            str: Returns the status of the service as a string.
            
        """
        from .modules.status import status
        return status(self.name)
        
    def restart(self) -> bool:
        """
        
        Restart service by its name.

        Returns:
            bool: Returns True if the service restarted successfully, False otherwise.
            
        """
        from .modules.restart import restart
        return restart(self.name)
    
    def enable(self) -> bool:
        """
        
        Enable service by its name.

        Returns:
            bool: Returns True if the service was enabled successfully, False otherwise.
            
        """
        from .modules.enable import enable
        return enable(self.name)
        
    def disable(self) -> bool:
        """
        
        Disable service by its name.

        Returns:
            bool: Returns True if the service was disabled successfully, False otherwise.
            
        """
        from .modules.disable import disable
        return disable(self.name)
        
    def is_enabled(self) -> bool:
        """
        
        Check if the service is enabled.

        Returns:
            bool: Returns True if the service is enabled, False otherwise.
            
        """
        from .modules.is_enabled import is_enabled
        return is_enabled(self.name)
    
    def is_active(self) -> bool:
        """
        
        Check if the service is active.

        Returns:
            bool: Returns True if the service is active, False otherwise.
            
        """
        from .modules.is_active import is_active
        return is_active(self.name)
    
    def reload(self) -> bool:
        """
        
        Reload service by its name.

        Returns:
            bool: Returns True if the service reloaded successfully, False otherwise.
            
        """
        from .modules.reload import reload
        return reload(self.name)
    
    def mask(self) -> bool:
        """
        
        Mask service by its name.

        Returns:
            bool: Returns True if the service was masked successfully, False otherwise.
            
        """
        from .modules.mask import mask
        return mask(self.name)
    
    def unmask(self) -> bool:
        """
        
        Unmask service by its name.

        Returns:
            bool: Returns True if the service was unmasked successfully, False otherwise.
            
        """
        from .modules.unmask import unmask
        return unmask(self.name)
    
    def is_masked(self) -> bool:
        """
        
        Check if the service is masked.

        Returns:
            bool: Returns True if the service is masked, False otherwise.
            
        """
        from .modules.is_masked import is_masked
        return is_masked(self.name)
    
    def get_main_pid(self) -> int:
        """
        
        Get the main PID of the service.

        Returns:
            int: Returns the main PID of the service, or -1 if not available.
            
        """
        from .modules.get_main_pid import get_main_pid
        return get_main_pid(self.name)
    
    def get_description(self) -> str:
        """
        
        Get the description of the service.

        Returns:
            str: Returns the description of the service.
            
        """
        from .modules.get_description import get_description
        return get_description(self.name)
    
    def get_unit_file_state(self) -> str:
        """
        
        Get the unit file state of the service.

        Returns:
            str: Returns the unit file state of the service.
            
        """
        from .modules.get_unit_file_state import get_unit_file_state
        return get_unit_file_state(self.name)
    
    def reload_daemon(self) -> bool:
        """
        
        Reload the systemd manager configuration.

        Returns:
            bool: Returns True if the daemon reloaded successfully, False otherwise.
            
        """
        from .modules.reload_daemon import reload_daemon
        return reload_daemon()
    
    def list_dependencies(self) -> list:
        """
        
        List the dependencies of the service.

        Returns:
            list: Returns a list of dependencies for the service.
            
        """
        from .modules.list_dependencies import list_dependencies
        return list_dependencies(self.name)