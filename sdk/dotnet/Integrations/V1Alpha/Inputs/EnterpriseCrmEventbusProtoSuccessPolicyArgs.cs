// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Integrations.V1Alpha.Inputs
{

    /// <summary>
    /// Policy that dictates the behavior for the task after it completes successfully.
    /// </summary>
    public sealed class EnterpriseCrmEventbusProtoSuccessPolicyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// State to which the execution snapshot status will be set if the task succeeds.
        /// </summary>
        [Input("finalState")]
        public Input<Pulumi.GoogleNative.Integrations.V1Alpha.EnterpriseCrmEventbusProtoSuccessPolicyFinalState>? FinalState { get; set; }

        public EnterpriseCrmEventbusProtoSuccessPolicyArgs()
        {
        }
        public static new EnterpriseCrmEventbusProtoSuccessPolicyArgs Empty => new EnterpriseCrmEventbusProtoSuccessPolicyArgs();
    }
}