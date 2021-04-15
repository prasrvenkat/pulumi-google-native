// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GcpNative.CloudBuild.V1.Outputs
{

    [OutputType]
    public sealed class BuildStepResponse
    {
        /// <summary>
        /// A list of arguments that will be presented to the step when it is started. If the image used to run the step's container has an entrypoint, the `args` are used as arguments to that entrypoint. If the image does not define an entrypoint, the first element in args is used as the entrypoint, and the remainder will be used as arguments.
        /// </summary>
        public readonly ImmutableArray<string> Args;
        /// <summary>
        /// Working directory to use when running this step's container. If this value is a relative path, it is relative to the build's working directory. If this value is absolute, it may be outside the build's working directory, in which case the contents of the path may not be persisted across build step executions, unless a `volume` for that path is specified. If the build specifies a `RepoSource` with `dir` and a step with a `dir`, which specifies an absolute path, the `RepoSource` `dir` is ignored for the step's execution.
        /// </summary>
        public readonly string Dir;
        /// <summary>
        /// Entrypoint to be used instead of the build step image's default entrypoint. If unset, the image's default entrypoint is used.
        /// </summary>
        public readonly string Entrypoint;
        /// <summary>
        /// A list of environment variable definitions to be used when running a step. The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE".
        /// </summary>
        public readonly ImmutableArray<string> Env;
        /// <summary>
        /// Required. The name of the container image that will run this particular build step. If the image is available in the host's Docker daemon's cache, it will be run directly. If not, the host will attempt to pull the image first, using the builder service account's credentials if necessary. The Docker daemon's cache will already have the latest versions of all of the officially supported build steps ([https://github.com/GoogleCloudPlatform/cloud-builders](https://github.com/GoogleCloudPlatform/cloud-builders)). The Docker daemon will also have cached many of the layers for some popular images, like "ubuntu", "debian", but they will be refreshed at the time you attempt to use them. If you built an image in a previous build step, it will be stored in the host's Docker daemon's cache and is available to use as the name for a later build step.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Stores timing information for pulling this build step's builder image only.
        /// </summary>
        public readonly Outputs.TimeSpanResponse PullTiming;
        /// <summary>
        /// A list of environment variables which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's `Secret`.
        /// </summary>
        public readonly ImmutableArray<string> SecretEnv;
        /// <summary>
        /// Status of the build step. At this time, build step status is only updated on build completion; step status is not updated in real-time as the build progresses.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// Time limit for executing this build step. If not defined, the step has no time limit and will be allowed to continue to run until either it completes or the build itself times out.
        /// </summary>
        public readonly string Timeout;
        /// <summary>
        /// Stores timing information for executing this build step.
        /// </summary>
        public readonly Outputs.TimeSpanResponse Timing;
        /// <summary>
        /// List of volumes to mount into the build step. Each volume is created as an empty volume prior to execution of the build step. Upon completion of the build, volumes and their contents are discarded. Using a named volume in only one step is not valid as it is indicative of a build request with an incorrect configuration.
        /// </summary>
        public readonly ImmutableArray<Outputs.VolumeResponse> Volumes;
        /// <summary>
        /// The ID(s) of the step(s) that this build step depends on. This build step will not start until all the build steps in `wait_for` have completed successfully. If `wait_for` is empty, this build step will start when all previous build steps in the `Build.Steps` list have completed successfully.
        /// </summary>
        public readonly ImmutableArray<string> WaitFor;

        [OutputConstructor]
        private BuildStepResponse(
            ImmutableArray<string> args,

            string dir,

            string entrypoint,

            ImmutableArray<string> env,

            string name,

            Outputs.TimeSpanResponse pullTiming,

            ImmutableArray<string> secretEnv,

            string status,

            string timeout,

            Outputs.TimeSpanResponse timing,

            ImmutableArray<Outputs.VolumeResponse> volumes,

            ImmutableArray<string> waitFor)
        {
            Args = args;
            Dir = dir;
            Entrypoint = entrypoint;
            Env = env;
            Name = name;
            PullTiming = pullTiming;
            SecretEnv = secretEnv;
            Status = status;
            Timeout = timeout;
            Timing = timing;
            Volumes = volumes;
            WaitFor = waitFor;
        }
    }
}