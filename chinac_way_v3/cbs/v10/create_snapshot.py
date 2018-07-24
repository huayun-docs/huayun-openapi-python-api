import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class CreateSnapshot(RpcRequest):
    def __init__(self):
        super(CreateSnapshot, self).__init__('Cbs', '1.0', 'CreateSnapshot')

    def get_volume_id(self):
        return self.get_query_params().get('VolumeId')

    def set_volume_id(self, volume_id):
        self.add_query_params('VolumeId', volume_id)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_description(self):
        return self.get_query_params().get('Description')

    def set_description(self, description):
        self.add_query_params('Description', description)

    def get_create_type(self):
        return self.get_query_params().get('CreateType')

    def set_create_type(self, create_type):
        self.add_query_params('CreateType', create_type)
