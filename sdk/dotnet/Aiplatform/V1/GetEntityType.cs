// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1
{
    public static class GetEntityType
    {
        /// <summary>
        /// Gets details of a single EntityType.
        /// </summary>
        public static Task<GetEntityTypeResult> InvokeAsync(GetEntityTypeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetEntityTypeResult>("google-native:aiplatform/v1:getEntityType", args ?? new GetEntityTypeArgs(), options.WithDefaults());

        /// <summary>
        /// Gets details of a single EntityType.
        /// </summary>
        public static Output<GetEntityTypeResult> Invoke(GetEntityTypeInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetEntityTypeResult>("google-native:aiplatform/v1:getEntityType", args ?? new GetEntityTypeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEntityTypeArgs : global::Pulumi.InvokeArgs
    {
        [Input("entityTypeId", required: true)]
        public string EntityTypeId { get; set; } = null!;

        [Input("featurestoreId", required: true)]
        public string FeaturestoreId { get; set; } = null!;

        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        public GetEntityTypeArgs()
        {
        }
        public static new GetEntityTypeArgs Empty => new GetEntityTypeArgs();
    }

    public sealed class GetEntityTypeInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("entityTypeId", required: true)]
        public Input<string> EntityTypeId { get; set; } = null!;

        [Input("featurestoreId", required: true)]
        public Input<string> FeaturestoreId { get; set; } = null!;

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        public GetEntityTypeInvokeArgs()
        {
        }
        public static new GetEntityTypeInvokeArgs Empty => new GetEntityTypeInvokeArgs();
    }


    [OutputType]
    public sealed class GetEntityTypeResult
    {
        /// <summary>
        /// Timestamp when this EntityType was created.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Optional. Description of the EntityType.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Optional. Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
        /// </summary>
        public readonly string Etag;
        /// <summary>
        /// Optional. The labels with user-defined metadata to organize your EntityTypes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one EntityType (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Labels;
        /// <summary>
        /// Optional. The default monitoring configuration for all Features with value type (Feature.ValueType) BOOL, STRING, DOUBLE or INT64 under this EntityType. If this is populated with [FeaturestoreMonitoringConfig.monitoring_interval] specified, snapshot analysis monitoring is enabled. Otherwise, snapshot analysis monitoring is disabled.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1FeaturestoreMonitoringConfigResponse MonitoringConfig;
        /// <summary>
        /// Immutable. Name of the EntityType. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` The last part entity_type is assigned by the client. The entity_type can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z and underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given a featurestore.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Optional. Config for data retention policy in offline storage. TTL in days for feature values that will be stored in offline storage. The Feature Store offline storage periodically removes obsolete feature values older than `offline_storage_ttl_days` since the feature generation time. If unset (or explicitly set to 0), default to 4000 days TTL.
        /// </summary>
        public readonly int OfflineStorageTtlDays;
        /// <summary>
        /// Timestamp when this EntityType was most recently updated.
        /// </summary>
        public readonly string UpdateTime;

        [OutputConstructor]
        private GetEntityTypeResult(
            string createTime,

            string description,

            string etag,

            ImmutableDictionary<string, string> labels,

            Outputs.GoogleCloudAiplatformV1FeaturestoreMonitoringConfigResponse monitoringConfig,

            string name,

            int offlineStorageTtlDays,

            string updateTime)
        {
            CreateTime = createTime;
            Description = description;
            Etag = etag;
            Labels = labels;
            MonitoringConfig = monitoringConfig;
            Name = name;
            OfflineStorageTtlDays = offlineStorageTtlDays;
            UpdateTime = updateTime;
        }
    }
}
