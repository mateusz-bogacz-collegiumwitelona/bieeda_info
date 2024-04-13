#Audio.py

import wmi

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
        except wmi.x_wmi as e:
            # Handle WMI exceptions
            return None
