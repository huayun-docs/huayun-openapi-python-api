import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class DissociateEips(RpcRequest):
    def __init__(self):
        super(DissociateEips, self).__init__('Vpc', '1.0', 'DissociateEips')

    def get_eip0(self):
        return self.get_query_params().get('Eip.0')

    def set_eip0(self, eip0):
        self.add_query_params('Eip.0', eip0)
