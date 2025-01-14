// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Batch.V1.Inputs
{

    /// <summary>
    /// Represents an NFS volume.
    /// </summary>
    public sealed class NFSArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Remote source path exported from the NFS, e.g., "/share".
        /// </summary>
        [Input("remotePath")]
        public Input<string>? RemotePath { get; set; }

        /// <summary>
        /// The IP address of the NFS.
        /// </summary>
        [Input("server")]
        public Input<string>? Server { get; set; }

        public NFSArgs()
        {
        }
        public static new NFSArgs Empty => new NFSArgs();
    }
}
