import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class ChangeInstancePassword(RpcRequest):
    def __init__(self):
        super(ChangeInstancePassword, self).__init__('Ecs', '1.0', 'ChangeInstancePassword')

    def get_id(self):
        return self.get_query_params().get('Id')

    def set_id(self, id):
        self.add_query_params('Id', id)

    def get_password(self):
        return self.get_query_params().get('Password')

    def set_password(self, password):
        self.add_query_params('Password', password)
