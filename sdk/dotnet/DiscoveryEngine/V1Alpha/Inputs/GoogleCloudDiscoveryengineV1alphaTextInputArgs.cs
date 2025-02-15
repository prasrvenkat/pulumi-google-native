// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DiscoveryEngine.V1Alpha.Inputs
{

    /// <summary>
    /// Defines text input.
    /// </summary>
    public sealed class GoogleCloudDiscoveryengineV1alphaTextInputArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Conversation context of the input.
        /// </summary>
        [Input("context")]
        public Input<Inputs.GoogleCloudDiscoveryengineV1alphaConversationContextArgs>? Context { get; set; }

        /// <summary>
        /// Text input.
        /// </summary>
        [Input("input")]
        public Input<string>? Input { get; set; }

        public GoogleCloudDiscoveryengineV1alphaTextInputArgs()
        {
        }
        public static new GoogleCloudDiscoveryengineV1alphaTextInputArgs Empty => new GoogleCloudDiscoveryengineV1alphaTextInputArgs();
    }
}
