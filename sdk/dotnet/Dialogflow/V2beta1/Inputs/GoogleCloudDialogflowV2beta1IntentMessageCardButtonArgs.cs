// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Dialogflow.V2beta1.Inputs
{

    /// <summary>
    /// Optional. Contains information about a button.
    /// </summary>
    public sealed class GoogleCloudDialogflowV2beta1IntentMessageCardButtonArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. The text to send back to the Dialogflow API or a URI to open.
        /// </summary>
        [Input("postback")]
        public Input<string>? Postback { get; set; }

        /// <summary>
        /// Optional. The text to show on the button.
        /// </summary>
        [Input("text")]
        public Input<string>? Text { get; set; }

        public GoogleCloudDialogflowV2beta1IntentMessageCardButtonArgs()
        {
        }
    }
}