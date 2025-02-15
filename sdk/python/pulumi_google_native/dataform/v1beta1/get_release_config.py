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
    'GetReleaseConfigResult',
    'AwaitableGetReleaseConfigResult',
    'get_release_config',
    'get_release_config_output',
]

@pulumi.output_type
class GetReleaseConfigResult:
    def __init__(__self__, code_compilation_config=None, cron_schedule=None, git_commitish=None, name=None, recent_scheduled_release_records=None, release_compilation_result=None, time_zone=None):
        if code_compilation_config and not isinstance(code_compilation_config, dict):
            raise TypeError("Expected argument 'code_compilation_config' to be a dict")
        pulumi.set(__self__, "code_compilation_config", code_compilation_config)
        if cron_schedule and not isinstance(cron_schedule, str):
            raise TypeError("Expected argument 'cron_schedule' to be a str")
        pulumi.set(__self__, "cron_schedule", cron_schedule)
        if git_commitish and not isinstance(git_commitish, str):
            raise TypeError("Expected argument 'git_commitish' to be a str")
        pulumi.set(__self__, "git_commitish", git_commitish)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if recent_scheduled_release_records and not isinstance(recent_scheduled_release_records, list):
            raise TypeError("Expected argument 'recent_scheduled_release_records' to be a list")
        pulumi.set(__self__, "recent_scheduled_release_records", recent_scheduled_release_records)
        if release_compilation_result and not isinstance(release_compilation_result, str):
            raise TypeError("Expected argument 'release_compilation_result' to be a str")
        pulumi.set(__self__, "release_compilation_result", release_compilation_result)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="codeCompilationConfig")
    def code_compilation_config(self) -> 'outputs.CodeCompilationConfigResponse':
        """
        Optional. If set, fields of `code_compilation_config` override the default compilation settings that are specified in dataform.json.
        """
        return pulumi.get(self, "code_compilation_config")

    @property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> str:
        """
        Optional. Optional schedule (in cron format) for automatic creation of compilation results.
        """
        return pulumi.get(self, "cron_schedule")

    @property
    @pulumi.getter(name="gitCommitish")
    def git_commitish(self) -> str:
        """
        Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: `12ade345` - a tag: `tag1` - a branch name: `branch1`
        """
        return pulumi.get(self, "git_commitish")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The release config's name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recentScheduledReleaseRecords")
    def recent_scheduled_release_records(self) -> Sequence['outputs.ScheduledReleaseRecordResponse']:
        """
        Records of the 10 most recent scheduled release attempts, ordered in in descending order of `release_time`. Updated whenever automatic creation of a compilation result is triggered by cron_schedule.
        """
        return pulumi.get(self, "recent_scheduled_release_records")

    @property
    @pulumi.getter(name="releaseCompilationResult")
    def release_compilation_result(self) -> str:
        """
        Optional. The name of the currently released compilation result for this release config. This value is updated when a compilation result is created from this release config, or when this resource is updated by API call (perhaps to roll back to an earlier release). The compilation result must have been created using this release config. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.
        """
        return pulumi.get(self, "release_compilation_result")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC.
        """
        return pulumi.get(self, "time_zone")


class AwaitableGetReleaseConfigResult(GetReleaseConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReleaseConfigResult(
            code_compilation_config=self.code_compilation_config,
            cron_schedule=self.cron_schedule,
            git_commitish=self.git_commitish,
            name=self.name,
            recent_scheduled_release_records=self.recent_scheduled_release_records,
            release_compilation_result=self.release_compilation_result,
            time_zone=self.time_zone)


def get_release_config(location: Optional[str] = None,
                       project: Optional[str] = None,
                       release_config_id: Optional[str] = None,
                       repository_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReleaseConfigResult:
    """
    Fetches a single ReleaseConfig.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['releaseConfigId'] = release_config_id
    __args__['repositoryId'] = repository_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:dataform/v1beta1:getReleaseConfig', __args__, opts=opts, typ=GetReleaseConfigResult).value

    return AwaitableGetReleaseConfigResult(
        code_compilation_config=pulumi.get(__ret__, 'code_compilation_config'),
        cron_schedule=pulumi.get(__ret__, 'cron_schedule'),
        git_commitish=pulumi.get(__ret__, 'git_commitish'),
        name=pulumi.get(__ret__, 'name'),
        recent_scheduled_release_records=pulumi.get(__ret__, 'recent_scheduled_release_records'),
        release_compilation_result=pulumi.get(__ret__, 'release_compilation_result'),
        time_zone=pulumi.get(__ret__, 'time_zone'))


@_utilities.lift_output_func(get_release_config)
def get_release_config_output(location: Optional[pulumi.Input[str]] = None,
                              project: Optional[pulumi.Input[Optional[str]]] = None,
                              release_config_id: Optional[pulumi.Input[str]] = None,
                              repository_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReleaseConfigResult]:
    """
    Fetches a single ReleaseConfig.
    """
    ...
