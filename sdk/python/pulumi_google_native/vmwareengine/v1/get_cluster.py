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

__all__ = [
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    def __init__(__self__, create_time=None, management=None, name=None, node_type_configs=None, state=None, stretched_cluster_config=None, uid=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if management and not isinstance(management, bool):
            raise TypeError("Expected argument 'management' to be a bool")
        pulumi.set(__self__, "management", management)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_type_configs and not isinstance(node_type_configs, dict):
            raise TypeError("Expected argument 'node_type_configs' to be a dict")
        pulumi.set(__self__, "node_type_configs", node_type_configs)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if stretched_cluster_config and not isinstance(stretched_cluster_config, dict):
            raise TypeError("Expected argument 'stretched_cluster_config' to be a dict")
        pulumi.set(__self__, "stretched_cluster_config", stretched_cluster_config)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Creation time of this resource.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def management(self) -> bool:
        """
        True if the cluster is a management cluster; false otherwise. There can only be one management cluster in a private cloud and it has to be the first one.
        """
        return pulumi.get(self, "management")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of this cluster. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeTypeConfigs")
    def node_type_configs(self) -> Mapping[str, str]:
        """
        The map of cluster node types in this cluster, where the key is canonical identifier of the node type (corresponds to the `NodeType`).
        """
        return pulumi.get(self, "node_type_configs")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stretchedClusterConfig")
    def stretched_cluster_config(self) -> 'outputs.StretchedClusterConfigResponse':
        """
        Optional. Configuration of a stretched cluster. Required for clusters that belong to a STRETCHED private cloud.
        """
        return pulumi.get(self, "stretched_cluster_config")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        System-generated unique identifier for the resource.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Last update time of this resource.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            create_time=self.create_time,
            management=self.management,
            name=self.name,
            node_type_configs=self.node_type_configs,
            state=self.state,
            stretched_cluster_config=self.stretched_cluster_config,
            uid=self.uid,
            update_time=self.update_time)


def get_cluster(cluster_id: Optional[str] = None,
                location: Optional[str] = None,
                private_cloud_id: Optional[str] = None,
                project: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Retrieves a `Cluster` resource by its resource name.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['location'] = location
    __args__['privateCloudId'] = private_cloud_id
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:vmwareengine/v1:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        create_time=pulumi.get(__ret__, 'create_time'),
        management=pulumi.get(__ret__, 'management'),
        name=pulumi.get(__ret__, 'name'),
        node_type_configs=pulumi.get(__ret__, 'node_type_configs'),
        state=pulumi.get(__ret__, 'state'),
        stretched_cluster_config=pulumi.get(__ret__, 'stretched_cluster_config'),
        uid=pulumi.get(__ret__, 'uid'),
        update_time=pulumi.get(__ret__, 'update_time'))


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(cluster_id: Optional[pulumi.Input[str]] = None,
                       location: Optional[pulumi.Input[str]] = None,
                       private_cloud_id: Optional[pulumi.Input[str]] = None,
                       project: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    Retrieves a `Cluster` resource by its resource name.
    """
    ...