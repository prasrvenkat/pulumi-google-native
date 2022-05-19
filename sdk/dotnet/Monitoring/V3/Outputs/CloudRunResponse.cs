// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Monitoring.V3.Outputs
{

    /// <summary>
    /// Cloud Run service. Learn more at https://cloud.google.com/run.
    /// </summary>
    [OutputType]
    public sealed class CloudRunResponse
    {
        /// <summary>
        /// The location the service is run. Corresponds to the location resource label in the cloud_run_revision monitored resource: https://cloud.google.com/monitoring/api/resources#tag_cloud_run_revision
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// The name of the Cloud Run service. Corresponds to the service_name resource label in the cloud_run_revision monitored resource: https://cloud.google.com/monitoring/api/resources#tag_cloud_run_revision
        /// </summary>
        public readonly string ServiceName;

        [OutputConstructor]
        private CloudRunResponse(
            string location,

            string serviceName)
        {
            Location = location;
            ServiceName = serviceName;
        }
    }
}