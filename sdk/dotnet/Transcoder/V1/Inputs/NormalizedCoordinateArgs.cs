// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Transcoder.V1.Inputs
{

    /// <summary>
    /// 2D normalized coordinates. Default: `{0.0, 0.0}`
    /// </summary>
    public sealed class NormalizedCoordinateArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Normalized x coordinate.
        /// </summary>
        [Input("x")]
        public Input<double>? X { get; set; }

        /// <summary>
        /// Normalized y coordinate.
        /// </summary>
        [Input("y")]
        public Input<double>? Y { get; set; }

        public NormalizedCoordinateArgs()
        {
        }
    }
}