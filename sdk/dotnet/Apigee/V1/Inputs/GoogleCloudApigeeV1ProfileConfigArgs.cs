// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Apigee.V1.Inputs
{

    /// <summary>
    /// ProfileConfig defines a set of categories and policies which will be used to compute security score.
    /// </summary>
    public sealed class GoogleCloudApigeeV1ProfileConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("categories")]
        private InputList<Inputs.GoogleCloudApigeeV1ProfileConfigCategoryArgs>? _categories;

        /// <summary>
        /// List of categories of profile config.
        /// </summary>
        public InputList<Inputs.GoogleCloudApigeeV1ProfileConfigCategoryArgs> Categories
        {
            get => _categories ?? (_categories = new InputList<Inputs.GoogleCloudApigeeV1ProfileConfigCategoryArgs>());
            set => _categories = value;
        }

        public GoogleCloudApigeeV1ProfileConfigArgs()
        {
        }
        public static new GoogleCloudApigeeV1ProfileConfigArgs Empty => new GoogleCloudApigeeV1ProfileConfigArgs();
    }
}
