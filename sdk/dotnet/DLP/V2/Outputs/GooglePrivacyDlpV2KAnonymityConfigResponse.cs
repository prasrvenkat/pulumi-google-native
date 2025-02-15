// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DLP.V2.Outputs
{

    /// <summary>
    /// k-anonymity metric, used for analysis of reidentification risk.
    /// </summary>
    [OutputType]
    public sealed class GooglePrivacyDlpV2KAnonymityConfigResponse
    {
        /// <summary>
        /// Message indicating that multiple rows might be associated to a single individual. If the same entity_id is associated to multiple quasi-identifier tuples over distinct rows, we consider the entire collection of tuples as the composite quasi-identifier. This collection is a multiset: the order in which the different tuples appear in the dataset is ignored, but their frequency is taken into account. Important note: a maximum of 1000 rows can be associated to a single entity ID. If more rows are associated with the same entity ID, some might be ignored.
        /// </summary>
        public readonly Outputs.GooglePrivacyDlpV2EntityIdResponse EntityId;
        /// <summary>
        /// Set of fields to compute k-anonymity over. When multiple fields are specified, they are considered a single composite key. Structs and repeated data types are not supported; however, nested fields are supported so long as they are not structs themselves or nested within a repeated field.
        /// </summary>
        public readonly ImmutableArray<Outputs.GooglePrivacyDlpV2FieldIdResponse> QuasiIds;

        [OutputConstructor]
        private GooglePrivacyDlpV2KAnonymityConfigResponse(
            Outputs.GooglePrivacyDlpV2EntityIdResponse entityId,

            ImmutableArray<Outputs.GooglePrivacyDlpV2FieldIdResponse> quasiIds)
        {
            EntityId = entityId;
            QuasiIds = quasiIds;
        }
    }
}
