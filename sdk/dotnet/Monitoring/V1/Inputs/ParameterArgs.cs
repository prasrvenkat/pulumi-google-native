// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Monitoring.V1.Inputs
{

    /// <summary>
    /// Preview: Parameter value applied to the aggregation function. This is a preview feature and may be subject to change before final release.
    /// </summary>
    public sealed class ParameterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A floating-point parameter value.
        /// </summary>
        [Input("doubleValue")]
        public Input<double>? DoubleValue { get; set; }

        /// <summary>
        /// An integer parameter value.
        /// </summary>
        [Input("intValue")]
        public Input<string>? IntValue { get; set; }

        public ParameterArgs()
        {
        }
        public static new ParameterArgs Empty => new ParameterArgs();
    }
}
