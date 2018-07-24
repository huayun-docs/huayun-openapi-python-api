import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class DescribeRouters(RpcRequest):
    def __init__(self):
        super(DescribeRouters, self).__init__('Vpc', '1.0', 'DescribeRouters')

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

    def get_name0(self):
        return self.get_query_params().get('Name.0')

    def set_name0(self, name0):
        self.add_query_params('Name.0', name0)

    def get_eip(self):
        return self.get_query_params().get('Eip')

    def set_eip(self, eip):
        self.add_query_params('Eip', eip)

    def get_start_time(self):
        return self.get_query_params().get('StartTime')

    def set_start_time(self, start_time):
        self.add_query_params('StartTime', start_time)

    def get_end_time(self):
        return self.get_query_params().get('EndTime')

    def set_end_time(self, end_time):
        self.add_query_params('EndTime', end_time)

    def get_product_status(self):
        return self.get_query_params().get('ProductStatus')

    def set_product_status(self, product_status):
        self.add_query_params('ProductStatus', product_status)

    def get_pay_type(self):
        return self.get_query_params().get('PayType')

    def set_pay_type(self, pay_type):
        self.add_query_params('PayType', pay_type)

    def get_locked(self):
        return self.get_query_params().get('Locked')

    def set_locked(self, locked):
        self.add_query_params('Locked', locked)
