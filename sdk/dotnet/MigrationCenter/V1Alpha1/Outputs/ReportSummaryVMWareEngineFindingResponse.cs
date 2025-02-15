// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.MigrationCenter.V1Alpha1.Outputs
{

    /// <summary>
    /// A set of findings that applies to assets destined for VMWare Engine.
    /// </summary>
    [OutputType]
    public sealed class ReportSummaryVMWareEngineFindingResponse
    {
        /// <summary>
        /// Count of assets which are allocated
        /// </summary>
        public readonly string AllocatedAssetCount;
        /// <summary>
        /// Set of regions in which the assets were allocated
        /// </summary>
        public readonly ImmutableArray<string> AllocatedRegions;
        /// <summary>
        /// Set of per-nodetype allocation records
        /// </summary>
        public readonly ImmutableArray<Outputs.ReportSummaryVMWareNodeAllocationResponse> NodeAllocations;

        [OutputConstructor]
        private ReportSummaryVMWareEngineFindingResponse(
            string allocatedAssetCount,

            ImmutableArray<string> allocatedRegions,

            ImmutableArray<Outputs.ReportSummaryVMWareNodeAllocationResponse> nodeAllocations)
        {
            AllocatedAssetCount = allocatedAssetCount;
            AllocatedRegions = allocatedRegions;
            NodeAllocations = nodeAllocations;
        }
    }
}
