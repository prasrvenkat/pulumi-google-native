// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1
{
    public static class GetHyperparameterTuningJob
    {
        /// <summary>
        /// Gets a HyperparameterTuningJob
        /// </summary>
        public static Task<GetHyperparameterTuningJobResult> InvokeAsync(GetHyperparameterTuningJobArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetHyperparameterTuningJobResult>("google-native:aiplatform/v1:getHyperparameterTuningJob", args ?? new GetHyperparameterTuningJobArgs(), options.WithDefaults());

        /// <summary>
        /// Gets a HyperparameterTuningJob
        /// </summary>
        public static Output<GetHyperparameterTuningJobResult> Invoke(GetHyperparameterTuningJobInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetHyperparameterTuningJobResult>("google-native:aiplatform/v1:getHyperparameterTuningJob", args ?? new GetHyperparameterTuningJobInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetHyperparameterTuningJobArgs : global::Pulumi.InvokeArgs
    {
        [Input("hyperparameterTuningJobId", required: true)]
        public string HyperparameterTuningJobId { get; set; } = null!;

        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        public GetHyperparameterTuningJobArgs()
        {
        }
        public static new GetHyperparameterTuningJobArgs Empty => new GetHyperparameterTuningJobArgs();
    }

    public sealed class GetHyperparameterTuningJobInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("hyperparameterTuningJobId", required: true)]
        public Input<string> HyperparameterTuningJobId { get; set; } = null!;

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        public GetHyperparameterTuningJobInvokeArgs()
        {
        }
        public static new GetHyperparameterTuningJobInvokeArgs Empty => new GetHyperparameterTuningJobInvokeArgs();
    }


    [OutputType]
    public sealed class GetHyperparameterTuningJobResult
    {
        /// <summary>
        /// Time when the HyperparameterTuningJob was created.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// The display name of the HyperparameterTuningJob. The name can be up to 128 characters long and can consist of any UTF-8 characters.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// Customer-managed encryption key options for a HyperparameterTuningJob. If this is set, then all resources created by the HyperparameterTuningJob will be encrypted with the provided encryption key.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1EncryptionSpecResponse EncryptionSpec;
        /// <summary>
        /// Time when the HyperparameterTuningJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`.
        /// </summary>
        public readonly string EndTime;
        /// <summary>
        /// Only populated when job's state is JOB_STATE_FAILED or JOB_STATE_CANCELLED.
        /// </summary>
        public readonly Outputs.GoogleRpcStatusResponse Error;
        /// <summary>
        /// The labels with user-defined metadata to organize HyperparameterTuningJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Labels;
        /// <summary>
        /// The number of failed Trials that need to be seen before failing the HyperparameterTuningJob. If set to 0, Vertex AI decides how many Trials must fail before the whole job fails.
        /// </summary>
        public readonly int MaxFailedTrialCount;
        /// <summary>
        /// The desired total number of Trials.
        /// </summary>
        public readonly int MaxTrialCount;
        /// <summary>
        /// Resource name of the HyperparameterTuningJob.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The desired number of Trials to run in parallel.
        /// </summary>
        public readonly int ParallelTrialCount;
        /// <summary>
        /// Time when the HyperparameterTuningJob for the first time entered the `JOB_STATE_RUNNING` state.
        /// </summary>
        public readonly string StartTime;
        /// <summary>
        /// The detailed state of the job.
        /// </summary>
        public readonly string State;
        /// <summary>
        /// Study configuration of the HyperparameterTuningJob.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1StudySpecResponse StudySpec;
        /// <summary>
        /// The spec of a trial job. The same spec applies to the CustomJobs created in all the trials.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1CustomJobSpecResponse TrialJobSpec;
        /// <summary>
        /// Trials of the HyperparameterTuningJob.
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleCloudAiplatformV1TrialResponse> Trials;
        /// <summary>
        /// Time when the HyperparameterTuningJob was most recently updated.
        /// </summary>
        public readonly string UpdateTime;

        [OutputConstructor]
        private GetHyperparameterTuningJobResult(
            string createTime,

            string displayName,

            Outputs.GoogleCloudAiplatformV1EncryptionSpecResponse encryptionSpec,

            string endTime,

            Outputs.GoogleRpcStatusResponse error,

            ImmutableDictionary<string, string> labels,

            int maxFailedTrialCount,

            int maxTrialCount,

            string name,

            int parallelTrialCount,

            string startTime,

            string state,

            Outputs.GoogleCloudAiplatformV1StudySpecResponse studySpec,

            Outputs.GoogleCloudAiplatformV1CustomJobSpecResponse trialJobSpec,

            ImmutableArray<Outputs.GoogleCloudAiplatformV1TrialResponse> trials,

            string updateTime)
        {
            CreateTime = createTime;
            DisplayName = displayName;
            EncryptionSpec = encryptionSpec;
            EndTime = endTime;
            Error = error;
            Labels = labels;
            MaxFailedTrialCount = maxFailedTrialCount;
            MaxTrialCount = maxTrialCount;
            Name = name;
            ParallelTrialCount = parallelTrialCount;
            StartTime = startTime;
            State = state;
            StudySpec = studySpec;
            TrialJobSpec = trialJobSpec;
            Trials = trials;
            UpdateTime = updateTime;
        }
    }
}