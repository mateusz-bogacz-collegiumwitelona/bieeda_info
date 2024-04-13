# Gui.py

import tkinter as tk
from tkinter import ttk, filedialog

from Audio import Audio
from Cpu import CPU
from Gpu import GraphicsCard
from Optical_drivers import Optical_drivers
from Ram import Ram
from System import System
from Motherboard import Motherboard
from Storage import Storage
from Network import Network


class SystemInfoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bieda info")

        # Create the main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Labels to display system information
        # Processor
        self.cpu_title_label = ttk.Label(self.main_frame, text="Processor:")
        self.cpu_title_label.grid(row=0, column=0, sticky="w")
        self.cpu_label = ttk.Label(self.main_frame, text="")
        self.cpu_label.grid(row=0, column=1, sticky="w")

        # Graphics Card
        self.gpu_title_label = ttk.Label(self.main_frame, text="Graphics Card:")
        self.gpu_title_label.grid(row=1, column=0, sticky="w")
        self.gpu_label = ttk.Label(self.main_frame, text="")
        self.gpu_label.grid(row=1, column=1, sticky="w")

        # RAM
        self.ram_title_label = ttk.Label(self.main_frame, text="RAM:")
        self.ram_title_label.grid(row=2, column=0, sticky="w")
        self.ram_label = ttk.Label(self.main_frame, text="")
        self.ram_label.grid(row=2, column=1, sticky="w")

        # System
        self.system_title_label = ttk.Label(self.main_frame, text="System:")
        self.system_title_label.grid(row=3, column=0, sticky="w")
        self.system_label = ttk.Label(self.main_frame, text="")
        self.system_label.grid(row=3, column=1, sticky="w")

        # Motherboard
        self.board_title_label = ttk.Label(self.main_frame, text="Motherboard:")
        self.board_title_label.grid(row=4, column=0, sticky="w")
        self.board_label = ttk.Label(self.main_frame, text="")
        self.board_label.grid(row=4, column=1, sticky="w")

        # Storage
        self.storage_title_label = ttk.Label(self.main_frame, text="Storage:")
        self.storage_title_label.grid(row=5, column=0, sticky="w")
        self.storage_label = ttk.Label(self.main_frame, text="")
        self.storage_label.grid(row=5, column=1, sticky="w")

        # Optical Drivers
        self.optical_title_label = ttk.Label(self.main_frame, text="Optical Drivers:")
        self.optical_title_label.grid(row=6, column=0, sticky="w")
        self.optical_label = ttk.Label(self.main_frame, text="")
        self.optical_label.grid(row=6, column=1, sticky="w")

        # Audio Devices
        self.audio_title_label = ttk.Label(self.main_frame, text="Audio Devices:")
        self.audio_title_label.grid(row=7, column=0, sticky="w")
        self.audio_label = ttk.Label(self.main_frame, text="")
        self.audio_label.grid(row=7, column=1, sticky="w")

        # Network
        self.network_title_label = ttk.Label(self.main_frame, text="Network information:")
        self.network_title_label.grid(row=6, column=0, sticky="w")
        self.network_label = ttk.Label(self.main_frame, text="")
        self.network_label.grid(row=6, column=1, sticky="w")

        # Button to export information to a file
        self.export_button = ttk.Button(self.main_frame, text="Export to File", command=self.export_to_file)
        self.export_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Display system information when the app starts
        self.display_info()

    # Method to display system information
    def display_info(self):
        # Instantiate classes for system components
        cpu_instance = CPU()
        gpu_instance = GraphicsCard()
        ram_instance = Ram()
        system_instance = System()
        board_instance = Motherboard()
        storage_instance = Storage()
        optical_instance = Optical_drivers()
        audio_instance = Audio()
        network_instance = Network()

        # Update labels with retrieved information
        self.cpu_label.config(text=cpu_instance.get_cpu_info() if cpu_instance else "N/A")
        self.gpu_label.config(text=gpu_instance.get_graphics_card_name() if gpu_instance else "N/A")
        self.ram_label.config(
            text=f"{round(ram_instance.get_ram_size())} GB = {ram_instance.count_memory_modules()} * {ram_instance.get_modules_size()} GB" if ram_instance else "N/A")
        self.system_label.config(text=system_instance.Get_System_caption() if system_instance else "N/A")
        self.board_label.config(text=str(board_instance.get_motherboard()) if board_instance else "N/A")

        # Retrieve and format storage information
        storage_info = ""
        if storage_instance:
            disk_names = storage_instance.get_disk_names()
            disk_sizes = storage_instance.get_disk_sizes()
            disk_types = storage_instance.get_disk_types()
            for name, size, disk_type in zip(disk_names, disk_sizes, disk_types):
                storage_info += f"{name}  {size} GB ({disk_type})\n"
        self.storage_label.config(text=storage_info if storage_info else "N/A")

        # Display optical drivers information
        self.optical_label.config(text=str(optical_instance.get_optical_drivers()) if optical_instance else "N/A")

        # Retrieve and format audio devices information
        audio_info = ""
        if audio_instance:
            audio_devices = audio_instance.get_audio_devices()
            for device in audio_devices:
                audio_info += f"{device}\n"
        self.audio_label.config(text=audio_info if audio_info else "N/A")

        # Display Network information
        network_info = ""
        if network_instance:
            network_devices = network_instance.get_network_card_name()
            ip_address = network_instance.get_network_ip_address()
            subnet_mask = network_instance.get_network_subnet_mask()
            network_geteway = network_instance.get_network_gateway()
            for device, ip, mask, geteway in zip(network_devices, ip_address, subnet_mask, network_geteway):
                network_info += (f"{device} \n"
                                 f"    Address:{ip} \n"
                                 f"    SubnetMask: {mask} \n"
                                 f"    Gateway: {geteway} \n")
        self.network_label.config(text=network_info if network_info else "N/A")

    # Method to export information to a file
    def export_to_file(self):
        # Open file dialog to choose save location
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            # Write system information to the selected file
            with open(file_path, "w") as file:
                file.write("System Information\n\n")
                file.write("Processor: " + self.cpu_label.cget("text") + "\n")
                file.write("Graphics Card: " + self.gpu_label.cget("text") + "\n")
                file.write("RAM: " + self.ram_label.cget("text") + "\n")
                file.write("System: " + self.system_label.cget("text") + "\n")
                file.write("Motherboard: " + self.board_label.cget("text") + "\n")
                file.write("Storage: " + self.storage_label.cget("text") + "\n")
                file.write("Optical Drivers: " + self.optical_label.cget("text") + "\n")
                file.write("Audio Devices: " + self.audio_label.cget("text") + "\n")
                file.write("Network:" + self.network_label.cget("text") + "\n")
