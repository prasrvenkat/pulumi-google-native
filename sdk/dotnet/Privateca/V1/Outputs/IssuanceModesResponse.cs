// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Privateca.V1.Outputs
{

    /// <summary>
    /// IssuanceModes specifies the allowed ways in which Certificates may be requested from this CaPool.
    /// </summary>
    [OutputType]
    public sealed class IssuanceModesResponse
    {
        /// <summary>
        /// Optional. When true, allows callers to create Certificates by specifying a CertificateConfig.
        /// </summary>
        public readonly bool AllowConfigBasedIssuance;
        /// <summary>
        /// Optional. When true, allows callers to create Certificates by specifying a CSR.
        /// </summary>
        public readonly bool AllowCsrBasedIssuance;

        [OutputConstructor]
        private IssuanceModesResponse(
            bool allowConfigBasedIssuance,

            bool allowCsrBasedIssuance)
        {
            AllowConfigBasedIssuance = allowConfigBasedIssuance;
            AllowCsrBasedIssuance = allowCsrBasedIssuance;
        }
    }
}
