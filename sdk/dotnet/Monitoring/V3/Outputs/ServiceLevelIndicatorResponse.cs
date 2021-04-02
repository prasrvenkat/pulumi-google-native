// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Monitoring.V3.Outputs
{

    [OutputType]
    public sealed class ServiceLevelIndicatorResponse
    {
        /// <summary>
        /// Basic SLI on a well-known service type.
        /// </summary>
        public readonly Outputs.BasicSliResponse BasicSli;
        /// <summary>
        /// Request-based SLIs
        /// </summary>
        public readonly Outputs.RequestBasedSliResponse RequestBased;
        /// <summary>
        /// Windows-based SLIs
        /// </summary>
        public readonly Outputs.WindowsBasedSliResponse WindowsBased;

        [OutputConstructor]
        private ServiceLevelIndicatorResponse(
            Outputs.BasicSliResponse basicSli,

            Outputs.RequestBasedSliResponse requestBased,

            Outputs.WindowsBasedSliResponse windowsBased)
        {
            BasicSli = basicSli;
            RequestBased = requestBased;
            WindowsBased = windowsBased;
        }
    }
}