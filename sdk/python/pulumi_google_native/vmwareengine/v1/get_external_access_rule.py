# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetExternalAccessRuleResult',
    'AwaitableGetExternalAccessRuleResult',
    'get_external_access_rule',
    'get_external_access_rule_output',
]

@pulumi.output_type
class GetExternalAccessRuleResult:
    def __init__(__self__, action=None, create_time=None, description=None, destination_ip_ranges=None, destination_ports=None, ip_protocol=None, name=None, priority=None, source_ip_ranges=None, source_ports=None, state=None, uid=None, update_time=None):
        if action and not isinstance(action, str):
            raise TypeError("Expected argument 'action' to be a str")
        pulumi.set(__self__, "action", action)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if destination_ip_ranges and not isinstance(destination_ip_ranges, list):
            raise TypeError("Expected argument 'destination_ip_ranges' to be a list")
        pulumi.set(__self__, "destination_ip_ranges", destination_ip_ranges)
        if destination_ports and not isinstance(destination_ports, list):
            raise TypeError("Expected argument 'destination_ports' to be a list")
        pulumi.set(__self__, "destination_ports", destination_ports)
        if ip_protocol and not isinstance(ip_protocol, str):
            raise TypeError("Expected argument 'ip_protocol' to be a str")
        pulumi.set(__self__, "ip_protocol", ip_protocol)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if source_ip_ranges and not isinstance(source_ip_ranges, list):
            raise TypeError("Expected argument 'source_ip_ranges' to be a list")
        pulumi.set(__self__, "source_ip_ranges", source_ip_ranges)
        if source_ports and not isinstance(source_ports, list):
            raise TypeError("Expected argument 'source_ports' to be a list")
        pulumi.set(__self__, "source_ports", source_ports)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        The action that the external access rule performs.
        """
        return pulumi.get(self, "action")

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
        User-provided description for this external access rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(self) -> Sequence['outputs.IpRangeResponse']:
        """
        If destination ranges are specified, the external access rule applies only to the traffic that has a destination IP address in these ranges. The specified IP addresses must have reserved external IP addresses in the scope of the parent network policy. To match all external IP addresses in the scope of the parent network policy, specify `0.0.0.0/0`. To match a specific external IP address, specify it using the `IpRange.external_address` property.
        """
        return pulumi.get(self, "destination_ip_ranges")

    @property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(self) -> Sequence[str]:
        """
        A list of destination ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all destination ports, specify `["0-65535"]`.
        """
        return pulumi.get(self, "destination_ports")

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> str:
        """
        The IP protocol to which the external access rule applies. This value can be one of the following three protocol strings (not case-sensitive): `tcp`, `udp`, or `icmp`.
        """
        return pulumi.get(self, "ip_protocol")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of this external access rule. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        External access rule priority, which determines the external access rule to use when multiple rules apply. If multiple rules have the same priority, their ordering is non-deterministic. If specific ordering is required, assign unique priorities to enforce such ordering. The external access rule priority is an integer from 100 to 4096, both inclusive. Lower integers indicate higher precedence. For example, a rule with priority `100` has higher precedence than a rule with priority `101`.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> Sequence['outputs.IpRangeResponse']:
        """
        If source ranges are specified, the external access rule applies only to traffic that has a source IP address in these ranges. These ranges can either be expressed in the CIDR format or as an IP address. As only inbound rules are supported, `ExternalAddress` resources cannot be the source IP addresses of an external access rule. To match all source addresses, specify `0.0.0.0/0`.
        """
        return pulumi.get(self, "source_ip_ranges")

    @property
    @pulumi.getter(name="sourcePorts")
    def source_ports(self) -> Sequence[str]:
        """
        A list of source ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all source ports, specify `["0-65535"]`.
        """
        return pulumi.get(self, "source_ports")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the resource.
        """
        return pulumi.get(self, "state")

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


class AwaitableGetExternalAccessRuleResult(GetExternalAccessRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalAccessRuleResult(
            action=self.action,
            create_time=self.create_time,
            description=self.description,
            destination_ip_ranges=self.destination_ip_ranges,
            destination_ports=self.destination_ports,
            ip_protocol=self.ip_protocol,
            name=self.name,
            priority=self.priority,
            source_ip_ranges=self.source_ip_ranges,
            source_ports=self.source_ports,
            state=self.state,
            uid=self.uid,
            update_time=self.update_time)


def get_external_access_rule(external_access_rule_id: Optional[str] = None,
                             location: Optional[str] = None,
                             network_policy_id: Optional[str] = None,
                             project: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalAccessRuleResult:
    """
    Gets details of a single external access rule.
    """
    __args__ = dict()
    __args__['externalAccessRuleId'] = external_access_rule_id
    __args__['location'] = location
    __args__['networkPolicyId'] = network_policy_id
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:vmwareengine/v1:getExternalAccessRule', __args__, opts=opts, typ=GetExternalAccessRuleResult).value

    return AwaitableGetExternalAccessRuleResult(
        action=pulumi.get(__ret__, 'action'),
        create_time=pulumi.get(__ret__, 'create_time'),
        description=pulumi.get(__ret__, 'description'),
        destination_ip_ranges=pulumi.get(__ret__, 'destination_ip_ranges'),
        destination_ports=pulumi.get(__ret__, 'destination_ports'),
        ip_protocol=pulumi.get(__ret__, 'ip_protocol'),
        name=pulumi.get(__ret__, 'name'),
        priority=pulumi.get(__ret__, 'priority'),
        source_ip_ranges=pulumi.get(__ret__, 'source_ip_ranges'),
        source_ports=pulumi.get(__ret__, 'source_ports'),
        state=pulumi.get(__ret__, 'state'),
        uid=pulumi.get(__ret__, 'uid'),
        update_time=pulumi.get(__ret__, 'update_time'))


@_utilities.lift_output_func(get_external_access_rule)
def get_external_access_rule_output(external_access_rule_id: Optional[pulumi.Input[str]] = None,
                                    location: Optional[pulumi.Input[str]] = None,
                                    network_policy_id: Optional[pulumi.Input[str]] = None,
                                    project: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalAccessRuleResult]:
    """
    Gets details of a single external access rule.
    """
    ...
