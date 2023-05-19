// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Contentwarehouse.V1.Inputs
{

    /// <summary>
    /// Property values.
    /// </summary>
    public sealed class GoogleCloudContentwarehouseV1PropertyArrayArgs : global::Pulumi.ResourceArgs
    {
        [Input("properties")]
        private InputList<Inputs.GoogleCloudContentwarehouseV1PropertyArgs>? _properties;

        /// <summary>
        /// List of property values.
        /// </summary>
        public InputList<Inputs.GoogleCloudContentwarehouseV1PropertyArgs> Properties
        {
            get => _properties ?? (_properties = new InputList<Inputs.GoogleCloudContentwarehouseV1PropertyArgs>());
            set => _properties = value;
        }

        public GoogleCloudContentwarehouseV1PropertyArrayArgs()
        {
        }
        public static new GoogleCloudContentwarehouseV1PropertyArrayArgs Empty => new GoogleCloudContentwarehouseV1PropertyArrayArgs();
    }
}