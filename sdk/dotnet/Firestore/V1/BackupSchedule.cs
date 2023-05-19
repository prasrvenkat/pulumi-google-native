// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Firestore.V1
{
    /// <summary>
    /// Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule with retention up to 7 days and one weekly backup schedule with retention up to 14 weeks.
    /// Auto-naming is currently not supported for this resource.
    /// </summary>
    [GoogleNativeResourceType("google-native:firestore/v1:BackupSchedule")]
    public partial class BackupSchedule : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The timestamp at which this backup schedule was created and effective since. No backups will be created for this schedule before this time.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// For a schedule that runs daily at a specified time.
        /// </summary>
        [Output("dailyRecurrence")]
        public Output<Outputs.GoogleFirestoreAdminV1DailyRecurrenceResponse> DailyRecurrence { get; private set; } = null!;

        [Output("databaseId")]
        public Output<string> DatabaseId { get; private set; } = null!;

        /// <summary>
        /// The unique backup schedule identifier across all locations and databases for the given project. This will be auto-assigned. Format is `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// At what relative time in the future, compared to the creation time of the backup should the backup be deleted, i.e. keep backups for 7 days.
        /// </summary>
        [Output("retention")]
        public Output<string> Retention { get; private set; } = null!;

        /// <summary>
        /// The timestamp at which this backup schedule was most recently updated. When a backup schedule is first created, this is the same as create_time.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;

        /// <summary>
        /// For a schedule that runs weekly on a specific day and time.
        /// </summary>
        [Output("weeklyRecurrence")]
        public Output<Outputs.GoogleFirestoreAdminV1WeeklyRecurrenceResponse> WeeklyRecurrence { get; private set; } = null!;


        /// <summary>
        /// Create a BackupSchedule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BackupSchedule(string name, BackupScheduleArgs args, CustomResourceOptions? options = null)
            : base("google-native:firestore/v1:BackupSchedule", name, args ?? new BackupScheduleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BackupSchedule(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:firestore/v1:BackupSchedule", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "databaseId",
                    "project",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BackupSchedule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BackupSchedule Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new BackupSchedule(name, id, options);
        }
    }

    public sealed class BackupScheduleArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// For a schedule that runs daily at a specified time.
        /// </summary>
        [Input("dailyRecurrence")]
        public Input<Inputs.GoogleFirestoreAdminV1DailyRecurrenceArgs>? DailyRecurrence { get; set; }

        [Input("databaseId", required: true)]
        public Input<string> DatabaseId { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// At what relative time in the future, compared to the creation time of the backup should the backup be deleted, i.e. keep backups for 7 days.
        /// </summary>
        [Input("retention")]
        public Input<string>? Retention { get; set; }

        /// <summary>
        /// For a schedule that runs weekly on a specific day and time.
        /// </summary>
        [Input("weeklyRecurrence")]
        public Input<Inputs.GoogleFirestoreAdminV1WeeklyRecurrenceArgs>? WeeklyRecurrence { get; set; }

        public BackupScheduleArgs()
        {
        }
        public static new BackupScheduleArgs Empty => new BackupScheduleArgs();
    }
}