import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from chinac_way_v3.core.rpc_request import RpcRequest


class RunInstance(RpcRequest):
    def __init__(self):
        super(RunInstance, self).__init__('Ecs', '1.0', 'RunInstance')

    def get_name(self):
        return self.get_query_params().get('Name')

    def set_name(self, name):
        self.add_query_params('Name', name)

    def get_image_id(self):
        return self.get_query_params().get('ImageId')

    def set_image_id(self, image_id):
        self.add_query_params('ImageId', image_id)

    def get_instance_type(self):
        return self.get_query_params().get('InstanceType')

    def set_instance_type(self, instance_type):
        self.add_query_params('InstanceType', instance_type)

    def get_password(self):
        return self.get_query_params().get('Password')

    def set_password(self, password):
        self.add_query_params('Password', password)

    def get_key_pair(self):
        return self.get_query_params().get('KeyPair')

    def set_key_pair(self, key_pair):
        self.add_query_params('KeyPair', key_pair)

    def get_firewall_id(self):
        return self.get_query_params().get('FirewallId')

    def set_firewall_id(self, firewall_id):
        self.add_query_params('FirewallId', firewall_id)

    def get_interface0network_id(self):
        return self.get_query_params().get('Interface.0.NetworkId')

    def set_interface0network_id(self, interface0network_id):
        self.add_query_params('Interface.0.NetworkId', interface0network_id)

    def get_interface0ipAddress(self):
        return self.get_query_params().get('Interface.0.IpAddress')

    def set_interface0ipAddress(self, interface0ipAddress):
        self.add_query_params('Interface.0.IpAddress', interface0ipAddress)

    def get_internet_bandwidth(self):
        return self.get_query_params().get('Internet.Bandwidth')

    def set_internet_bandwidth(self, internet_bandwidth):
        self.add_query_params('Internet.Bandwidth', internet_bandwidth)

    def get_internet_router_id(self):
        return self.get_query_params().get('Internet.RouterId')

    def set_internet_router_id(self, internet_router_id):
        self.add_query_params('Internet.RouterId', internet_router_id)

    def get_volumes0type(self):
        return self.get_query_params().get('Volumes.0.Type')

    def set_volumes0type(self, volumes0type):
        self.add_query_params('Volumes.0.Type', volumes0type)

    def get_volumes0size(self):
        return self.get_query_params().get('Volumes.0.Size')

    def set_volumes0size(self, volumes0size):
        self.add_query_params('Volumes.0.Size', volumes0size)

    def get_volumes1type(self):
        return self.get_query_params().get('Volumes.1.Type')

    def set_volumes1type(self, volumes1type):
        self.add_query_params('Volumes.1.Type', volumes1type)

    def get_volumes1size(self):
        return self.get_query_params().get('Volumes.1.Size')

    def set_volumes1size(self, volumes1size):
        self.add_query_params('Volumes.1.Size', volumes1size)

    def get_volumes2type(self):
        return self.get_query_params().get('Volumes.2.Type')

    def set_volumes2type(self, volumes2type):
        self.add_query_params('Volumes.2.Type', volumes2type)

    def get_volumes2size(self):
        return self.get_query_params().get('Volumes.2.Size')

    def set_volumes2size(self, volumes2size):
        self.add_query_params('Volumes.2.Size', volumes2size)

    def get_volumes3type(self):
        return self.get_query_params().get('Volumes.3.Type')

    def set_volumes3type(self, volumes3type):
        self.add_query_params('Volumes.3.Type', volumes3type)

    def get_volumes3size(self):
        return self.get_query_params().get('Volumes.3.Size')

    def set_volumes3size(self, volumes3size):
        self.add_query_params('Volumes.3.Size', volumes3size)

    def get_volumes4type(self):
        return self.get_query_params().get('Volumes.4.Type')

    def set_volumes4type(self, volumes4type):
        self.add_query_params('Volumes.4.Type', volumes4type)

    def get_volumes4size(self):
        return self.get_query_params().get('Volumes.4.Size')

    def set_volumes4size(self, volumes4size):
        self.add_query_params('Volumes.4.Size', volumes4size)

    def get_volumes4size(self):
        return self.get_query_params().get('Volumes.4.Size')

    def set_volumes4size(self, volumes4size):
        self.add_query_params('Volumes.4.Size', volumes4size)

    def get_pay_type(self):
        return self.get_query_params().get('PayType')

    def set_pay_type(self, pay_type):
        self.add_query_params('PayType', pay_type)

    def get_period(self):
        return self.get_query_params().get('Period')

    def set_period(self, period):
        self.add_query_params('Period', period)

    def get_instance_series(self):
        return self.get_query_params().get('InstanceSeries')

    def set_instance_series(self, instance_series):
        self.add_query_params('InstanceSeries', instance_series)
