// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Bigqueryreservation.V1beta1
{
    /// <summary>
    /// Creates an assignment object which allows the given project to submit jobs of a certain type using slots from the specified reservation. Currently a resource (project, folder, organization) can only have one assignment per each (job_type, location) combination, and that reservation will be used for all jobs of the matching type. Different assignments can be created on different levels of the projects, folders or organization hierarchy. During query execution, the assignment is looked up at the project, folder and organization levels in that order. The first assignment found is applied to the query. When creating assignments, it does not matter if other assignments exist at higher levels. Example: * The organization `organizationA` contains two projects, `project1` and `project2`. * Assignments for all three entities (`organizationA`, `project1`, and `project2`) could all be created and mapped to the same or different reservations. "None" assignments represent an absence of the assignment. Projects assigned to None use on-demand pricing. To create a "None" assignment, use "none" as a reservation_id in the parent. Example parent: `projects/myproject/locations/US/reservations/none`. Returns `google.rpc.Code.PERMISSION_DENIED` if user does not have 'bigquery.admin' permissions on the project using the reservation and the project that owns this reservation. Returns `google.rpc.Code.INVALID_ARGUMENT` when location of the assignment does not match location of the reservation.
    /// </summary>
    [GoogleCloudResourceType("google-cloud:bigqueryreservation/v1beta1:ReservationAssignment")]
    public partial class ReservationAssignment : Pulumi.CustomResource
    {
        /// <summary>
        /// Create a ReservationAssignment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ReservationAssignment(string name, ReservationAssignmentArgs args, CustomResourceOptions? options = null)
            : base("google-cloud:bigqueryreservation/v1beta1:ReservationAssignment", name, args ?? new ReservationAssignmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ReservationAssignment(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-cloud:bigqueryreservation/v1beta1:ReservationAssignment", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ReservationAssignment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ReservationAssignment Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ReservationAssignment(name, id, options);
        }
    }

    public sealed class ReservationAssignmentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The resource which will use the reservation. E.g. `projects/myproject`, `folders/123`, or `organizations/456`.
        /// </summary>
        [Input("assignee")]
        public Input<string>? Assignee { get; set; }

        [Input("assignmentsId", required: true)]
        public Input<string> AssignmentsId { get; set; } = null!;

        /// <summary>
        /// Which type of jobs will use the reservation.
        /// </summary>
        [Input("jobType")]
        public Input<string>? JobType { get; set; }

        [Input("locationsId", required: true)]
        public Input<string> LocationsId { get; set; } = null!;

        [Input("projectsId", required: true)]
        public Input<string> ProjectsId { get; set; } = null!;

        [Input("reservationsId", required: true)]
        public Input<string> ReservationsId { get; set; } = null!;

        public ReservationAssignmentArgs()
        {
        }
    }
}