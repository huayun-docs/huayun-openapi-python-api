import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class AssignRouterEip(RpcRequest):
    def __init__(self):
        super(AssignRouterEip, self).__init__('Vpc', '1.0', 'AssignRouterEip')

    def get_router_id(self):
        return self.get_query_params().get('RouterId')

    def set_router_id(self, router_id):
        self.add_query_params('RouterId', router_id)

    def get_eip(self):
        return self.get_query_params().get('Eip')

    def set_eip(self, eip):
        self.add_query_params('Eip', eip)
