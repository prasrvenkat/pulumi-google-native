// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BeyondCorp.V1.Inputs
{

    /// <summary>
    /// PrincipalInfo represents an Identity oneof.
    /// </summary>
    public sealed class GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A GCP service account.
        /// </summary>
        [Input("serviceAccount")]
        public Input<Inputs.GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountArgs>? ServiceAccount { get; set; }

        public GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoArgs()
        {
        }
    }
}