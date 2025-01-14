// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AccessContextManager.V1Beta
{
    public static class GetAccessPolicy
    {
        /// <summary>
        /// Get an AccessPolicy by name.
        /// </summary>
        public static Task<GetAccessPolicyResult> InvokeAsync(GetAccessPolicyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAccessPolicyResult>("google-native:accesscontextmanager/v1beta:getAccessPolicy", args ?? new GetAccessPolicyArgs(), options.WithDefaults());

        /// <summary>
        /// Get an AccessPolicy by name.
        /// </summary>
        public static Output<GetAccessPolicyResult> Invoke(GetAccessPolicyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAccessPolicyResult>("google-native:accesscontextmanager/v1beta:getAccessPolicy", args ?? new GetAccessPolicyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAccessPolicyArgs : global::Pulumi.InvokeArgs
    {
        [Input("accessPolicyId", required: true)]
        public string AccessPolicyId { get; set; } = null!;

        public GetAccessPolicyArgs()
        {
        }
        public static new GetAccessPolicyArgs Empty => new GetAccessPolicyArgs();
    }

    public sealed class GetAccessPolicyInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("accessPolicyId", required: true)]
        public Input<string> AccessPolicyId { get; set; } = null!;

        public GetAccessPolicyInvokeArgs()
        {
        }
        public static new GetAccessPolicyInvokeArgs Empty => new GetAccessPolicyInvokeArgs();
    }


    [OutputType]
    public sealed class GetAccessPolicyResult
    {
        /// <summary>
        /// Resource name of the `AccessPolicy`. Format: `accessPolicies/{policy_id}`
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The parent of this `AccessPolicy` in the Cloud Resource Hierarchy. Currently immutable once created. Format: `organizations/{organization_id}`
        /// </summary>
        public readonly string Parent;
        /// <summary>
        /// Human readable title. Does not affect behavior.
        /// </summary>
        public readonly string Title;

        [OutputConstructor]
        private GetAccessPolicyResult(
            string name,

            string parent,

            string title)
        {
            Name = name;
            Parent = parent;
            Title = title;
        }
    }
}
