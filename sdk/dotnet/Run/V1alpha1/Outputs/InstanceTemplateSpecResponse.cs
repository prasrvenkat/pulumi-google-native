// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Run.V1alpha1.Outputs
{

    [OutputType]
    public sealed class InstanceTemplateSpecResponse
    {
        /// <summary>
        /// Optional. Specification of the desired behavior of the instance. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status +optional
        /// </summary>
        public readonly Outputs.InstanceSpecResponse Spec;

        [OutputConstructor]
        private InstanceTemplateSpecResponse(Outputs.InstanceSpecResponse spec)
        {
            Spec = spec;
        }
    }
}