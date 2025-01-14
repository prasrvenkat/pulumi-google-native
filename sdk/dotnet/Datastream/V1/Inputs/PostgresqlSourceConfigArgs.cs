// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Datastream.V1.Inputs
{

    /// <summary>
    /// PostgreSQL data source configuration
    /// </summary>
    public sealed class PostgresqlSourceConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// PostgreSQL objects to exclude from the stream.
        /// </summary>
        [Input("excludeObjects")]
        public Input<Inputs.PostgresqlRdbmsArgs>? ExcludeObjects { get; set; }

        /// <summary>
        /// PostgreSQL objects to include in the stream.
        /// </summary>
        [Input("includeObjects")]
        public Input<Inputs.PostgresqlRdbmsArgs>? IncludeObjects { get; set; }

        /// <summary>
        /// Maximum number of concurrent backfill tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used.
        /// </summary>
        [Input("maxConcurrentBackfillTasks")]
        public Input<int>? MaxConcurrentBackfillTasks { get; set; }

        /// <summary>
        /// The name of the publication that includes the set of all tables that are defined in the stream's include_objects.
        /// </summary>
        [Input("publication", required: true)]
        public Input<string> Publication { get; set; } = null!;

        /// <summary>
        /// Immutable. The name of the logical replication slot that's configured with the pgoutput plugin.
        /// </summary>
        [Input("replicationSlot", required: true)]
        public Input<string> ReplicationSlot { get; set; } = null!;

        public PostgresqlSourceConfigArgs()
        {
        }
        public static new PostgresqlSourceConfigArgs Empty => new PostgresqlSourceConfigArgs();
    }
}
