// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Container.V1Beta1.Outputs
{

    /// <summary>
    /// Parameters that can be configured on Windows nodes. Windows Node Config that define the parameters that will be used to configure the Windows node pool settings
    /// </summary>
    [OutputType]
    public sealed class WindowsNodeConfigResponse
    {
        /// <summary>
        /// OSVersion specifies the Windows node config to be used on the node
        /// </summary>
        public readonly string OsVersion;

        [OutputConstructor]
        private WindowsNodeConfigResponse(string osVersion)
        {
            OsVersion = osVersion;
        }
    }
}