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
    /// Defines a reply message to user.
    /// </summary>
    public sealed class GoogleCloudDiscoveryengineV1alphaReplyArgs : global::Pulumi.ResourceArgs
    {
        [Input("references")]
        private InputList<Inputs.GoogleCloudDiscoveryengineV1alphaReplyReferenceArgs>? _references;

        /// <summary>
        /// References in the reply.
        /// </summary>
        public InputList<Inputs.GoogleCloudDiscoveryengineV1alphaReplyReferenceArgs> References
        {
            get => _references ?? (_references = new InputList<Inputs.GoogleCloudDiscoveryengineV1alphaReplyReferenceArgs>());
            set => _references = value;
        }

        /// <summary>
        /// DEPRECATED: use `summary` instead. Text reply.
        /// </summary>
        [Input("reply")]
        public Input<string>? Reply { get; set; }

        /// <summary>
        /// Summary based on search results.
        /// </summary>
        [Input("summary")]
        public Input<Inputs.GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryArgs>? Summary { get; set; }

        public GoogleCloudDiscoveryengineV1alphaReplyArgs()
        {
        }
        public static new GoogleCloudDiscoveryengineV1alphaReplyArgs Empty => new GoogleCloudDiscoveryengineV1alphaReplyArgs();
    }
}
