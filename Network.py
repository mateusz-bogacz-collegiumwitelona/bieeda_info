# Network.py
import wmi


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
