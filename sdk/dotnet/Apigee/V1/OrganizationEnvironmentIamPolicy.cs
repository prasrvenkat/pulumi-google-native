// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Apigee.V1
{
    /// <summary>
    /// Sets the IAM policy on an environment, if the policy already exists it will be replaced. For more information, see [Manage users, roles, and permissions using the API](https://cloud.google.com/apigee/docs/api-platform/system-administration/manage-users-roles). You must have the `apigee.environments.setIamPolicy` permission to call this API.
    /// </summary>
    [GoogleCloudResourceType("google-cloud:apigee/v1:OrganizationEnvironmentIamPolicy")]
    public partial class OrganizationEnvironmentIamPolicy : Pulumi.CustomResource
    {
        /// <summary>
        /// Specifies cloud audit logging configuration for this policy.
        /// </summary>
        [Output("auditConfigs")]
        public Output<ImmutableArray<Outputs.GoogleIamV1AuditConfigResponse>> AuditConfigs { get; private set; } = null!;

        /// <summary>
        /// Associates a list of `members` to a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one member.
        /// </summary>
        [Output("bindings")]
        public Output<ImmutableArray<Outputs.GoogleIamV1BindingResponse>> Bindings { get; private set; } = null!;

        /// <summary>
        /// `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy. **Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// Specifies the format of the policy. Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected. Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations: * Getting a policy that includes a conditional role binding * Adding a conditional role binding to a policy * Changing a conditional role binding in a policy * Removing any role binding, with or without a condition, from a policy that includes conditions **Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost. If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
        /// </summary>
        [Output("version")]
        public Output<int> Version { get; private set; } = null!;


        /// <summary>
        /// Create a OrganizationEnvironmentIamPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public OrganizationEnvironmentIamPolicy(string name, OrganizationEnvironmentIamPolicyArgs args, CustomResourceOptions? options = null)
            : base("google-cloud:apigee/v1:OrganizationEnvironmentIamPolicy", name, args ?? new OrganizationEnvironmentIamPolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private OrganizationEnvironmentIamPolicy(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-cloud:apigee/v1:OrganizationEnvironmentIamPolicy", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing OrganizationEnvironmentIamPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static OrganizationEnvironmentIamPolicy Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new OrganizationEnvironmentIamPolicy(name, id, options);
        }
    }

    public sealed class OrganizationEnvironmentIamPolicyArgs : Pulumi.ResourceArgs
    {
        [Input("environmentsId", required: true)]
        public Input<string> EnvironmentsId { get; set; } = null!;

        [Input("organizationsId", required: true)]
        public Input<string> OrganizationsId { get; set; } = null!;

        /// <summary>
        /// REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.
        /// </summary>
        [Input("policy")]
        public Input<Inputs.GoogleIamV1PolicyArgs>? Policy { get; set; }

        /// <summary>
        /// OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used: `paths: "bindings, etag"`
        /// </summary>
        [Input("updateMask")]
        public Input<string>? UpdateMask { get; set; }

        public OrganizationEnvironmentIamPolicyArgs()
        {
        }
    }
}