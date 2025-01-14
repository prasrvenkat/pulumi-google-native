// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1.Inputs
{

    /// <summary>
    /// Configures the input to BatchPredictionJob. See Model.supported_input_storage_formats for Model's supported input formats, and how instances should be expressed via any of them.
    /// </summary>
    public sealed class GoogleCloudAiplatformV1BatchPredictionJobInputConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The BigQuery location of the input table. The schema of the table should be in the format described by the given context OpenAPI Schema, if one is provided. The table may contain additional columns that are not described by the schema, and they will be ignored.
        /// </summary>
        [Input("bigquerySource")]
        public Input<Inputs.GoogleCloudAiplatformV1BigQuerySourceArgs>? BigquerySource { get; set; }

        /// <summary>
        /// The Cloud Storage location for the input instances.
        /// </summary>
        [Input("gcsSource")]
        public Input<Inputs.GoogleCloudAiplatformV1GcsSourceArgs>? GcsSource { get; set; }

        /// <summary>
        /// The format in which instances are given, must be one of the Model's supported_input_storage_formats.
        /// </summary>
        [Input("instancesFormat", required: true)]
        public Input<string> InstancesFormat { get; set; } = null!;

        public GoogleCloudAiplatformV1BatchPredictionJobInputConfigArgs()
        {
        }
        public static new GoogleCloudAiplatformV1BatchPredictionJobInputConfigArgs Empty => new GoogleCloudAiplatformV1BatchPredictionJobInputConfigArgs();
    }
}
