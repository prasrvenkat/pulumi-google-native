// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BinaryAuthorization.V1.Outputs
{

    /// <summary>
    /// Require a signed [DSSE](https://github.com/secure-systems-lab/dsse) attestation with type SimpleSigning.
    /// </summary>
    [OutputType]
    public sealed class SimpleSigningAttestationCheckResponse
    {
        /// <summary>
        /// The authenticators required by this check to verify an attestation. Typically this is one or more PKIX public keys for signature verification. Only one authenticator needs to consider an attestation verified in order for an attestation to be considered fully authenticated. In otherwords, this list of authenticators is an "OR" of the authenticator results. At least one authenticator is required.
        /// </summary>
        public readonly ImmutableArray<Outputs.AttestationAuthenticatorResponse> AttestationAuthenticators;
        /// <summary>
        /// Optional. The projects where attestations are stored as Container Analysis Occurrences. Only one attestation needs to successfully verify an image for this check to pass, so a single verified attestation found in any of `container_analysis_attestation_projects` is sufficient for the check to pass. When fetching Occurrences from Container Analysis, only 'AttestationOccurrence' kinds are considered. In the future, additional Occurrence kinds may be added to the query.
        /// </summary>
        public readonly ImmutableArray<string> ContainerAnalysisAttestationProjects;

        [OutputConstructor]
        private SimpleSigningAttestationCheckResponse(
            ImmutableArray<Outputs.AttestationAuthenticatorResponse> attestationAuthenticators,

            ImmutableArray<string> containerAnalysisAttestationProjects)
        {
            AttestationAuthenticators = attestationAuthenticators;
            ContainerAnalysisAttestationProjects = containerAnalysisAttestationProjects;
        }
    }
}
