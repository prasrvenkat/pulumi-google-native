// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.VMMigration.V1.Outputs
{

    /// <summary>
    /// AwsSourceDetails message describes a specific source details for the AWS source type.
    /// </summary>
    [OutputType]
    public sealed class AwsSourceDetailsResponse
    {
        /// <summary>
        /// AWS Credentials using access key id and secret.
        /// </summary>
        public readonly Outputs.AccessKeyCredentialsResponse AccessKeyCreds;
        /// <summary>
        /// Immutable. The AWS region that the source VMs will be migrated from.
        /// </summary>
        public readonly string AwsRegion;
        /// <summary>
        /// Provides details on the state of the Source in case of an error.
        /// </summary>
        public readonly Outputs.StatusResponse Error;
        /// <summary>
        /// AWS security group names to limit the scope of the source inventory.
        /// </summary>
        public readonly ImmutableArray<string> InventorySecurityGroupNames;
        /// <summary>
        /// AWS resource tags to limit the scope of the source inventory.
        /// </summary>
        public readonly ImmutableArray<Outputs.TagResponse> InventoryTagList;
        /// <summary>
        /// User specified tags to add to every M2VM generated resource in AWS. These tags will be set in addition to the default tags that are set as part of the migration process. The tags must not begin with the reserved prefix `m2vm`.
        /// </summary>
        public readonly ImmutableDictionary<string, string> MigrationResourcesUserTags;
        /// <summary>
        /// The source's public IP. All communication initiated by this source will originate from this IP.
        /// </summary>
        public readonly string PublicIp;
        /// <summary>
        /// State of the source as determined by the health check.
        /// </summary>
        public readonly string State;

        [OutputConstructor]
        private AwsSourceDetailsResponse(
            Outputs.AccessKeyCredentialsResponse accessKeyCreds,

            string awsRegion,

            Outputs.StatusResponse error,

            ImmutableArray<string> inventorySecurityGroupNames,

            ImmutableArray<Outputs.TagResponse> inventoryTagList,

            ImmutableDictionary<string, string> migrationResourcesUserTags,

            string publicIp,

            string state)
        {
            AccessKeyCreds = accessKeyCreds;
            AwsRegion = awsRegion;
            Error = error;
            InventorySecurityGroupNames = inventorySecurityGroupNames;
            InventoryTagList = inventoryTagList;
            MigrationResourcesUserTags = migrationResourcesUserTags;
            PublicIp = publicIp;
            State = state;
        }
    }
}