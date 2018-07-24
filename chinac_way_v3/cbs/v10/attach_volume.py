import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class AttachVolume(RpcRequest):
    def __init__(self):
        super(AttachVolume, self).__init__('Cbs', '1.0', 'AttachVolume')

    def get_volume_id(self):
        return self.get_query_params().get('VolumeId')

    def set_volume_id(self, volume_id):
        self.add_query_params('VolumeId', volume_id)

    def get_instance_id(self):
        return self.get_query_params().get('InstanceId')

    def set_instance_id(self, instance_id):
        self.add_query_params('InstanceId', instance_id)
