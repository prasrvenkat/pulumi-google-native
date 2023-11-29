# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['SecurityProfileGroupArgs', 'SecurityProfileGroup']

@pulumi.input_type
class SecurityProfileGroupArgs:
    def __init__(__self__, *,
                 organization_id: pulumi.Input[str],
                 security_profile_group_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 threat_prevention_profile: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecurityProfileGroup resource.
        :param pulumi.Input[str] security_profile_group_id: Required. Short name of the SecurityProfileGroup resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "security_profile_group1".
        :param pulumi.Input[str] description: Optional. An optional description of the profile group. Max length 2048 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Labels as key value pairs.
        :param pulumi.Input[str] name: Immutable. Identifier. Name of the SecurityProfileGroup resource. It matches pattern `projects|organizations/*/locations/{location}/securityProfileGroups/{security_profile_group}`.
        :param pulumi.Input[str] threat_prevention_profile: Optional. Reference to a SecurityProfile with the threat prevention configuration for the SecurityProfileGroup.
        """
        pulumi.set(__self__, "organization_id", organization_id)
        pulumi.set(__self__, "security_profile_group_id", security_profile_group_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if threat_prevention_profile is not None:
            pulumi.set(__self__, "threat_prevention_profile", threat_prevention_profile)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="securityProfileGroupId")
    def security_profile_group_id(self) -> pulumi.Input[str]:
        """
        Required. Short name of the SecurityProfileGroup resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "security_profile_group1".
        """
        return pulumi.get(self, "security_profile_group_id")

    @security_profile_group_id.setter
    def security_profile_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "security_profile_group_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. An optional description of the profile group. Max length 2048 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. Labels as key value pairs.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. Identifier. Name of the SecurityProfileGroup resource. It matches pattern `projects|organizations/*/locations/{location}/securityProfileGroups/{security_profile_group}`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="threatPreventionProfile")
    def threat_prevention_profile(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Reference to a SecurityProfile with the threat prevention configuration for the SecurityProfileGroup.
        """
        return pulumi.get(self, "threat_prevention_profile")

    @threat_prevention_profile.setter
    def threat_prevention_profile(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "threat_prevention_profile", value)


class SecurityProfileGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 security_profile_group_id: Optional[pulumi.Input[str]] = None,
                 threat_prevention_profile: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new SecurityProfileGroup in a given organization and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Optional. An optional description of the profile group. Max length 2048 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Labels as key value pairs.
        :param pulumi.Input[str] name: Immutable. Identifier. Name of the SecurityProfileGroup resource. It matches pattern `projects|organizations/*/locations/{location}/securityProfileGroups/{security_profile_group}`.
        :param pulumi.Input[str] security_profile_group_id: Required. Short name of the SecurityProfileGroup resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "security_profile_group1".
        :param pulumi.Input[str] threat_prevention_profile: Optional. Reference to a SecurityProfile with the threat prevention configuration for the SecurityProfileGroup.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityProfileGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new SecurityProfileGroup in a given organization and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param SecurityProfileGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityProfileGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 security_profile_group_id: Optional[pulumi.Input[str]] = None,
                 threat_prevention_profile: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityProfileGroupArgs.__new__(SecurityProfileGroupArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            if security_profile_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'security_profile_group_id'")
            __props__.__dict__["security_profile_group_id"] = security_profile_group_id
            __props__.__dict__["threat_prevention_profile"] = threat_prevention_profile
            __props__.__dict__["create_time"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "organization_id", "security_profile_group_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SecurityProfileGroup, __self__).__init__(
            'google-native:networksecurity/v1beta1:SecurityProfileGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SecurityProfileGroup':
        """
        Get an existing SecurityProfileGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecurityProfileGroupArgs.__new__(SecurityProfileGroupArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["organization_id"] = None
        __props__.__dict__["security_profile_group_id"] = None
        __props__.__dict__["threat_prevention_profile"] = None
        __props__.__dict__["update_time"] = None
        return SecurityProfileGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Resource creation timestamp.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. An optional description of the profile group. Max length 2048 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Labels as key value pairs.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. Identifier. Name of the SecurityProfileGroup resource. It matches pattern `projects|organizations/*/locations/{location}/securityProfileGroups/{security_profile_group}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="securityProfileGroupId")
    def security_profile_group_id(self) -> pulumi.Output[str]:
        """
        Required. Short name of the SecurityProfileGroup resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "security_profile_group1".
        """
        return pulumi.get(self, "security_profile_group_id")

    @property
    @pulumi.getter(name="threatPreventionProfile")
    def threat_prevention_profile(self) -> pulumi.Output[str]:
        """
        Optional. Reference to a SecurityProfile with the threat prevention configuration for the SecurityProfileGroup.
        """
        return pulumi.get(self, "threat_prevention_profile")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Last resource update timestamp.
        """
        return pulumi.get(self, "update_time")
