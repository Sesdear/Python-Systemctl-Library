from typing import Dict, Any

class ShowModel:
    def __init__(self):
        # Unit Identification
        self.Id = None
        self.Names = None
        self.Description = None
        self.FragmentPath = None
        self.DropInPaths = None
        self.UnitFileState = None
        self.UnitFilePreset = None
        self.Transient = None
        self.Perpetual = None
        # Unit States
        self.LoadState = None
        self.ActiveState = None
        self.FreezerState = None
        self.SubState = None
        self.StatusErrno = None
        self.Result = None
        self.ReloadResult = None
        self.CleanResult = None
        self.LiveMountResult = None
        # Dependencies and Ordering
        self.Requires = None
        self.Wants = None
        self.WantedBy = None
        self.Conflicts = None
        self.Before = None
        self.After = None
        self.DefaultDependencies = None
        self.IgnoreOnIsolate = None
        self.StopWhenUnneeded = None
        # Timestamps
        self.StateChangeTimestamp = None
        self.StateChangeTimestampMonotonic = None
        self.InactiveExitTimestamp = None
        self.InactiveExitTimestampMonotonic = None
        self.ActiveEnterTimestamp = None
        self.ActiveEnterTimestampMonotonic = None
        self.ActiveExitTimestamp = None
        self.ActiveExitTimestampMonotonic = None
        self.InactiveEnterTimestamp = None
        self.InactiveEnterTimestampMonotonic = None
        self.ConditionTimestamp = None
        self.ConditionTimestampMonotonic = None
        self.AssertTimestamp = None
        self.AssertTimestampMonotonic = None
        # Execution Control
        self.CanStart = None
        self.CanStop = None
        self.CanReload = None
        self.CanIsolate = None
        self.CanFreeze = None
        self.CanLiveMount = None
        self.RefuseManualStart = None
        self.RefuseManualStop = None
        self.AllowIsolate = None
        # Service Type and Restart
        self.Type = None
        self.ExitType = None
        self.Restart = None
        self.RestartMode = None
        self.RestartUSec = None
        self.RestartSteps = None
        self.RestartMaxDelayUSec = None
        self.RestartUSecNext = None
        self.RemainAfterExit = None
        # Process Information
        self.MainPID = None
        self.ControlPID = None
        self.GuessMainPID = None
        self.NRestarts = None
        # Exec Commands
        self.ExecStart = None
        self.ExecStartEx = None
        self.ExecStop = None
        self.ExecStopEx = None
        self.ExecMainPID = None
        self.ExecMainCode = None
        self.ExecMainStatus = None
        self.ExecMainStartTimestampMonotonic = None
        self.ExecMainExitTimestampMonotonic = None
        self.ExecMainHandoffTimestampMonotonic = None
        # Timeouts
        self.TimeoutStartUSec = None
        self.TimeoutStopUSec = None
        self.TimeoutAbortUSec = None
        self.TimeoutCleanUSec = None
        self.TimeoutStartFailureMode = None
        self.TimeoutStopFailureMode = None
        # Job Control
        self.JobTimeoutUSec = None
        self.JobRunningTimeoutUSec = None
        self.JobTimeoutAction = None
        self.OnSuccessJobMode = None
        self.OnFailureJobMode = None
        # Start Limits
        self.StartLimitIntervalUSec = None
        self.StartLimitBurst = None
        self.StartLimitAction = None
        self.FailureAction = None
        self.SuccessAction = None
        # Resource Control (cgroups)
        self.Slice = None
        self.ControlGroup = None
        self.ControlGroupId = None
        # Memory Resources
        self.MemoryCurrent = None
        self.MemoryPeak = None
        self.MemorySwapCurrent = None
        self.MemorySwapPeak = None
        self.MemoryZSwapCurrent = None
        self.MemoryAvailable = None
        self.EffectiveMemoryMax = None
        self.EffectiveMemoryHigh = None
        self.MemoryAccounting = None
        self.MemoryMin = None
        self.MemoryLow = None
        self.MemoryHigh = None
        self.MemoryMax = None
        self.MemorySwapMax = None
        self.MemoryZSwapMax = None
        self.MemoryZSwapWriteback = None
        self.DefaultMemoryLow = None
        self.DefaultMemoryMin = None
        self.StartupMemoryLow = None
        self.StartupMemoryHigh = None
        self.StartupMemoryMax = None
        self.StartupMemorySwapMax = None
        self.StartupMemoryZSwapMax = None
        # CPU Resources
        self.CPUUsageNSec = None
        self.CPUWeight = None
        self.StartupCPUWeight = None
        self.CPUQuotaPerSecUSec = None
        self.CPUQuotaPeriodUSec = None
        self.CPUSchedulingPolicy = None
        self.CPUSchedulingPriority = None
        self.CPUAffinityFromNUMA = None
        self.CPUSchedulingResetOnFork = None
        # IO Resources
        self.IOAccounting = None
        self.IOWeight = None
        self.StartupIOWeight = None
        self.IOReadBytes = None
        self.IOReadOperations = None
        self.IOWriteBytes = None
        self.IOWriteOperations = None
        self.IOSchedulingClass = None
        self.IOSchedulingPriority = None
        # Tasks and Processes
        self.TasksCurrent = None
        self.TasksMax = None
        self.EffectiveTasksMax = None
        self.TasksAccounting = None
        # Network
        self.IPAccounting = None
        self.IPIngressBytes = None
        self.IPIngressPackets = None
        self.IPEgressBytes = None
        self.IPEgressPackets = None
        # User and Permissions
        self.UID = None
        self.GID = None
        self.UMask = None
        self.SecureBits = None
        self.CapabilityBoundingSet = None
        self.DynamicUser = None
        self.SetLoginEnvironment = None
        self.RemoveIPC = None
        self.Nice = None
        # Security and Sandboxing
        self.AccessSELinuxContext = None
        self.NoNewPrivileges = None
        self.KeyringMode = None
        self.ProtectProc = None
        self.ProcSubset = None
        self.ProtectHostname = None
        self.LockPersonality = None
        # Private Directories and Mounts
        self.PrivateTmp = None
        self.PrivateTmpEx = None
        self.PrivateDevices = None
        self.PrivateNetwork = None
        self.PrivateUsers = None
        self.PrivateUsersEx = None
        self.PrivateMounts = None
        self.PrivateIPC = None
        self.PrivatePIDs = None
        self.PrivateBPF = None
        # Protection Flags
        self.ProtectHome = None
        self.ProtectSystem = None
        self.ProtectClock = None
        self.ProtectKernelTunables = None
        self.ProtectKernelModules = None
        self.ProtectKernelLogs = None
        self.ProtectControlGroups = None
        self.ProtectControlGroupsEx = None
        self.MemoryDenyWriteExecute = None
        self.RestrictRealtime = None
        self.RestrictSUIDSGID = None
        self.RestrictNamespaces = None
        # Namespaces
        self.Delegate = None
        self.DelegateNamespaces = None
        self.MountAPIVFS = None
        self.BindLogSockets = None
        # Directories
        self.RuntimeDirectoryPreserve = None
        self.RuntimeDirectoryMode = None
        self.StateDirectoryMode = None
        self.StateDirectoryAccounting = None
        self.StateDirectoryQuota = None
        self.CacheDirectoryMode = None
        self.CacheDirectoryAccounting = None
        self.CacheDirectoryQuota = None
        self.LogsDirectoryMode = None
        self.LogsDirectoryAccounting = None
        self.LogsDirectoryQuota = None
        self.ConfigurationDirectoryMode = None
        # Signals and Kill
        self.KillMode = None
        self.KillSignal = None
        self.RestartKillSignal = None
        self.FinalKillSignal = None
        self.SendSIGKILL = None
        self.SendSIGHUP = None
        self.WatchdogSignal = None
        self.ReloadSignal = None
        self.IgnoreSIGPIPE = None
        # Watchdog
        self.WatchdogUSec = None
        self.WatchdogTimestampMonotonic = None
        # File Descriptors
        self.FileDescriptorStoreMax = None
        self.NFileDescriptorStore = None
        self.FileDescriptorStorePreserve = None
        # OOM (Out Of Memory)
        self.OOMPolicy = None
        self.OOMScoreAdjust = None
        self.ManagedOOMSwap = None
        self.ManagedOOMMemoryPressure = None
        self.ManagedOOMMemoryPressureLimit = None
        self.ManagedOOMMemoryPressureDurationUSec = None
        self.ManagedOOMPreference = None
        # Memory Pressure
        self.MemoryPressureWatch = None
        self.MemoryPressureThresholdUSec = None
        # Coredump
        self.CoredumpReceive = None
        self.CoredumpFilter = None
        # Runtime Limits
        self.RuntimeMaxUSec = None
        self.RuntimeRandomizedExtraUSec = None
        # System Calls
        self.SystemCallErrorNumber = None
        # Conditions and Assertions
        self.ConditionResult = None
        self.AssertResult = None
        # Misc Flags
        self.SurviveFinalKillSignal = None
        self.RootDirectoryStartOnly = None
        self.SameProcessGroup = None
        self.UtmpMode = None
        self.RootEphemeral = None
        # NUMA Policy
        self.NUMAPolicy = None
        # Timer Slack
        self.TimerSlackNSec = None
        # Standard Streams
        self.StandardInput = None
        self.StandardOutput = None
        self.StandardError = None
        self.NonBlocking = None
        # TTY Settings
        self.TTYReset = None
        self.TTYVHangup = None
        self.TTYVTDisallocate = None
        # Logging and Syslog
        self.SyslogPriority = None
        self.SyslogLevelPrefix = None
        self.SyslogLevel = None
        self.SyslogFacility = None
        self.LogLevelMax = None
        self.LogRateLimitIntervalUSec = None
        self.LogRateLimitBurst = None
        # Collect Mode
        self.CollectMode = None
        self.DebugInvocation = None
        self.InvocationID = None
        # Need Daemon Reload
        self.NeedDaemonReload = None
        # KSM (Kernel Samepage Merging)
        self.MemoryKSM = None
        # Image Policies
        self.RootImagePolicy = None
        self.MountImagePolicy = None
        self.ExtensionImagePolicy = None
        # Resource Limits (ulimit)
        self.LimitCPU = None
        self.LimitCPUSoft = None
        self.LimitFSIZE = None
        self.LimitFSIZESoft = None
        self.LimitDATA = None
        self.LimitDATASoft = None
        self.LimitSTACK = None
        self.LimitSTACKSoft = None
        self.LimitCORE = None
        self.LimitCORESoft = None
        self.LimitRSS = None
        self.LimitRSSSoft = None
        self.LimitNOFILE = None
        self.LimitNOFILESoft = None
        self.LimitAS = None
        self.LimitASSoft = None
        self.LimitNPROC = None
        self.LimitNPROCSoft = None
        self.LimitMEMLOCK = None
        self.LimitMEMLOCKSoft = None
        self.LimitLOCKS = None
        self.LimitLOCKSSoft = None
        self.LimitSIGPENDING = None
        self.LimitSIGPENDINGSoft = None
        self.LimitMSGQUEUE = None
        self.LimitMSGQUEUESoft = None
        self.LimitNICE = None
        self.LimitNICESoft = None
        self.LimitRTPRIO = None
        self.LimitRTPRIOSoft = None
        self.LimitRTTIME = None
        self.LimitRTTIMESoft = None
        # Notify Access
        self.NotifyAccess = None
        self.DevicePolicy = None
        
def show_full(service_name: str) -> ShowModel:
    import re
    import subprocess

    sm = ShowModel()

    result = subprocess.run(
        ['systemctl', 'show', service_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False
    )

    pattern = re.compile(r"([^=]+)=(.*)")

    for line in result.stdout.splitlines():
        match = pattern.match(line)
        if not match:
            continue
        key, value = match.group(1), match.group(2)
        if hasattr(sm, key):
            setattr(sm, key, value)

    return sm
