// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ContainerAnalysis.V1Beta1.Outputs
{

    /// <summary>
    /// Metadata for any related URL information.
    /// </summary>
    [OutputType]
    public sealed class RelatedUrlResponse
    {
        /// <summary>
        /// Label to describe usage of the URL.
        /// </summary>
        public readonly string Label;
        /// <summary>
        /// Specific URL associated with the resource.
        /// </summary>
        public readonly string Url;

        [OutputConstructor]
        private RelatedUrlResponse(
            string label,

            string url)
        {
            Label = label;
            Url = url;
        }
    }
}
