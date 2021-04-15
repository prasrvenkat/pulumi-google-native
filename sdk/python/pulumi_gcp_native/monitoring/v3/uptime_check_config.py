# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['UptimeCheckConfigArgs', 'UptimeCheckConfig']

@pulumi.input_type
class UptimeCheckConfigArgs:
    def __init__(__self__, *,
                 projects_id: pulumi.Input[str],
                 uptime_check_configs_id: pulumi.Input[str],
                 content_matchers: Optional[pulumi.Input[Sequence[pulumi.Input['ContentMatcherArgs']]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 http_check: Optional[pulumi.Input['HttpCheckArgs']] = None,
                 internal_checkers: Optional[pulumi.Input[Sequence[pulumi.Input['InternalCheckerArgs']]]] = None,
                 is_internal: Optional[pulumi.Input[bool]] = None,
                 monitored_resource: Optional[pulumi.Input['MonitoredResourceArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input['ResourceGroupArgs']] = None,
                 selected_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tcp_check: Optional[pulumi.Input['TcpCheckArgs']] = None,
                 timeout: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UptimeCheckConfig resource.
        :param pulumi.Input[Sequence[pulumi.Input['ContentMatcherArgs']]] content_matchers: The content that is expected to appear in the data returned by the target server against which the check is run. Currently, only the first entry in the content_matchers list is supported, and additional entries will be ignored. This field is optional and should only be specified if a content match is required as part of the/ Uptime check.
        :param pulumi.Input[str] display_name: A human-friendly name for the Uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced. Required.
        :param pulumi.Input['HttpCheckArgs'] http_check: Contains information needed to make an HTTP or HTTPS check.
        :param pulumi.Input[Sequence[pulumi.Input['InternalCheckerArgs']]] internal_checkers: The internal checkers that this check will egress from. If is_internal is true and this list is empty, the check will egress from all the InternalCheckers configured for the project that owns this UptimeCheckConfig.
        :param pulumi.Input[bool] is_internal: If this is true, then checks are made only from the 'internal_checkers'. If it is false, then checks are made only from the 'selected_regions'. It is an error to provide 'selected_regions' when is_internal is true, or to provide 'internal_checkers' when is_internal is false.
        :param pulumi.Input['MonitoredResourceArgs'] monitored_resource: The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The following monitored resource types are valid for this field: uptime_url, gce_instance, gae_app, aws_ec2_instance, aws_elb_load_balancer
        :param pulumi.Input[str] name: A unique resource name for this Uptime check configuration. The format is: projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID] [PROJECT_ID_OR_NUMBER] is the Workspace host project associated with the Uptime check.This field should be omitted when creating the Uptime check configuration; on create, the resource name is assigned by the server and included in the response.
        :param pulumi.Input[str] period: How often, in seconds, the Uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 60s.
        :param pulumi.Input['ResourceGroupArgs'] resource_group: The group resource associated with the configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] selected_regions: The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions must be provided to include a minimum of 3 locations. Not specifying this field will result in Uptime checks running from all available regions.
        :param pulumi.Input['TcpCheckArgs'] tcp_check: Contains information needed to make a TCP check.
        :param pulumi.Input[str] timeout: The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Required.
        """
        pulumi.set(__self__, "projects_id", projects_id)
        pulumi.set(__self__, "uptime_check_configs_id", uptime_check_configs_id)
        if content_matchers is not None:
            pulumi.set(__self__, "content_matchers", content_matchers)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if http_check is not None:
            pulumi.set(__self__, "http_check", http_check)
        if internal_checkers is not None:
            pulumi.set(__self__, "internal_checkers", internal_checkers)
        if is_internal is not None:
            pulumi.set(__self__, "is_internal", is_internal)
        if monitored_resource is not None:
            pulumi.set(__self__, "monitored_resource", monitored_resource)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if period is not None:
            pulumi.set(__self__, "period", period)
        if resource_group is not None:
            pulumi.set(__self__, "resource_group", resource_group)
        if selected_regions is not None:
            pulumi.set(__self__, "selected_regions", selected_regions)
        if tcp_check is not None:
            pulumi.set(__self__, "tcp_check", tcp_check)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="uptimeCheckConfigsId")
    def uptime_check_configs_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "uptime_check_configs_id")

    @uptime_check_configs_id.setter
    def uptime_check_configs_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "uptime_check_configs_id", value)

    @property
    @pulumi.getter(name="contentMatchers")
    def content_matchers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContentMatcherArgs']]]]:
        """
        The content that is expected to appear in the data returned by the target server against which the check is run. Currently, only the first entry in the content_matchers list is supported, and additional entries will be ignored. This field is optional and should only be specified if a content match is required as part of the/ Uptime check.
        """
        return pulumi.get(self, "content_matchers")

    @content_matchers.setter
    def content_matchers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContentMatcherArgs']]]]):
        pulumi.set(self, "content_matchers", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A human-friendly name for the Uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced. Required.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="httpCheck")
    def http_check(self) -> Optional[pulumi.Input['HttpCheckArgs']]:
        """
        Contains information needed to make an HTTP or HTTPS check.
        """
        return pulumi.get(self, "http_check")

    @http_check.setter
    def http_check(self, value: Optional[pulumi.Input['HttpCheckArgs']]):
        pulumi.set(self, "http_check", value)

    @property
    @pulumi.getter(name="internalCheckers")
    def internal_checkers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InternalCheckerArgs']]]]:
        """
        The internal checkers that this check will egress from. If is_internal is true and this list is empty, the check will egress from all the InternalCheckers configured for the project that owns this UptimeCheckConfig.
        """
        return pulumi.get(self, "internal_checkers")

    @internal_checkers.setter
    def internal_checkers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InternalCheckerArgs']]]]):
        pulumi.set(self, "internal_checkers", value)

    @property
    @pulumi.getter(name="isInternal")
    def is_internal(self) -> Optional[pulumi.Input[bool]]:
        """
        If this is true, then checks are made only from the 'internal_checkers'. If it is false, then checks are made only from the 'selected_regions'. It is an error to provide 'selected_regions' when is_internal is true, or to provide 'internal_checkers' when is_internal is false.
        """
        return pulumi.get(self, "is_internal")

    @is_internal.setter
    def is_internal(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_internal", value)

    @property
    @pulumi.getter(name="monitoredResource")
    def monitored_resource(self) -> Optional[pulumi.Input['MonitoredResourceArgs']]:
        """
        The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The following monitored resource types are valid for this field: uptime_url, gce_instance, gae_app, aws_ec2_instance, aws_elb_load_balancer
        """
        return pulumi.get(self, "monitored_resource")

    @monitored_resource.setter
    def monitored_resource(self, value: Optional[pulumi.Input['MonitoredResourceArgs']]):
        pulumi.set(self, "monitored_resource", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique resource name for this Uptime check configuration. The format is: projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID] [PROJECT_ID_OR_NUMBER] is the Workspace host project associated with the Uptime check.This field should be omitted when creating the Uptime check configuration; on create, the resource name is assigned by the server and included in the response.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[str]]:
        """
        How often, in seconds, the Uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 60s.
        """
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input['ResourceGroupArgs']]:
        """
        The group resource associated with the configuration.
        """
        return pulumi.get(self, "resource_group")

    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input['ResourceGroupArgs']]):
        pulumi.set(self, "resource_group", value)

    @property
    @pulumi.getter(name="selectedRegions")
    def selected_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions must be provided to include a minimum of 3 locations. Not specifying this field will result in Uptime checks running from all available regions.
        """
        return pulumi.get(self, "selected_regions")

    @selected_regions.setter
    def selected_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "selected_regions", value)

    @property
    @pulumi.getter(name="tcpCheck")
    def tcp_check(self) -> Optional[pulumi.Input['TcpCheckArgs']]:
        """
        Contains information needed to make a TCP check.
        """
        return pulumi.get(self, "tcp_check")

    @tcp_check.setter
    def tcp_check(self, value: Optional[pulumi.Input['TcpCheckArgs']]):
        pulumi.set(self, "tcp_check", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[str]]:
        """
        The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Required.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timeout", value)


class UptimeCheckConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContentMatcherArgs']]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 http_check: Optional[pulumi.Input[pulumi.InputType['HttpCheckArgs']]] = None,
                 internal_checkers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InternalCheckerArgs']]]]] = None,
                 is_internal: Optional[pulumi.Input[bool]] = None,
                 monitored_resource: Optional[pulumi.Input[pulumi.InputType['MonitoredResourceArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[pulumi.InputType['ResourceGroupArgs']]] = None,
                 selected_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tcp_check: Optional[pulumi.Input[pulumi.InputType['TcpCheckArgs']]] = None,
                 timeout: Optional[pulumi.Input[str]] = None,
                 uptime_check_configs_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new Uptime check configuration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContentMatcherArgs']]]] content_matchers: The content that is expected to appear in the data returned by the target server against which the check is run. Currently, only the first entry in the content_matchers list is supported, and additional entries will be ignored. This field is optional and should only be specified if a content match is required as part of the/ Uptime check.
        :param pulumi.Input[str] display_name: A human-friendly name for the Uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced. Required.
        :param pulumi.Input[pulumi.InputType['HttpCheckArgs']] http_check: Contains information needed to make an HTTP or HTTPS check.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InternalCheckerArgs']]]] internal_checkers: The internal checkers that this check will egress from. If is_internal is true and this list is empty, the check will egress from all the InternalCheckers configured for the project that owns this UptimeCheckConfig.
        :param pulumi.Input[bool] is_internal: If this is true, then checks are made only from the 'internal_checkers'. If it is false, then checks are made only from the 'selected_regions'. It is an error to provide 'selected_regions' when is_internal is true, or to provide 'internal_checkers' when is_internal is false.
        :param pulumi.Input[pulumi.InputType['MonitoredResourceArgs']] monitored_resource: The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The following monitored resource types are valid for this field: uptime_url, gce_instance, gae_app, aws_ec2_instance, aws_elb_load_balancer
        :param pulumi.Input[str] name: A unique resource name for this Uptime check configuration. The format is: projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID] [PROJECT_ID_OR_NUMBER] is the Workspace host project associated with the Uptime check.This field should be omitted when creating the Uptime check configuration; on create, the resource name is assigned by the server and included in the response.
        :param pulumi.Input[str] period: How often, in seconds, the Uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 60s.
        :param pulumi.Input[pulumi.InputType['ResourceGroupArgs']] resource_group: The group resource associated with the configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] selected_regions: The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions must be provided to include a minimum of 3 locations. Not specifying this field will result in Uptime checks running from all available regions.
        :param pulumi.Input[pulumi.InputType['TcpCheckArgs']] tcp_check: Contains information needed to make a TCP check.
        :param pulumi.Input[str] timeout: The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Required.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UptimeCheckConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Uptime check configuration.

        :param str resource_name: The name of the resource.
        :param UptimeCheckConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UptimeCheckConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContentMatcherArgs']]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 http_check: Optional[pulumi.Input[pulumi.InputType['HttpCheckArgs']]] = None,
                 internal_checkers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InternalCheckerArgs']]]]] = None,
                 is_internal: Optional[pulumi.Input[bool]] = None,
                 monitored_resource: Optional[pulumi.Input[pulumi.InputType['MonitoredResourceArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[pulumi.InputType['ResourceGroupArgs']]] = None,
                 selected_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tcp_check: Optional[pulumi.Input[pulumi.InputType['TcpCheckArgs']]] = None,
                 timeout: Optional[pulumi.Input[str]] = None,
                 uptime_check_configs_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UptimeCheckConfigArgs.__new__(UptimeCheckConfigArgs)

            __props__.__dict__["content_matchers"] = content_matchers
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["http_check"] = http_check
            __props__.__dict__["internal_checkers"] = internal_checkers
            __props__.__dict__["is_internal"] = is_internal
            __props__.__dict__["monitored_resource"] = monitored_resource
            __props__.__dict__["name"] = name
            __props__.__dict__["period"] = period
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["resource_group"] = resource_group
            __props__.__dict__["selected_regions"] = selected_regions
            __props__.__dict__["tcp_check"] = tcp_check
            __props__.__dict__["timeout"] = timeout
            if uptime_check_configs_id is None and not opts.urn:
                raise TypeError("Missing required property 'uptime_check_configs_id'")
            __props__.__dict__["uptime_check_configs_id"] = uptime_check_configs_id
        super(UptimeCheckConfig, __self__).__init__(
            'gcp-native:monitoring/v3:UptimeCheckConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UptimeCheckConfig':
        """
        Get an existing UptimeCheckConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UptimeCheckConfigArgs.__new__(UptimeCheckConfigArgs)

        __props__.__dict__["content_matchers"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["http_check"] = None
        __props__.__dict__["internal_checkers"] = None
        __props__.__dict__["is_internal"] = None
        __props__.__dict__["monitored_resource"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["period"] = None
        __props__.__dict__["resource_group"] = None
        __props__.__dict__["selected_regions"] = None
        __props__.__dict__["tcp_check"] = None
        __props__.__dict__["timeout"] = None
        return UptimeCheckConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contentMatchers")
    def content_matchers(self) -> pulumi.Output[Sequence['outputs.ContentMatcherResponse']]:
        """
        The content that is expected to appear in the data returned by the target server against which the check is run. Currently, only the first entry in the content_matchers list is supported, and additional entries will be ignored. This field is optional and should only be specified if a content match is required as part of the/ Uptime check.
        """
        return pulumi.get(self, "content_matchers")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        A human-friendly name for the Uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced. Required.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="httpCheck")
    def http_check(self) -> pulumi.Output['outputs.HttpCheckResponse']:
        """
        Contains information needed to make an HTTP or HTTPS check.
        """
        return pulumi.get(self, "http_check")

    @property
    @pulumi.getter(name="internalCheckers")
    def internal_checkers(self) -> pulumi.Output[Sequence['outputs.InternalCheckerResponse']]:
        """
        The internal checkers that this check will egress from. If is_internal is true and this list is empty, the check will egress from all the InternalCheckers configured for the project that owns this UptimeCheckConfig.
        """
        return pulumi.get(self, "internal_checkers")

    @property
    @pulumi.getter(name="isInternal")
    def is_internal(self) -> pulumi.Output[bool]:
        """
        If this is true, then checks are made only from the 'internal_checkers'. If it is false, then checks are made only from the 'selected_regions'. It is an error to provide 'selected_regions' when is_internal is true, or to provide 'internal_checkers' when is_internal is false.
        """
        return pulumi.get(self, "is_internal")

    @property
    @pulumi.getter(name="monitoredResource")
    def monitored_resource(self) -> pulumi.Output['outputs.MonitoredResourceResponse']:
        """
        The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The following monitored resource types are valid for this field: uptime_url, gce_instance, gae_app, aws_ec2_instance, aws_elb_load_balancer
        """
        return pulumi.get(self, "monitored_resource")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique resource name for this Uptime check configuration. The format is: projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID] [PROJECT_ID_OR_NUMBER] is the Workspace host project associated with the Uptime check.This field should be omitted when creating the Uptime check configuration; on create, the resource name is assigned by the server and included in the response.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def period(self) -> pulumi.Output[str]:
        """
        How often, in seconds, the Uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 60s.
        """
        return pulumi.get(self, "period")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Output['outputs.ResourceGroupResponse']:
        """
        The group resource associated with the configuration.
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="selectedRegions")
    def selected_regions(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions must be provided to include a minimum of 3 locations. Not specifying this field will result in Uptime checks running from all available regions.
        """
        return pulumi.get(self, "selected_regions")

    @property
    @pulumi.getter(name="tcpCheck")
    def tcp_check(self) -> pulumi.Output['outputs.TcpCheckResponse']:
        """
        Contains information needed to make a TCP check.
        """
        return pulumi.get(self, "tcp_check")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[str]:
        """
        The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Required.
        """
        return pulumi.get(self, "timeout")
