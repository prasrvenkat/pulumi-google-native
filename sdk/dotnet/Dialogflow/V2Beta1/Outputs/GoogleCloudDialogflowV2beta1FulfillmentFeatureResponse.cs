// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V2Beta1.Outputs
{

    /// <summary>
    /// Whether fulfillment is enabled for the specific feature.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowV2beta1FulfillmentFeatureResponse
    {
        /// <summary>
        /// The type of the feature that enabled for fulfillment.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GoogleCloudDialogflowV2beta1FulfillmentFeatureResponse(string type)
        {
            Type = type;
        }
    }
}
