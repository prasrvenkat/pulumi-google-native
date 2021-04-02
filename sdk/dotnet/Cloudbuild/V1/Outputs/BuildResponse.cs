// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Cloudbuild.V1.Outputs
{

    [OutputType]
    public sealed class BuildResponse
    {
        /// <summary>
        /// Artifacts produced by the build that should be uploaded upon successful completion of all build steps.
        /// </summary>
        public readonly Outputs.ArtifactsResponse Artifacts;
        /// <summary>
        /// Secrets and secret environment variables.
        /// </summary>
        public readonly Outputs.SecretsResponse AvailableSecrets;
        /// <summary>
        /// The ID of the `BuildTrigger` that triggered this build, if it was triggered automatically.
        /// </summary>
        public readonly string BuildTriggerId;
        /// <summary>
        /// Time at which the request to create the build was received.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Time at which execution of the build was finished. The difference between finish_time and start_time is the duration of the build's execution.
        /// </summary>
        public readonly string FinishTime;
        /// <summary>
        /// A list of images to be pushed upon the successful completion of all build steps. The images are pushed using the builder service account's credentials. The digests of the pushed images will be stored in the `Build` resource's results field. If any of the images fail to be pushed, the build status is marked `FAILURE`.
        /// </summary>
        public readonly ImmutableArray<string> Images;
        /// <summary>
        /// URL to logs for this build in Google Cloud Console.
        /// </summary>
        public readonly string LogUrl;
        /// <summary>
        /// Google Cloud Storage bucket where logs should be written (see [Bucket Name Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)). Logs file names will be of the format `${logs_bucket}/log-${build_id}.txt`.
        /// </summary>
        public readonly string LogsBucket;
        /// <summary>
        /// The 'Build' name with format: `projects/{project}/locations/{location}/builds/{build}`, where {build} is a unique identifier generated by the service.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Special options for this build.
        /// </summary>
        public readonly Outputs.BuildOptionsResponse Options;
        /// <summary>
        /// ID of the project.
        /// </summary>
        public readonly string ProjectId;
        /// <summary>
        /// TTL in queue for this build. If provided and the build is enqueued longer than this value, the build will expire and the build status will be `EXPIRED`. The TTL starts ticking from create_time.
        /// </summary>
        public readonly string QueueTtl;
        /// <summary>
        /// Results of the build.
        /// </summary>
        public readonly Outputs.ResultsResponse Results;
        /// <summary>
        /// Secrets to decrypt using Cloud Key Management Service. Note: Secret Manager is the recommended technique for managing sensitive data with Cloud Build. Use `available_secrets` to configure builds to access secrets from Secret Manager. For instructions, see: https://cloud.google.com/cloud-build/docs/securing-builds/use-secrets
        /// </summary>
        public readonly ImmutableArray<Outputs.SecretResponse> Secrets;
        /// <summary>
        /// IAM service account whose credentials will be used at build runtime. Must be of the format `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`. ACCOUNT can be email address or uniqueId of the service account. This field is in beta.
        /// </summary>
        public readonly string ServiceAccount;
        /// <summary>
        /// The location of the source files to build.
        /// </summary>
        public readonly Outputs.SourceResponse Source;
        /// <summary>
        /// A permanent fixed identifier for source.
        /// </summary>
        public readonly Outputs.SourceProvenanceResponse SourceProvenance;
        /// <summary>
        /// Time at which execution of the build was started.
        /// </summary>
        public readonly string StartTime;
        /// <summary>
        /// Status of the build.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// Customer-readable message about the current status.
        /// </summary>
        public readonly string StatusDetail;
        /// <summary>
        /// Required. The operations to be performed on the workspace.
        /// </summary>
        public readonly ImmutableArray<Outputs.BuildStepResponse> Steps;
        /// <summary>
        /// Substitutions data for `Build` resource.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Substitutions;
        /// <summary>
        /// Tags for annotation of a `Build`. These are not docker tags.
        /// </summary>
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// Amount of time that this build should be allowed to run, to second granularity. If this amount of time elapses, work on the build will cease and the build status will be `TIMEOUT`. `timeout` starts ticking from `startTime`. Default time is ten minutes.
        /// </summary>
        public readonly string Timeout;
        /// <summary>
        /// Stores timing information for phases of the build. Valid keys are: * BUILD: time to execute all build steps * PUSH: time to push all specified images. * FETCHSOURCE: time to fetch source. If the build does not specify source or images, these keys will not be included.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Timing;

        [OutputConstructor]
        private BuildResponse(
            Outputs.ArtifactsResponse artifacts,

            Outputs.SecretsResponse availableSecrets,

            string buildTriggerId,

            string createTime,

            string finishTime,

            ImmutableArray<string> images,

            string logUrl,

            string logsBucket,

            string name,

            Outputs.BuildOptionsResponse options,

            string projectId,

            string queueTtl,

            Outputs.ResultsResponse results,

            ImmutableArray<Outputs.SecretResponse> secrets,

            string serviceAccount,

            Outputs.SourceResponse source,

            Outputs.SourceProvenanceResponse sourceProvenance,

            string startTime,

            string status,

            string statusDetail,

            ImmutableArray<Outputs.BuildStepResponse> steps,

            ImmutableDictionary<string, string> substitutions,

            ImmutableArray<string> tags,

            string timeout,

            ImmutableDictionary<string, string> timing)
        {
            Artifacts = artifacts;
            AvailableSecrets = availableSecrets;
            BuildTriggerId = buildTriggerId;
            CreateTime = createTime;
            FinishTime = finishTime;
            Images = images;
            LogUrl = logUrl;
            LogsBucket = logsBucket;
            Name = name;
            Options = options;
            ProjectId = projectId;
            QueueTtl = queueTtl;
            Results = results;
            Secrets = secrets;
            ServiceAccount = serviceAccount;
            Source = source;
            SourceProvenance = sourceProvenance;
            StartTime = startTime;
            Status = status;
            StatusDetail = statusDetail;
            Steps = steps;
            Substitutions = substitutions;
            Tags = tags;
            Timeout = timeout;
            Timing = timing;
        }
    }
}