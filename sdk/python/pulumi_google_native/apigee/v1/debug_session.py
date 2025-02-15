# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['DebugSessionArgs', 'DebugSession']

@pulumi.input_type
class DebugSessionArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 environment_id: pulumi.Input[str],
                 organization_id: pulumi.Input[str],
                 revision_id: pulumi.Input[str],
                 count: Optional[pulumi.Input[int]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[str]] = None,
                 tracesize: Optional[pulumi.Input[int]] = None,
                 validity: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a DebugSession resource.
        :param pulumi.Input[int] count: Optional. The number of request to be traced. Min = 1, Max = 15, Default = 10.
        :param pulumi.Input[str] filter: Optional. A conditional statement which is evaluated against the request message to determine if it should be traced. Syntax matches that of on API Proxy bundle flow Condition.
        :param pulumi.Input[str] name: A unique ID for this DebugSession.
        :param pulumi.Input[str] timeout: Optional. The time in seconds after which this DebugSession should end. This value will override the value in query param, if both are provided.
        :param pulumi.Input[int] tracesize: Optional. The maximum number of bytes captured from the response payload. Min = 0, Max = 5120, Default = 5120.
        :param pulumi.Input[int] validity: Optional. The length of time, in seconds, that this debug session is valid, starting from when it's received in the control plane. Min = 1, Max = 15, Default = 10.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "environment_id", environment_id)
        pulumi.set(__self__, "organization_id", organization_id)
        pulumi.set(__self__, "revision_id", revision_id)
        if count is not None:
            pulumi.set(__self__, "count", count)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)
        if tracesize is not None:
            pulumi.set(__self__, "tracesize", tracesize)
        if validity is not None:
            pulumi.set(__self__, "validity", validity)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "environment_id")

    @environment_id.setter
    def environment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_id", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "revision_id")

    @revision_id.setter
    def revision_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "revision_id", value)

    @property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[int]]:
        """
        Optional. The number of request to be traced. Min = 1, Max = 15, Default = 10.
        """
        return pulumi.get(self, "count")

    @count.setter
    def count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "count", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A conditional statement which is evaluated against the request message to determine if it should be traced. Syntax matches that of on API Proxy bundle flow Condition.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique ID for this DebugSession.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The time in seconds after which this DebugSession should end. This value will override the value in query param, if both are provided.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timeout", value)

    @property
    @pulumi.getter
    def tracesize(self) -> Optional[pulumi.Input[int]]:
        """
        Optional. The maximum number of bytes captured from the response payload. Min = 0, Max = 5120, Default = 5120.
        """
        return pulumi.get(self, "tracesize")

    @tracesize.setter
    def tracesize(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tracesize", value)

    @property
    @pulumi.getter
    def validity(self) -> Optional[pulumi.Input[int]]:
        """
        Optional. The length of time, in seconds, that this debug session is valid, starting from when it's received in the control plane. Min = 1, Max = 15, Default = 10.
        """
        return pulumi.get(self, "validity")

    @validity.setter
    def validity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "validity", value)


class DebugSession(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 count: Optional[pulumi.Input[int]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 revision_id: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[str]] = None,
                 tracesize: Optional[pulumi.Input[int]] = None,
                 validity: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Creates a debug session for a deployed API Proxy revision.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] count: Optional. The number of request to be traced. Min = 1, Max = 15, Default = 10.
        :param pulumi.Input[str] filter: Optional. A conditional statement which is evaluated against the request message to determine if it should be traced. Syntax matches that of on API Proxy bundle flow Condition.
        :param pulumi.Input[str] name: A unique ID for this DebugSession.
        :param pulumi.Input[str] timeout: Optional. The time in seconds after which this DebugSession should end. This value will override the value in query param, if both are provided.
        :param pulumi.Input[int] tracesize: Optional. The maximum number of bytes captured from the response payload. Min = 0, Max = 5120, Default = 5120.
        :param pulumi.Input[int] validity: Optional. The length of time, in seconds, that this debug session is valid, starting from when it's received in the control plane. Min = 1, Max = 15, Default = 10.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DebugSessionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a debug session for a deployed API Proxy revision.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param DebugSessionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DebugSessionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 count: Optional[pulumi.Input[int]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 revision_id: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[str]] = None,
                 tracesize: Optional[pulumi.Input[int]] = None,
                 validity: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DebugSessionArgs.__new__(DebugSessionArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["count"] = count
            if environment_id is None and not opts.urn:
                raise TypeError("Missing required property 'environment_id'")
            __props__.__dict__["environment_id"] = environment_id
            __props__.__dict__["filter"] = filter
            __props__.__dict__["name"] = name
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            if revision_id is None and not opts.urn:
                raise TypeError("Missing required property 'revision_id'")
            __props__.__dict__["revision_id"] = revision_id
            __props__.__dict__["timeout"] = timeout
            __props__.__dict__["tracesize"] = tracesize
            __props__.__dict__["validity"] = validity
            __props__.__dict__["create_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["api_id", "environment_id", "organization_id", "revision_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DebugSession, __self__).__init__(
            'google-native:apigee/v1:DebugSession',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DebugSession':
        """
        Get an existing DebugSession resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DebugSessionArgs.__new__(DebugSessionArgs)

        __props__.__dict__["api_id"] = None
        __props__.__dict__["count"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["environment_id"] = None
        __props__.__dict__["filter"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["organization_id"] = None
        __props__.__dict__["revision_id"] = None
        __props__.__dict__["timeout"] = None
        __props__.__dict__["tracesize"] = None
        __props__.__dict__["validity"] = None
        return DebugSession(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter
    def count(self) -> pulumi.Output[int]:
        """
        Optional. The number of request to be traced. Min = 1, Max = 15, Default = 10.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The first transaction creation timestamp, recorded by UAP.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[str]:
        """
        Optional. A conditional statement which is evaluated against the request message to determine if it should be traced. Syntax matches that of on API Proxy bundle flow Condition.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique ID for this DebugSession.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "revision_id")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[str]:
        """
        Optional. The time in seconds after which this DebugSession should end. A timeout specified in DebugSession will overwrite this value.
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter
    def tracesize(self) -> pulumi.Output[int]:
        """
        Optional. The maximum number of bytes captured from the response payload. Min = 0, Max = 5120, Default = 5120.
        """
        return pulumi.get(self, "tracesize")

    @property
    @pulumi.getter
    def validity(self) -> pulumi.Output[int]:
        """
        Optional. The length of time, in seconds, that this debug session is valid, starting from when it's received in the control plane. Min = 1, Max = 15, Default = 10.
        """
        return pulumi.get(self, "validity")

