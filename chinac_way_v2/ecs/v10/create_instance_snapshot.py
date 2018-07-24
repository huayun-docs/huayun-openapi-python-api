import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class CreateInstanceSnapshot(RpcRequest):
    def __init__(self):
        super(CreateInstanceSnapshot, self).__init__('Ecs', '1.0', 'CreateInstanceSnapshot')

    def get_instance_id(self):
        return self.get_query_params().get('InstanceId')

    def set_instance_id(self, instance_id):
        self.add_query_params('InstanceId', instance_id)

    def get_create_type(self):
        return self.get_query_params().get('CreateType')

    def set_create_type(self, create_type):
        self.add_query_params('CreateType', create_type)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_description(self):
        return self.get_query_params().get('Description')

    def set_description(self, description):
        self.add_query_params('Description', description)
