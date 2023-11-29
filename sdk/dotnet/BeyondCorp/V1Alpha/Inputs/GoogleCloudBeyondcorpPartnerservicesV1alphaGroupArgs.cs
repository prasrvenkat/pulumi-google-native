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
    /// Message to capture group information
    /// </summary>
    public sealed class GoogleCloudBeyondcorpPartnerservicesV1alphaGroupArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The group email id
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// Google group id
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        public GoogleCloudBeyondcorpPartnerservicesV1alphaGroupArgs()
        {
        }
        public static new GoogleCloudBeyondcorpPartnerservicesV1alphaGroupArgs Empty => new GoogleCloudBeyondcorpPartnerservicesV1alphaGroupArgs();
    }
}