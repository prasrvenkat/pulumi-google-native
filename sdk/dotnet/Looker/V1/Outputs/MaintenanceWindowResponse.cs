// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Looker.V1.Outputs
{

    /// <summary>
    /// Specifies the recurring maintenance window.
    /// </summary>
    [OutputType]
    public sealed class MaintenanceWindowResponse
    {
        /// <summary>
        /// Day of the week for this MaintenanceWindow (in UTC).
        /// </summary>
        public readonly string DayOfWeek;
        /// <summary>
        /// Time in UTC when the period starts. Maintenance will be scheduled within 60 minutes.
        /// </summary>
        public readonly Outputs.TimeOfDayResponse StartTime;

        [OutputConstructor]
        private MaintenanceWindowResponse(
            string dayOfWeek,

            Outputs.TimeOfDayResponse startTime)
        {
            DayOfWeek = dayOfWeek;
            StartTime = startTime;
        }
    }
}