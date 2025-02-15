// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DataLabeling.V1Beta1
{
    /// <summary>
    /// Creates an annotation spec set by providing a set of labels.
    /// Auto-naming is currently not supported for this resource.
    /// </summary>
    [GoogleNativeResourceType("google-native:datalabeling/v1beta1:AnnotationSpecSet")]
    public partial class AnnotationSpecSet : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The array of AnnotationSpecs that you define when you create the AnnotationSpecSet. These are the possible labels for the labeling task.
        /// </summary>
        [Output("annotationSpecs")]
        public Output<ImmutableArray<Outputs.GoogleCloudDatalabelingV1beta1AnnotationSpecResponse>> AnnotationSpecs { get; private set; } = null!;

        /// <summary>
        /// The names of any related resources that are blocking changes to the annotation spec set.
        /// </summary>
        [Output("blockingResources")]
        public Output<ImmutableArray<string>> BlockingResources { get; private set; } = null!;

        /// <summary>
        /// Optional. User-provided description of the annotation specification set. The description can be up to 10,000 characters long.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The display name for AnnotationSpecSet that you define when you create it. Maximum of 64 characters.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// The AnnotationSpecSet resource name in the following format: "projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}"
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;


        /// <summary>
        /// Create a AnnotationSpecSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AnnotationSpecSet(string name, AnnotationSpecSetArgs args, CustomResourceOptions? options = null)
            : base("google-native:datalabeling/v1beta1:AnnotationSpecSet", name, args ?? new AnnotationSpecSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AnnotationSpecSet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:datalabeling/v1beta1:AnnotationSpecSet", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "project",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AnnotationSpecSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AnnotationSpecSet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AnnotationSpecSet(name, id, options);
        }
    }

    public sealed class AnnotationSpecSetArgs : global::Pulumi.ResourceArgs
    {
        [Input("annotationSpecs", required: true)]
        private InputList<Inputs.GoogleCloudDatalabelingV1beta1AnnotationSpecArgs>? _annotationSpecs;

        /// <summary>
        /// The array of AnnotationSpecs that you define when you create the AnnotationSpecSet. These are the possible labels for the labeling task.
        /// </summary>
        public InputList<Inputs.GoogleCloudDatalabelingV1beta1AnnotationSpecArgs> AnnotationSpecs
        {
            get => _annotationSpecs ?? (_annotationSpecs = new InputList<Inputs.GoogleCloudDatalabelingV1beta1AnnotationSpecArgs>());
            set => _annotationSpecs = value;
        }

        /// <summary>
        /// Optional. User-provided description of the annotation specification set. The description can be up to 10,000 characters long.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The display name for AnnotationSpecSet that you define when you create it. Maximum of 64 characters.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        public AnnotationSpecSetArgs()
        {
        }
        public static new AnnotationSpecSetArgs Empty => new AnnotationSpecSetArgs();
    }
}
