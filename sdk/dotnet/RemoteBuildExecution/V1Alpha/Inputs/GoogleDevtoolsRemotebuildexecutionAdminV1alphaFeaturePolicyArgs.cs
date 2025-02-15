// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.RemoteBuildExecution.V1Alpha.Inputs
{

    /// <summary>
    /// FeaturePolicy defines features allowed to be used on RBE instances, as well as instance-wide behavior changes that take effect without opt-in or opt-out at usage time.
    /// </summary>
    public sealed class GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Which container image sources are allowed. Currently only RBE-supported registry (gcr.io) is allowed. One can allow all repositories under a project or one specific repository only. E.g. container_image_sources { policy: RESTRICTED allowed_values: [ "gcr.io/project-foo", "gcr.io/project-bar/repo-baz", ] } will allow any repositories under "gcr.io/project-foo" plus the repository "gcr.io/project-bar/repo-baz". Default (UNSPECIFIED) is equivalent to any source is allowed.
        /// </summary>
        [Input("containerImageSources")]
        public Input<Inputs.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeatureArgs>? ContainerImageSources { get; set; }

        /// <summary>
        /// Whether dockerAddCapabilities can be used or what capabilities are allowed.
        /// </summary>
        [Input("dockerAddCapabilities")]
        public Input<Inputs.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeatureArgs>? DockerAddCapabilities { get; set; }

        /// <summary>
        /// Whether dockerChrootPath can be used.
        /// </summary>
        [Input("dockerChrootPath")]
        public Input<Inputs.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeatureArgs>? DockerChrootPath { get; set; }

        /// <summary>
        /// Whether dockerNetwork can be used or what network modes are allowed. E.g. one may allow `off` value only via `allowed_values`.
        /// </summary>
        [Input("dockerNetwork")]
        public Input<Inputs.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeatureArgs>? DockerNetwork { get; set; }

        /// <summary>
        /// Whether dockerPrivileged can be used.
        /// </summary>
        [Input("dockerPrivileged")]
        public Input<Inputs.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeatureArgs>? DockerPrivileged { get; set; }

        /// <summary>
        /// Whether dockerRunAsRoot can be used.
        /// </summary>
        [Input("dockerRunAsRoot")]
        public Input<Inputs.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeatureArgs>? DockerRunAsRoot { get; set; }

        /// <summary>
        /// Whether dockerRuntime is allowed to be set or what runtimes are allowed. Note linux_isolation takes precedence, and if set, docker_runtime values may be rejected if they are incompatible with the selected isolation.
        /// </summary>
        [Input("dockerRuntime")]
        public Input<Inputs.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeatureArgs>? DockerRuntime { get; set; }

        /// <summary>
        /// Whether dockerSiblingContainers can be used.
        /// </summary>
        [Input("dockerSiblingContainers")]
        public Input<Inputs.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeatureArgs>? DockerSiblingContainers { get; set; }

        /// <summary>
        /// linux_isolation allows overriding the docker runtime used for containers started on Linux.
        /// </summary>
        [Input("linuxIsolation")]
        public Input<Pulumi.GoogleNative.RemoteBuildExecution.V1Alpha.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyLinuxIsolation>? LinuxIsolation { get; set; }

        public GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyArgs()
        {
        }
        public static new GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyArgs Empty => new GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyArgs();
    }
}
