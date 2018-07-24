import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class DescribeFirewallRules(RpcRequest):
    def __init__(self):
        super(DescribeFirewallRules, self).__init__('Vpc', '1.0', 'DescribeFirewallRules')

    def get_offset(self):
        return self.get_query_params().get('Offset')

    def set_offset(self, offset):
        self.add_query_params('Offset', offset)

    def get_count(self):
        return self.get_query_params().get('Count')

    def set_count(self, count):
        self.add_query_params('Count', count)

    def get_firewall_rule(self):
        return self.get_query_params().get('FirewallRule')

    def set_firewall_rule(self, firewall_rule):
        self.add_query_params('FirewallRule', firewall_rule)

    def get_firewall0(self):
        return self.get_query_params().get('Firewall.0')

    def set_firewall0(self, firewall0):
        self.add_query_params('Firewall.0', firewall0)
