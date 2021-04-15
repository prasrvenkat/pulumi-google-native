# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['OrganizationEnvironmentKeystoreArgs', 'OrganizationEnvironmentKeystore']

@pulumi.input_type
class OrganizationEnvironmentKeystoreArgs:
    def __init__(__self__, *,
                 environments_id: pulumi.Input[str],
                 keystores_id: pulumi.Input[str],
                 organizations_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OrganizationEnvironmentKeystore resource.
        :param pulumi.Input[str] name: Required. Resource ID for this keystore. Values must match the regular expression `[\w[:space:]-.]{1,255}`.
        """
        pulumi.set(__self__, "environments_id", environments_id)
        pulumi.set(__self__, "keystores_id", keystores_id)
        pulumi.set(__self__, "organizations_id", organizations_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="environmentsId")
    def environments_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "environments_id")

    @environments_id.setter
    def environments_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "environments_id", value)

    @property
    @pulumi.getter(name="keystoresId")
    def keystores_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "keystores_id")

    @keystores_id.setter
    def keystores_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "keystores_id", value)

    @property
    @pulumi.getter(name="organizationsId")
    def organizations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organizations_id")

    @organizations_id.setter
    def organizations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organizations_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Resource ID for this keystore. Values must match the regular expression `[\w[:space:]-.]{1,255}`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class OrganizationEnvironmentKeystore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environments_id: Optional[pulumi.Input[str]] = None,
                 keystores_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a keystore or truststore. - Keystore: Contains certificates and their associated keys. - Truststore: Contains trusted certificates used to validate a server's certificate. These certificates are typically self-signed certificates or certificates that are not signed by a trusted CA.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Required. Resource ID for this keystore. Values must match the regular expression `[\w[:space:]-.]{1,255}`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationEnvironmentKeystoreArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a keystore or truststore. - Keystore: Contains certificates and their associated keys. - Truststore: Contains trusted certificates used to validate a server's certificate. These certificates are typically self-signed certificates or certificates that are not signed by a trusted CA.

        :param str resource_name: The name of the resource.
        :param OrganizationEnvironmentKeystoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationEnvironmentKeystoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environments_id: Optional[pulumi.Input[str]] = None,
                 keystores_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = OrganizationEnvironmentKeystoreArgs.__new__(OrganizationEnvironmentKeystoreArgs)

            if environments_id is None and not opts.urn:
                raise TypeError("Missing required property 'environments_id'")
            __props__.__dict__["environments_id"] = environments_id
            if keystores_id is None and not opts.urn:
                raise TypeError("Missing required property 'keystores_id'")
            __props__.__dict__["keystores_id"] = keystores_id
            __props__.__dict__["name"] = name
            if organizations_id is None and not opts.urn:
                raise TypeError("Missing required property 'organizations_id'")
            __props__.__dict__["organizations_id"] = organizations_id
            __props__.__dict__["aliases"] = None
        super(OrganizationEnvironmentKeystore, __self__).__init__(
            'gcp-native:apigee/v1:OrganizationEnvironmentKeystore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationEnvironmentKeystore':
        """
        Get an existing OrganizationEnvironmentKeystore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationEnvironmentKeystoreArgs.__new__(OrganizationEnvironmentKeystoreArgs)

        __props__.__dict__["aliases"] = None
        __props__.__dict__["name"] = None
        return OrganizationEnvironmentKeystore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def aliases(self) -> pulumi.Output[Sequence[str]]:
        """
        Aliases in this keystore.
        """
        return pulumi.get(self, "aliases")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. Resource ID for this keystore. Values must match the regular expression `[\w[:space:]-.]{1,255}`.
        """
        return pulumi.get(self, "name")
