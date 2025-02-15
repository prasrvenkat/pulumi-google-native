// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Alpha.Outputs
{

    [OutputType]
    public sealed class SecurityPolicyAdvancedOptionsConfigResponse
    {
        /// <summary>
        /// Custom configuration to apply the JSON parsing. Only applicable when json_parsing is set to STANDARD.
        /// </summary>
        public readonly Outputs.SecurityPolicyAdvancedOptionsConfigJsonCustomConfigResponse JsonCustomConfig;
        public readonly string JsonParsing;
        public readonly string LogLevel;
        /// <summary>
        /// An optional list of case-insensitive request header names to use for resolving the callers client IP address.
        /// </summary>
        public readonly ImmutableArray<string> UserIpRequestHeaders;

        [OutputConstructor]
        private SecurityPolicyAdvancedOptionsConfigResponse(
            Outputs.SecurityPolicyAdvancedOptionsConfigJsonCustomConfigResponse jsonCustomConfig,

            string jsonParsing,

            string logLevel,

            ImmutableArray<string> userIpRequestHeaders)
        {
            JsonCustomConfig = jsonCustomConfig;
            JsonParsing = jsonParsing;
            LogLevel = logLevel;
            UserIpRequestHeaders = userIpRequestHeaders;
        }
    }
}
