// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.CloudBuild.V1.Outputs
{

    /// <summary>
    /// A Maven artifact to upload to Artifact Registry upon successful completion of all build steps.
    /// </summary>
    [OutputType]
    public sealed class MavenArtifactResponse
    {
        /// <summary>
        /// Maven `artifactId` value used when uploading the artifact to Artifact Registry.
        /// </summary>
        public readonly string ArtifactId;
        /// <summary>
        /// Maven `groupId` value used when uploading the artifact to Artifact Registry.
        /// </summary>
        public readonly string GroupId;
        /// <summary>
        /// Path to an artifact in the build's workspace to be uploaded to Artifact Registry. This can be either an absolute path, e.g. /workspace/my-app/target/my-app-1.0.SNAPSHOT.jar or a relative path from /workspace, e.g. my-app/target/my-app-1.0.SNAPSHOT.jar.
        /// </summary>
        public readonly string Path;
        /// <summary>
        /// Artifact Registry repository, in the form "https://$REGION-maven.pkg.dev/$PROJECT/$REPOSITORY" Artifact in the workspace specified by path will be uploaded to Artifact Registry with this location as a prefix.
        /// </summary>
        public readonly string Repository;
        /// <summary>
        /// Maven `version` value used when uploading the artifact to Artifact Registry.
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private MavenArtifactResponse(
            string artifactId,

            string groupId,

            string path,

            string repository,

            string version)
        {
            ArtifactId = artifactId;
            GroupId = groupId;
            Path = path;
            Repository = repository;
            Version = version;
        }
    }
}