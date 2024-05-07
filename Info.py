# Info.py

import wmi
import cpuinfo
import platform
import subprocess


# Audio
class Audio:
    def __init__(self):
        self.c = wmi.WMI()

    def get_audio_devices(self):
        try:
            # Query Win32_SoundDevice class to get audio devices information
            audio_devices = self.c.Win32_SoundDevice()
            device_info = []
            # Extract device names from the queried information
            for device in audio_devices:
                device_info.append(device.Name)
            return device_info
        except wmi.x_wmi:
            # Handle WMI exceptions
            return None


# Cpu
class CPU:
    @staticmethod
    def get_cpu_info():
        try:
            # Retrieve CPU information using cpuinfo library
            cpu_info = cpuinfo.get_cpu_info()
            # Extract the CPU model name
            model = cpu_info.get('brand_raw', None)
            return model
        except cpuinfo.UnexpectedException:
            # Handle unexpected exceptions
            return None

    @staticmethod
    def get_arch():
        try:
            # Retrieve CPU architecture using platform module
            arch = platform.architecture()[0]
            return arch
        except Exception:
            # Handle exceptions
            return None


# Gup
class GraphicsCard:
    def __init__(self):
        self.c = wmi.WMI()

    def get_graphics_card_name(self):
        try:
            # Query Win32_VideoController class to get graphics card information
            for gpu in self.c.Win32_VideoController():
                return gpu.Name
        except wmi.x_wmi:
            return None  # Handle WMI exceptions


# Motherboard
class Motherboard:
    def __init__(self):
        self.result = subprocess.check_output("wmic baseboard get product, manufacturer, version, serialnumber",
                                              shell=True)

    def get_motherboard(self):
        try:
            # Execute the command to get motherboard information using subprocess
            result = self.result.decode("utf-8")
            lines = result.strip().split("\n")
            motherboard_info = {}
            for line in lines[1:]:
                elements = line.split()
                # Extract relevant information from the command output
                if len(elements) >= 4:
                    motherboard_info = elements[0] + " " + elements[1]
            return motherboard_info
        except Exception:
            return None  # Handle exceptions


# Netowrk
class Network:
    def __init__(self):
        self.c = wmi.WMI()
        self.network = self.c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

    def get_network_card_name(self):
        try:
            network_card_name = []

            for adapter in self.network:
                adapter_name = adapter.Description
                network_card_name.append(adapter_name)

            return network_card_name

        except Exception:
            return None

    def get_network_ip_address(self):
        try:
            network_ip_address = []
            for address in self.network:
                ip_address = address.IPAddress[0] if address.IPAddress else None
                network_ip_address.append(ip_address)
            return network_ip_address
        except Exception:
            return None

    def get_network_subnet_mask(self):
        try:
            network_subnet_mask = []
            for mask in self.network:
                network_mask = mask.IPSubnet[0] if mask.IPSubnet else None
                network_subnet_mask.append(network_mask)
            return network_subnet_mask
        except Exception:
            return None

    def get_network_gateway(self):
        try:
            network_gateway = []
            for gateway in self.network:
                ip_gateway = gateway.DefaultIPGateway[0] if gateway.DefaultIPGateway else None
                network_gateway.append(ip_gateway)
            return network_gateway
        except Exception:
            return None


# Optical_drivers
class Optical_drivers:
    def __init__(self):
        self.c = wmi.WMI()
        self.optical_drivers = self.c.Win32_CDROMDrive()

    def get_optical_drivers(self):
        try:
            optical_drivers = self.c.Win32_CDROMDrive()
            driver_list = []
            for drive in optical_drivers:
                driver_info = {
                    'Name': drive.Name,
                    'Drive': drive.Drive,
                    'MediaLoaded': drive.MediaLoaded,
                    'MediaType': drive.MediaType
                }
                driver_list.append(driver_info)
            return driver_list
        except Exception:
            return False


# Ram
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


# Storage
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


# System
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
