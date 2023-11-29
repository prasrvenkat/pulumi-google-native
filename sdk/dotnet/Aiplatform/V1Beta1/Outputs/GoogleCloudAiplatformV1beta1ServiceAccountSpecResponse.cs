// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1Beta1.Outputs
{

    /// <summary>
    /// Configuration for the use of custom service account to run the workloads.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1beta1ServiceAccountSpecResponse
    {
        /// <summary>
        /// If true, custom user-managed service account is enforced to run any workloads (for example, Vertex Jobs) on the resource. Otherwise, uses the [Vertex AI Custom Code Service Agent](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents).
        /// </summary>
        public readonly bool EnableCustomServiceAccount;
        /// <summary>
        /// Optional. Default service account that this PersistentResource's workloads run as. The workloads include: * Any runtime specified via `ResourceRuntimeSpec` on creation time, for example, Ray. * Jobs submitted to PersistentResource, if no other service account specified in the job specs. Only works when custom service account is enabled and users have the `iam.serviceAccounts.actAs` permission on this service account. Required if any containers are specified in `ResourceRuntimeSpec`.
        /// </summary>
        public readonly string ServiceAccount;

        [OutputConstructor]
        private GoogleCloudAiplatformV1beta1ServiceAccountSpecResponse(
            bool enableCustomServiceAccount,

            string serviceAccount)
        {
            EnableCustomServiceAccount = enableCustomServiceAccount;
            ServiceAccount = serviceAccount;
        }
    }
}