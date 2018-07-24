import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class DescribeInstances(RpcRequest):
    def __init__(self):
        super(DescribeInstances, self).__init__('Ecs', '1.0', 'DescribeInstances')

    def get_id0(self):
        return self.get_query_params().get('Id0')

    def set_id0(self, id0):
        self.add_query_params('Id0', id0);

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name);

    def get_status(self):
        return self.get_query_params().get('Status')

    def set_status(self, status):
        self.add_query_params('Status', status);

    def get_firewallId0(self):
        return self.get_query_params().get('FirewallId0')

    def set_firewallId0(self, firewallId0):
        self.add_query_params('FirewallId0', firewallId0);

    def get_start_time(self):
        return self.get_query_params().get('StartTime')

    def set_start_time(self, start_time):
        self.add_query_params('StartTime', start_time);

    def get_end_time(self):
        return self.get_query_params().get('EndTime')

    def set_end_time(self, end_time):
        self.add_query_params('EndTime', end_time);

    def get_due_start_time(self):
        return self.get_query_params().get('DueStartTime')

    def set_due_start_time(self, due_start_time):
        self.add_query_params('DueStartTime', due_start_time);

    def get_due_end_time(self):
        return self.get_query_params().get('DueEndTime')

    def set_due_end_time(self, due_end_time):
        self.add_query_params('DueEndTime', due_end_time);

    def get_product_status(self):
        return self.get_query_params().get('ProductStatus')

    def set_product_status(self, product_status):
        self.add_query_params('ProductStatus', product_status);

    def get_pay_type(self):
        return self.get_query_params().get('PayType')

    def set_pay_type(self, pay_type):
        self.add_query_params('PayType', pay_type);

    def get_image_id(self):
        return self.get_query_params().get('ImageId')

    def set_image_id(self, image_id):
        self.add_query_params('ImageId', image_id);

    def get_offset(self):
        return self.get_query_params().get('Offset')

    def set_offset(self, offset):
        self.add_query_params('Offset', offset);

    def get_count(self):
        return self.get_query_params().get('Count')

    def set_count(self, count):
        self.add_query_params('Count', count);

    def get_instance_series(self):
        return self.get_query_params().get('InstanceSeries')

    def set_instance_series(self, instance_series):
        self.add_query_params('InstanceSeries', instance_series);
