// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.TPU.V2Alpha1.Inputs
{

    /// <summary>
    /// Boot disk configurations.
    /// </summary>
    public sealed class BootDiskConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. Customer encryption key for boot disk.
        /// </summary>
        [Input("customerEncryptionKey")]
        public Input<Inputs.CustomerEncryptionKeyArgs>? CustomerEncryptionKey { get; set; }

        /// <summary>
        /// Optional. Whether the boot disk will be created with confidential compute mode.
        /// </summary>
        [Input("enableConfidentialCompute")]
        public Input<bool>? EnableConfidentialCompute { get; set; }

        public BootDiskConfigArgs()
        {
        }
        public static new BootDiskConfigArgs Empty => new BootDiskConfigArgs();
    }
}
