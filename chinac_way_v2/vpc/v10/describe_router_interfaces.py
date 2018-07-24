import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class DescribeRouterInterfaces(RpcRequest):
    def __init__(self):
        super(DescribeRouterInterfaces, self).__init__('Vpc', '1.0', 'DescribeRouterInterfaces')

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

    def get_router_id0(self):
        return self.get_query_params().get('RouterId.0')

    def set_router_id0(self, router_id0):
        self.add_query_params('RouterId.0', router_id0)

    def get_ip_address0(self):
        return self.get_query_params().get('IpAddress.0')

    def set_ip_address0(self, ip_address0):
        self.add_query_params('IpAddress.0', ip_address0)

    def get_network_id0(self):
        return self.get_query_params().get('NetworkId.0')

    def set_network_id0(self, network_id0):
        self.add_query_params('NetworkId.0', network_id0)
