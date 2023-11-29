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
    'GetTrialResult',
    'AwaitableGetTrialResult',
    'get_trial',
    'get_trial_output',
]

@pulumi.output_type
class GetTrialResult:
    def __init__(__self__, client_id=None, custom_job=None, end_time=None, final_measurement=None, infeasible_reason=None, measurements=None, name=None, parameters=None, start_time=None, state=None, web_access_uris=None):
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if custom_job and not isinstance(custom_job, str):
            raise TypeError("Expected argument 'custom_job' to be a str")
        pulumi.set(__self__, "custom_job", custom_job)
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if final_measurement and not isinstance(final_measurement, dict):
            raise TypeError("Expected argument 'final_measurement' to be a dict")
        pulumi.set(__self__, "final_measurement", final_measurement)
        if infeasible_reason and not isinstance(infeasible_reason, str):
            raise TypeError("Expected argument 'infeasible_reason' to be a str")
        pulumi.set(__self__, "infeasible_reason", infeasible_reason)
        if measurements and not isinstance(measurements, list):
            raise TypeError("Expected argument 'measurements' to be a list")
        pulumi.set(__self__, "measurements", measurements)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, list):
            raise TypeError("Expected argument 'parameters' to be a list")
        pulumi.set(__self__, "parameters", parameters)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if web_access_uris and not isinstance(web_access_uris, dict):
            raise TypeError("Expected argument 'web_access_uris' to be a dict")
        pulumi.set(__self__, "web_access_uris", web_access_uris)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        The identifier of the client that originally requested this Trial. Each client is identified by a unique client_id. When a client asks for a suggestion, Vertex AI Vizier will assign it a Trial. The client should evaluate the Trial, complete it, and report back to Vertex AI Vizier. If suggestion is asked again by same client_id before the Trial is completed, the same Trial will be returned. Multiple clients with different client_ids can ask for suggestions simultaneously, each of them will get their own Trial.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="customJob")
    def custom_job(self) -> str:
        """
        The CustomJob name linked to the Trial. It's set for a HyperparameterTuningJob's Trial.
        """
        return pulumi.get(self, "custom_job")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        Time when the Trial's status changed to `SUCCEEDED` or `INFEASIBLE`.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="finalMeasurement")
    def final_measurement(self) -> 'outputs.GoogleCloudAiplatformV1beta1MeasurementResponse':
        """
        The final measurement containing the objective value.
        """
        return pulumi.get(self, "final_measurement")

    @property
    @pulumi.getter(name="infeasibleReason")
    def infeasible_reason(self) -> str:
        """
        A human readable string describing why the Trial is infeasible. This is set only if Trial state is `INFEASIBLE`.
        """
        return pulumi.get(self, "infeasible_reason")

    @property
    @pulumi.getter
    def measurements(self) -> Sequence['outputs.GoogleCloudAiplatformV1beta1MeasurementResponse']:
        """
        A list of measurements that are strictly lexicographically ordered by their induced tuples (steps, elapsed_duration). These are used for early stopping computations.
        """
        return pulumi.get(self, "measurements")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name of the Trial assigned by the service.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Sequence['outputs.GoogleCloudAiplatformV1beta1TrialParameterResponse']:
        """
        The parameters of the Trial.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        Time when the Trial was started.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The detailed state of the Trial.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="webAccessUris")
    def web_access_uris(self) -> Mapping[str, str]:
        """
        URIs for accessing [interactive shells](https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell) (one URI for each training node). Only available if this trial is part of a HyperparameterTuningJob and the job's trial_job_spec.enable_web_access field is `true`. The keys are names of each node used for the trial; for example, `workerpool0-0` for the primary node, `workerpool1-0` for the first node in the second worker pool, and `workerpool1-1` for the second node in the second worker pool. The values are the URIs for each node's interactive shell.
        """
        return pulumi.get(self, "web_access_uris")


class AwaitableGetTrialResult(GetTrialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrialResult(
            client_id=self.client_id,
            custom_job=self.custom_job,
            end_time=self.end_time,
            final_measurement=self.final_measurement,
            infeasible_reason=self.infeasible_reason,
            measurements=self.measurements,
            name=self.name,
            parameters=self.parameters,
            start_time=self.start_time,
            state=self.state,
            web_access_uris=self.web_access_uris)


def get_trial(location: Optional[str] = None,
              project: Optional[str] = None,
              study_id: Optional[str] = None,
              trial_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrialResult:
    """
    Gets a Trial.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['studyId'] = study_id
    __args__['trialId'] = trial_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:aiplatform/v1beta1:getTrial', __args__, opts=opts, typ=GetTrialResult).value

    return AwaitableGetTrialResult(
        client_id=pulumi.get(__ret__, 'client_id'),
        custom_job=pulumi.get(__ret__, 'custom_job'),
        end_time=pulumi.get(__ret__, 'end_time'),
        final_measurement=pulumi.get(__ret__, 'final_measurement'),
        infeasible_reason=pulumi.get(__ret__, 'infeasible_reason'),
        measurements=pulumi.get(__ret__, 'measurements'),
        name=pulumi.get(__ret__, 'name'),
        parameters=pulumi.get(__ret__, 'parameters'),
        start_time=pulumi.get(__ret__, 'start_time'),
        state=pulumi.get(__ret__, 'state'),
        web_access_uris=pulumi.get(__ret__, 'web_access_uris'))


@_utilities.lift_output_func(get_trial)
def get_trial_output(location: Optional[pulumi.Input[str]] = None,
                     project: Optional[pulumi.Input[Optional[str]]] = None,
                     study_id: Optional[pulumi.Input[str]] = None,
                     trial_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTrialResult]:
    """
    Gets a Trial.
    """
    ...