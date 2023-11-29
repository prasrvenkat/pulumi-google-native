// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.VMMigration.V1Alpha1.Inputs
{

    /// <summary>
    /// Contains details about the image source used to create the disk.
    /// </summary>
    public sealed class DiskImageDefaultsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Image resource used when creating the disk.
        /// </summary>
        [Input("sourceImage", required: true)]
        public Input<string> SourceImage { get; set; } = null!;

        public DiskImageDefaultsArgs()
        {
        }
        public static new DiskImageDefaultsArgs Empty => new DiskImageDefaultsArgs();
    }
}