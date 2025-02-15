// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.CloudBuild.V1Alpha1
{
    public static class GetWorkerPool
    {
        /// <summary>
        /// Returns information about a `WorkerPool`.
        /// </summary>
        public static Task<GetWorkerPoolResult> InvokeAsync(GetWorkerPoolArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetWorkerPoolResult>("google-native:cloudbuild/v1alpha1:getWorkerPool", args ?? new GetWorkerPoolArgs(), options.WithDefaults());

        /// <summary>
        /// Returns information about a `WorkerPool`.
        /// </summary>
        public static Output<GetWorkerPoolResult> Invoke(GetWorkerPoolInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetWorkerPoolResult>("google-native:cloudbuild/v1alpha1:getWorkerPool", args ?? new GetWorkerPoolInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetWorkerPoolArgs : global::Pulumi.InvokeArgs
    {
        [Input("project")]
        public string? Project { get; set; }

        [Input("workerPoolId", required: true)]
        public string WorkerPoolId { get; set; } = null!;

        public GetWorkerPoolArgs()
        {
        }
        public static new GetWorkerPoolArgs Empty => new GetWorkerPoolArgs();
    }

    public sealed class GetWorkerPoolInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("workerPoolId", required: true)]
        public Input<string> WorkerPoolId { get; set; } = null!;

        public GetWorkerPoolInvokeArgs()
        {
        }
        public static new GetWorkerPoolInvokeArgs Empty => new GetWorkerPoolInvokeArgs();
    }


    [OutputType]
    public sealed class GetWorkerPoolResult
    {
        /// <summary>
        /// Time at which the request to create the `WorkerPool` was received.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Time at which the request to delete the `WorkerPool` was received.
        /// </summary>
        public readonly string DeleteTime;
        /// <summary>
        /// User-defined name of the `WorkerPool`.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The project ID of the GCP project for which the `WorkerPool` is created.
        /// </summary>
        public readonly string Project;
        /// <summary>
        /// List of regions to create the `WorkerPool`. Regions can't be empty. If Cloud Build adds a new GCP region in the future, the existing `WorkerPool` will not be enabled in the new region automatically; you must add the new region to the `regions` field to enable the `WorkerPool` in that region.
        /// </summary>
        public readonly ImmutableArray<string> Regions;
        /// <summary>
        /// The service account used to manage the `WorkerPool`. The service account must have the Compute Instance Admin (Beta) permission at the project level.
        /// </summary>
        public readonly string ServiceAccountEmail;
        /// <summary>
        /// WorkerPool Status.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// Time at which the request to update the `WorkerPool` was received.
        /// </summary>
        public readonly string UpdateTime;
        /// <summary>
        /// Configuration to be used for a creating workers in the `WorkerPool`.
        /// </summary>
        public readonly Outputs.WorkerConfigResponse WorkerConfig;
        /// <summary>
        /// Total number of workers to be created across all requested regions.
        /// </summary>
        public readonly string WorkerCount;

        [OutputConstructor]
        private GetWorkerPoolResult(
            string createTime,

            string deleteTime,

            string name,

            string project,

            ImmutableArray<string> regions,

            string serviceAccountEmail,

            string status,

            string updateTime,

            Outputs.WorkerConfigResponse workerConfig,

            string workerCount)
        {
            CreateTime = createTime;
            DeleteTime = deleteTime;
            Name = name;
            Project = project;
            Regions = regions;
            ServiceAccountEmail = serviceAccountEmail;
            Status = status;
            UpdateTime = updateTime;
            WorkerConfig = workerConfig;
            WorkerCount = workerCount;
        }
    }
}
