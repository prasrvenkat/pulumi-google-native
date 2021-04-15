// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GcpNative.GKEHub.V1
{
    /// <summary>
    /// Adds a new Membership.
    /// </summary>
    [GcpNativeResourceType("gcp-native:gkehub/v1:Membership")]
    public partial class Membership : Pulumi.CustomResource
    {
        /// <summary>
        /// Optional. How to identify workloads from this Membership. See the documentation on Workload Identity for more details: https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
        /// </summary>
        [Output("authority")]
        public Output<Outputs.AuthorityResponse> Authority { get; private set; } = null!;

        /// <summary>
        /// When the Membership was created.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// When the Membership was deleted.
        /// </summary>
        [Output("deleteTime")]
        public Output<string> DeleteTime { get; private set; } = null!;

        /// <summary>
        /// Description of this membership, limited to 63 characters. Must match the regex: `a-zA-Z0-9*` This field is present for legacy purposes.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// Optional. Endpoint information to reach this member.
        /// </summary>
        [Output("endpoint")]
        public Output<Outputs.MembershipEndpointResponse> Endpoint { get; private set; } = null!;

        /// <summary>
        /// Optional. An externally-generated and managed ID for this Membership. This ID may be modified after creation, but this is not recommended. The ID must match the regex: `a-zA-Z0-9*` If this Membership represents a Kubernetes cluster, this value should be set to the UID of the `kube-system` namespace object.
        /// </summary>
        [Output("externalId")]
        public Output<string> ExternalId { get; private set; } = null!;

        /// <summary>
        /// Optional. GCP labels for this membership.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        /// <summary>
        /// For clusters using Connect, the timestamp of the most recent connection established with Google Cloud. This time is updated every several minutes, not continuously. For clusters that do not use GKE Connect, or that have never connected successfully, this field will be unset.
        /// </summary>
        [Output("lastConnectionTime")]
        public Output<string> LastConnectionTime { get; private set; } = null!;

        /// <summary>
        /// The full, unique name of this Membership resource in the format `projects/*/locations/*/memberships/{membership_id}`, set during creation. `membership_id` must be a valid RFC 1123 compliant DNS label: 1. At most 63 characters in length 2. It must consist of lower case alphanumeric characters or `-` 3. It must start and end with an alphanumeric character Which can be expressed as the regex: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`, with a maximum length of 63 characters.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// State of the Membership resource.
        /// </summary>
        [Output("state")]
        public Output<Outputs.MembershipStateResponse> State { get; private set; } = null!;

        /// <summary>
        /// Google-generated UUID for this resource. This is unique across all Membership resources. If a Membership resource is deleted and another resource with the same name is created, it gets a different unique_id.
        /// </summary>
        [Output("uniqueId")]
        public Output<string> UniqueId { get; private set; } = null!;

        /// <summary>
        /// When the Membership was last updated.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a Membership resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Membership(string name, MembershipArgs args, CustomResourceOptions? options = null)
            : base("gcp-native:gkehub/v1:Membership", name, args ?? new MembershipArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Membership(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("gcp-native:gkehub/v1:Membership", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Membership resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Membership Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Membership(name, id, options);
        }
    }

    public sealed class MembershipArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. How to identify workloads from this Membership. See the documentation on Workload Identity for more details: https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
        /// </summary>
        [Input("authority")]
        public Input<Inputs.AuthorityArgs>? Authority { get; set; }

        /// <summary>
        /// Optional. Endpoint information to reach this member.
        /// </summary>
        [Input("endpoint")]
        public Input<Inputs.MembershipEndpointArgs>? Endpoint { get; set; }

        /// <summary>
        /// Optional. An externally-generated and managed ID for this Membership. This ID may be modified after creation, but this is not recommended. The ID must match the regex: `a-zA-Z0-9*` If this Membership represents a Kubernetes cluster, this value should be set to the UID of the `kube-system` namespace object.
        /// </summary>
        [Input("externalId")]
        public Input<string>? ExternalId { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Optional. GCP labels for this membership.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("locationsId", required: true)]
        public Input<string> LocationsId { get; set; } = null!;

        [Input("membershipsId", required: true)]
        public Input<string> MembershipsId { get; set; } = null!;

        [Input("projectsId", required: true)]
        public Input<string> ProjectsId { get; set; } = null!;

        public MembershipArgs()
        {
        }
    }
}