import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class CreateRouterInterface(RpcRequest):
    def __init__(self):
        super(CreateRouterInterface, self).__init__('Vpc', '1.0', 'CreateRouterInterface')

    def get_router_id(self):
        return self.get_query_params().get('RouterId')

    def set_router_id(self, router_id):
        self.add_query_params('RouterId', router_id)

    def get_network_id(self):
        return self.get_query_params().get('NetworkId')

    def set_network_id(self, network_id):
        self.add_query_params('NetworkId', network_id)
