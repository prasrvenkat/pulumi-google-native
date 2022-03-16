// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V2
{
    public static class GetConversationDataset
    {
        /// <summary>
        /// Retrieves the specified conversation dataset.
        /// </summary>
        public static Task<GetConversationDatasetResult> InvokeAsync(GetConversationDatasetArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetConversationDatasetResult>("google-native:dialogflow/v2:getConversationDataset", args ?? new GetConversationDatasetArgs(), options.WithDefaults());

        /// <summary>
        /// Retrieves the specified conversation dataset.
        /// </summary>
        public static Output<GetConversationDatasetResult> Invoke(GetConversationDatasetInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetConversationDatasetResult>("google-native:dialogflow/v2:getConversationDataset", args ?? new GetConversationDatasetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetConversationDatasetArgs : Pulumi.InvokeArgs
    {
        [Input("conversationDatasetId", required: true)]
        public string ConversationDatasetId { get; set; } = null!;

        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        public GetConversationDatasetArgs()
        {
        }
    }

    public sealed class GetConversationDatasetInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("conversationDatasetId", required: true)]
        public Input<string> ConversationDatasetId { get; set; } = null!;

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        public GetConversationDatasetInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetConversationDatasetResult
    {
        /// <summary>
        /// The number of conversations this conversation dataset contains.
        /// </summary>
        public readonly string ConversationCount;
        /// <summary>
        /// Metadata set during conversation data import.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowV2ConversationInfoResponse ConversationInfo;
        /// <summary>
        /// Creation time of this dataset.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Optional. The description of the dataset. Maximum of 10000 bytes.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The display name of the dataset. Maximum of 64 bytes.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// Input configurations set during conversation data import.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowV2InputConfigResponse InputConfig;
        /// <summary>
        /// ConversationDataset resource name. Format: `projects//locations//conversationDatasets/`
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetConversationDatasetResult(
            string conversationCount,

            Outputs.GoogleCloudDialogflowV2ConversationInfoResponse conversationInfo,

            string createTime,

            string description,

            string displayName,

            Outputs.GoogleCloudDialogflowV2InputConfigResponse inputConfig,

            string name)
        {
            ConversationCount = conversationCount;
            ConversationInfo = conversationInfo;
            CreateTime = createTime;
            Description = description;
            DisplayName = displayName;
            InputConfig = inputConfig;
            Name = name;
        }
    }
}