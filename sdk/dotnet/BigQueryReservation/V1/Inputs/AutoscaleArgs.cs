// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BigQueryReservation.V1.Inputs
{

    /// <summary>
    /// Auto scaling settings.
    /// </summary>
    public sealed class AutoscaleArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Number of slots to be scaled when needed.
        /// </summary>
        [Input("maxSlots")]
        public Input<string>? MaxSlots { get; set; }

        public AutoscaleArgs()
        {
        }
        public static new AutoscaleArgs Empty => new AutoscaleArgs();
    }
}