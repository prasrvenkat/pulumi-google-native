// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.NetworkSecurity.V1
{
    public static class GetGatewaySecurityPolicy
    {
        /// <summary>
        /// Gets details of a single GatewaySecurityPolicy.
        /// </summary>
        public static Task<GetGatewaySecurityPolicyResult> InvokeAsync(GetGatewaySecurityPolicyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetGatewaySecurityPolicyResult>("google-native:networksecurity/v1:getGatewaySecurityPolicy", args ?? new GetGatewaySecurityPolicyArgs(), options.WithDefaults());

        /// <summary>
        /// Gets details of a single GatewaySecurityPolicy.
        /// </summary>
        public static Output<GetGatewaySecurityPolicyResult> Invoke(GetGatewaySecurityPolicyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetGatewaySecurityPolicyResult>("google-native:networksecurity/v1:getGatewaySecurityPolicy", args ?? new GetGatewaySecurityPolicyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetGatewaySecurityPolicyArgs : global::Pulumi.InvokeArgs
    {
        [Input("gatewaySecurityPolicyId", required: true)]
        public string GatewaySecurityPolicyId { get; set; } = null!;

        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        public GetGatewaySecurityPolicyArgs()
        {
        }
        public static new GetGatewaySecurityPolicyArgs Empty => new GetGatewaySecurityPolicyArgs();
    }

    public sealed class GetGatewaySecurityPolicyInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("gatewaySecurityPolicyId", required: true)]
        public Input<string> GatewaySecurityPolicyId { get; set; } = null!;

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        public GetGatewaySecurityPolicyInvokeArgs()
        {
        }
        public static new GetGatewaySecurityPolicyInvokeArgs Empty => new GetGatewaySecurityPolicyInvokeArgs();
    }


    [OutputType]
    public sealed class GetGatewaySecurityPolicyResult
    {
        /// <summary>
        /// The timestamp when the resource was created.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Optional. Free-text description of the resource.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Name of the resource. Name is of the form projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy} gateway_security_policy should match the pattern:(^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$).
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Optional. Name of a TLS Inspection Policy resource that defines how TLS inspection will be performed for any rule(s) which enables it.
        /// </summary>
        public readonly string TlsInspectionPolicy;
        /// <summary>
        /// The timestamp when the resource was updated.
        /// </summary>
        public readonly string UpdateTime;

        [OutputConstructor]
        private GetGatewaySecurityPolicyResult(
            string createTime,

            string description,

            string name,

            string tlsInspectionPolicy,

            string updateTime)
        {
            CreateTime = createTime;
            Description = description;
            Name = name;
            TlsInspectionPolicy = tlsInspectionPolicy;
            UpdateTime = updateTime;
        }
    }
}