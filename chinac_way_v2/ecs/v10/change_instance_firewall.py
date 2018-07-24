import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class ChangeInstanceFirewall(RpcRequest):
    def __init__(self):
        super(ChangeInstanceFirewall, self).__init__('Ecs', '1.0', 'ChangeInstanceFirewall')

    def get_id(self):
        return self.get_query_params().get('Id')

    def set_id(self, id):
        self.add_query_params('Id', id)

    def get_firewall_id(self):
        return self.get_query_params().get('FirewallId')

    def set_firewall_id(self, firewall_id):
        self.add_query_params('FirewallId', firewall_id)
