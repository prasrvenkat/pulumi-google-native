// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1Beta1.Inputs
{

    /// <summary>
    /// Represents a customer-managed encryption key spec that can be applied to a top-level resource.
    /// </summary>
    public sealed class GoogleCloudAiplatformV1beta1EncryptionSpecArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Cloud KMS resource identifier of the customer managed encryption key used to protect a resource. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created.
        /// </summary>
        [Input("kmsKeyName", required: true)]
        public Input<string> KmsKeyName { get; set; } = null!;

        public GoogleCloudAiplatformV1beta1EncryptionSpecArgs()
        {
        }
        public static new GoogleCloudAiplatformV1beta1EncryptionSpecArgs Empty => new GoogleCloudAiplatformV1beta1EncryptionSpecArgs();
    }
}
