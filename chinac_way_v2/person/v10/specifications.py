import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class Specifications(RpcRequest):
    def __init__(self):
        super(Specifications, self).__init__('Person', '2.0', 'Specifications')
