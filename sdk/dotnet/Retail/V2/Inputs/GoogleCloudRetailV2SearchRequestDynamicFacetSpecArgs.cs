// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Retail.V2.Inputs
{

    /// <summary>
    /// The specifications of dynamically generated facets.
    /// </summary>
    public sealed class GoogleCloudRetailV2SearchRequestDynamicFacetSpecArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Mode of the DynamicFacet feature. Defaults to Mode.DISABLED if it's unset.
        /// </summary>
        [Input("mode")]
        public Input<Pulumi.GoogleNative.Retail.V2.GoogleCloudRetailV2SearchRequestDynamicFacetSpecMode>? Mode { get; set; }

        public GoogleCloudRetailV2SearchRequestDynamicFacetSpecArgs()
        {
        }
        public static new GoogleCloudRetailV2SearchRequestDynamicFacetSpecArgs Empty => new GoogleCloudRetailV2SearchRequestDynamicFacetSpecArgs();
    }
}