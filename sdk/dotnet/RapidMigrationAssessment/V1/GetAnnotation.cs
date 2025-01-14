// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.RapidMigrationAssessment.V1
{
    public static class GetAnnotation
    {
        /// <summary>
        /// Gets details of a single Annotation.
        /// </summary>
        public static Task<GetAnnotationResult> InvokeAsync(GetAnnotationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAnnotationResult>("google-native:rapidmigrationassessment/v1:getAnnotation", args ?? new GetAnnotationArgs(), options.WithDefaults());

        /// <summary>
        /// Gets details of a single Annotation.
        /// </summary>
        public static Output<GetAnnotationResult> Invoke(GetAnnotationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAnnotationResult>("google-native:rapidmigrationassessment/v1:getAnnotation", args ?? new GetAnnotationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAnnotationArgs : global::Pulumi.InvokeArgs
    {
        [Input("annotationId", required: true)]
        public string AnnotationId { get; set; } = null!;

        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        public GetAnnotationArgs()
        {
        }
        public static new GetAnnotationArgs Empty => new GetAnnotationArgs();
    }

    public sealed class GetAnnotationInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("annotationId", required: true)]
        public Input<string> AnnotationId { get; set; } = null!;

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        public GetAnnotationInvokeArgs()
        {
        }
        public static new GetAnnotationInvokeArgs Empty => new GetAnnotationInvokeArgs();
    }


    [OutputType]
    public sealed class GetAnnotationResult
    {
        /// <summary>
        /// Create time stamp.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Labels as key value pairs.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Labels;
        /// <summary>
        /// name of resource.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Type of an annotation.
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// Update time stamp.
        /// </summary>
        public readonly string UpdateTime;

        [OutputConstructor]
        private GetAnnotationResult(
            string createTime,

            ImmutableDictionary<string, string> labels,

            string name,

            string type,

            string updateTime)
        {
            CreateTime = createTime;
            Labels = labels;
            Name = name;
            Type = type;
            UpdateTime = updateTime;
        }
    }
}
