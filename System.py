# System.py

import wmi


class System(object):
    def __init__(self):
        self.c = wmi.WMI()

    def Get_System_caption(self):
        try:
            # Query Win32_OperatingSystem class to get OS information
            os_info = self.c.Win32_OperatingSystem()[0]
            return os_info.Caption
        except Exception:
            return None  # Handle exceptions

    def Get_System_version(self):
        try:
            # Query Win32_OperatingSystem class to get OS information
            os_info = self.c.Win32_OperatingSystem()[0]
            return os_info.Version
        except Exception:
            return None  # Handle exceptions
