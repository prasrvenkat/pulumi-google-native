// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Bigquery.V2.Inputs
{

    public sealed class JobStatisticsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// [TrustedTester] [Output-only] Job progress (0.0 -&gt; 1.0) for LOAD and EXTRACT jobs.
        /// </summary>
        [Input("completionRatio")]
        public Input<double>? CompletionRatio { get; set; }

        /// <summary>
        /// [Output-only] Creation time of this job, in milliseconds since the epoch. This field will be present on all jobs.
        /// </summary>
        [Input("creationTime")]
        public Input<string>? CreationTime { get; set; }

        /// <summary>
        /// [Output-only] End time of this job, in milliseconds since the epoch. This field will be present whenever a job is in the DONE state.
        /// </summary>
        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        /// <summary>
        /// [Output-only] Statistics for an extract job.
        /// </summary>
        [Input("extract")]
        public Input<Inputs.JobStatistics4Args>? Extract { get; set; }

        /// <summary>
        /// [Output-only] Statistics for a load job.
        /// </summary>
        [Input("load")]
        public Input<Inputs.JobStatistics3Args>? Load { get; set; }

        /// <summary>
        /// [Output-only] Number of child jobs executed.
        /// </summary>
        [Input("numChildJobs")]
        public Input<string>? NumChildJobs { get; set; }

        /// <summary>
        /// [Output-only] If this is a child job, the id of the parent.
        /// </summary>
        [Input("parentJobId")]
        public Input<string>? ParentJobId { get; set; }

        /// <summary>
        /// [Output-only] Statistics for a query job.
        /// </summary>
        [Input("query")]
        public Input<Inputs.JobStatistics2Args>? Query { get; set; }

        [Input("quotaDeferments")]
        private InputList<string>? _quotaDeferments;

        /// <summary>
        /// [Output-only] Quotas which delayed this job's start time.
        /// </summary>
        public InputList<string> QuotaDeferments
        {
            get => _quotaDeferments ?? (_quotaDeferments = new InputList<string>());
            set => _quotaDeferments = value;
        }

        [Input("reservationUsage")]
        private InputList<ImmutableDictionary<string, string>>? _reservationUsage;

        /// <summary>
        /// [Output-only] Job resource usage breakdown by reservation.
        /// </summary>
        public InputList<ImmutableDictionary<string, string>> ReservationUsage
        {
            get => _reservationUsage ?? (_reservationUsage = new InputList<ImmutableDictionary<string, string>>());
            set => _reservationUsage = value;
        }

        /// <summary>
        /// [Output-only] Name of the primary reservation assigned to this job. Note that this could be different than reservations reported in the reservation usage field if parent reservations were used to execute this job.
        /// </summary>
        [Input("reservation_id")]
        public Input<string>? Reservation_id { get; set; }

        /// <summary>
        /// [Output-only] [Preview] Statistics for row-level security. Present only for query and extract jobs.
        /// </summary>
        [Input("rowLevelSecurityStatistics")]
        public Input<Inputs.RowLevelSecurityStatisticsArgs>? RowLevelSecurityStatistics { get; set; }

        /// <summary>
        /// [Output-only] Statistics for a child job of a script.
        /// </summary>
        [Input("scriptStatistics")]
        public Input<Inputs.ScriptStatisticsArgs>? ScriptStatistics { get; set; }

        /// <summary>
        /// [Output-only] [Preview] Information of the session if this job is part of one.
        /// </summary>
        [Input("sessionInfoTemplate")]
        public Input<Inputs.SessionInfoArgs>? SessionInfoTemplate { get; set; }

        /// <summary>
        /// [Output-only] Start time of this job, in milliseconds since the epoch. This field will be present when the job transitions from the PENDING state to either RUNNING or DONE.
        /// </summary>
        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        /// <summary>
        /// [Output-only] [Deprecated] Use the bytes processed in the query statistics instead.
        /// </summary>
        [Input("totalBytesProcessed")]
        public Input<string>? TotalBytesProcessed { get; set; }

        /// <summary>
        /// [Output-only] Slot-milliseconds for the job.
        /// </summary>
        [Input("totalSlotMs")]
        public Input<string>? TotalSlotMs { get; set; }

        /// <summary>
        /// [Output-only] [Alpha] Information of the multi-statement transaction if this job is part of one.
        /// </summary>
        [Input("transactionInfoTemplate")]
        public Input<Inputs.TransactionInfoArgs>? TransactionInfoTemplate { get; set; }

        public JobStatisticsArgs()
        {
        }
    }
}