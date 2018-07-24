import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class AllocateEips(RpcRequest):
    def __init__(self):
        super(AllocateEips, self).__init__('Vpc', '1.0', 'AllocateEips')

    def get_bandwidth(self):
        return self.get_query_params().get('Bandwidth')

    def set_bandwidth(self, bandwidth):
        self.add_query_params('Bandwidth', bandwidth)

    def get_pay_type(self):
        return self.get_query_params().get('PayType')

    def set_pay_type(self, pay_type):
        self.add_query_params('PayType', pay_type)

    def get_period(self):
        return self.get_query_params().get('Period')

    def set_period(self, period):
        self.add_query_params('Period', period)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_eip_type(self):
        return self.get_query_params().get('EipType')

    def set_eip_type(self, eip_type):
        self.add_query_params('EipType', eip_type)
