import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class DetachKeyPair(RpcRequest):
    def __init__(self):
        super(DetachKeyPair, self).__init__('Ecs', '1.0', 'DetachKeyPair')

    def get_key_pair_id(self):
        return self.get_query_params().get('KeyPairId')

    def set_key_pair_id(self, key_pair_id):
        self.add_query_params('KeyPairId', key_pair_id)

    def get_instance_id(self):
        return self.get_query_params().get('InstanceId')

    def set_instance_id(self, instance_id):
        self.add_query_params('InstanceId', instance_id)
