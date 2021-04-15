# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'AuthenticationResponse',
    'CustomAccountResponse',
    'GoogleAccountResponse',
    'ScanRunResponse',
    'ScheduleResponse',
]

@pulumi.output_type
class AuthenticationResponse(dict):
    """
    Scan authentication configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "customAccount":
            suggest = "custom_account"
        elif key == "googleAccount":
            suggest = "google_account"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AuthenticationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AuthenticationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AuthenticationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 custom_account: 'outputs.CustomAccountResponse',
                 google_account: 'outputs.GoogleAccountResponse'):
        """
        Scan authentication configuration.
        :param 'CustomAccountResponseArgs' custom_account: Authentication using a custom account.
        :param 'GoogleAccountResponseArgs' google_account: Authentication using a Google account.
        """
        pulumi.set(__self__, "custom_account", custom_account)
        pulumi.set(__self__, "google_account", google_account)

    @property
    @pulumi.getter(name="customAccount")
    def custom_account(self) -> 'outputs.CustomAccountResponse':
        """
        Authentication using a custom account.
        """
        return pulumi.get(self, "custom_account")

    @property
    @pulumi.getter(name="googleAccount")
    def google_account(self) -> 'outputs.GoogleAccountResponse':
        """
        Authentication using a Google account.
        """
        return pulumi.get(self, "google_account")


@pulumi.output_type
class CustomAccountResponse(dict):
    """
    Describes authentication configuration that uses a custom account.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "loginUrl":
            suggest = "login_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomAccountResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomAccountResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomAccountResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 login_url: str,
                 password: str,
                 username: str):
        """
        Describes authentication configuration that uses a custom account.
        :param str login_url: Required. The login form URL of the website.
        :param str password: Required. Input only. The password of the custom account. The credential is stored encrypted and not returned in any response nor included in audit logs.
        :param str username: Required. The user name of the custom account.
        """
        pulumi.set(__self__, "login_url", login_url)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="loginUrl")
    def login_url(self) -> str:
        """
        Required. The login form URL of the website.
        """
        return pulumi.get(self, "login_url")

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        Required. Input only. The password of the custom account. The credential is stored encrypted and not returned in any response nor included in audit logs.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        Required. The user name of the custom account.
        """
        return pulumi.get(self, "username")


@pulumi.output_type
class GoogleAccountResponse(dict):
    """
    Describes authentication configuration that uses a Google account.
    """
    def __init__(__self__, *,
                 password: str,
                 username: str):
        """
        Describes authentication configuration that uses a Google account.
        :param str password: Required. Input only. The password of the Google account. The credential is stored encrypted and not returned in any response nor included in audit logs.
        :param str username: Required. The user name of the Google account.
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        Required. Input only. The password of the Google account. The credential is stored encrypted and not returned in any response nor included in audit logs.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        Required. The user name of the Google account.
        """
        return pulumi.get(self, "username")


@pulumi.output_type
class ScanRunResponse(dict):
    """
    A ScanRun is a output-only resource representing an actual run of the scan.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endTime":
            suggest = "end_time"
        elif key == "executionState":
            suggest = "execution_state"
        elif key == "hasVulnerabilities":
            suggest = "has_vulnerabilities"
        elif key == "progressPercent":
            suggest = "progress_percent"
        elif key == "resultState":
            suggest = "result_state"
        elif key == "startTime":
            suggest = "start_time"
        elif key == "urlsCrawledCount":
            suggest = "urls_crawled_count"
        elif key == "urlsTestedCount":
            suggest = "urls_tested_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScanRunResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScanRunResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScanRunResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 end_time: str,
                 execution_state: str,
                 has_vulnerabilities: bool,
                 name: str,
                 progress_percent: int,
                 result_state: str,
                 start_time: str,
                 urls_crawled_count: str,
                 urls_tested_count: str):
        """
        A ScanRun is a output-only resource representing an actual run of the scan.
        :param str end_time: The time at which the ScanRun reached termination state - that the ScanRun is either finished or stopped by user.
        :param str execution_state: The execution state of the ScanRun.
        :param bool has_vulnerabilities: Whether the scan run has found any vulnerabilities.
        :param str name: The resource name of the ScanRun. The name follows the format of 'projects/{projectId}/scanConfigs/{scanConfigId}/scanRuns/{scanRunId}'. The ScanRun IDs are generated by the system.
        :param int progress_percent: The percentage of total completion ranging from 0 to 100. If the scan is in queue, the value is 0. If the scan is running, the value ranges from 0 to 100. If the scan is finished, the value is 100.
        :param str result_state: The result state of the ScanRun. This field is only available after the execution state reaches "FINISHED".
        :param str start_time: The time at which the ScanRun started.
        :param str urls_crawled_count: The number of URLs crawled during this ScanRun. If the scan is in progress, the value represents the number of URLs crawled up to now.
        :param str urls_tested_count: The number of URLs tested during this ScanRun. If the scan is in progress, the value represents the number of URLs tested up to now. The number of URLs tested is usually larger than the number URLS crawled because typically a crawled URL is tested with multiple test payloads.
        """
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "execution_state", execution_state)
        pulumi.set(__self__, "has_vulnerabilities", has_vulnerabilities)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "progress_percent", progress_percent)
        pulumi.set(__self__, "result_state", result_state)
        pulumi.set(__self__, "start_time", start_time)
        pulumi.set(__self__, "urls_crawled_count", urls_crawled_count)
        pulumi.set(__self__, "urls_tested_count", urls_tested_count)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        The time at which the ScanRun reached termination state - that the ScanRun is either finished or stopped by user.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="executionState")
    def execution_state(self) -> str:
        """
        The execution state of the ScanRun.
        """
        return pulumi.get(self, "execution_state")

    @property
    @pulumi.getter(name="hasVulnerabilities")
    def has_vulnerabilities(self) -> bool:
        """
        Whether the scan run has found any vulnerabilities.
        """
        return pulumi.get(self, "has_vulnerabilities")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the ScanRun. The name follows the format of 'projects/{projectId}/scanConfigs/{scanConfigId}/scanRuns/{scanRunId}'. The ScanRun IDs are generated by the system.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="progressPercent")
    def progress_percent(self) -> int:
        """
        The percentage of total completion ranging from 0 to 100. If the scan is in queue, the value is 0. If the scan is running, the value ranges from 0 to 100. If the scan is finished, the value is 100.
        """
        return pulumi.get(self, "progress_percent")

    @property
    @pulumi.getter(name="resultState")
    def result_state(self) -> str:
        """
        The result state of the ScanRun. This field is only available after the execution state reaches "FINISHED".
        """
        return pulumi.get(self, "result_state")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        The time at which the ScanRun started.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter(name="urlsCrawledCount")
    def urls_crawled_count(self) -> str:
        """
        The number of URLs crawled during this ScanRun. If the scan is in progress, the value represents the number of URLs crawled up to now.
        """
        return pulumi.get(self, "urls_crawled_count")

    @property
    @pulumi.getter(name="urlsTestedCount")
    def urls_tested_count(self) -> str:
        """
        The number of URLs tested during this ScanRun. If the scan is in progress, the value represents the number of URLs tested up to now. The number of URLs tested is usually larger than the number URLS crawled because typically a crawled URL is tested with multiple test payloads.
        """
        return pulumi.get(self, "urls_tested_count")


@pulumi.output_type
class ScheduleResponse(dict):
    """
    Scan schedule configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "intervalDurationDays":
            suggest = "interval_duration_days"
        elif key == "scheduleTime":
            suggest = "schedule_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 interval_duration_days: int,
                 schedule_time: str):
        """
        Scan schedule configuration.
        :param int interval_duration_days: Required. The duration of time between executions in days.
        :param str schedule_time: A timestamp indicates when the next run will be scheduled. The value is refreshed by the server after each run. If unspecified, it will default to current server time, which means the scan will be scheduled to start immediately.
        """
        pulumi.set(__self__, "interval_duration_days", interval_duration_days)
        pulumi.set(__self__, "schedule_time", schedule_time)

    @property
    @pulumi.getter(name="intervalDurationDays")
    def interval_duration_days(self) -> int:
        """
        Required. The duration of time between executions in days.
        """
        return pulumi.get(self, "interval_duration_days")

    @property
    @pulumi.getter(name="scheduleTime")
    def schedule_time(self) -> str:
        """
        A timestamp indicates when the next run will be scheduled. The value is refreshed by the server after each run. If unspecified, it will default to current server time, which means the scan will be scheduled to start immediately.
        """
        return pulumi.get(self, "schedule_time")

