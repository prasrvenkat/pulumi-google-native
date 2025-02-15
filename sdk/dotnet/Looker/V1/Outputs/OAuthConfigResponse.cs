// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Looker.V1.Outputs
{

    /// <summary>
    /// Looker instance OAuth login settings.
    /// </summary>
    [OutputType]
    public sealed class OAuthConfigResponse
    {
        /// <summary>
        /// Input only. Client ID from an external OAuth application. This is an input-only field, and thus will not be set in any responses.
        /// </summary>
        public readonly string ClientId;
        /// <summary>
        /// Input only. Client secret from an external OAuth application. This is an input-only field, and thus will not be set in any responses.
        /// </summary>
        public readonly string ClientSecret;

        [OutputConstructor]
        private OAuthConfigResponse(
            string clientId,

            string clientSecret)
        {
            ClientId = clientId;
            ClientSecret = clientSecret;
        }
    }
}
