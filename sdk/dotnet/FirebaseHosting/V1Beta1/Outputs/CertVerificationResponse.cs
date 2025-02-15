// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.FirebaseHosting.V1Beta1.Outputs
{

    /// <summary>
    /// A set of ACME challenges you can use to allow Hosting to create an SSL certificate for your domain name before directing traffic to Hosting servers. Use either the DNS or HTTP challenge; it's not necessary to provide both.
    /// </summary>
    [OutputType]
    public sealed class CertVerificationResponse
    {
        /// <summary>
        /// A `TXT` record to add to your DNS records that confirms your intent to let Hosting create an SSL cert for your domain name.
        /// </summary>
        public readonly Outputs.DnsUpdatesResponse Dns;
        /// <summary>
        /// A file to add to your existing, non-Hosting hosting service that confirms your intent to let Hosting create an SSL cert for your domain name.
        /// </summary>
        public readonly Outputs.HttpUpdateResponse Http;

        [OutputConstructor]
        private CertVerificationResponse(
            Outputs.DnsUpdatesResponse dns,

            Outputs.HttpUpdateResponse http)
        {
            Dns = dns;
            Http = http;
        }
    }
}
