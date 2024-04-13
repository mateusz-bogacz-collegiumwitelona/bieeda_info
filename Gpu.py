# Gpu.py
import wmi


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
