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

__all__ = ['DeveloperAppArgs', 'DeveloperApp']

@pulumi.input_type
class DeveloperAppArgs:
    def __init__(__self__, *,
                 developer_id: pulumi.Input[str],
                 organization_id: pulumi.Input[str],
                 api_products: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 app_family: Optional[pulumi.Input[str]] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1AttributeArgs']]]] = None,
                 callback_url: Optional[pulumi.Input[str]] = None,
                 key_expires_in: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DeveloperApp resource.
        :param pulumi.Input[str] developer_id: ID of the developer.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] api_products: List of API products associated with the developer app.
        :param pulumi.Input[str] app_family: Developer app family.
        :param pulumi.Input[str] app_id: ID of the developer app.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1AttributeArgs']]] attributes: List of attributes for the developer app.
        :param pulumi.Input[str] callback_url: Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to developer apps.
        :param pulumi.Input[str] key_expires_in: Expiration time, in milliseconds, for the consumer key that is generated for the developer app. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set.
        :param pulumi.Input[str] name: Name of the developer app.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Scopes to apply to the developer app. The specified scopes must already exist for the API product that you associate with the developer app.
        :param pulumi.Input[str] status: Status of the credential. Valid values include `approved` or `revoked`.
        """
        pulumi.set(__self__, "developer_id", developer_id)
        pulumi.set(__self__, "organization_id", organization_id)
        if api_products is not None:
            pulumi.set(__self__, "api_products", api_products)
        if app_family is not None:
            pulumi.set(__self__, "app_family", app_family)
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if callback_url is not None:
            pulumi.set(__self__, "callback_url", callback_url)
        if key_expires_in is not None:
            pulumi.set(__self__, "key_expires_in", key_expires_in)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="developerId")
    def developer_id(self) -> pulumi.Input[str]:
        """
        ID of the developer.
        """
        return pulumi.get(self, "developer_id")

    @developer_id.setter
    def developer_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "developer_id", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="apiProducts")
    def api_products(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of API products associated with the developer app.
        """
        return pulumi.get(self, "api_products")

    @api_products.setter
    def api_products(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "api_products", value)

    @property
    @pulumi.getter(name="appFamily")
    def app_family(self) -> Optional[pulumi.Input[str]]:
        """
        Developer app family.
        """
        return pulumi.get(self, "app_family")

    @app_family.setter
    def app_family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_family", value)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the developer app.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1AttributeArgs']]]]:
        """
        List of attributes for the developer app.
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1AttributeArgs']]]]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter(name="callbackUrl")
    def callback_url(self) -> Optional[pulumi.Input[str]]:
        """
        Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to developer apps.
        """
        return pulumi.get(self, "callback_url")

    @callback_url.setter
    def callback_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "callback_url", value)

    @property
    @pulumi.getter(name="keyExpiresIn")
    def key_expires_in(self) -> Optional[pulumi.Input[str]]:
        """
        Expiration time, in milliseconds, for the consumer key that is generated for the developer app. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set.
        """
        return pulumi.get(self, "key_expires_in")

    @key_expires_in.setter
    def key_expires_in(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_expires_in", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the developer app.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Scopes to apply to the developer app. The specified scopes must already exist for the API product that you associate with the developer app.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the credential. Valid values include `approved` or `revoked`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class DeveloperApp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_products: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 app_family: Optional[pulumi.Input[str]] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1AttributeArgs']]]]] = None,
                 callback_url: Optional[pulumi.Input[str]] = None,
                 developer_id: Optional[pulumi.Input[str]] = None,
                 key_expires_in: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an app associated with a developer. This API associates the developer app with the specified API product and auto-generates an API key for the app to use in calls to API proxies inside that API product. The `name` is the unique ID of the app that you can use in API calls. The `DisplayName` (set as an attribute) appears in the UI. If you don't set the `DisplayName` attribute, the `name` appears in the UI.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] api_products: List of API products associated with the developer app.
        :param pulumi.Input[str] app_family: Developer app family.
        :param pulumi.Input[str] app_id: ID of the developer app.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1AttributeArgs']]]] attributes: List of attributes for the developer app.
        :param pulumi.Input[str] callback_url: Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to developer apps.
        :param pulumi.Input[str] developer_id: ID of the developer.
        :param pulumi.Input[str] key_expires_in: Expiration time, in milliseconds, for the consumer key that is generated for the developer app. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set.
        :param pulumi.Input[str] name: Name of the developer app.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Scopes to apply to the developer app. The specified scopes must already exist for the API product that you associate with the developer app.
        :param pulumi.Input[str] status: Status of the credential. Valid values include `approved` or `revoked`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeveloperAppArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an app associated with a developer. This API associates the developer app with the specified API product and auto-generates an API key for the app to use in calls to API proxies inside that API product. The `name` is the unique ID of the app that you can use in API calls. The `DisplayName` (set as an attribute) appears in the UI. If you don't set the `DisplayName` attribute, the `name` appears in the UI.

        :param str resource_name: The name of the resource.
        :param DeveloperAppArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeveloperAppArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_products: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 app_family: Optional[pulumi.Input[str]] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1AttributeArgs']]]]] = None,
                 callback_url: Optional[pulumi.Input[str]] = None,
                 developer_id: Optional[pulumi.Input[str]] = None,
                 key_expires_in: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeveloperAppArgs.__new__(DeveloperAppArgs)

            __props__.__dict__["api_products"] = api_products
            __props__.__dict__["app_family"] = app_family
            __props__.__dict__["app_id"] = app_id
            __props__.__dict__["attributes"] = attributes
            __props__.__dict__["callback_url"] = callback_url
            if developer_id is None and not opts.urn:
                raise TypeError("Missing required property 'developer_id'")
            __props__.__dict__["developer_id"] = developer_id
            __props__.__dict__["key_expires_in"] = key_expires_in
            __props__.__dict__["name"] = name
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["status"] = status
            __props__.__dict__["created_at"] = None
            __props__.__dict__["credentials"] = None
            __props__.__dict__["last_modified_at"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["developer_id", "organization_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DeveloperApp, __self__).__init__(
            'google-native:apigee/v1:DeveloperApp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DeveloperApp':
        """
        Get an existing DeveloperApp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeveloperAppArgs.__new__(DeveloperAppArgs)

        __props__.__dict__["api_products"] = None
        __props__.__dict__["app_family"] = None
        __props__.__dict__["app_id"] = None
        __props__.__dict__["attributes"] = None
        __props__.__dict__["callback_url"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["credentials"] = None
        __props__.__dict__["developer_id"] = None
        __props__.__dict__["key_expires_in"] = None
        __props__.__dict__["last_modified_at"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["organization_id"] = None
        __props__.__dict__["scopes"] = None
        __props__.__dict__["status"] = None
        return DeveloperApp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiProducts")
    def api_products(self) -> pulumi.Output[Sequence[str]]:
        """
        List of API products associated with the developer app.
        """
        return pulumi.get(self, "api_products")

    @property
    @pulumi.getter(name="appFamily")
    def app_family(self) -> pulumi.Output[str]:
        """
        Developer app family.
        """
        return pulumi.get(self, "app_family")

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        """
        ID of the developer app.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Sequence['outputs.GoogleCloudApigeeV1AttributeResponse']]:
        """
        List of attributes for the developer app.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="callbackUrl")
    def callback_url(self) -> pulumi.Output[str]:
        """
        Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to developer apps.
        """
        return pulumi.get(self, "callback_url")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Time the developer app was created in milliseconds since epoch.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Sequence['outputs.GoogleCloudApigeeV1CredentialResponse']]:
        """
        Set of credentials for the developer app consisting of the consumer key/secret pairs associated with the API products.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="developerId")
    def developer_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "developer_id")

    @property
    @pulumi.getter(name="keyExpiresIn")
    def key_expires_in(self) -> pulumi.Output[str]:
        """
        Expiration time, in milliseconds, for the consumer key that is generated for the developer app. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set.
        """
        return pulumi.get(self, "key_expires_in")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[str]:
        """
        Time the developer app was modified in milliseconds since epoch.
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the developer app.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Sequence[str]]:
        """
        Scopes to apply to the developer app. The specified scopes must already exist for the API product that you associate with the developer app.
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the credential. Valid values include `approved` or `revoked`.
        """
        return pulumi.get(self, "status")
