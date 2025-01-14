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
    /// Rich Business Messaging (RBM) Card content
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentResponse
    {
        /// <summary>
        /// Optional. Description of the card (at most 2000 bytes). At least one of the title, description or media must be set.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Optional. However at least one of the title, description or media must be set. Media (image, GIF or a video) to include in the card.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaResponse Media;
        /// <summary>
        /// Optional. List of suggestions to include in the card.
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionResponse> Suggestions;
        /// <summary>
        /// Optional. Title of the card (at most 200 bytes). At least one of the title, description or media must be set.
        /// </summary>
        public readonly string Title;

        [OutputConstructor]
        private GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentResponse(
            string description,

            Outputs.GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMediaResponse media,

            ImmutableArray<Outputs.GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestionResponse> suggestions,

            string title)
        {
            Description = description;
            Media = media;
            Suggestions = suggestions;
            Title = title;
        }
    }
}
