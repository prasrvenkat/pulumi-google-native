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
from ._inputs import *

__all__ = ['AppgroupArgs', 'Appgroup']

@pulumi.input_type
class AppgroupArgs:
    def __init__(__self__, *,
                 organization_id: pulumi.Input[str],
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1AttributeArgs']]]] = None,
                 channel_id: Optional[pulumi.Input[str]] = None,
                 channel_uri: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Appgroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1AttributeArgs']]] attributes: A list of attributes
        :param pulumi.Input[str] channel_id: channel identifier identifies the owner maintaing this grouping.
        :param pulumi.Input[str] channel_uri: A reference to the associated storefront/marketplace.
        :param pulumi.Input[str] display_name: app group name displayed in the UI
        :param pulumi.Input[str] name: Immutable. Name of the AppGroup. Characters you can use in the name are restricted to: A-Z0-9._\\-$ %.
        :param pulumi.Input[str] organization: Immutable. the org the app group is created
        """
        pulumi.set(__self__, "organization_id", organization_id)
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if channel_id is not None:
            pulumi.set(__self__, "channel_id", channel_id)
        if channel_uri is not None:
            pulumi.set(__self__, "channel_uri", channel_uri)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization is not None:
            pulumi.set(__self__, "organization", organization)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1AttributeArgs']]]]:
        """
        A list of attributes
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1AttributeArgs']]]]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[pulumi.Input[str]]:
        """
        channel identifier identifies the owner maintaing this grouping.
        """
        return pulumi.get(self, "channel_id")

    @channel_id.setter
    def channel_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_id", value)

    @property
    @pulumi.getter(name="channelUri")
    def channel_uri(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the associated storefront/marketplace.
        """
        return pulumi.get(self, "channel_uri")

    @channel_uri.setter
    def channel_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_uri", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        app group name displayed in the UI
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. Name of the AppGroup. Characters you can use in the name are restricted to: A-Z0-9._\\-$ %.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. the org the app group is created
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization", value)


class Appgroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1AttributeArgs']]]]] = None,
                 channel_id: Optional[pulumi.Input[str]] = None,
                 channel_uri: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an AppGroup. Once created, user can register apps under the AppGroup to obtain secret key and password. At creation time, the AppGroup's state is set as `active`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1AttributeArgs']]]] attributes: A list of attributes
        :param pulumi.Input[str] channel_id: channel identifier identifies the owner maintaing this grouping.
        :param pulumi.Input[str] channel_uri: A reference to the associated storefront/marketplace.
        :param pulumi.Input[str] display_name: app group name displayed in the UI
        :param pulumi.Input[str] name: Immutable. Name of the AppGroup. Characters you can use in the name are restricted to: A-Z0-9._\\-$ %.
        :param pulumi.Input[str] organization: Immutable. the org the app group is created
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppgroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an AppGroup. Once created, user can register apps under the AppGroup to obtain secret key and password. At creation time, the AppGroup's state is set as `active`.

        :param str resource_name: The name of the resource.
        :param AppgroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppgroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1AttributeArgs']]]]] = None,
                 channel_id: Optional[pulumi.Input[str]] = None,
                 channel_uri: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppgroupArgs.__new__(AppgroupArgs)

            __props__.__dict__["attributes"] = attributes
            __props__.__dict__["channel_id"] = channel_id
            __props__.__dict__["channel_uri"] = channel_uri
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["name"] = name
            __props__.__dict__["organization"] = organization
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            __props__.__dict__["app_group_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["last_modified_at"] = None
            __props__.__dict__["status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["organization_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Appgroup, __self__).__init__(
            'google-native:apigee/v1:Appgroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Appgroup':
        """
        Get an existing Appgroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AppgroupArgs.__new__(AppgroupArgs)

        __props__.__dict__["app_group_id"] = None
        __props__.__dict__["attributes"] = None
        __props__.__dict__["channel_id"] = None
        __props__.__dict__["channel_uri"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["last_modified_at"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["organization"] = None
        __props__.__dict__["organization_id"] = None
        __props__.__dict__["status"] = None
        return Appgroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appGroupId")
    def app_group_id(self) -> pulumi.Output[str]:
        """
        Internal identifier that cannot be edited
        """
        return pulumi.get(self, "app_group_id")

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Sequence['outputs.GoogleCloudApigeeV1AttributeResponse']]:
        """
        A list of attributes
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Output[str]:
        """
        channel identifier identifies the owner maintaing this grouping.
        """
        return pulumi.get(self, "channel_id")

    @property
    @pulumi.getter(name="channelUri")
    def channel_uri(self) -> pulumi.Output[str]:
        """
        A reference to the associated storefront/marketplace.
        """
        return pulumi.get(self, "channel_uri")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Created time as milliseconds since epoch.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        app group name displayed in the UI
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[str]:
        """
        Modified time as milliseconds since epoch.
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. Name of the AppGroup. Characters you can use in the name are restricted to: A-Z0-9._\\-$ %.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Output[str]:
        """
        Immutable. the org the app group is created
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Valid values are `active` or `inactive`. Note that the status of the AppGroup should be updated via UpdateAppGroupRequest by setting the action as `active` or `inactive`.
        """
        return pulumi.get(self, "status")
