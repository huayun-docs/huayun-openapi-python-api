import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class CreateRouter(RpcRequest):
    def __init__(self):
        super(CreateRouter, self).__init__('Vpc', '1.0', 'CreateRouter')

    def get_pay_type(self):
        return self.get_query_params().get('PayType')

    def set_pay_type(self, pay_type):
        self.add_query_params('PayType', pay_type)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_description(self):
        return self.get_query_params().get('Description')

    def set_description(self, description):
        self.add_query_params('Description', description)

    def get_firewall_id(self):
        return self.get_query_params().get('FirewallId')

    def set_firewall_id(self, firewall_id):
        self.add_query_params('FirewallId', firewall_id)

    def get_interface0network_id(self):
        return self.get_query_params().get('Interface.0.NetworkId')

    def set_interface0network_id(self, interface0network_id):
        self.add_query_params('Interface.0.NetworkId', interface0network_id)

    def get_period(self):
        return self.get_query_params().get('Period')

    def set_period(self, period):
        self.add_query_params('Period', period)
