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
    /// Configuration for fine-grained cost management feature.
    /// </summary>
    public sealed class CostManagementConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether the feature is enabled or not.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        public CostManagementConfigArgs()
        {
        }
        public static new CostManagementConfigArgs Empty => new CostManagementConfigArgs();
    }
}