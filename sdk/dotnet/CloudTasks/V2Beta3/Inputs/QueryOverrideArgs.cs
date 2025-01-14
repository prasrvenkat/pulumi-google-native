// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.CloudTasks.V2Beta3.Inputs
{

    /// <summary>
    /// QueryOverride. Query message defines query override for HTTP targets.
    /// </summary>
    public sealed class QueryOverrideArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The query parameters (e.g., qparam1=123&amp;qparam2=456). Default is an empty string.
        /// </summary>
        [Input("queryParams")]
        public Input<string>? QueryParams { get; set; }

        public QueryOverrideArgs()
        {
        }
        public static new QueryOverrideArgs Empty => new QueryOverrideArgs();
    }
}
