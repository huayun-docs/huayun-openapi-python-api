import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class DescribeKeyPairs(RpcRequest):
    def __init__(self):
        super(DescribeKeyPairs, self).__init__('Ecs', '1.0', 'DescribeKeyPairs')

    def get_id0(self):
        return self.get_query_params().get('Id.0')

    def set_id0(self, id0):
        self.add_query_params('Id.0', id0)

    def get_name0(self):
        return self.get_query_params().get('Name.0')

    def set_name0(self, name0):
        self.add_query_params('Name.0', name0)

    def get_offset(self):
        return self.get_query_params().get('Offset')

    def set_offset(self, offset):
        self.add_query_params('Offset', offset)

    def get_count(self):
        return self.get_query_params().get('Count')

    def set_count(self, count):
        self.add_query_params('Count', count)
