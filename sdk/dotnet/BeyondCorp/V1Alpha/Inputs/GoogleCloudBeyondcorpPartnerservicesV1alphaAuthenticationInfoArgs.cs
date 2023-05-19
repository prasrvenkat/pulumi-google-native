// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BeyondCorp.V1Alpha.Inputs
{

    /// <summary>
    /// Message contains the authentication information to validate against the proxy server.
    /// </summary>
    public sealed class GoogleCloudBeyondcorpPartnerservicesV1alphaAuthenticationInfoArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. Service Account for encrypting the JWT.
        /// </summary>
        [Input("encryptionSaEmail")]
        public Input<string>? EncryptionSaEmail { get; set; }

        public GoogleCloudBeyondcorpPartnerservicesV1alphaAuthenticationInfoArgs()
        {
        }
        public static new GoogleCloudBeyondcorpPartnerservicesV1alphaAuthenticationInfoArgs Empty => new GoogleCloudBeyondcorpPartnerservicesV1alphaAuthenticationInfoArgs();
    }
}