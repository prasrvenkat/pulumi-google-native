// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ArtifactRegistry.V1.Outputs
{

    /// <summary>
    /// Configuration for a Npm remote repository.
    /// </summary>
    [OutputType]
    public sealed class NpmRepositoryResponse
    {
        /// <summary>
        /// One of the publicly available Npm repositories supported by Artifact Registry.
        /// </summary>
        public readonly string PublicRepository;

        [OutputConstructor]
        private NpmRepositoryResponse(string publicRepository)
        {
            PublicRepository = publicRepository;
        }
    }
}