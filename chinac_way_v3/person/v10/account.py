import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class Account(RpcRequest):
    def __init__(self):
        super(Account, self).__init__('Person', '2.0', 'Account')
