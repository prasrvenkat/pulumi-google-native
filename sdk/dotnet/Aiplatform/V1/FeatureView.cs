// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1
{
    /// <summary>
    /// Creates a new FeatureView in a given FeatureOnlineStore.
    /// Auto-naming is currently not supported for this resource.
    /// </summary>
    [GoogleNativeResourceType("google-native:aiplatform/v1:FeatureView")]
    public partial class FeatureView : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Optional. Configures how data is supposed to be extracted from a BigQuery source to be loaded onto the FeatureOnlineStore.
        /// </summary>
        [Output("bigQuerySource")]
        public Output<Outputs.GoogleCloudAiplatformV1FeatureViewBigQuerySourceResponse> BigQuerySource { get; private set; } = null!;

        /// <summary>
        /// Timestamp when this FeatureView was created.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        [Output("featureOnlineStoreId")]
        public Output<string> FeatureOnlineStoreId { get; private set; } = null!;

        /// <summary>
        /// Optional. Configures the features from a Feature Registry source that need to be loaded onto the FeatureOnlineStore.
        /// </summary>
        [Output("featureRegistrySource")]
        public Output<Outputs.GoogleCloudAiplatformV1FeatureViewFeatureRegistrySourceResponse> FeatureRegistrySource { get; private set; } = null!;

        /// <summary>
        /// Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.
        /// </summary>
        [Output("featureViewId")]
        public Output<string> FeatureViewId { get; private set; } = null!;

        /// <summary>
        /// Optional. The labels with user-defined metadata to organize your FeatureViews. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// Name of the FeatureView. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// Immutable. If set to true, one on demand sync will be run immediately, regardless whether the FeatureView.sync_config is configured or not.
        /// </summary>
        [Output("runSyncImmediately")]
        public Output<bool?> RunSyncImmediately { get; private set; } = null!;

        /// <summary>
        /// Configures when data is to be synced/updated for this FeatureView. At the end of the sync the latest featureValues for each entityId of this FeatureView are made ready for online serving.
        /// </summary>
        [Output("syncConfig")]
        public Output<Outputs.GoogleCloudAiplatformV1FeatureViewSyncConfigResponse> SyncConfig { get; private set; } = null!;

        /// <summary>
        /// Timestamp when this FeatureView was last updated.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a FeatureView resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FeatureView(string name, FeatureViewArgs args, CustomResourceOptions? options = null)
            : base("google-native:aiplatform/v1:FeatureView", name, args ?? new FeatureViewArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FeatureView(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:aiplatform/v1:FeatureView", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "featureOnlineStoreId",
                    "featureViewId",
                    "location",
                    "project",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FeatureView resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FeatureView Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FeatureView(name, id, options);
        }
    }

    public sealed class FeatureViewArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. Configures how data is supposed to be extracted from a BigQuery source to be loaded onto the FeatureOnlineStore.
        /// </summary>
        [Input("bigQuerySource")]
        public Input<Inputs.GoogleCloudAiplatformV1FeatureViewBigQuerySourceArgs>? BigQuerySource { get; set; }

        /// <summary>
        /// Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        [Input("featureOnlineStoreId", required: true)]
        public Input<string> FeatureOnlineStoreId { get; set; } = null!;

        /// <summary>
        /// Optional. Configures the features from a Feature Registry source that need to be loaded onto the FeatureOnlineStore.
        /// </summary>
        [Input("featureRegistrySource")]
        public Input<Inputs.GoogleCloudAiplatformV1FeatureViewFeatureRegistrySourceArgs>? FeatureRegistrySource { get; set; }

        /// <summary>
        /// Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.
        /// </summary>
        [Input("featureViewId", required: true)]
        public Input<string> FeatureViewId { get; set; } = null!;

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Optional. The labels with user-defined metadata to organize your FeatureViews. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("location")]
        public Input<string>? Location { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// Immutable. If set to true, one on demand sync will be run immediately, regardless whether the FeatureView.sync_config is configured or not.
        /// </summary>
        [Input("runSyncImmediately")]
        public Input<bool>? RunSyncImmediately { get; set; }

        /// <summary>
        /// Configures when data is to be synced/updated for this FeatureView. At the end of the sync the latest featureValues for each entityId of this FeatureView are made ready for online serving.
        /// </summary>
        [Input("syncConfig")]
        public Input<Inputs.GoogleCloudAiplatformV1FeatureViewSyncConfigArgs>? SyncConfig { get; set; }

        public FeatureViewArgs()
        {
        }
        public static new FeatureViewArgs Empty => new FeatureViewArgs();
    }
}