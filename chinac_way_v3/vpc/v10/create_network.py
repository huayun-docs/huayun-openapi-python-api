import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class CreateNetwork(RpcRequest):
    def __init__(self):
        super(CreateNetwork, self).__init__('Vpc', '1.0', 'CreateNetwork')

    def get_cidr(self):
        return self.get_query_params().get('Cidr')

    def set_cidr(self, cidr):
        self.add_query_params('Cidr', cidr)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_description(self):
        return self.get_query_params().get('Description')

    def set_description(self, description):
        self.add_query_params('Description', description)

    def get_ip_start(self):
        return self.get_query_params().get('IpStart')

    def set_ip_start(self, ip_start):
        self.add_query_params('IpStart', ip_start)

    def get_ip_end(self):
        return self.get_query_params().get('IpEnd')

    def set_ip_end(self, ip_end):
        self.add_query_params('IpEnd', ip_end)

    def get_dhcp(self):
        return self.get_query_params().get('Dhcp')

    def set_dhcp(self, dhcp):
        self.add_query_params('Dhcp', dhcp)

    def get_gateway(self):
        return self.get_query_params().get('Gateway')

    def set_gateway(self, gateway):
        self.add_query_params('Gateway', gateway)
