import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class DescribeEips(RpcRequest):
    def __init__(self):
        super(DescribeEips, self).__init__('Vpc', '1.0', 'DescribeEips')

    def get_offset(self):
        return self.get_query_params().get('Offset')

    def set_offset(self, offset):
        self.add_query_params('Offset', offset)

    def get_count(self):
        return self.get_query_params().get('Count')

    def set_count(self, count):
        self.add_query_params('Count', count)

    def get_eip0(self):
        return self.get_query_params().get('Eip.0')

    def set_eip0(self, eip0):
        self.add_query_params('Eip.0', eip0)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_status(self):
        return self.get_query_params().get('Status')

    def set_status(self, status):
        self.add_query_params('Status', status)

    def get_start_time(self):
        return self.get_query_params().get('StartTime')

    def set_start_time(self, start_time):
        self.add_query_params('StartTime', start_time)

    def get_end_time(self):
        return self.get_query_params().get('EndTime')

    def set_end_time(self, end_time):
        self.add_query_params('EndTime', end_time)

    def get_allocate_start_time(self):
        return self.get_query_params().get('AllocateStartTime')

    def set_allocate_start_time(self, allocate_start_time):
        self.add_query_params('AllocateStartTime', allocate_start_time)

    def get_allocate_end_time(self):
        return self.get_query_params().get('AllocateEndTime')

    def set_allocate_end_time(self, allocate_end_time):
        self.add_query_params('AllocateEndTime', allocate_end_time)

    def get_product_status(self):
        return self.get_query_params().get('ProductStatus')

    def set_product_status(self, product_status):
        self.add_query_params('ProductStatus', product_status)

    def get_pay_type(self):
        return self.get_query_params().get('PayType')

    def set_pay_type(self, pay_type):
        self.add_query_params('PayType', pay_type)
