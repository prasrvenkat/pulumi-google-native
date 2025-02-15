// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AssuredWorkloads.V1Beta1.Outputs
{

    /// <summary>
    /// Settings specific to resources needed for CJIS.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettingsResponse
    {
        /// <summary>
        /// Input only. Immutable. Settings used to create a CMEK crypto key.
        /// </summary>
        public readonly Outputs.GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse KmsSettings;

        [OutputConstructor]
        private GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettingsResponse(Outputs.GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse kmsSettings)
        {
            KmsSettings = kmsSettings;
        }
    }
}
