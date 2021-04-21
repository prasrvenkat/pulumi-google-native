// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Storage.V1.Outputs
{

    [OutputType]
    public sealed class BucketRetentionPolicyResponse
    {
        /// <summary>
        /// Server-determined value that indicates the time from which policy was enforced and effective. This value is in RFC 3339 format.
        /// </summary>
        public readonly string EffectiveTime;
        /// <summary>
        /// Once locked, an object retention policy cannot be modified.
        /// </summary>
        public readonly bool IsLocked;
        /// <summary>
        /// The duration in seconds that objects need to be retained. Retention duration must be greater than zero and less than 100 years. Note that enforcement of retention periods less than a day is not guaranteed. Such periods should only be used for testing purposes.
        /// </summary>
        public readonly string RetentionPeriod;

        [OutputConstructor]
        private BucketRetentionPolicyResponse(
            string effectiveTime,

            bool isLocked,

            string retentionPeriod)
        {
            EffectiveTime = effectiveTime;
            IsLocked = isLocked;
            RetentionPeriod = retentionPeriod;
        }
    }
}