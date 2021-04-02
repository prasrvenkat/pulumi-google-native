# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs

__all__ = ['Taxonomy']


class Taxonomy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activated_policy_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 taxonomies_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a taxonomy in the specified project.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] activated_policy_types: Optional. A list of policy types that are activated for this taxonomy. If not set, defaults to an empty list.
        :param pulumi.Input[str] description: Optional. Description of this taxonomy. It must: contain only unicode characters, tabs, newlines, carriage returns and page breaks; and be at most 2000 bytes long when encoded in UTF-8. If not set, defaults to an empty description.
        :param pulumi.Input[str] display_name: Required. User defined name of this taxonomy. It must: contain only unicode letters, numbers, underscores, dashes and spaces; not start or end with spaces; and be at most 200 bytes long when encoded in UTF-8.
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

            __props__['activated_policy_types'] = activated_policy_types
            __props__['description'] = description
            __props__['display_name'] = display_name
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__['locations_id'] = locations_id
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            if taxonomies_id is None and not opts.urn:
                raise TypeError("Missing required property 'taxonomies_id'")
            __props__['taxonomies_id'] = taxonomies_id
            __props__['name'] = None
            __props__['policy_tag_count'] = None
            __props__['taxonomy_timestamps'] = None
        super(Taxonomy, __self__).__init__(
            'google-cloud:datacatalog/v1beta1:Taxonomy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Taxonomy':
        """
        Get an existing Taxonomy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["activated_policy_types"] = None
        __props__["description"] = None
        __props__["display_name"] = None
        __props__["name"] = None
        __props__["policy_tag_count"] = None
        __props__["taxonomy_timestamps"] = None
        return Taxonomy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activatedPolicyTypes")
    def activated_policy_types(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. A list of policy types that are activated for this taxonomy. If not set, defaults to an empty list.
        """
        return pulumi.get(self, "activated_policy_types")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. Description of this taxonomy. It must: contain only unicode characters, tabs, newlines, carriage returns and page breaks; and be at most 2000 bytes long when encoded in UTF-8. If not set, defaults to an empty description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Required. User defined name of this taxonomy. It must: contain only unicode letters, numbers, underscores, dashes and spaces; not start or end with spaces; and be at most 200 bytes long when encoded in UTF-8.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of this taxonomy, whose format is: "projects/{project_number}/locations/{location_id}/taxonomies/{id}".
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyTagCount")
    def policy_tag_count(self) -> pulumi.Output[int]:
        """
        Number of policy tags contained in this taxonomy.
        """
        return pulumi.get(self, "policy_tag_count")

    @property
    @pulumi.getter(name="taxonomyTimestamps")
    def taxonomy_timestamps(self) -> pulumi.Output['outputs.GoogleCloudDatacatalogV1beta1SystemTimestampsResponse']:
        """
        Timestamps about this taxonomy. Only create_time and update_time are used.
        """
        return pulumi.get(self, "taxonomy_timestamps")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
