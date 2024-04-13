# Cpu.py
import cpuinfo
import platform


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


