// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1
{
    public static class GetMetadataStore
    {
        /// <summary>
        /// Retrieves a specific MetadataStore.
        /// </summary>
        public static Task<GetMetadataStoreResult> InvokeAsync(GetMetadataStoreArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetMetadataStoreResult>("google-native:aiplatform/v1:getMetadataStore", args ?? new GetMetadataStoreArgs(), options.WithDefaults());

        /// <summary>
        /// Retrieves a specific MetadataStore.
        /// </summary>
        public static Output<GetMetadataStoreResult> Invoke(GetMetadataStoreInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetMetadataStoreResult>("google-native:aiplatform/v1:getMetadataStore", args ?? new GetMetadataStoreInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMetadataStoreArgs : global::Pulumi.InvokeArgs
    {
        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("metadataStoreId", required: true)]
        public string MetadataStoreId { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        public GetMetadataStoreArgs()
        {
        }
        public static new GetMetadataStoreArgs Empty => new GetMetadataStoreArgs();
    }

    public sealed class GetMetadataStoreInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("metadataStoreId", required: true)]
        public Input<string> MetadataStoreId { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        public GetMetadataStoreInvokeArgs()
        {
        }
        public static new GetMetadataStoreInvokeArgs Empty => new GetMetadataStoreInvokeArgs();
    }


    [OutputType]
    public sealed class GetMetadataStoreResult
    {
        /// <summary>
        /// Timestamp when this MetadataStore was created.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Description of the MetadataStore.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Customer-managed encryption key spec for a Metadata Store. If set, this Metadata Store and all sub-resources of this Metadata Store are secured using this key.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1EncryptionSpecResponse EncryptionSpec;
        /// <summary>
        /// The resource name of the MetadataStore instance.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// State information of the MetadataStore.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1MetadataStoreMetadataStoreStateResponse State;
        /// <summary>
        /// Timestamp when this MetadataStore was last updated.
        /// </summary>
        public readonly string UpdateTime;

        [OutputConstructor]
        private GetMetadataStoreResult(
            string createTime,

            string description,

            Outputs.GoogleCloudAiplatformV1EncryptionSpecResponse encryptionSpec,

            string name,

            Outputs.GoogleCloudAiplatformV1MetadataStoreMetadataStoreStateResponse state,

            string updateTime)
        {
            CreateTime = createTime;
            Description = description;
            EncryptionSpec = encryptionSpec;
            Name = name;
            State = state;
            UpdateTime = updateTime;
        }
    }
}