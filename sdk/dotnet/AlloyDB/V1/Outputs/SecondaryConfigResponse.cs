// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AlloyDB.V1.Outputs
{

    /// <summary>
    /// Configuration information for the secondary cluster. This should be set if and only if the cluster is of type SECONDARY.
    /// </summary>
    [OutputType]
    public sealed class SecondaryConfigResponse
    {
        /// <summary>
        /// The name of the primary cluster name with the format: * projects/{project}/locations/{region}/clusters/{cluster_id}
        /// </summary>
        public readonly string PrimaryClusterName;

        [OutputConstructor]
        private SecondaryConfigResponse(string primaryClusterName)
        {
            PrimaryClusterName = primaryClusterName;
        }
    }
}