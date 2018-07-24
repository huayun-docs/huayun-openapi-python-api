import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class ResizeVolume(RpcRequest):
    def __init__(self):
        super(ResizeVolume, self).__init__('Cbs', '1.0', 'ResizeVolume')

    def get_id(self):
        return self.get_query_params().get('Id')

    def set_id(self, id):
        self.add_query_params('Id', id)

    def get_size(self):
        return self.get_query_params().get('Size')

    def set_size(self, size):
        self.add_query_params('Size', size)
