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
    /// Artifacts produced by a build that should be uploaded upon successful completion of all build steps.
    /// </summary>
    [OutputType]
    public sealed class ArtifactsResponse
    {
        /// <summary>
        /// A list of images to be pushed upon the successful completion of all build steps. The images will be pushed using the builder service account's credentials. The digests of the pushed images will be stored in the Build resource's results field. If any of the images fail to be pushed, the build is marked FAILURE.
        /// </summary>
        public readonly ImmutableArray<string> Images;
        /// <summary>
        /// A list of Maven artifacts to be uploaded to Artifact Registry upon successful completion of all build steps. Artifacts in the workspace matching specified paths globs will be uploaded to the specified Artifact Registry repository using the builder service account's credentials. If any artifacts fail to be pushed, the build is marked FAILURE.
        /// </summary>
        public readonly ImmutableArray<Outputs.MavenArtifactResponse> MavenArtifacts;
        /// <summary>
        /// A list of npm packages to be uploaded to Artifact Registry upon successful completion of all build steps. Npm packages in the specified paths will be uploaded to the specified Artifact Registry repository using the builder service account's credentials. If any packages fail to be pushed, the build is marked FAILURE.
        /// </summary>
        public readonly ImmutableArray<Outputs.NpmPackageResponse> NpmPackages;
        /// <summary>
        /// A list of objects to be uploaded to Cloud Storage upon successful completion of all build steps. Files in the workspace matching specified paths globs will be uploaded to the specified Cloud Storage location using the builder service account's credentials. The location and generation of the uploaded objects will be stored in the Build resource's results field. If any objects fail to be pushed, the build is marked FAILURE.
        /// </summary>
        public readonly Outputs.ArtifactObjectsResponse Objects;
        /// <summary>
        /// A list of Python packages to be uploaded to Artifact Registry upon successful completion of all build steps. The build service account credentials will be used to perform the upload. If any objects fail to be pushed, the build is marked FAILURE.
        /// </summary>
        public readonly ImmutableArray<Outputs.PythonPackageResponse> PythonPackages;

        [OutputConstructor]
        private ArtifactsResponse(
            ImmutableArray<string> images,

            ImmutableArray<Outputs.MavenArtifactResponse> mavenArtifacts,

            ImmutableArray<Outputs.NpmPackageResponse> npmPackages,

            Outputs.ArtifactObjectsResponse objects,

            ImmutableArray<Outputs.PythonPackageResponse> pythonPackages)
        {
            Images = images;
            MavenArtifacts = mavenArtifacts;
            NpmPackages = npmPackages;
            Objects = objects;
            PythonPackages = pythonPackages;
        }
    }
}
