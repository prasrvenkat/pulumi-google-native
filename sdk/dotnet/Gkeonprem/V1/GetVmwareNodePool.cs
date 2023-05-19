// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Gkeonprem.V1
{
    public static class GetVmwareNodePool
    {
        /// <summary>
        /// Gets details of a single VMware node pool.
        /// </summary>
        public static Task<GetVmwareNodePoolResult> InvokeAsync(GetVmwareNodePoolArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVmwareNodePoolResult>("google-native:gkeonprem/v1:getVmwareNodePool", args ?? new GetVmwareNodePoolArgs(), options.WithDefaults());

        /// <summary>
        /// Gets details of a single VMware node pool.
        /// </summary>
        public static Output<GetVmwareNodePoolResult> Invoke(GetVmwareNodePoolInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVmwareNodePoolResult>("google-native:gkeonprem/v1:getVmwareNodePool", args ?? new GetVmwareNodePoolInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVmwareNodePoolArgs : global::Pulumi.InvokeArgs
    {
        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        [Input("vmwareClusterId", required: true)]
        public string VmwareClusterId { get; set; } = null!;

        [Input("vmwareNodePoolId", required: true)]
        public string VmwareNodePoolId { get; set; } = null!;

        public GetVmwareNodePoolArgs()
        {
        }
        public static new GetVmwareNodePoolArgs Empty => new GetVmwareNodePoolArgs();
    }

    public sealed class GetVmwareNodePoolInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("vmwareClusterId", required: true)]
        public Input<string> VmwareClusterId { get; set; } = null!;

        [Input("vmwareNodePoolId", required: true)]
        public Input<string> VmwareNodePoolId { get; set; } = null!;

        public GetVmwareNodePoolInvokeArgs()
        {
        }
        public static new GetVmwareNodePoolInvokeArgs Empty => new GetVmwareNodePoolInvokeArgs();
    }


    [OutputType]
    public sealed class GetVmwareNodePoolResult
    {
        /// <summary>
        /// Annotations on the node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Annotations;
        /// <summary>
        /// The node configuration of the node pool.
        /// </summary>
        public readonly Outputs.VmwareNodeConfigResponse Config;
        /// <summary>
        /// The time at which this node pool was created.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// The time at which this node pool was deleted. If the resource is not deleted, this must be empty
        /// </summary>
        public readonly string DeleteTime;
        /// <summary>
        /// The display name for the node pool.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control.
        /// </summary>
        public readonly string Etag;
        /// <summary>
        /// Immutable. The resource name of this node pool.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Node pool autoscaling config for the node pool.
        /// </summary>
        public readonly Outputs.VmwareNodePoolAutoscalingConfigResponse NodePoolAutoscaling;
        /// <summary>
        /// Anthos version for the node pool. Defaults to the user cluster version.
        /// </summary>
        public readonly string OnPremVersion;
        /// <summary>
        /// If set, there are currently changes in flight to the node pool.
        /// </summary>
        public readonly bool Reconciling;
        /// <summary>
        /// The current state of the node pool.
        /// </summary>
        public readonly string State;
        /// <summary>
        /// ResourceStatus representing the detailed VMware node pool state.
        /// </summary>
        public readonly Outputs.ResourceStatusResponse Status;
        /// <summary>
        /// The unique identifier of the node pool.
        /// </summary>
        public readonly string Uid;
        /// <summary>
        /// The time at which this node pool was last updated.
        /// </summary>
        public readonly string UpdateTime;

        [OutputConstructor]
        private GetVmwareNodePoolResult(
            ImmutableDictionary<string, string> annotations,

            Outputs.VmwareNodeConfigResponse config,

            string createTime,

            string deleteTime,

            string displayName,

            string etag,

            string name,

            Outputs.VmwareNodePoolAutoscalingConfigResponse nodePoolAutoscaling,

            string onPremVersion,

            bool reconciling,

            string state,

            Outputs.ResourceStatusResponse status,

            string uid,

            string updateTime)
        {
            Annotations = annotations;
            Config = config;
            CreateTime = createTime;
            DeleteTime = deleteTime;
            DisplayName = displayName;
            Etag = etag;
            Name = name;
            NodePoolAutoscaling = nodePoolAutoscaling;
            OnPremVersion = onPremVersion;
            Reconciling = reconciling;
            State = state;
            Status = status;
            Uid = uid;
            UpdateTime = updateTime;
        }
    }
}