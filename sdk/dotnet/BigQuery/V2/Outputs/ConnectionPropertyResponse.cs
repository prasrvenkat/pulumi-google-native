// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BigQuery.V2.Outputs
{

    [OutputType]
    public sealed class ConnectionPropertyResponse
    {
        /// <summary>
        /// [Required] Name of the connection property to set.
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// [Required] Value of the connection property.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private ConnectionPropertyResponse(
            string key,

            string value)
        {
            Key = key;
            Value = value;
        }
    }
}
