import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class CreateFirewallRule(RpcRequest):
    def __init__(self):
        super(CreateFirewallRule, self).__init__('Vpc', '1.0', 'CreateFirewallRule')

    def get_firewall_id(self):
        return self.get_query_params().get('FirewallId')

    def set_firewall_id(self, firewall_id):
        self.add_query_params('FirewallId', firewall_id)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_direction(self):
        return self.get_query_params().get('Direction')

    def set_direction(self, direction):
        self.add_query_params('Direction', direction)

    def get_port_start(self):
        return self.get_query_params().get('PortStart')

    def set_port_start(self, port_start):
        self.add_query_params('PortStart', port_start)

    def get_port_end(self):
        return self.get_query_params().get('PortEnd')

    def set_port_end(self, port_end):
        self.add_query_params('PortEnd', port_end)

    def get_protocol(self):
        return self.get_query_params().get('Protocol')

    def set_protocol(self, protocol):
        self.add_query_params('Protocol', protocol)

    def get_priority(self):
        return self.get_query_params().get('Priority')

    def set_priority(self, priority):
        self.add_query_params('Priority', priority)

    def get_remote_ip_prefix(self):
        return self.get_query_params().get('RemoteIpPrefix')

    def set_remote_ip_prefix(self, remote_ip_prefix):
        self.add_query_params('RemoteIpPrefix', remote_ip_prefix)

    def get_enabled(self):
        return self.get_query_params().get('Enabled')

    def set_enabled(self, enabled):
        self.add_query_params('Enabled', enabled)
