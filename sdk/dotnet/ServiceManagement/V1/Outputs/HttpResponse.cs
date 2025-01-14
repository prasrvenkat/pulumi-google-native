// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ServiceManagement.V1.Outputs
{

    /// <summary>
    /// Defines the HTTP configuration for an API service. It contains a list of HttpRule, each specifying the mapping of an RPC method to one or more HTTP REST API methods.
    /// </summary>
    [OutputType]
    public sealed class HttpResponse
    {
        /// <summary>
        /// When set to true, URL path parameters will be fully URI-decoded except in cases of single segment matches in reserved expansion, where "%2F" will be left encoded. The default behavior is to not decode RFC 6570 reserved characters in multi segment matches.
        /// </summary>
        public readonly bool FullyDecodeReservedExpansion;
        /// <summary>
        /// A list of HTTP configuration rules that apply to individual API methods. **NOTE:** All service configuration rules follow "last one wins" order.
        /// </summary>
        public readonly ImmutableArray<Outputs.HttpRuleResponse> Rules;

        [OutputConstructor]
        private HttpResponse(
            bool fullyDecodeReservedExpansion,

            ImmutableArray<Outputs.HttpRuleResponse> rules)
        {
            FullyDecodeReservedExpansion = fullyDecodeReservedExpansion;
            Rules = rules;
        }
    }
}
