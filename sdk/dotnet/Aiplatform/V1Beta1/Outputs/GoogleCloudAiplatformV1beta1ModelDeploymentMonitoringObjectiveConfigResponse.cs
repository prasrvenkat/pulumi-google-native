// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1Beta1.Outputs
{

    /// <summary>
    /// ModelDeploymentMonitoringObjectiveConfig contains the pair of deployed_model_id to ModelMonitoringObjectiveConfig.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringObjectiveConfigResponse
    {
        /// <summary>
        /// The DeployedModel ID of the objective config.
        /// </summary>
        public readonly string DeployedModelId;
        /// <summary>
        /// The objective config of for the modelmonitoring job of this deployed model.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigResponse ObjectiveConfig;

        [OutputConstructor]
        private GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringObjectiveConfigResponse(
            string deployedModelId,

            Outputs.GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigResponse objectiveConfig)
        {
            DeployedModelId = deployedModelId;
            ObjectiveConfig = objectiveConfig;
        }
    }
}