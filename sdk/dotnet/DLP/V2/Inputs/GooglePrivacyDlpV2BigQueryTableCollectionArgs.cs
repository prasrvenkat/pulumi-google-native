// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DLP.V2.Inputs
{

    /// <summary>
    /// Specifies a collection of BigQuery tables. Used for Discovery.
    /// </summary>
    public sealed class GooglePrivacyDlpV2BigQueryTableCollectionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A collection of regular expressions to match a BigQuery table against.
        /// </summary>
        [Input("includeRegexes")]
        public Input<Inputs.GooglePrivacyDlpV2BigQueryRegexesArgs>? IncludeRegexes { get; set; }

        public GooglePrivacyDlpV2BigQueryTableCollectionArgs()
        {
        }
        public static new GooglePrivacyDlpV2BigQueryTableCollectionArgs Empty => new GooglePrivacyDlpV2BigQueryTableCollectionArgs();
    }
}