// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Pubsub.V1.Outputs
{

    /// <summary>
    /// Contains information needed for generating an [OpenID Connect token](https://developers.google.com/identity/protocols/OpenIDConnect).
    /// </summary>
    [OutputType]
    public sealed class OidcTokenResponse
    {
        /// <summary>
        /// Optional. Audience to be used when generating OIDC token. The audience claim identifies the recipients that the JWT is intended for. The audience value is a single case-sensitive string. Having multiple values (array) for the audience field is not supported. More info about the OIDC JWT token audience here: https://tools.ietf.org/html/rfc7519#section-4.1.3 Note: if not specified, the Push endpoint URL will be used.
        /// </summary>
        public readonly string Audience;
        /// <summary>
        /// Optional. [Service account email](https://cloud.google.com/iam/docs/service-accounts) used for generating the OIDC token. For more information on setting up authentication, see [Push subscriptions](https://cloud.google.com/pubsub/docs/push).
        /// </summary>
        public readonly string ServiceAccountEmail;

        [OutputConstructor]
        private OidcTokenResponse(
            string audience,

            string serviceAccountEmail)
        {
            Audience = audience;
            ServiceAccountEmail = serviceAccountEmail;
        }
    }
}
