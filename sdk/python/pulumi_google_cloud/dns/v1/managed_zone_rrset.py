# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['ManagedZoneRrset']


class ManagedZoneRrset(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 managed_zone: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 rrdatas: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 signature_rrdatas: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new ResourceRecordSet.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: For example, www.example.com.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rrdatas: As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) -- see examples.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] signature_rrdatas: As defined in RFC 4034 (section 3.2).
        :param pulumi.Input[int] ttl: Number of seconds that this ResourceRecordSet can be cached by resolvers.
        :param pulumi.Input[str] type: The identifier of a supported record type. See the list of Supported DNS record types.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['kind'] = kind
            if managed_zone is None and not opts.urn:
                raise TypeError("Missing required property 'managed_zone'")
            __props__['managed_zone'] = managed_zone
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__['name'] = name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            __props__['rrdatas'] = rrdatas
            __props__['signature_rrdatas'] = signature_rrdatas
            __props__['ttl'] = ttl
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
        super(ManagedZoneRrset, __self__).__init__(
            'google-cloud:dns/v1:ManagedZoneRrset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedZoneRrset':
        """
        Get an existing ManagedZoneRrset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["kind"] = None
        __props__["name"] = None
        __props__["rrdatas"] = None
        __props__["signature_rrdatas"] = None
        __props__["ttl"] = None
        __props__["type"] = None
        return ManagedZoneRrset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        For example, www.example.com.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rrdatas(self) -> pulumi.Output[Sequence[str]]:
        """
        As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) -- see examples.
        """
        return pulumi.get(self, "rrdatas")

    @property
    @pulumi.getter(name="signatureRrdatas")
    def signature_rrdatas(self) -> pulumi.Output[Sequence[str]]:
        """
        As defined in RFC 4034 (section 3.2).
        """
        return pulumi.get(self, "signature_rrdatas")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[int]:
        """
        Number of seconds that this ResourceRecordSet can be cached by resolvers.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The identifier of a supported record type. See the list of Supported DNS record types.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
