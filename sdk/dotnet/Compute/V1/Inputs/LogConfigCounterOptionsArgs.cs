// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.V1.Inputs
{

    /// <summary>
    /// This is deprecated and has no effect. Do not use.
    /// </summary>
    public sealed class LogConfigCounterOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("customFields")]
        private InputList<Inputs.LogConfigCounterOptionsCustomFieldArgs>? _customFields;

        /// <summary>
        /// This is deprecated and has no effect. Do not use.
        /// </summary>
        public InputList<Inputs.LogConfigCounterOptionsCustomFieldArgs> CustomFields
        {
            get => _customFields ?? (_customFields = new InputList<Inputs.LogConfigCounterOptionsCustomFieldArgs>());
            set => _customFields = value;
        }

        /// <summary>
        /// This is deprecated and has no effect. Do not use.
        /// </summary>
        [Input("field")]
        public Input<string>? Field { get; set; }

        /// <summary>
        /// This is deprecated and has no effect. Do not use.
        /// </summary>
        [Input("metric")]
        public Input<string>? Metric { get; set; }

        public LogConfigCounterOptionsArgs()
        {
        }
        public static new LogConfigCounterOptionsArgs Empty => new LogConfigCounterOptionsArgs();
    }
}
