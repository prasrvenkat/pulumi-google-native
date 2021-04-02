# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Service']


class Service(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['ObjectMetaArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 services_id: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['ServiceSpecArgs']]] = None,
                 status: Optional[pulumi.Input[pulumi.InputType['ServiceStatusArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Rpc to create a service.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_version: The API version for this call such as "serving.knative.dev/v1alpha1".
        :param pulumi.Input[str] kind: The kind of resource, in this case "Service".
        :param pulumi.Input[pulumi.InputType['ObjectMetaArgs']] metadata: Metadata associated with this Service, including name, namespace, labels, and annotations.
        :param pulumi.Input[pulumi.InputType['ServiceSpecArgs']] spec: Spec holds the desired state of the Service (from the client).
        :param pulumi.Input[pulumi.InputType['ServiceStatusArgs']] status: Status communicates the observed state of the Service (from the controller).
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

            __props__['api_version'] = api_version
            __props__['kind'] = kind
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            __props__['metadata'] = metadata
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            if services_id is None and not opts.urn:
                raise TypeError("Missing required property 'services_id'")
            __props__['services_id'] = services_id
            __props__['spec'] = spec
            __props__['status'] = status
        super(Service, __self__).__init__(
            'google-cloud:run/v1alpha1:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_version"] = None
        __props__["kind"] = None
        __props__["metadata"] = None
        __props__["spec"] = None
        __props__["status"] = None
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[str]:
        """
        The API version for this call such as "serving.knative.dev/v1alpha1".
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of resource, in this case "Service".
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.ObjectMetaResponse']:
        """
        Metadata associated with this Service, including name, namespace, labels, and annotations.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output['outputs.ServiceSpecResponse']:
        """
        Spec holds the desired state of the Service (from the client).
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.ServiceStatusResponse']:
        """
        Status communicates the observed state of the Service (from the controller).
        """
        return pulumi.get(self, "status")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
