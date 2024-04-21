import wmi

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
