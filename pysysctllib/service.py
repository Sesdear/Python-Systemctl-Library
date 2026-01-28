from .modules.unit.status import StatusModel
from .modules.unit.show_full import ShowModel


class Systemctl:
    def __init__(self, service_name: str, **kwargs):
        """
        Create a Systemctl wrapper for a systemd service.

        Args:
            service_name: Name of the systemd service.
            **kwargs: Optional parameters
                parameter: Service parameter name for the `show` method
                |mode: Mode name for the `is_failed`, `is_enabled`, `is_active` methods|
                |    modes: single (default), pattern               in progress...     |
        """
        self.service_name = service_name
        self.value = kwargs.get("parameter", "")
        self.is_modules_mode = kwargs.get("mode", "")

#------------------------------------------------------
#status change methods
    def start(self) -> bool:
        """
        Start the service.

        Returns:
            bool: True if the service started successfully, False otherwise.
        """
        from .modules.unit.start import start
        return start(self.service_name)

    def stop(self) -> bool:
        """
        Stop the service.

        Returns:
            bool: True if the service stopped successfully, False otherwise.
        """
        from .modules.unit.stop import stop
        return stop(self.service_name)

    def restart(self) -> bool:
        """
        Restart the service.

        Returns:
            bool: True if the service restarted successfully, False otherwise.
        """
        from .modules.unit.restart import restart
        return restart(self.service_name)

    def enable(self) -> bool:
        """
        Enable the service at boot.

        Returns:
            bool: True if the service was enabled successfully, False otherwise.
        """
        from .modules.unit_file.enable import enable
        return enable(self.service_name)

    def disable(self) -> bool:
        """
        Disable the service at boot.

        Returns:
            bool: True if the service was disabled successfully, False otherwise.
        """
        from .modules.unit_file.disable import disable
        return disable(self.service_name)
    
    def reload(self) -> bool:
        """
        Reload the service configuration.

        Returns:
            bool: True if the service was reloaded successfully, False otherwise.
        """
        from .modules.unit.reload import reload
        return reload(self.service_name)

    def mask(self) -> bool:
        """
        Mask the service.

        Returns:
            bool: True if the service was masked successfully, False otherwise.
        """
        from .modules.unit_file.mask import mask
        return mask(self.service_name)

    def unmask(self) -> bool:
        """
        Unmask the service.

        Returns:
            bool: True if the service was unmasked successfully, False otherwise.
        """
        from .modules.unit_file.unmask import unmask
        return unmask(self.service_name)
#------------------------------------------------------
#is methods

    def is_enabled(self) -> bool:
        """
        Check whether the service is enabled.

        Returns:
            bool: True if the service is enabled, False otherwise.
        """
        from .modules.unit_file.is_enabled import is_enabled
        return is_enabled(self.service_name)

    def is_active(self) -> bool:
        """
        Check whether the service is active.

        Returns:
            bool: True if the service is active, False otherwise.
        """
        from .modules.unit.is_active import is_active
        return is_active(self.service_name)

    def is_masked(self) -> bool:
        """
        Check whether the service is masked.

        Returns:
            bool: True if the service is masked, False otherwise.
        """
        from .modules.unit_file.is_masked import is_masked
        return is_masked(self.service_name)
#------------------------------------------------------
#other methods

    def reload_daemon(self) -> bool:
        """
        Reload the systemd manager configuration.

        Returns:
            bool: True if the daemon was reloaded successfully, False otherwise.
        """
        from .modules.reload_daemon import reload_daemon
        return reload_daemon()

    def list_dependencies(self) -> list:
        """
        List service dependencies.

        Returns:
            list: List of service dependencies.
        """
        from .modules.unit.list_dependencies import list_dependencies
        return list_dependencies(self.service_name)

    def show_full(self) -> ShowModel:
        """
        Get full service information.

        Returns:
            ShowModel: Model containing all available service properties.
        """
        from .modules.unit.show_full import show_full
        return show_full(self.service_name)

    def show(self) -> str:
        """
        Get a specific service parameter value.

        Returns:
            str: Value of the requested service parameter.
        """
        from .modules.unit.show import show
        return show(name=self.service_name, parameter=self.value)

    def status(self) -> StatusModel:
        """
        !!! Not Stable !!!
        
        Get the current service status.

        Returns:
            StatusModel: Model containing service status information.
        """
        from .modules.unit.status import status
        return status(self.service_name)