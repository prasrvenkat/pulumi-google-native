// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1.Outputs
{

    /// <summary>
    /// Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1ProbeResponse
    {
        /// <summary>
        /// Exec specifies the action to take.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1ProbeExecActionResponse Exec;
        /// <summary>
        /// How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Must be less than timeout_seconds. Maps to Kubernetes probe argument 'periodSeconds'.
        /// </summary>
        public readonly int PeriodSeconds;
        /// <summary>
        /// Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Must be greater or equal to period_seconds. Maps to Kubernetes probe argument 'timeoutSeconds'.
        /// </summary>
        public readonly int TimeoutSeconds;

        [OutputConstructor]
        private GoogleCloudAiplatformV1ProbeResponse(
            Outputs.GoogleCloudAiplatformV1ProbeExecActionResponse exec,

            int periodSeconds,

            int timeoutSeconds)
        {
            Exec = exec;
            PeriodSeconds = periodSeconds;
            TimeoutSeconds = timeoutSeconds;
        }
    }
}
