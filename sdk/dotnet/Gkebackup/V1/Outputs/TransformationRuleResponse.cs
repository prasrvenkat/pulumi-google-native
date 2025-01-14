// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Gkebackup.V1.Outputs
{

    /// <summary>
    /// A transformation rule to be applied against Kubernetes resources as they are selected for restoration from a Backup. A rule contains both filtering logic (which resources are subject to transform) and transformation logic.
    /// </summary>
    [OutputType]
    public sealed class TransformationRuleResponse
    {
        /// <summary>
        /// Optional. The description is a user specified string description of the transformation rule.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// A list of transformation rule actions to take against candidate resources. Actions are executed in order defined - this order matters, as they could potentially interfere with each other and the first operation could affect the outcome of the second operation.
        /// </summary>
        public readonly ImmutableArray<Outputs.TransformationRuleActionResponse> FieldActions;
        /// <summary>
        /// Optional. This field is used to specify a set of fields that should be used to determine which resources in backup should be acted upon by the supplied transformation rule actions, and this will ensure that only specific resources are affected by transformation rule actions.
        /// </summary>
        public readonly Outputs.ResourceFilterResponse ResourceFilter;

        [OutputConstructor]
        private TransformationRuleResponse(
            string description,

            ImmutableArray<Outputs.TransformationRuleActionResponse> fieldActions,

            Outputs.ResourceFilterResponse resourceFilter)
        {
            Description = description;
            FieldActions = fieldActions;
            ResourceFilter = resourceFilter;
        }
    }
}
