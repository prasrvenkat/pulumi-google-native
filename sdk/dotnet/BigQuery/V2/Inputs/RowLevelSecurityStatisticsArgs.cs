// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GcpNative.BigQuery.V2.Inputs
{

    public sealed class RowLevelSecurityStatisticsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// [Output-only] [Preview] Whether any accessed data was protected by row access policies.
        /// </summary>
        [Input("rowLevelSecurityApplied")]
        public Input<bool>? RowLevelSecurityApplied { get; set; }

        public RowLevelSecurityStatisticsArgs()
        {
        }
    }
}