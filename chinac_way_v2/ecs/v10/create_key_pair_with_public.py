import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class CreateKeyPairWithPublic(RpcRequest):
    def __init__(self):
        super(CreateKeyPairWithPublic, self).__init__('Ecs', '1.0', 'CreateKeyPairWithPublic')

    def get_public_key(self):
        return self.get_query_params().get('PublicKey')

    def set_public_key(self, public_key):
        self.add_query_params('PublicKey', public_key)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_description(self):
        return self.get_query_params().get('Description')

    def set_description(self, description):
        self.add_query_params('Description', description)
