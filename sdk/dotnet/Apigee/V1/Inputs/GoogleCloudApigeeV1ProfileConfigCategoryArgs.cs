// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Apigee.V1.Inputs
{

    /// <summary>
    /// Advanced API Security provides security profile that scores the following categories.
    /// </summary>
    public sealed class GoogleCloudApigeeV1ProfileConfigCategoryArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Checks for abuse, which includes any requests sent to the API for purposes other than what it is intended for, such as high volumes of requests, data scraping, and abuse related to authorization.
        /// </summary>
        [Input("abuse")]
        public Input<Inputs.GoogleCloudApigeeV1ProfileConfigAbuseArgs>? Abuse { get; set; }

        /// <summary>
        /// Checks to see if you have an authorization policy in place.
        /// </summary>
        [Input("authorization")]
        public Input<Inputs.GoogleCloudApigeeV1ProfileConfigAuthorizationArgs>? Authorization { get; set; }

        /// <summary>
        /// Checks to see if you have CORS policy in place.
        /// </summary>
        [Input("cors")]
        public Input<Inputs.GoogleCloudApigeeV1ProfileConfigCORSArgs>? Cors { get; set; }

        /// <summary>
        /// Checks to see if you have a mediation policy in place.
        /// </summary>
        [Input("mediation")]
        public Input<Inputs.GoogleCloudApigeeV1ProfileConfigMediationArgs>? Mediation { get; set; }

        /// <summary>
        /// Checks to see if you have configured mTLS for the target server.
        /// </summary>
        [Input("mtls")]
        public Input<Inputs.GoogleCloudApigeeV1ProfileConfigMTLSArgs>? Mtls { get; set; }

        /// <summary>
        /// Checks to see if you have a threat protection policy in place.
        /// </summary>
        [Input("threat")]
        public Input<Inputs.GoogleCloudApigeeV1ProfileConfigThreatArgs>? Threat { get; set; }

        public GoogleCloudApigeeV1ProfileConfigCategoryArgs()
        {
        }
        public static new GoogleCloudApigeeV1ProfileConfigCategoryArgs Empty => new GoogleCloudApigeeV1ProfileConfigCategoryArgs();
    }
}