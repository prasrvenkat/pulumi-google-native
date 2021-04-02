// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Dialogflow.V2beta1.Outputs
{

    [OutputType]
    public sealed class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonResponse
    {
        /// <summary>
        /// Required. Action to take when a user taps on the button.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionResponse OpenUriAction;
        /// <summary>
        /// Required. The title of the button.
        /// </summary>
        public readonly string Title;

        [OutputConstructor]
        private GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonResponse(
            Outputs.GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionResponse openUriAction,

            string title)
        {
            OpenUriAction = openUriAction;
            Title = title;
        }
    }
}