// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.SQLAdmin.V1.Outputs
{

    /// <summary>
    /// Maintenance window. This specifies when a Cloud SQL instance is restarted for system maintenance purposes.
    /// </summary>
    [OutputType]
    public sealed class MaintenanceWindowResponse
    {
        /// <summary>
        /// day of week (1-7), starting on Monday.
        /// </summary>
        public readonly int Day;
        /// <summary>
        /// hour of day - 0 to 23.
        /// </summary>
        public readonly int Hour;
        /// <summary>
        /// This is always `sql#maintenanceWindow`.
        /// </summary>
        public readonly string Kind;
        /// <summary>
        /// Maintenance timing setting: `canary` (Earlier) or `stable` (Later). [Learn more](https://cloud.google.com/sql/docs/mysql/instance-settings#maintenance-timing-2ndgen).
        /// </summary>
        public readonly string UpdateTrack;

        [OutputConstructor]
        private MaintenanceWindowResponse(
            int day,

            int hour,

            string kind,

            string updateTrack)
        {
            Day = day;
            Hour = hour;
            Kind = kind;
            UpdateTrack = updateTrack;
        }
    }
}
