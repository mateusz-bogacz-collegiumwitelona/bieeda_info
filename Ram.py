# Ram.py

import wmi


class Ram:
    def __init__(self):
        self.c = wmi.WMI()

    def get_ram_size(self):
        try:
            # Query Win32_ComputerSystem class to get total physical memory size
            for mem in self.c.Win32_ComputerSystem():
                ram_size = int(mem.TotalPhysicalMemory) / (1024 ** 3)  # Convert total physical memory to GB
                return ram_size
        except wmi.x_wmi:
            return None  # Handle WMI exceptions

    def count_memory_modules(self):
        try:
            # Query Win32_PhysicalMemory class to get information about memory modules
            memory_modules = self.c.Win32_PhysicalMemory()
            return len(memory_modules)  # Return the count of memory modules
        except wmi.x_wmi:
            return None  # Handle WMI exceptions

    def get_modules_size(self):
        try:
            ram = Ram.get_ram_size(self)
            moduls = Ram.count_memory_modules(self)
            modules_size = round(ram) / moduls
            return modules_size
        except Exception:
            return None
