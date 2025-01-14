// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dataplex.V1.Outputs
{

    /// <summary>
    /// Describes the access mechanism of the data within its storage location.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDataplexV1StorageAccessResponse
    {
        /// <summary>
        /// Describes the read access mechanism of the data. Not user settable.
        /// </summary>
        public readonly string Read;

        [OutputConstructor]
        private GoogleCloudDataplexV1StorageAccessResponse(string read)
        {
            Read = read;
        }
    }
}
