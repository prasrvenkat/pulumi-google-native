// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DiscoveryEngine.V1Alpha
{
    public static class GetDataStore
    {
        /// <summary>
        /// Gets a DataStore.
        /// </summary>
        public static Task<GetDataStoreResult> InvokeAsync(GetDataStoreArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDataStoreResult>("google-native:discoveryengine/v1alpha:getDataStore", args ?? new GetDataStoreArgs(), options.WithDefaults());

        /// <summary>
        /// Gets a DataStore.
        /// </summary>
        public static Output<GetDataStoreResult> Invoke(GetDataStoreInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDataStoreResult>("google-native:discoveryengine/v1alpha:getDataStore", args ?? new GetDataStoreInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDataStoreArgs : global::Pulumi.InvokeArgs
    {
        [Input("collectionId", required: true)]
        public string CollectionId { get; set; } = null!;

        [Input("dataStoreId", required: true)]
        public string DataStoreId { get; set; } = null!;

        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        public GetDataStoreArgs()
        {
        }
        public static new GetDataStoreArgs Empty => new GetDataStoreArgs();
    }

    public sealed class GetDataStoreInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("collectionId", required: true)]
        public Input<string> CollectionId { get; set; } = null!;

        [Input("dataStoreId", required: true)]
        public Input<string> DataStoreId { get; set; } = null!;

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        public GetDataStoreInvokeArgs()
        {
        }
        public static new GetDataStoreInvokeArgs Empty => new GetDataStoreInvokeArgs();
    }


    [OutputType]
    public sealed class GetDataStoreResult
    {
        /// <summary>
        /// Immutable. The content config of the data store. If this field is unset, the server behavior defaults to ContentConfig.NO_CONTENT.
        /// </summary>
        public readonly string ContentConfig;
        /// <summary>
        /// Timestamp the DataStore was created at.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// The id of the default Schema asscociated to this data store.
        /// </summary>
        public readonly string DefaultSchemaId;
        /// <summary>
        /// The data store display name. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// Immutable. The industry vertical that the data store registers.
        /// </summary>
        public readonly string IndustryVertical;
        /// <summary>
        /// Immutable. The full resource name of the data store. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}`. This field must be a UTF-8 encoded string with a length limit of 1024 characters.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The solutions that the data store enrolls. Available solutions for each industry_vertical: * `MEDIA`: `SOLUTION_TYPE_RECOMMENDATION` and `SOLUTION_TYPE_SEARCH`. * `SITE_SEARCH`: `SOLUTION_TYPE_SEARCH` is automatically enrolled. Other solutions cannot be enrolled.
        /// </summary>
        public readonly ImmutableArray<string> SolutionTypes;

        [OutputConstructor]
        private GetDataStoreResult(
            string contentConfig,

            string createTime,

            string defaultSchemaId,

            string displayName,

            string industryVertical,

            string name,

            ImmutableArray<string> solutionTypes)
        {
            ContentConfig = contentConfig;
            CreateTime = createTime;
            DefaultSchemaId = defaultSchemaId;
            DisplayName = displayName;
            IndustryVertical = industryVertical;
            Name = name;
            SolutionTypes = solutionTypes;
        }
    }
}