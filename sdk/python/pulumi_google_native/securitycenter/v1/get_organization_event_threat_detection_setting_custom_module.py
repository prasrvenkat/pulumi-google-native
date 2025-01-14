# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetOrganizationEventThreatDetectionSettingCustomModuleResult',
    'AwaitableGetOrganizationEventThreatDetectionSettingCustomModuleResult',
    'get_organization_event_threat_detection_setting_custom_module',
    'get_organization_event_threat_detection_setting_custom_module_output',
]

@pulumi.output_type
class GetOrganizationEventThreatDetectionSettingCustomModuleResult:
    def __init__(__self__, config=None, description=None, display_name=None, enablement_state=None, last_editor=None, name=None, type=None, update_time=None):
        if config and not isinstance(config, dict):
            raise TypeError("Expected argument 'config' to be a dict")
        pulumi.set(__self__, "config", config)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if enablement_state and not isinstance(enablement_state, str):
            raise TypeError("Expected argument 'enablement_state' to be a str")
        pulumi.set(__self__, "enablement_state", enablement_state)
        if last_editor and not isinstance(last_editor, str):
            raise TypeError("Expected argument 'last_editor' to be a str")
        pulumi.set(__self__, "last_editor", last_editor)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def config(self) -> Mapping[str, str]:
        """
        Config for the module. For the resident module, its config value is defined at this level. For the inherited module, its config value is inherited from the ancestor module.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description for the module.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The human readable name to be displayed for the module.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enablementState")
    def enablement_state(self) -> str:
        """
        The state of enablement for the module at the given level of the hierarchy.
        """
        return pulumi.get(self, "enablement_state")

    @property
    @pulumi.getter(name="lastEditor")
    def last_editor(self) -> str:
        """
        The editor the module was last updated by.
        """
        return pulumi.get(self, "last_editor")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Immutable. The resource name of the Event Threat Detection custom module. Its format is: * "organizations/{organization}/eventThreatDetectionSettings/customModules/{module}". * "folders/{folder}/eventThreatDetectionSettings/customModules/{module}". * "projects/{project}/eventThreatDetectionSettings/customModules/{module}".
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type for the module. e.g. CONFIGURABLE_BAD_IP.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time the module was last updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetOrganizationEventThreatDetectionSettingCustomModuleResult(GetOrganizationEventThreatDetectionSettingCustomModuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationEventThreatDetectionSettingCustomModuleResult(
            config=self.config,
            description=self.description,
            display_name=self.display_name,
            enablement_state=self.enablement_state,
            last_editor=self.last_editor,
            name=self.name,
            type=self.type,
            update_time=self.update_time)


def get_organization_event_threat_detection_setting_custom_module(custom_module_id: Optional[str] = None,
                                                                  organization_id: Optional[str] = None,
                                                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationEventThreatDetectionSettingCustomModuleResult:
    """
    Gets an Event Threat Detection custom module.
    """
    __args__ = dict()
    __args__['customModuleId'] = custom_module_id
    __args__['organizationId'] = organization_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:securitycenter/v1:getOrganizationEventThreatDetectionSettingCustomModule', __args__, opts=opts, typ=GetOrganizationEventThreatDetectionSettingCustomModuleResult).value

    return AwaitableGetOrganizationEventThreatDetectionSettingCustomModuleResult(
        config=pulumi.get(__ret__, 'config'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        enablement_state=pulumi.get(__ret__, 'enablement_state'),
        last_editor=pulumi.get(__ret__, 'last_editor'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'),
        update_time=pulumi.get(__ret__, 'update_time'))


@_utilities.lift_output_func(get_organization_event_threat_detection_setting_custom_module)
def get_organization_event_threat_detection_setting_custom_module_output(custom_module_id: Optional[pulumi.Input[str]] = None,
                                                                         organization_id: Optional[pulumi.Input[str]] = None,
                                                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrganizationEventThreatDetectionSettingCustomModuleResult]:
    """
    Gets an Event Threat Detection custom module.
    """
    ...
