# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetNetworkPeeringResult',
    'AwaitableGetNetworkPeeringResult',
    'get_network_peering',
    'get_network_peering_output',
]

@pulumi.output_type
class GetNetworkPeeringResult:
    def __init__(__self__, create_time=None, description=None, exchange_subnet_routes=None, export_custom_routes=None, export_custom_routes_with_public_ip=None, import_custom_routes=None, import_custom_routes_with_public_ip=None, name=None, peer_mtu=None, peer_network=None, peer_network_type=None, state=None, state_details=None, uid=None, update_time=None, vmware_engine_network=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if exchange_subnet_routes and not isinstance(exchange_subnet_routes, bool):
            raise TypeError("Expected argument 'exchange_subnet_routes' to be a bool")
        pulumi.set(__self__, "exchange_subnet_routes", exchange_subnet_routes)
        if export_custom_routes and not isinstance(export_custom_routes, bool):
            raise TypeError("Expected argument 'export_custom_routes' to be a bool")
        pulumi.set(__self__, "export_custom_routes", export_custom_routes)
        if export_custom_routes_with_public_ip and not isinstance(export_custom_routes_with_public_ip, bool):
            raise TypeError("Expected argument 'export_custom_routes_with_public_ip' to be a bool")
        pulumi.set(__self__, "export_custom_routes_with_public_ip", export_custom_routes_with_public_ip)
        if import_custom_routes and not isinstance(import_custom_routes, bool):
            raise TypeError("Expected argument 'import_custom_routes' to be a bool")
        pulumi.set(__self__, "import_custom_routes", import_custom_routes)
        if import_custom_routes_with_public_ip and not isinstance(import_custom_routes_with_public_ip, bool):
            raise TypeError("Expected argument 'import_custom_routes_with_public_ip' to be a bool")
        pulumi.set(__self__, "import_custom_routes_with_public_ip", import_custom_routes_with_public_ip)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peer_mtu and not isinstance(peer_mtu, int):
            raise TypeError("Expected argument 'peer_mtu' to be a int")
        pulumi.set(__self__, "peer_mtu", peer_mtu)
        if peer_network and not isinstance(peer_network, str):
            raise TypeError("Expected argument 'peer_network' to be a str")
        pulumi.set(__self__, "peer_network", peer_network)
        if peer_network_type and not isinstance(peer_network_type, str):
            raise TypeError("Expected argument 'peer_network_type' to be a str")
        pulumi.set(__self__, "peer_network_type", peer_network_type)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if state_details and not isinstance(state_details, str):
            raise TypeError("Expected argument 'state_details' to be a str")
        pulumi.set(__self__, "state_details", state_details)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)
        if vmware_engine_network and not isinstance(vmware_engine_network, str):
            raise TypeError("Expected argument 'vmware_engine_network' to be a str")
        pulumi.set(__self__, "vmware_engine_network", vmware_engine_network)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Creation time of this resource.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional. User-provided description for this network peering.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="exchangeSubnetRoutes")
    def exchange_subnet_routes(self) -> bool:
        """
        Optional. True if full mesh connectivity is created and managed automatically between peered networks; false otherwise. Currently this field is always true because Google Compute Engine automatically creates and manages subnetwork routes between two VPC networks when peering state is 'ACTIVE'.
        """
        return pulumi.get(self, "exchange_subnet_routes")

    @property
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> bool:
        """
        Optional. True if custom routes are exported to the peered network; false otherwise. The default value is true.
        """
        return pulumi.get(self, "export_custom_routes")

    @property
    @pulumi.getter(name="exportCustomRoutesWithPublicIp")
    def export_custom_routes_with_public_ip(self) -> bool:
        """
        Optional. True if all subnet routes with a public IP address range are exported; false otherwise. The default value is true. IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always exported to peers and are not controlled by this field.
        """
        return pulumi.get(self, "export_custom_routes_with_public_ip")

    @property
    @pulumi.getter(name="importCustomRoutes")
    def import_custom_routes(self) -> bool:
        """
        Optional. True if custom routes are imported from the peered network; false otherwise. The default value is true.
        """
        return pulumi.get(self, "import_custom_routes")

    @property
    @pulumi.getter(name="importCustomRoutesWithPublicIp")
    def import_custom_routes_with_public_ip(self) -> bool:
        """
        Optional. True if all subnet routes with public IP address range are imported; false otherwise. The default value is true. IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always imported to peers and are not controlled by this field.
        """
        return pulumi.get(self, "import_custom_routes_with_public_ip")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the network peering. Resource names are scheme-less URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/global/networkPeerings/my-peering`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerMtu")
    def peer_mtu(self) -> int:
        """
        Optional. Maximum transmission unit (MTU) in bytes. The default value is `1500`. If a value of `0` is provided for this field, VMware Engine uses the default value instead.
        """
        return pulumi.get(self, "peer_mtu")

    @property
    @pulumi.getter(name="peerNetwork")
    def peer_network(self) -> str:
        """
        The relative resource name of the network to peer with a standard VMware Engine network. The provided network can be a consumer VPC network or another standard VMware Engine network. If the `peer_network_type` is VMWARE_ENGINE_NETWORK, specify the name in the form: `projects/{project}/locations/global/vmwareEngineNetworks/{vmware_engine_network_id}`. Otherwise specify the name in the form: `projects/{project}/global/networks/{network_id}`, where `{project}` can either be a project number or a project ID.
        """
        return pulumi.get(self, "peer_network")

    @property
    @pulumi.getter(name="peerNetworkType")
    def peer_network_type(self) -> str:
        """
        The type of the network to peer with the VMware Engine network.
        """
        return pulumi.get(self, "peer_network_type")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the network peering. This field has a value of 'ACTIVE' when there's a matching configuration in the peer network. New values may be added to this enum when appropriate.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> str:
        """
        Output Only. Details about the current state of the network peering.
        """
        return pulumi.get(self, "state_details")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        System-generated unique identifier for the resource.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Last update time of this resource.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> str:
        """
        The relative resource name of the VMware Engine network. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}` where `{project}` can either be a project number or a project ID.
        """
        return pulumi.get(self, "vmware_engine_network")


class AwaitableGetNetworkPeeringResult(GetNetworkPeeringResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkPeeringResult(
            create_time=self.create_time,
            description=self.description,
            exchange_subnet_routes=self.exchange_subnet_routes,
            export_custom_routes=self.export_custom_routes,
            export_custom_routes_with_public_ip=self.export_custom_routes_with_public_ip,
            import_custom_routes=self.import_custom_routes,
            import_custom_routes_with_public_ip=self.import_custom_routes_with_public_ip,
            name=self.name,
            peer_mtu=self.peer_mtu,
            peer_network=self.peer_network,
            peer_network_type=self.peer_network_type,
            state=self.state,
            state_details=self.state_details,
            uid=self.uid,
            update_time=self.update_time,
            vmware_engine_network=self.vmware_engine_network)


def get_network_peering(network_peering_id: Optional[str] = None,
                        project: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkPeeringResult:
    """
    Retrieves a `NetworkPeering` resource by its resource name. The resource contains details of the network peering, such as peered networks, import and export custom route configurations, and peering state.
    """
    __args__ = dict()
    __args__['networkPeeringId'] = network_peering_id
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:vmwareengine/v1:getNetworkPeering', __args__, opts=opts, typ=GetNetworkPeeringResult).value

    return AwaitableGetNetworkPeeringResult(
        create_time=pulumi.get(__ret__, 'create_time'),
        description=pulumi.get(__ret__, 'description'),
        exchange_subnet_routes=pulumi.get(__ret__, 'exchange_subnet_routes'),
        export_custom_routes=pulumi.get(__ret__, 'export_custom_routes'),
        export_custom_routes_with_public_ip=pulumi.get(__ret__, 'export_custom_routes_with_public_ip'),
        import_custom_routes=pulumi.get(__ret__, 'import_custom_routes'),
        import_custom_routes_with_public_ip=pulumi.get(__ret__, 'import_custom_routes_with_public_ip'),
        name=pulumi.get(__ret__, 'name'),
        peer_mtu=pulumi.get(__ret__, 'peer_mtu'),
        peer_network=pulumi.get(__ret__, 'peer_network'),
        peer_network_type=pulumi.get(__ret__, 'peer_network_type'),
        state=pulumi.get(__ret__, 'state'),
        state_details=pulumi.get(__ret__, 'state_details'),
        uid=pulumi.get(__ret__, 'uid'),
        update_time=pulumi.get(__ret__, 'update_time'),
        vmware_engine_network=pulumi.get(__ret__, 'vmware_engine_network'))


@_utilities.lift_output_func(get_network_peering)
def get_network_peering_output(network_peering_id: Optional[pulumi.Input[str]] = None,
                               project: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkPeeringResult]:
    """
    Retrieves a `NetworkPeering` resource by its resource name. The resource contains details of the network peering, such as peered networks, import and export custom route configurations, and peering state.
    """
    ...