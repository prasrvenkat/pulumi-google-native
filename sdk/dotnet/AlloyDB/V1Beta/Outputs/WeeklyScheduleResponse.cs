// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AlloyDB.V1Beta.Outputs
{

    /// <summary>
    /// A weekly schedule starts a backup at prescribed start times within a day, for the specified days of the week. The weekly schedule message is flexible and can be used to create many types of schedules. For example, to have a daily backup that starts at 22:00, configure the `start_times` field to have one element "22:00" and the `days_of_week` field to have all seven days of the week.
    /// </summary>
    [OutputType]
    public sealed class WeeklyScheduleResponse
    {
        /// <summary>
        /// The days of the week to perform a backup. If this field is left empty, the default of every day of the week is used.
        /// </summary>
        public readonly ImmutableArray<string> DaysOfWeek;
        /// <summary>
        /// The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00). If no start times are provided, a single fixed start time is chosen arbitrarily.
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleTypeTimeOfDayResponse> StartTimes;

        [OutputConstructor]
        private WeeklyScheduleResponse(
            ImmutableArray<string> daysOfWeek,

            ImmutableArray<Outputs.GoogleTypeTimeOfDayResponse> startTimes)
        {
            DaysOfWeek = daysOfWeek;
            StartTimes = startTimes;
        }
    }
}
