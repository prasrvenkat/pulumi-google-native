// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1Beta1.Outputs
{

    [OutputType]
    public sealed class GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigResponse
    {
        /// <summary>
        /// Email alert config.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigEmailAlertConfigResponse EmailAlertConfig;
        /// <summary>
        /// Dump the anomalies to Cloud Logging. The anomalies will be put to json payload encoded from proto google.cloud.aiplatform.logging.ModelMonitoringAnomaliesLogEntry. This can be further sinked to Pub/Sub or any other services supported by Cloud Logging.
        /// </summary>
        public readonly bool EnableLogging;
        /// <summary>
        /// Resource names of the NotificationChannels to send alert. Must be of the format `projects//notificationChannels/`
        /// </summary>
        public readonly ImmutableArray<string> NotificationChannels;

        [OutputConstructor]
        private GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigResponse(
            Outputs.GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigEmailAlertConfigResponse emailAlertConfig,

            bool enableLogging,

            ImmutableArray<string> notificationChannels)
        {
            EmailAlertConfig = emailAlertConfig;
            EnableLogging = enableLogging;
            NotificationChannels = notificationChannels;
        }
    }
}