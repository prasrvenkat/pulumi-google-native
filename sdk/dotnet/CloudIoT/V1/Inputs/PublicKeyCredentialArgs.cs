// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GcpNative.CloudIoT.V1.Inputs
{

    /// <summary>
    /// A public key format and data.
    /// </summary>
    public sealed class PublicKeyCredentialArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The format of the key.
        /// </summary>
        [Input("format")]
        public Input<string>? Format { get; set; }

        /// <summary>
        /// The key data.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        public PublicKeyCredentialArgs()
        {
        }
    }
}