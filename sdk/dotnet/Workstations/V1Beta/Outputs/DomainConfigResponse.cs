// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Workstations.V1Beta.Outputs
{

    /// <summary>
    /// Configuration options for a custom domain.
    /// </summary>
    [OutputType]
    public sealed class DomainConfigResponse
    {
        /// <summary>
        /// Immutable. Domain used by Workstations for HTTP ingress.
        /// </summary>
        public readonly string Domain;

        [OutputConstructor]
        private DomainConfigResponse(string domain)
        {
            Domain = domain;
        }
    }
}