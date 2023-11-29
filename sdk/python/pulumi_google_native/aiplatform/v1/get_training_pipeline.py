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
    'GetTrainingPipelineResult',
    'AwaitableGetTrainingPipelineResult',
    'get_training_pipeline',
    'get_training_pipeline_output',
]

@pulumi.output_type
class GetTrainingPipelineResult:
    def __init__(__self__, create_time=None, display_name=None, encryption_spec=None, end_time=None, error=None, input_data_config=None, labels=None, model_id=None, model_to_upload=None, name=None, parent_model=None, start_time=None, state=None, training_task_definition=None, training_task_inputs=None, training_task_metadata=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if encryption_spec and not isinstance(encryption_spec, dict):
            raise TypeError("Expected argument 'encryption_spec' to be a dict")
        pulumi.set(__self__, "encryption_spec", encryption_spec)
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if input_data_config and not isinstance(input_data_config, dict):
            raise TypeError("Expected argument 'input_data_config' to be a dict")
        pulumi.set(__self__, "input_data_config", input_data_config)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if model_id and not isinstance(model_id, str):
            raise TypeError("Expected argument 'model_id' to be a str")
        pulumi.set(__self__, "model_id", model_id)
        if model_to_upload and not isinstance(model_to_upload, dict):
            raise TypeError("Expected argument 'model_to_upload' to be a dict")
        pulumi.set(__self__, "model_to_upload", model_to_upload)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parent_model and not isinstance(parent_model, str):
            raise TypeError("Expected argument 'parent_model' to be a str")
        pulumi.set(__self__, "parent_model", parent_model)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if training_task_definition and not isinstance(training_task_definition, str):
            raise TypeError("Expected argument 'training_task_definition' to be a str")
        pulumi.set(__self__, "training_task_definition", training_task_definition)
        if training_task_inputs and not isinstance(training_task_inputs, dict):
            raise TypeError("Expected argument 'training_task_inputs' to be a dict")
        pulumi.set(__self__, "training_task_inputs", training_task_inputs)
        if training_task_metadata and not isinstance(training_task_metadata, dict):
            raise TypeError("Expected argument 'training_task_metadata' to be a dict")
        pulumi.set(__self__, "training_task_metadata", training_task_metadata)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Time when the TrainingPipeline was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The user-defined name of this TrainingPipeline.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> 'outputs.GoogleCloudAiplatformV1EncryptionSpecResponse':
        """
        Customer-managed encryption key spec for a TrainingPipeline. If set, this TrainingPipeline will be secured by this key. Note: Model trained by this TrainingPipeline is also secured by this key if model_to_upload is not set separately.
        """
        return pulumi.get(self, "encryption_spec")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        Time when the TrainingPipeline entered any of the following states: `PIPELINE_STATE_SUCCEEDED`, `PIPELINE_STATE_FAILED`, `PIPELINE_STATE_CANCELLED`.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def error(self) -> 'outputs.GoogleRpcStatusResponse':
        """
        Only populated when the pipeline's state is `PIPELINE_STATE_FAILED` or `PIPELINE_STATE_CANCELLED`.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter(name="inputDataConfig")
    def input_data_config(self) -> 'outputs.GoogleCloudAiplatformV1InputDataConfigResponse':
        """
        Specifies Vertex AI owned input data that may be used for training the Model. The TrainingPipeline's training_task_definition should make clear whether this config is used and if there are any special requirements on how it should be filled. If nothing about this config is mentioned in the training_task_definition, then it should be assumed that the TrainingPipeline does not depend on this configuration.
        """
        return pulumi.get(self, "input_data_config")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        The labels with user-defined metadata to organize TrainingPipelines. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="modelId")
    def model_id(self) -> str:
        """
        Optional. The ID to use for the uploaded Model, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.
        """
        return pulumi.get(self, "model_id")

    @property
    @pulumi.getter(name="modelToUpload")
    def model_to_upload(self) -> 'outputs.GoogleCloudAiplatformV1ModelResponse':
        """
        Describes the Model that may be uploaded (via ModelService.UploadModel) by this TrainingPipeline. The TrainingPipeline's training_task_definition should make clear whether this Model description should be populated, and if there are any special requirements regarding how it should be filled. If nothing is mentioned in the training_task_definition, then it should be assumed that this field should not be filled and the training task either uploads the Model without a need of this information, or that training task does not support uploading a Model as part of the pipeline. When the Pipeline's state becomes `PIPELINE_STATE_SUCCEEDED` and the trained Model had been uploaded into Vertex AI, then the model_to_upload's resource name is populated. The Model is always uploaded into the Project and Location in which this pipeline is.
        """
        return pulumi.get(self, "model_to_upload")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name of the TrainingPipeline.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentModel")
    def parent_model(self) -> str:
        """
        Optional. When specify this field, the `model_to_upload` will not be uploaded as a new model, instead, it will become a new version of this `parent_model`.
        """
        return pulumi.get(self, "parent_model")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        Time when the TrainingPipeline for the first time entered the `PIPELINE_STATE_RUNNING` state.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The detailed state of the pipeline.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="trainingTaskDefinition")
    def training_task_definition(self) -> str:
        """
        A Google Cloud Storage path to the YAML file that defines the training task which is responsible for producing the model artifact, and may also include additional auxiliary work. The definition files that can be used here are found in gs://google-cloud-aiplatform/schema/trainingjob/definition/. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.
        """
        return pulumi.get(self, "training_task_definition")

    @property
    @pulumi.getter(name="trainingTaskInputs")
    def training_task_inputs(self) -> Any:
        """
        The training task's parameter(s), as specified in the training_task_definition's `inputs`.
        """
        return pulumi.get(self, "training_task_inputs")

    @property
    @pulumi.getter(name="trainingTaskMetadata")
    def training_task_metadata(self) -> Any:
        """
        The metadata information as specified in the training_task_definition's `metadata`. This metadata is an auxiliary runtime and final information about the training task. While the pipeline is running this information is populated only at a best effort basis. Only present if the pipeline's training_task_definition contains `metadata` object.
        """
        return pulumi.get(self, "training_task_metadata")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Time when the TrainingPipeline was most recently updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetTrainingPipelineResult(GetTrainingPipelineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrainingPipelineResult(
            create_time=self.create_time,
            display_name=self.display_name,
            encryption_spec=self.encryption_spec,
            end_time=self.end_time,
            error=self.error,
            input_data_config=self.input_data_config,
            labels=self.labels,
            model_id=self.model_id,
            model_to_upload=self.model_to_upload,
            name=self.name,
            parent_model=self.parent_model,
            start_time=self.start_time,
            state=self.state,
            training_task_definition=self.training_task_definition,
            training_task_inputs=self.training_task_inputs,
            training_task_metadata=self.training_task_metadata,
            update_time=self.update_time)


def get_training_pipeline(location: Optional[str] = None,
                          project: Optional[str] = None,
                          training_pipeline_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrainingPipelineResult:
    """
    Gets a TrainingPipeline.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['trainingPipelineId'] = training_pipeline_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:aiplatform/v1:getTrainingPipeline', __args__, opts=opts, typ=GetTrainingPipelineResult).value

    return AwaitableGetTrainingPipelineResult(
        create_time=pulumi.get(__ret__, 'create_time'),
        display_name=pulumi.get(__ret__, 'display_name'),
        encryption_spec=pulumi.get(__ret__, 'encryption_spec'),
        end_time=pulumi.get(__ret__, 'end_time'),
        error=pulumi.get(__ret__, 'error'),
        input_data_config=pulumi.get(__ret__, 'input_data_config'),
        labels=pulumi.get(__ret__, 'labels'),
        model_id=pulumi.get(__ret__, 'model_id'),
        model_to_upload=pulumi.get(__ret__, 'model_to_upload'),
        name=pulumi.get(__ret__, 'name'),
        parent_model=pulumi.get(__ret__, 'parent_model'),
        start_time=pulumi.get(__ret__, 'start_time'),
        state=pulumi.get(__ret__, 'state'),
        training_task_definition=pulumi.get(__ret__, 'training_task_definition'),
        training_task_inputs=pulumi.get(__ret__, 'training_task_inputs'),
        training_task_metadata=pulumi.get(__ret__, 'training_task_metadata'),
        update_time=pulumi.get(__ret__, 'update_time'))


@_utilities.lift_output_func(get_training_pipeline)
def get_training_pipeline_output(location: Optional[pulumi.Input[str]] = None,
                                 project: Optional[pulumi.Input[Optional[str]]] = None,
                                 training_pipeline_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTrainingPipelineResult]:
    """
    Gets a TrainingPipeline.
    """
    ...