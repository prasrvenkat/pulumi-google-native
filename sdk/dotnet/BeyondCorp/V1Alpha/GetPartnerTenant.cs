// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BeyondCorp.V1Alpha
{
    public static class GetPartnerTenant
    {
        /// <summary>
        /// Gets details of a single PartnerTenant.
        /// </summary>
        public static Task<GetPartnerTenantResult> InvokeAsync(GetPartnerTenantArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPartnerTenantResult>("google-native:beyondcorp/v1alpha:getPartnerTenant", args ?? new GetPartnerTenantArgs(), options.WithDefaults());

        /// <summary>
        /// Gets details of a single PartnerTenant.
        /// </summary>
        public static Output<GetPartnerTenantResult> Invoke(GetPartnerTenantInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPartnerTenantResult>("google-native:beyondcorp/v1alpha:getPartnerTenant", args ?? new GetPartnerTenantInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPartnerTenantArgs : global::Pulumi.InvokeArgs
    {
        [Input("organizationId", required: true)]
        public string OrganizationId { get; set; } = null!;

        [Input("partnerTenantId", required: true)]
        public string PartnerTenantId { get; set; } = null!;

        public GetPartnerTenantArgs()
        {
        }
        public static new GetPartnerTenantArgs Empty => new GetPartnerTenantArgs();
    }

    public sealed class GetPartnerTenantInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("organizationId", required: true)]
        public Input<string> OrganizationId { get; set; } = null!;

        [Input("partnerTenantId", required: true)]
        public Input<string> PartnerTenantId { get; set; } = null!;

        public GetPartnerTenantInvokeArgs()
        {
        }
        public static new GetPartnerTenantInvokeArgs Empty => new GetPartnerTenantInvokeArgs();
    }


    [OutputType]
    public sealed class GetPartnerTenantResult
    {
        /// <summary>
        /// Timestamp when the resource was created.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Optional. An arbitrary caller-provided name for the PartnerTenant. Cannot exceed 64 characters.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// Optional. Group information for the users enabled to use the partnerTenant. If the group information is not provided then the partnerTenant will be enabled for all users.
        /// </summary>
        public readonly Outputs.GoogleCloudBeyondcorpPartnerservicesV1alphaGroupResponse Group;
        /// <summary>
        /// Unique resource name of the PartnerTenant. The name is ignored when creating PartnerTenant.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Optional. Metadata provided by the Partner associated with PartnerTenant.
        /// </summary>
        public readonly Outputs.GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerMetadataResponse PartnerMetadata;
        /// <summary>
        /// Timestamp when the resource was last modified.
        /// </summary>
        public readonly string UpdateTime;

        [OutputConstructor]
        private GetPartnerTenantResult(
            string createTime,

            string displayName,

            Outputs.GoogleCloudBeyondcorpPartnerservicesV1alphaGroupResponse group,

            string name,

            Outputs.GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerMetadataResponse partnerMetadata,

            string updateTime)
        {
            CreateTime = createTime;
            DisplayName = displayName;
            Group = group;
            Name = name;
            PartnerMetadata = partnerMetadata;
            UpdateTime = updateTime;
        }
    }
}