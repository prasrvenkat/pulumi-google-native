// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Container.V1.Inputs
{

    /// <summary>
    /// NodePoolLoggingConfig specifies logging configuration for nodepools.
    /// </summary>
    public sealed class NodePoolLoggingConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Logging variant configuration.
        /// </summary>
        [Input("variantConfig")]
        public Input<Inputs.LoggingVariantConfigArgs>? VariantConfig { get; set; }

        public NodePoolLoggingConfigArgs()
        {
        }
        public static new NodePoolLoggingConfigArgs Empty => new NodePoolLoggingConfigArgs();
    }
}