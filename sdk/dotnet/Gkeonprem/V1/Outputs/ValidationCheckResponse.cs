// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Gkeonprem.V1.Outputs
{

    /// <summary>
    /// ValidationCheck represents the result of preflight check.
    /// </summary>
    [OutputType]
    public sealed class ValidationCheckResponse
    {
        /// <summary>
        /// Options used for the validation check
        /// </summary>
        public readonly string Option;
        /// <summary>
        /// The scenario when the preflight checks were run.
        /// </summary>
        public readonly string Scenario;
        /// <summary>
        /// The detailed validation check status.
        /// </summary>
        public readonly Outputs.ValidationCheckStatusResponse Status;

        [OutputConstructor]
        private ValidationCheckResponse(
            string option,

            string scenario,

            Outputs.ValidationCheckStatusResponse status)
        {
            Option = option;
            Scenario = scenario;
            Status = status;
        }
    }
}
