// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Datalabeling.V1beta1.Inputs
{

    /// <summary>
    /// The configuration of input data, including data type, location, etc.
    /// </summary>
    public sealed class GoogleCloudDatalabelingV1beta1InputConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. The type of annotation to be performed on this data. You must specify this field if you are using this InputConfig in an EvaluationJob.
        /// </summary>
        [Input("annotationType")]
        public Input<string>? AnnotationType { get; set; }

        /// <summary>
        /// Source located in BigQuery. You must specify this field if you are using this InputConfig in an EvaluationJob.
        /// </summary>
        [Input("bigquerySource")]
        public Input<Inputs.GoogleCloudDatalabelingV1beta1BigQuerySourceArgs>? BigquerySource { get; set; }

        /// <summary>
        /// Optional. Metadata about annotations for the input. You must specify this field if you are using this InputConfig in an EvaluationJob for a model version that performs classification.
        /// </summary>
        [Input("classificationMetadata")]
        public Input<Inputs.GoogleCloudDatalabelingV1beta1ClassificationMetadataArgs>? ClassificationMetadata { get; set; }

        /// <summary>
        /// Required. Data type must be specifed when user tries to import data.
        /// </summary>
        [Input("dataType")]
        public Input<string>? DataType { get; set; }

        /// <summary>
        /// Source located in Cloud Storage.
        /// </summary>
        [Input("gcsSource")]
        public Input<Inputs.GoogleCloudDatalabelingV1beta1GcsSourceArgs>? GcsSource { get; set; }

        /// <summary>
        /// Required for text import, as language code must be specified.
        /// </summary>
        [Input("textMetadata")]
        public Input<Inputs.GoogleCloudDatalabelingV1beta1TextMetadataArgs>? TextMetadata { get; set; }

        public GoogleCloudDatalabelingV1beta1InputConfigArgs()
        {
        }
    }
}