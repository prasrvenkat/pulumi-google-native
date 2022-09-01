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

__all__ = ['OauthIdpConfigArgs', 'OauthIdpConfig']

@pulumi.input_type
class OauthIdpConfigArgs:
    def __init__(__self__, *,
                 tenant_id: pulumi.Input[str],
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 oauth_idp_config_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 response_type: Optional[pulumi.Input['GoogleCloudIdentitytoolkitAdminV2OAuthResponseTypeArgs']] = None):
        """
        The set of arguments for constructing a OauthIdpConfig resource.
        :param pulumi.Input[str] client_id: The client id of an OAuth client.
        :param pulumi.Input[str] client_secret: The client secret of the OAuth client, to enable OIDC code flow.
        :param pulumi.Input[str] display_name: The config's display name set by developers.
        :param pulumi.Input[bool] enabled: True if allows the user to sign in with the provider.
        :param pulumi.Input[str] issuer: For OIDC Idps, the issuer identifier.
        :param pulumi.Input[str] name: The name of the OAuthIdpConfig resource, for example: 'projects/my-awesome-project/oauthIdpConfigs/oauth-config-id'. Ignored during create requests.
        :param pulumi.Input[str] oauth_idp_config_id: The id to use for this config.
        :param pulumi.Input['GoogleCloudIdentitytoolkitAdminV2OAuthResponseTypeArgs'] response_type: The response type to request for in the OAuth authorization flow. You can set either `id_token` or `code` to true, but not both. Setting both types to be simultaneously true (`{code: true, id_token: true}`) is not yet supported.
        """
        pulumi.set(__self__, "tenant_id", tenant_id)
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_secret is not None:
            pulumi.set(__self__, "client_secret", client_secret)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if issuer is not None:
            pulumi.set(__self__, "issuer", issuer)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if oauth_idp_config_id is not None:
            pulumi.set(__self__, "oauth_idp_config_id", oauth_idp_config_id)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if response_type is not None:
            pulumi.set(__self__, "response_type", response_type)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The client id of an OAuth client.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[str]]:
        """
        The client secret of the OAuth client, to enable OIDC code flow.
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The config's display name set by developers.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        True if allows the user to sign in with the provider.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[str]]:
        """
        For OIDC Idps, the issuer identifier.
        """
        return pulumi.get(self, "issuer")

    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "issuer", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the OAuthIdpConfig resource, for example: 'projects/my-awesome-project/oauthIdpConfigs/oauth-config-id'. Ignored during create requests.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="oauthIdpConfigId")
    def oauth_idp_config_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id to use for this config.
        """
        return pulumi.get(self, "oauth_idp_config_id")

    @oauth_idp_config_id.setter
    def oauth_idp_config_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth_idp_config_id", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="responseType")
    def response_type(self) -> Optional[pulumi.Input['GoogleCloudIdentitytoolkitAdminV2OAuthResponseTypeArgs']]:
        """
        The response type to request for in the OAuth authorization flow. You can set either `id_token` or `code` to true, but not both. Setting both types to be simultaneously true (`{code: true, id_token: true}`) is not yet supported.
        """
        return pulumi.get(self, "response_type")

    @response_type.setter
    def response_type(self, value: Optional[pulumi.Input['GoogleCloudIdentitytoolkitAdminV2OAuthResponseTypeArgs']]):
        pulumi.set(self, "response_type", value)


class OauthIdpConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 oauth_idp_config_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 response_type: Optional[pulumi.Input[pulumi.InputType['GoogleCloudIdentitytoolkitAdminV2OAuthResponseTypeArgs']]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create an Oidc Idp configuration for an Identity Toolkit project.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: The client id of an OAuth client.
        :param pulumi.Input[str] client_secret: The client secret of the OAuth client, to enable OIDC code flow.
        :param pulumi.Input[str] display_name: The config's display name set by developers.
        :param pulumi.Input[bool] enabled: True if allows the user to sign in with the provider.
        :param pulumi.Input[str] issuer: For OIDC Idps, the issuer identifier.
        :param pulumi.Input[str] name: The name of the OAuthIdpConfig resource, for example: 'projects/my-awesome-project/oauthIdpConfigs/oauth-config-id'. Ignored during create requests.
        :param pulumi.Input[str] oauth_idp_config_id: The id to use for this config.
        :param pulumi.Input[pulumi.InputType['GoogleCloudIdentitytoolkitAdminV2OAuthResponseTypeArgs']] response_type: The response type to request for in the OAuth authorization flow. You can set either `id_token` or `code` to true, but not both. Setting both types to be simultaneously true (`{code: true, id_token: true}`) is not yet supported.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OauthIdpConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create an Oidc Idp configuration for an Identity Toolkit project.

        :param str resource_name: The name of the resource.
        :param OauthIdpConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OauthIdpConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 oauth_idp_config_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 response_type: Optional[pulumi.Input[pulumi.InputType['GoogleCloudIdentitytoolkitAdminV2OAuthResponseTypeArgs']]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OauthIdpConfigArgs.__new__(OauthIdpConfigArgs)

            __props__.__dict__["client_id"] = client_id
            __props__.__dict__["client_secret"] = client_secret
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["issuer"] = issuer
            __props__.__dict__["name"] = name
            __props__.__dict__["oauth_idp_config_id"] = oauth_idp_config_id
            __props__.__dict__["project"] = project
            __props__.__dict__["response_type"] = response_type
            if tenant_id is None and not opts.urn:
                raise TypeError("Missing required property 'tenant_id'")
            __props__.__dict__["tenant_id"] = tenant_id
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["project", "tenant_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(OauthIdpConfig, __self__).__init__(
            'google-native:identitytoolkit/v2:OauthIdpConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OauthIdpConfig':
        """
        Get an existing OauthIdpConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OauthIdpConfigArgs.__new__(OauthIdpConfigArgs)

        __props__.__dict__["client_id"] = None
        __props__.__dict__["client_secret"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["issuer"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["oauth_idp_config_id"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["response_type"] = None
        __props__.__dict__["tenant_id"] = None
        return OauthIdpConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        """
        The client id of an OAuth client.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[str]:
        """
        The client secret of the OAuth client, to enable OIDC code flow.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The config's display name set by developers.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        True if allows the user to sign in with the provider.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def issuer(self) -> pulumi.Output[str]:
        """
        For OIDC Idps, the issuer identifier.
        """
        return pulumi.get(self, "issuer")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the OAuthIdpConfig resource, for example: 'projects/my-awesome-project/oauthIdpConfigs/oauth-config-id'. Ignored during create requests.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oauthIdpConfigId")
    def oauth_idp_config_id(self) -> pulumi.Output[Optional[str]]:
        """
        The id to use for this config.
        """
        return pulumi.get(self, "oauth_idp_config_id")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="responseType")
    def response_type(self) -> pulumi.Output['outputs.GoogleCloudIdentitytoolkitAdminV2OAuthResponseTypeResponse']:
        """
        The response type to request for in the OAuth authorization flow. You can set either `id_token` or `code` to true, but not both. Setting both types to be simultaneously true (`{code: true, id_token: true}`) is not yet supported.
        """
        return pulumi.get(self, "response_type")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "tenant_id")
