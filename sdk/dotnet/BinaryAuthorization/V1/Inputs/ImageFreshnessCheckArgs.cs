// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BinaryAuthorization.V1.Inputs
{

    /// <summary>
    /// An image freshness check, which rejects images that were uploaded before the set number of days ago to the supported repositories.
    /// </summary>
    public sealed class ImageFreshnessCheckArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The max number of days that is allowed since the image was uploaded. Must be greater than zero.
        /// </summary>
        [Input("maxUploadAgeDays", required: true)]
        public Input<int> MaxUploadAgeDays { get; set; } = null!;

        public ImageFreshnessCheckArgs()
        {
        }
        public static new ImageFreshnessCheckArgs Empty => new ImageFreshnessCheckArgs();
    }
}
