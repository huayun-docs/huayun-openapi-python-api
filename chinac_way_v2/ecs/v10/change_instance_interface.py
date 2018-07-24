import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class ChangeInstanceInterface(RpcRequest):
    def __init__(self):
        super(ChangeInstanceInterface, self).__init__('Ecs', '1.0', 'ChangeInstanceInterface')

    def get_instance_id(self):
        return self.get_query_params().get('InstanceId')

    def set_instance_id(self, instance_id):
        self.add_query_params('InstanceId', instance_id)

    def get_old_network_id(self):
        return self.get_query_params().get('OldNetworkId')

    def set_old_network_id(self, old_network_id):
        self.add_query_params('OldNetworkId', old_network_id)

    def get_new_network_id(self):
        return self.get_query_params().get('NewNetworkId')

    def set_new_network_id(self, new_network_id):
        self.add_query_params('NewNetworkId', new_network_id)

    def get_network_ip_address(self):
        return self.get_query_params().get('NetworkIpAddress')

    def set_network_ip_address(self, network_ip_address):
        self.add_query_params('NetworkIpAddress', network_ip_address)
