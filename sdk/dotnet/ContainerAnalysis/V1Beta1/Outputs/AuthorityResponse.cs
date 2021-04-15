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
    public sealed class AuthorityResponse
    {
        /// <summary>
        /// Hint hints at the purpose of the attestation authority.
        /// </summary>
        public readonly Outputs.HintResponse Hint;

        [OutputConstructor]
        private AuthorityResponse(Outputs.HintResponse hint)
        {
            Hint = hint;
        }
    }
}