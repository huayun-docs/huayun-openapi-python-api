import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class AssociateEip(RpcRequest):
    def __init__(self):
        super(AssociateEip, self).__init__('Vpc', '1.0', 'AssociateEip')

    def get_eip(self):
        return self.get_query_params().get('Eip')

    def set_eip(self, eip):
        self.add_query_params('Eip', eip)

    def get_local_ip_address(self):
        return self.get_query_params().get('LocalIpAddress')

    def set_local_ip_address(self, local_ip_address):
        self.add_query_params('LocalIpAddress', local_ip_address)

    def get_local_network_id(self):
        return self.get_query_params().get('LocalNetworkId')

    def set_local_network_id(self, local_network_id):
        self.add_query_params('LocalNetworkId', local_network_id)

    def get_router_id(self):
        return self.get_query_params().get('RouterId')

    def set_router_id(self, router_id):
        self.add_query_params('RouterId', router_id)
