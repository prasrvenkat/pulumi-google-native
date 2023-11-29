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

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[str],
                 disable_proxy_access: Optional[pulumi.Input[bool]] = None,
                 gce_setup: Optional[pulumi.Input['GceSetupArgs']] = None,
                 instance_owners: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input[str] instance_id: Required. User-defined unique ID of this instance.
        :param pulumi.Input[bool] disable_proxy_access: Optional. If true, the notebook instance will not register with the proxy.
        :param pulumi.Input['GceSetupArgs'] gce_setup: Optional. Compute Engine setup for the notebook. Uses notebook-defined fields.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_owners: Optional. Input only. The owner of this instance after creation. Format: `alias@example.com` Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Labels to apply to this instance. These can be later modified by the UpdateInstance method.
        :param pulumi.Input[str] request_id: Optional. Idempotent request UUID.
        """
        pulumi.set(__self__, "instance_id", instance_id)
        if disable_proxy_access is not None:
            pulumi.set(__self__, "disable_proxy_access", disable_proxy_access)
        if gce_setup is not None:
            pulumi.set(__self__, "gce_setup", gce_setup)
        if instance_owners is not None:
            pulumi.set(__self__, "instance_owners", instance_owners)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        Required. User-defined unique ID of this instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="disableProxyAccess")
    def disable_proxy_access(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional. If true, the notebook instance will not register with the proxy.
        """
        return pulumi.get(self, "disable_proxy_access")

    @disable_proxy_access.setter
    def disable_proxy_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_proxy_access", value)

    @property
    @pulumi.getter(name="gceSetup")
    def gce_setup(self) -> Optional[pulumi.Input['GceSetupArgs']]:
        """
        Optional. Compute Engine setup for the notebook. Uses notebook-defined fields.
        """
        return pulumi.get(self, "gce_setup")

    @gce_setup.setter
    def gce_setup(self, value: Optional[pulumi.Input['GceSetupArgs']]):
        pulumi.set(self, "gce_setup", value)

    @property
    @pulumi.getter(name="instanceOwners")
    def instance_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Optional. Input only. The owner of this instance after creation. Format: `alias@example.com` Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance.
        """
        return pulumi.get(self, "instance_owners")

    @instance_owners.setter
    def instance_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "instance_owners", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. Labels to apply to this instance. These can be later modified by the UpdateInstance method.
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
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Idempotent request UUID.
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_proxy_access: Optional[pulumi.Input[bool]] = None,
                 gce_setup: Optional[pulumi.Input[pulumi.InputType['GceSetupArgs']]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 instance_owners: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new Instance in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disable_proxy_access: Optional. If true, the notebook instance will not register with the proxy.
        :param pulumi.Input[pulumi.InputType['GceSetupArgs']] gce_setup: Optional. Compute Engine setup for the notebook. Uses notebook-defined fields.
        :param pulumi.Input[str] instance_id: Required. User-defined unique ID of this instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_owners: Optional. Input only. The owner of this instance after creation. Format: `alias@example.com` Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Labels to apply to this instance. These can be later modified by the UpdateInstance method.
        :param pulumi.Input[str] request_id: Optional. Idempotent request UUID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Instance in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_proxy_access: Optional[pulumi.Input[bool]] = None,
                 gce_setup: Optional[pulumi.Input[pulumi.InputType['GceSetupArgs']]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 instance_owners: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceArgs.__new__(InstanceArgs)

            __props__.__dict__["disable_proxy_access"] = disable_proxy_access
            __props__.__dict__["gce_setup"] = gce_setup
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["instance_owners"] = instance_owners
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["creator"] = None
            __props__.__dict__["health_info"] = None
            __props__.__dict__["health_state"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["proxy_uri"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["update_time"] = None
            __props__.__dict__["upgrade_history"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["instance_id", "location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Instance, __self__).__init__(
            'google-native:notebooks/v2:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceArgs.__new__(InstanceArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["creator"] = None
        __props__.__dict__["disable_proxy_access"] = None
        __props__.__dict__["gce_setup"] = None
        __props__.__dict__["health_info"] = None
        __props__.__dict__["health_state"] = None
        __props__.__dict__["instance_id"] = None
        __props__.__dict__["instance_owners"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["proxy_uri"] = None
        __props__.__dict__["request_id"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["upgrade_history"] = None
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Instance creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def creator(self) -> pulumi.Output[str]:
        """
        Email address of entity that sent original CreateInstance request.
        """
        return pulumi.get(self, "creator")

    @property
    @pulumi.getter(name="disableProxyAccess")
    def disable_proxy_access(self) -> pulumi.Output[bool]:
        """
        Optional. If true, the notebook instance will not register with the proxy.
        """
        return pulumi.get(self, "disable_proxy_access")

    @property
    @pulumi.getter(name="gceSetup")
    def gce_setup(self) -> pulumi.Output['outputs.GceSetupResponse']:
        """
        Optional. Compute Engine setup for the notebook. Uses notebook-defined fields.
        """
        return pulumi.get(self, "gce_setup")

    @property
    @pulumi.getter(name="healthInfo")
    def health_info(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Additional information about instance health. Example: healthInfo": { "docker_proxy_agent_status": "1", "docker_status": "1", "jupyterlab_api_status": "-1", "jupyterlab_status": "-1", "updated": "2020-10-18 09:40:03.573409" }
        """
        return pulumi.get(self, "health_info")

    @property
    @pulumi.getter(name="healthState")
    def health_state(self) -> pulumi.Output[str]:
        """
        Instance health_state.
        """
        return pulumi.get(self, "health_state")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        Required. User-defined unique ID of this instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="instanceOwners")
    def instance_owners(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. Input only. The owner of this instance after creation. Format: `alias@example.com` Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance.
        """
        return pulumi.get(self, "instance_owners")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Labels to apply to this instance. These can be later modified by the UpdateInstance method.
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
        The name of this notebook instance. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="proxyUri")
    def proxy_uri(self) -> pulumi.Output[str]:
        """
        The proxy endpoint that is used to access the Jupyter notebook.
        """
        return pulumi.get(self, "proxy_uri")

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. Idempotent request UUID.
        """
        return pulumi.get(self, "request_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of this instance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Instance update time.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="upgradeHistory")
    def upgrade_history(self) -> pulumi.Output[Sequence['outputs.UpgradeHistoryEntryResponse']]:
        """
        The upgrade history of this instance.
        """
        return pulumi.get(self, "upgrade_history")
