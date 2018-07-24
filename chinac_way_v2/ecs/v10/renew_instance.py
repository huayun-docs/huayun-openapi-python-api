import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class RenewInstance(RpcRequest):
    def __init__(self):
        super(RenewInstance, self).__init__('Ecs', '1.0', 'RenewInstance')

    def get_id(self):
        return self.get_query_params().get('Id')

    def set_id(self, id):
        self.add_query_params('Id', id)

    def get_period(self):
        return self.get_query_params().get('Period')

    def set_period(self, period):
        self.add_query_params('Period', period)

    def get_pay_type(self):
        return self.get_query_params().get('PayType')

    def set_pay_type(self, pay_type):
        self.add_query_params('PayType', pay_type)
