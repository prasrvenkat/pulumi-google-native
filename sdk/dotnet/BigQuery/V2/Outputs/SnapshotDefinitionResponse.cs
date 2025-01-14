// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BigQuery.V2.Outputs
{

    [OutputType]
    public sealed class SnapshotDefinitionResponse
    {
        /// <summary>
        /// [Required] Reference describing the ID of the table that was snapshot.
        /// </summary>
        public readonly Outputs.TableReferenceResponse BaseTableReference;
        /// <summary>
        /// [Required] The time at which the base table was snapshot. This value is reported in the JSON response using RFC3339 format.
        /// </summary>
        public readonly string SnapshotTime;

        [OutputConstructor]
        private SnapshotDefinitionResponse(
            Outputs.TableReferenceResponse baseTableReference,

            string snapshotTime)
        {
            BaseTableReference = baseTableReference;
            SnapshotTime = snapshotTime;
        }
    }
}
