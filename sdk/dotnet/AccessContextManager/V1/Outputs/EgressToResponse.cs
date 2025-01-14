// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AccessContextManager.V1.Outputs
{

    /// <summary>
    /// Defines the conditions under which an EgressPolicy matches a request. Conditions are based on information about the ApiOperation intended to be performed on the `resources` specified. Note that if the destination of the request is also protected by a ServicePerimeter, then that ServicePerimeter must have an IngressPolicy which allows access in order for this request to succeed. The request must match `operations` AND `resources` fields in order to be allowed egress out of the perimeter.
    /// </summary>
    [OutputType]
    public sealed class EgressToResponse
    {
        /// <summary>
        /// A list of external resources that are allowed to be accessed. Only AWS and Azure resources are supported. For Amazon S3, the supported format is s3://BUCKET_NAME. For Azure Storage, the supported format is azure://myaccount.blob.core.windows.net/CONTAINER_NAME. A request matches if it contains an external resource in this list (Example: s3://bucket/path). Currently '*' is not allowed.
        /// </summary>
        public readonly ImmutableArray<string> ExternalResources;
        /// <summary>
        /// A list of ApiOperations allowed to be performed by the sources specified in the corresponding EgressFrom. A request matches if it uses an operation/service in this list.
        /// </summary>
        public readonly ImmutableArray<Outputs.ApiOperationResponse> Operations;
        /// <summary>
        /// A list of resources, currently only projects in the form `projects/`, that are allowed to be accessed by sources defined in the corresponding EgressFrom. A request matches if it contains a resource in this list. If `*` is specified for `resources`, then this EgressTo rule will authorize access to all resources outside the perimeter.
        /// </summary>
        public readonly ImmutableArray<string> Resources;

        [OutputConstructor]
        private EgressToResponse(
            ImmutableArray<string> externalResources,

            ImmutableArray<Outputs.ApiOperationResponse> operations,

            ImmutableArray<string> resources)
        {
            ExternalResources = externalResources;
            Operations = operations;
            Resources = resources;
        }
    }
}
