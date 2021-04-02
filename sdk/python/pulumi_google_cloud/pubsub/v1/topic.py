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

__all__ = ['Topic']


class Topic(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 message_storage_policy: Optional[pulumi.Input[pulumi.InputType['MessageStoragePolicyArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 satisfies_pzs: Optional[pulumi.Input[bool]] = None,
                 schema_settings: Optional[pulumi.Input[pulumi.InputType['SchemaSettingsArgs']]] = None,
                 topics_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates the given topic with the given name. See the [resource name rules] (https://cloud.google.com/pubsub/docs/admin#resource_names).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kms_key_name: The resource name of the Cloud KMS CryptoKey to be used to protect access to messages published on this topic. The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: See [Creating and managing labels] (https://cloud.google.com/pubsub/docs/labels).
        :param pulumi.Input[pulumi.InputType['MessageStoragePolicyArgs']] message_storage_policy: Policy constraining the set of Google Cloud Platform regions where messages published to the topic may be stored. If not present, then no constraints are in effect.
        :param pulumi.Input[str] name: Required. The name of the topic. It must have the format `"projects/{project}/topics/{topic}"`. `{topic}` must start with a letter, and contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (`~`), plus (`+`) or percent signs (`%`). It must be between 3 and 255 characters in length, and it must not start with `"goog"`.
        :param pulumi.Input[bool] satisfies_pzs: Reserved for future use. This field is set only in responses from the server; it is ignored if it is set in any requests.
        :param pulumi.Input[pulumi.InputType['SchemaSettingsArgs']] schema_settings: Settings for validating messages published against a schema.
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

            __props__['kms_key_name'] = kms_key_name
            __props__['labels'] = labels
            __props__['message_storage_policy'] = message_storage_policy
            __props__['name'] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__['projects_id'] = projects_id
            __props__['satisfies_pzs'] = satisfies_pzs
            __props__['schema_settings'] = schema_settings
            if topics_id is None and not opts.urn:
                raise TypeError("Missing required property 'topics_id'")
            __props__['topics_id'] = topics_id
        super(Topic, __self__).__init__(
            'google-cloud:pubsub/v1:Topic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Topic':
        """
        Get an existing Topic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["kms_key_name"] = None
        __props__["labels"] = None
        __props__["message_storage_policy"] = None
        __props__["name"] = None
        __props__["satisfies_pzs"] = None
        __props__["schema_settings"] = None
        return Topic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[str]:
        """
        The resource name of the Cloud KMS CryptoKey to be used to protect access to messages published on this topic. The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`.
        """
        return pulumi.get(self, "kms_key_name")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        See [Creating and managing labels] (https://cloud.google.com/pubsub/docs/labels).
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="messageStoragePolicy")
    def message_storage_policy(self) -> pulumi.Output['outputs.MessageStoragePolicyResponse']:
        """
        Policy constraining the set of Google Cloud Platform regions where messages published to the topic may be stored. If not present, then no constraints are in effect.
        """
        return pulumi.get(self, "message_storage_policy")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. The name of the topic. It must have the format `"projects/{project}/topics/{topic}"`. `{topic}` must start with a letter, and contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (`~`), plus (`+`) or percent signs (`%`). It must be between 3 and 255 characters in length, and it must not start with `"goog"`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> pulumi.Output[bool]:
        """
        Reserved for future use. This field is set only in responses from the server; it is ignored if it is set in any requests.
        """
        return pulumi.get(self, "satisfies_pzs")

    @property
    @pulumi.getter(name="schemaSettings")
    def schema_settings(self) -> pulumi.Output['outputs.SchemaSettingsResponse']:
        """
        Settings for validating messages published against a schema.
        """
        return pulumi.get(self, "schema_settings")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
