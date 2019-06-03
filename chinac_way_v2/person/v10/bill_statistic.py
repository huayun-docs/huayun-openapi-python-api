import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class BillStatistic(RpcRequest):
    def __init__(self):
        super(BillStatistic, self).__init__('Person', '2.0', 'BillStatistic')

    def get_dates(self):
        return self.get_query_params().get('Dates')

    def set_dates(self, dates):
        self.add_query_params('Dates', dates)
