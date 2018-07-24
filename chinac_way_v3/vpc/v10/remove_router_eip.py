import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class RemoveRouterEip(RpcRequest):
    def __init__(self):
        super(RemoveRouterEip, self).__init__('Vpc', '1.0', 'RemoveRouterEip')

    def get_router_id(self):
        return self.get_query_params().get('RouterId')

    def set_router_id(self, router_id):
        self.add_query_params('RouterId', router_id)
