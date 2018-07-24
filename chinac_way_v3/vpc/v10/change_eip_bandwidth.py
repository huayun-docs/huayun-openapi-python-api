import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class ChangeEipBandwidth(RpcRequest):
    def __init__(self):
        super(ChangeEipBandwidth, self).__init__('Vpc', '1.0', 'ChangeEipBandwidth')

    def get_eip(self):
        return self.get_query_params().get('Eip')

    def set_eip(self, eip):
        self.add_query_params('Eip', eip)

    def get_bandwidth(self):
        return self.get_query_params().get('Bandwidth')

    def set_bandwidth(self, bandwidth):
        self.add_query_params('Bandwidth', bandwidth)
