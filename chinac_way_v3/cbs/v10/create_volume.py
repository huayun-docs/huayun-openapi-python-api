import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class CreateVolume(RpcRequest):
    def __init__(self):
        super(CreateVolume, self).__init__('Cbs', '1.0', 'CreateVolume')

    def get_pay_type(self):
        return self.get_query_params().get('PayType')

    def set_pay_type(self, pay_type):
        self.add_query_params('PayType', pay_type)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_describe(self):
        return self.get_query_params().get('Describe')

    def set_describe(self, describe):
        self.add_query_params('Describe', describe)

    def get_size(self):
        return self.get_query_params().get('Size')

    def set_size(self, size):
        self.add_query_params('Size', size)

    def get_type(self):
        return self.get_query_params().get('Type')

    def set_type(self, gtype):
        self.add_query_params('Type', gtype)

    def get_snapshot_id(self):
        return self.get_query_params().get('SnapshotId')

    def set_snapshot_id(self, snapshot_id):
        self.add_query_params('SnapshotId', snapshot_id)

    def get_source_volume_id(self):
        return self.get_query_params().get('SourceVolumeId')

    def set_source_volume_id(self, source_volume_id):
        self.add_query_params('SourceVolumeId', source_volume_id)

    def get_image_id(self):
        return self.get_query_params().get('ImageId')

    def set_image_id(self, image_id):
        self.add_query_params('ImageId', image_id)

    def get_period(self):
        return self.get_query_params().get('Period')

    def set_period(self, period):
        self.add_query_params('Period', period)
