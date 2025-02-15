// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Redis.V1Beta1.Inputs
{

    /// <summary>
    /// Time window in which disruptive maintenance updates occur. Non-disruptive updates can occur inside or outside this window.
    /// </summary>
    public sealed class WeeklyMaintenanceWindowArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The day of week that maintenance updates occur.
        /// </summary>
        [Input("day", required: true)]
        public Input<Pulumi.GoogleNative.Redis.V1Beta1.WeeklyMaintenanceWindowDay> Day { get; set; } = null!;

        /// <summary>
        /// Start time of the window in UTC time.
        /// </summary>
        [Input("startTime", required: true)]
        public Input<Inputs.TimeOfDayArgs> StartTime { get; set; } = null!;

        public WeeklyMaintenanceWindowArgs()
        {
        }
        public static new WeeklyMaintenanceWindowArgs Empty => new WeeklyMaintenanceWindowArgs();
    }
}
