import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class CreateKeyPair(RpcRequest):
    def __init__(self):
        super(CreateKeyPair, self).__init__('Ecs', '1.0', 'CreateKeyPair')

    def get_encryption(self):
        return self.get_query_params().get('Encryption')

    def set_encryption(self, encryption):
        self.add_query_params('Encryption', encryption)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_description(self):
        return self.get_query_params().get('Description')

    def set_description(self, description):
        self.add_query_params('Description', description)
