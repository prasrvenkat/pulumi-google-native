# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['HubArgs', 'Hub']

@pulumi.input_type
class HubArgs:
    def __init__(__self__, *,
                 hubs_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Hub resource.
        :param pulumi.Input[str] create_time: Time when the Hub was created.
        :param pulumi.Input[str] description: Short description of the hub resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: User-defined labels.
        :param pulumi.Input[str] name: Immutable. The name of a Hub resource.
        :param pulumi.Input[str] update_time: Time when the Hub was updated.
        """
        pulumi.set(__self__, "hubs_id", hubs_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="hubsId")
    def hubs_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "hubs_id")

    @hubs_id.setter
    def hubs_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "hubs_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time when the Hub was created.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Short description of the hub resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        User-defined labels.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The name of a Hub resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time when the Hub was updated.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class Hub(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hubs_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new Hub in a given project and location.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Time when the Hub was created.
        :param pulumi.Input[str] description: Short description of the hub resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: User-defined labels.
        :param pulumi.Input[str] name: Immutable. The name of a Hub resource.
        :param pulumi.Input[str] update_time: Time when the Hub was updated.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HubArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Hub in a given project and location.

        :param str resource_name: The name of the resource.
        :param HubArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HubArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hubs_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
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
            __props__ = HubArgs.__new__(HubArgs)

            __props__.__dict__["create_time"] = create_time
            __props__.__dict__["description"] = description
            if hubs_id is None and not opts.urn:
                raise TypeError("Missing required property 'hubs_id'")
            __props__.__dict__["hubs_id"] = hubs_id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["update_time"] = update_time
            __props__.__dict__["spokes"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["unique_id"] = None
        super(Hub, __self__).__init__(
            'google-native:networkconnectivity/v1alpha1:Hub',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Hub':
        """
        Get an existing Hub resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HubArgs.__new__(HubArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["spokes"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["unique_id"] = None
        __props__.__dict__["update_time"] = None
        return Hub(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Time when the Hub was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Short description of the hub resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        User-defined labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. The name of a Hub resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def spokes(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of the URIs of all attached spokes
        """
        return pulumi.get(self, "spokes")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current lifecycle state of this Hub.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[str]:
        """
        Google-generated UUID for this resource. This is unique across all Hub resources. If a Hub resource is deleted and another with the same name is created, it gets a different unique_id.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Time when the Hub was updated.
        """
        return pulumi.get(self, "update_time")
