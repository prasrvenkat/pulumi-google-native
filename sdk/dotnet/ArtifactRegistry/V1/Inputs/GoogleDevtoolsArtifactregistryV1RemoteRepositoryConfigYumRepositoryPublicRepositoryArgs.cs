// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ArtifactRegistry.V1.Inputs
{

    /// <summary>
    /// Publicly available Yum repositories constructed from a common repository base and a custom repository path.
    /// </summary>
    public sealed class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepositoryArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A common public repository base for Yum.
        /// </summary>
        [Input("repositoryBase")]
        public Input<Pulumi.GoogleNative.ArtifactRegistry.V1.GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepositoryRepositoryBase>? RepositoryBase { get; set; }

        /// <summary>
        /// A custom field to define a path to a specific repository from the base.
        /// </summary>
        [Input("repositoryPath")]
        public Input<string>? RepositoryPath { get; set; }

        public GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepositoryArgs()
        {
        }
        public static new GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepositoryArgs Empty => new GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepositoryArgs();
    }
}
