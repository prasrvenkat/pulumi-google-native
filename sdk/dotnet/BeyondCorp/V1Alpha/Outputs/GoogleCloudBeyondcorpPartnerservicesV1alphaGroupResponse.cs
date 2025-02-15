// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BeyondCorp.V1Alpha.Outputs
{

    /// <summary>
    /// Message to capture group information
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudBeyondcorpPartnerservicesV1alphaGroupResponse
    {
        /// <summary>
        /// The group email id
        /// </summary>
        public readonly string Email;

        [OutputConstructor]
        private GoogleCloudBeyondcorpPartnerservicesV1alphaGroupResponse(string email)
        {
            Email = email;
        }
    }
}
