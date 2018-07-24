import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class DisablePortForwardingRules(RpcRequest):
    def __init__(self):
        super(DisablePortForwardingRules, self).__init__('Vpc', '1.0', 'DisablePortForwardingRules')

    def get_id0(self):
        return self.get_query_params().get('Id.0')

    def set_id0(self, id0):
        self.add_query_params('Id.0', id0)
