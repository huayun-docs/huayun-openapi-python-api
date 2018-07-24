import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v2.core.rpc_request import RpcRequest


class CreatePortForwardingRule(RpcRequest):
    def __init__(self):
        super(CreatePortForwardingRule, self).__init__('Vpc', '1.0', 'CreatePortForwardingRule')

    def get_router_id(self):
        return self.get_query_params().get('RouterId')

    def set_router_id(self, router_id):
        self.add_query_params('RouterId', router_id)

    def get_protocol(self):
        return self.get_query_params().get('Protocol')

    def set_protocol(self, protocol):
        self.add_query_params('Protocol', protocol)

    def get_external_start_port(self):
        return self.get_query_params().get('ExternalStartPort')

    def set_external_start_port(self, external_start_port):
        self.add_query_params('ExternalStartPort', external_start_port)

    def get_external_end_port(self):
        return self.get_query_params().get('ExternalEndPort')

    def set_external_end_port(self, external_end_port):
        self.add_query_params('ExternalEndPort', external_end_port)

    def get_internal_start_port(self):
        return self.get_query_params().get('InternalStartPort')

    def set_internal_start_port(self, internal_start_port):
        self.add_query_params('InternalStartPort', internal_start_port)

    def get_internal_end_port(self):
        return self.get_query_params().get('InternalEndPort')

    def set_internal_end_port(self, internal_end_port):
        self.add_query_params('InternalEndPort', internal_end_port)

    def get_local_ip_address(self):
        return self.get_query_params().get('LocalIpAddress')

    def set_local_ip_address(self, local_ip_address):
        self.add_query_params('LocalIpAddress', local_ip_address)

    def get_enabled(self):
        return self.get_query_params().get('Enabled')

    def set_enabled(self, enabled):
        self.add_query_params('Enabled', enabled)

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)
