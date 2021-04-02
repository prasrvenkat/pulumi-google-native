// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Cloudfunctions.V1.Outputs
{

    [OutputType]
    public sealed class HttpsTriggerResponse
    {
        /// <summary>
        /// The security level for the function.
        /// </summary>
        public readonly string SecurityLevel;
        /// <summary>
        /// The deployed url for the function.
        /// </summary>
        public readonly string Url;

        [OutputConstructor]
        private HttpsTriggerResponse(
            string securityLevel,

            string url)
        {
            SecurityLevel = securityLevel;
            Url = url;
        }
    }
}