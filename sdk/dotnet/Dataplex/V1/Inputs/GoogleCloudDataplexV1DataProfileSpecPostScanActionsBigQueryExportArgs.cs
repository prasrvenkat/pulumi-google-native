// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dataplex.V1.Inputs
{

    /// <summary>
    /// The configuration of BigQuery export post scan action.
    /// </summary>
    public sealed class GoogleCloudDataplexV1DataProfileSpecPostScanActionsBigQueryExportArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. The BigQuery table to export DataProfileScan results to. Format: //bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID
        /// </summary>
        [Input("resultsTable")]
        public Input<string>? ResultsTable { get; set; }

        public GoogleCloudDataplexV1DataProfileSpecPostScanActionsBigQueryExportArgs()
        {
        }
        public static new GoogleCloudDataplexV1DataProfileSpecPostScanActionsBigQueryExportArgs Empty => new GoogleCloudDataplexV1DataProfileSpecPostScanActionsBigQueryExportArgs();
    }
}
