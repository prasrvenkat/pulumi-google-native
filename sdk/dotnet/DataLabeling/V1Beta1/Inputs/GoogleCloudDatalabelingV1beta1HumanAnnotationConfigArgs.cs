// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DataLabeling.V1Beta1.Inputs
{

    /// <summary>
    /// Configuration for how human labeling task should be done.
    /// </summary>
    public sealed class GoogleCloudDatalabelingV1beta1HumanAnnotationConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. A human-readable description for AnnotatedDataset. The description can be up to 10000 characters long.
        /// </summary>
        [Input("annotatedDatasetDescription")]
        public Input<string>? AnnotatedDatasetDescription { get; set; }

        /// <summary>
        /// A human-readable name for AnnotatedDataset defined by users. Maximum of 64 characters .
        /// </summary>
        [Input("annotatedDatasetDisplayName", required: true)]
        public Input<string> AnnotatedDatasetDisplayName { get; set; } = null!;

        [Input("contributorEmails")]
        private InputList<string>? _contributorEmails;

        /// <summary>
        /// Optional. If you want your own labeling contributors to manage and work on this labeling request, you can set these contributors here. We will give them access to the question types in crowdcompute. Note that these emails must be registered in crowdcompute worker UI: https://crowd-compute.appspot.com/
        /// </summary>
        public InputList<string> ContributorEmails
        {
            get => _contributorEmails ?? (_contributorEmails = new InputList<string>());
            set => _contributorEmails = value;
        }

        /// <summary>
        /// Instruction resource name.
        /// </summary>
        [Input("instruction", required: true)]
        public Input<string> Instruction { get; set; } = null!;

        /// <summary>
        /// Optional. A human-readable label used to logically group labeling tasks. This string must match the regular expression `[a-zA-Z\\d_-]{0,128}`.
        /// </summary>
        [Input("labelGroup")]
        public Input<string>? LabelGroup { get; set; }

        /// <summary>
        /// Optional. The Language of this question, as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). Default value is en-US. Only need to set this when task is language related. For example, French text classification.
        /// </summary>
        [Input("languageCode")]
        public Input<string>? LanguageCode { get; set; }

        /// <summary>
        /// Optional. Maximum duration for contributors to answer a question. Maximum is 3600 seconds. Default is 3600 seconds.
        /// </summary>
        [Input("questionDuration")]
        public Input<string>? QuestionDuration { get; set; }

        /// <summary>
        /// Optional. Replication of questions. Each question will be sent to up to this number of contributors to label. Aggregated answers will be returned. Default is set to 1. For image related labeling, valid values are 1, 3, 5.
        /// </summary>
        [Input("replicaCount")]
        public Input<int>? ReplicaCount { get; set; }

        /// <summary>
        /// Email of the user who started the labeling task and should be notified by email. If empty no notification will be sent.
        /// </summary>
        [Input("userEmailAddress")]
        public Input<string>? UserEmailAddress { get; set; }

        public GoogleCloudDatalabelingV1beta1HumanAnnotationConfigArgs()
        {
        }
        public static new GoogleCloudDatalabelingV1beta1HumanAnnotationConfigArgs Empty => new GoogleCloudDatalabelingV1beta1HumanAnnotationConfigArgs();
    }
}
