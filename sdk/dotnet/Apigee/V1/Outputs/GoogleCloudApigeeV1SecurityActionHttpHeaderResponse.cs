// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Apigee.V1.Outputs
{

    /// <summary>
    /// An HTTP header.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudApigeeV1SecurityActionHttpHeaderResponse
    {
        /// <summary>
        /// The header name to be sent to the target.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The header value to be sent to the target.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private GoogleCloudApigeeV1SecurityActionHttpHeaderResponse(
            string name,

            string value)
        {
            Name = name;
            Value = value;
        }
    }
}
