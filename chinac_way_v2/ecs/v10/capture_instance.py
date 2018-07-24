import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class CaptureInstance(RpcRequest):
    def __init__(self):
        super(CaptureInstance, self).__init__('Ecs', '1.0', 'CaptureInstance')

    def get_instance_id(self):
        return self.get_query_params().get('InstanceId')

    def set_instance_id(self, instance_id):
        self.add_query_params('InstanceId', instance_id)

    def get_volumeType0(self):
        return self.get_query_params().get('VolumeType.0')

    def set_volumeType0(self, volumeType0):
        self.add_query_params('VolumeType.0', volumeType0)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_description(self):
        return self.get_query_params().get('Description')

    def set_description(self, description):
        self.add_query_params('Description', description)
