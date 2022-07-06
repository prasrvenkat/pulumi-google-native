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
from ._enums import *
from ._inputs import *

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 instance: pulumi.Input[str],
                 dual_password_type: Optional[pulumi.Input['UserDualPasswordType']] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 password_policy: Optional[pulumi.Input['UserPasswordValidationPolicyArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 sqlserver_user_details: Optional[pulumi.Input['SqlServerUserDetailsArgs']] = None,
                 type: Optional[pulumi.Input['UserType']] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. This does not include the project ID. Can be omitted for *update* because it is already specified on the URL.
        :param pulumi.Input['UserDualPasswordType'] dual_password_type: Dual password status for the user.
        :param pulumi.Input[str] etag: This field is deprecated and will be removed from a future version of the API.
        :param pulumi.Input[str] host: Optional. The host from which the user can connect. For `insert` operations, host defaults to an empty string. For `update` operations, host is specified as part of the request URL. The host name cannot be updated after insertion. For a MySQL instance, it's required; for a PostgreSQL or SQL Server instance, it's optional.
        :param pulumi.Input[str] kind: This is always `sql#user`.
        :param pulumi.Input[str] name: The name of the user in the Cloud SQL instance. Can be omitted for `update` because it is already specified in the URL.
        :param pulumi.Input[str] password: The password for the user.
        :param pulumi.Input['UserPasswordValidationPolicyArgs'] password_policy: User level password validation policy.
        :param pulumi.Input[str] project: The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable. Can be omitted for *update* because it is already specified on the URL.
        :param pulumi.Input['UserType'] type: The user type. It determines the method to authenticate the user during login. The default is the database's built-in user type.
        """
        pulumi.set(__self__, "instance", instance)
        if dual_password_type is not None:
            pulumi.set(__self__, "dual_password_type", dual_password_type)
        if etag is not None:
            warnings.warn("""This field is deprecated and will be removed from a future version of the API.""", DeprecationWarning)
            pulumi.log.warn("""etag is deprecated: This field is deprecated and will be removed from a future version of the API.""")
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if password_policy is not None:
            pulumi.set(__self__, "password_policy", password_policy)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if sqlserver_user_details is not None:
            pulumi.set(__self__, "sqlserver_user_details", sqlserver_user_details)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Input[str]:
        """
        The name of the Cloud SQL instance. This does not include the project ID. Can be omitted for *update* because it is already specified on the URL.
        """
        return pulumi.get(self, "instance")

    @instance.setter
    def instance(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance", value)

    @property
    @pulumi.getter(name="dualPasswordType")
    def dual_password_type(self) -> Optional[pulumi.Input['UserDualPasswordType']]:
        """
        Dual password status for the user.
        """
        return pulumi.get(self, "dual_password_type")

    @dual_password_type.setter
    def dual_password_type(self, value: Optional[pulumi.Input['UserDualPasswordType']]):
        pulumi.set(self, "dual_password_type", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        This field is deprecated and will be removed from a future version of the API.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The host from which the user can connect. For `insert` operations, host defaults to an empty string. For `update` operations, host is specified as part of the request URL. The host name cannot be updated after insertion. For a MySQL instance, it's required; for a PostgreSQL or SQL Server instance, it's optional.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        This is always `sql#user`.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user in the Cloud SQL instance. Can be omitted for `update` because it is already specified in the URL.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password for the user.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="passwordPolicy")
    def password_policy(self) -> Optional[pulumi.Input['UserPasswordValidationPolicyArgs']]:
        """
        User level password validation policy.
        """
        return pulumi.get(self, "password_policy")

    @password_policy.setter
    def password_policy(self, value: Optional[pulumi.Input['UserPasswordValidationPolicyArgs']]):
        pulumi.set(self, "password_policy", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable. Can be omitted for *update* because it is already specified on the URL.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="sqlserverUserDetails")
    def sqlserver_user_details(self) -> Optional[pulumi.Input['SqlServerUserDetailsArgs']]:
        return pulumi.get(self, "sqlserver_user_details")

    @sqlserver_user_details.setter
    def sqlserver_user_details(self, value: Optional[pulumi.Input['SqlServerUserDetailsArgs']]):
        pulumi.set(self, "sqlserver_user_details", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['UserType']]:
        """
        The user type. It determines the method to authenticate the user during login. The default is the database's built-in user type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['UserType']]):
        pulumi.set(self, "type", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dual_password_type: Optional[pulumi.Input['UserDualPasswordType']] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 password_policy: Optional[pulumi.Input[pulumi.InputType['UserPasswordValidationPolicyArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 sqlserver_user_details: Optional[pulumi.Input[pulumi.InputType['SqlServerUserDetailsArgs']]] = None,
                 type: Optional[pulumi.Input['UserType']] = None,
                 __props__=None):
        """
        Creates a new user in a Cloud SQL instance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['UserDualPasswordType'] dual_password_type: Dual password status for the user.
        :param pulumi.Input[str] etag: This field is deprecated and will be removed from a future version of the API.
        :param pulumi.Input[str] host: Optional. The host from which the user can connect. For `insert` operations, host defaults to an empty string. For `update` operations, host is specified as part of the request URL. The host name cannot be updated after insertion. For a MySQL instance, it's required; for a PostgreSQL or SQL Server instance, it's optional.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. This does not include the project ID. Can be omitted for *update* because it is already specified on the URL.
        :param pulumi.Input[str] kind: This is always `sql#user`.
        :param pulumi.Input[str] name: The name of the user in the Cloud SQL instance. Can be omitted for `update` because it is already specified in the URL.
        :param pulumi.Input[str] password: The password for the user.
        :param pulumi.Input[pulumi.InputType['UserPasswordValidationPolicyArgs']] password_policy: User level password validation policy.
        :param pulumi.Input[str] project: The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable. Can be omitted for *update* because it is already specified on the URL.
        :param pulumi.Input['UserType'] type: The user type. It determines the method to authenticate the user during login. The default is the database's built-in user type.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new user in a Cloud SQL instance.

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dual_password_type: Optional[pulumi.Input['UserDualPasswordType']] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 password_policy: Optional[pulumi.Input[pulumi.InputType['UserPasswordValidationPolicyArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 sqlserver_user_details: Optional[pulumi.Input[pulumi.InputType['SqlServerUserDetailsArgs']]] = None,
                 type: Optional[pulumi.Input['UserType']] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        else:
            opts = copy.copy(opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            __props__.__dict__["dual_password_type"] = dual_password_type
            if etag is not None and not opts.urn:
                warnings.warn("""This field is deprecated and will be removed from a future version of the API.""", DeprecationWarning)
                pulumi.log.warn("""etag is deprecated: This field is deprecated and will be removed from a future version of the API.""")
            __props__.__dict__["etag"] = etag
            __props__.__dict__["host"] = host
            if instance is None and not opts.urn:
                raise TypeError("Missing required property 'instance'")
            __props__.__dict__["instance"] = instance
            __props__.__dict__["kind"] = kind
            __props__.__dict__["name"] = name
            __props__.__dict__["password"] = password
            __props__.__dict__["password_policy"] = password_policy
            __props__.__dict__["project"] = project
            __props__.__dict__["sqlserver_user_details"] = sqlserver_user_details
            __props__.__dict__["type"] = type
        super(User, __self__).__init__(
            'google-native:sqladmin/v1beta4:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserArgs.__new__(UserArgs)

        __props__.__dict__["dual_password_type"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["host"] = None
        __props__.__dict__["instance"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["password"] = None
        __props__.__dict__["password_policy"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["sqlserver_user_details"] = None
        __props__.__dict__["type"] = None
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dualPasswordType")
    def dual_password_type(self) -> pulumi.Output[str]:
        """
        Dual password status for the user.
        """
        return pulumi.get(self, "dual_password_type")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        This field is deprecated and will be removed from a future version of the API.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[str]:
        """
        Optional. The host from which the user can connect. For `insert` operations, host defaults to an empty string. For `update` operations, host is specified as part of the request URL. The host name cannot be updated after insertion. For a MySQL instance, it's required; for a PostgreSQL or SQL Server instance, it's optional.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        This is always `sql#user`.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the user in the Cloud SQL instance. Can be omitted for `update` because it is already specified in the URL.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        The password for the user.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="passwordPolicy")
    def password_policy(self) -> pulumi.Output['outputs.UserPasswordValidationPolicyResponse']:
        """
        User level password validation policy.
        """
        return pulumi.get(self, "password_policy")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="sqlserverUserDetails")
    def sqlserver_user_details(self) -> pulumi.Output['outputs.SqlServerUserDetailsResponse']:
        return pulumi.get(self, "sqlserver_user_details")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The user type. It determines the method to authenticate the user during login. The default is the database's built-in user type.
        """
        return pulumi.get(self, "type")
