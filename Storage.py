# Storage.py

import wmi


class Storage:
    def __init__(self):
        self.c = wmi.WMI()

    def get_disk_names(self):
        try:
            # Query Win32_DiskDrive class to get disk names
            disks = self.c.Win32_DiskDrive()
            disk_names = [disk.Caption for disk in disks]
            return disk_names
        except Exception:
            return None  # Handle exceptions

    def get_disk_sizes(self):
        try:
            # Query Win32_DiskDrive class to get disk sizes
            disks = self.c.Win32_DiskDrive()
            disk_sizes = [round(int(disk.Size) / (1024 ** 3)) for disk in disks]
            return disk_sizes
        except Exception:
            return None  # Handle exceptions

    def get_disk_types(self):
        try:
            # Query Win32_DiskDrive class to get disk types
            disks = self.c.Win32_DiskDrive()
            disk_types = []
            for disk in disks:
                if disk.MediaType == "Fixed hard disk media":
                    disk_types.append("SSD")
                elif disk.MediaType == "Removable media":
                    disk_types.append("HDD")
                else:
                    disk_types.append("Unknown")
            return disk_types
        except Exception:
            return None  # Handle exceptions
