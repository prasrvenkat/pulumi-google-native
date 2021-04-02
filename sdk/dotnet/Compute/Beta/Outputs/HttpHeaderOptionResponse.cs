// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Compute.Beta.Outputs
{

    [OutputType]
    public sealed class HttpHeaderOptionResponse
    {
        /// <summary>
        /// The name of the header.
        /// </summary>
        public readonly string HeaderName;
        /// <summary>
        /// The value of the header to add.
        /// </summary>
        public readonly string HeaderValue;
        /// <summary>
        /// If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header.
        /// The default value is false.
        /// </summary>
        public readonly bool Replace;

        [OutputConstructor]
        private HttpHeaderOptionResponse(
            string headerName,

            string headerValue,

            bool replace)
        {
            HeaderName = headerName;
            HeaderValue = headerValue;
            Replace = replace;
        }
    }
}