// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.GKEHub.V1Beta.Outputs
{

    /// <summary>
    /// Configuration for the AzureAD Auth flow.
    /// </summary>
    [OutputType]
    public sealed class IdentityServiceAzureADConfigResponse
    {
        /// <summary>
        /// ID for the registered client application that makes authentication requests to the Azure AD identity provider.
        /// </summary>
        public readonly string ClientId;
        /// <summary>
        /// Input only. Unencrypted AzureAD client secret will be passed to the GKE Hub CLH.
        /// </summary>
        public readonly string ClientSecret;
        /// <summary>
        /// Encrypted AzureAD client secret.
        /// </summary>
        public readonly string EncryptedClientSecret;
        /// <summary>
        /// The redirect URL that kubectl uses for authorization.
        /// </summary>
        public readonly string KubectlRedirectUri;
        /// <summary>
        /// Kind of Azure AD account to be authenticated. Supported values are or for accounts belonging to a specific tenant.
        /// </summary>
        public readonly string Tenant;

        [OutputConstructor]
        private IdentityServiceAzureADConfigResponse(
            string clientId,

            string clientSecret,

            string encryptedClientSecret,

            string kubectlRedirectUri,

            string tenant)
        {
            ClientId = clientId;
            ClientSecret = clientSecret;
            EncryptedClientSecret = encryptedClientSecret;
            KubectlRedirectUri = kubectlRedirectUri;
            Tenant = tenant;
        }
    }
}
