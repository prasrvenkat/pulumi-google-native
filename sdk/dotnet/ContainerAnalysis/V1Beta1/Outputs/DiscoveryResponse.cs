// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GcpNative.ContainerAnalysis.V1Beta1.Outputs
{

    [OutputType]
    public sealed class DiscoveryResponse
    {
        /// <summary>
        /// Required. Immutable. The kind of analysis that is handled by this discovery.
        /// </summary>
        public readonly string AnalysisKind;

        [OutputConstructor]
        private DiscoveryResponse(string analysisKind)
        {
            AnalysisKind = analysisKind;
        }
    }
}