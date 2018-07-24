import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class DescribeSnapshots(RpcRequest):
    def __init__(self):
        super(DescribeSnapshots, self).__init__('Cbs', '1.0', 'DescribeSnapshots')

    def get_offset(self):
        return self.get_query_params().get('Offset')

    def set_offset(self, offset):
        self.add_query_params('Offset', offset)

    def get_count(self):
        return self.get_query_params().get('Count')

    def set_count(self, count):
        self.add_query_params('Count', count)

    def get_id0(self):
        return self.get_query_params().get('Id.0')

    def set_id0(self, id0):
        self.add_query_params('Id.0', id0)

    def get_volume_id(self):
        return self.get_query_params().get('VolumeId')

    def set_volume_id(self, volume_id):
        self.add_query_params('VolumeId', volume_id)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_start_time(self):
        return self.get_query_params().get('StartTime')

    def set_start_time(self, start_time):
        self.add_query_params('StartTime', start_time)

    def get_end_time(self):
        return self.get_query_params().get('EndTime')

    def set_end_time(self, end_time):
        self.add_query_params('EndTime', end_time)

    def get_is_locked(self):
        return self.get_query_params().get('IsLocked')

    def set_is_locked(self, is_locked):
        self.add_query_params('IsLocked', is_locked)
