import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class DeleteKeyPair(RpcRequest):
    def __init__(self):
        super(DeleteKeyPair, self).__init__('Ecs', '1.0', 'DeleteKeyPair')

    def get_id(self):
        return self.get_query_params().get('Id')

    def set_id(self, id):
        self.add_query_params('Id', id)
