// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Pubsublite.V1.Outputs
{

    /// <summary>
    /// Configuration for exporting to a Pub/Sub topic.
    /// </summary>
    [OutputType]
    public sealed class PubSubConfigResponse
    {
        /// <summary>
        /// The name of the Pub/Sub topic. Structured like: projects/{project_number}/topics/{topic_id}. The topic may be changed.
        /// </summary>
        public readonly string Topic;

        [OutputConstructor]
        private PubSubConfigResponse(string topic)
        {
            Topic = topic;
        }
    }
}