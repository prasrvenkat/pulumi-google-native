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
    /// Configuration for an Apt remote repository.
    /// </summary>
    public sealed class AptRepositoryArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// One of the publicly available Apt repositories supported by Artifact Registry.
        /// </summary>
        [Input("publicRepository")]
        public Input<Inputs.GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepositoryArgs>? PublicRepository { get; set; }

        public AptRepositoryArgs()
        {
        }
        public static new AptRepositoryArgs Empty => new AptRepositoryArgs();
    }
}