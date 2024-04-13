# Motherboard.py

import subprocess


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
