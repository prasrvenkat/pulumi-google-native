# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'BareMetalClusterUpgradePolicyPolicy',
    'BareMetalNodePoolConfigOperatingSystem',
    'BareMetalWorkloadNodeConfigContainerRuntime',
    'BinaryAuthorizationEvaluationMode',
    'NodeTaintEffect',
]


class BareMetalClusterUpgradePolicyPolicy(str, Enum):
    """
    Specifies which upgrade policy to use.
    """
    NODE_POOL_POLICY_UNSPECIFIED = "NODE_POOL_POLICY_UNSPECIFIED"
    """
    No upgrade policy selected.
    """
    SERIAL = "SERIAL"
    """
    Upgrade worker node pools sequentially.
    """
    CONCURRENT = "CONCURRENT"
    """
    Upgrade all worker node pools in parallel.
    """


class BareMetalNodePoolConfigOperatingSystem(str, Enum):
    """
    Specifies the nodes operating system (default: LINUX).
    """
    OPERATING_SYSTEM_UNSPECIFIED = "OPERATING_SYSTEM_UNSPECIFIED"
    """
    No operating system runtime selected.
    """
    LINUX = "LINUX"
    """
    Linux operating system.
    """


class BareMetalWorkloadNodeConfigContainerRuntime(str, Enum):
    """
    Specifies which container runtime will be used.
    """
    CONTAINER_RUNTIME_UNSPECIFIED = "CONTAINER_RUNTIME_UNSPECIFIED"
    """
    No container runtime selected.
    """
    CONTAINERD = "CONTAINERD"
    """
    Containerd runtime.
    """


class BinaryAuthorizationEvaluationMode(str, Enum):
    """
    Mode of operation for binauthz policy evaluation. If unspecified, defaults to DISABLED.
    """
    EVALUATION_MODE_UNSPECIFIED = "EVALUATION_MODE_UNSPECIFIED"
    """
    Default value
    """
    DISABLED = "DISABLED"
    """
    Disable BinaryAuthorization
    """
    PROJECT_SINGLETON_POLICY_ENFORCE = "PROJECT_SINGLETON_POLICY_ENFORCE"
    """
    Enforce Kubernetes admission requests with BinaryAuthorization using the project's singleton policy.
    """


class NodeTaintEffect(str, Enum):
    """
    The taint effect.
    """
    EFFECT_UNSPECIFIED = "EFFECT_UNSPECIFIED"
    """
    Not set.
    """
    NO_SCHEDULE = "NO_SCHEDULE"
    """
    Do not allow new pods to schedule onto the node unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. Enforced by the scheduler.
    """
    PREFER_NO_SCHEDULE = "PREFER_NO_SCHEDULE"
    """
    Like TaintEffectNoSchedule, but the scheduler tries not to schedule new pods onto the node, rather than prohibiting new pods from scheduling onto the node entirely. Enforced by the scheduler.
    """
    NO_EXECUTE = "NO_EXECUTE"
    """
    Evict any already-running pods that do not tolerate the taint. Currently enforced by NodeController.
    """
