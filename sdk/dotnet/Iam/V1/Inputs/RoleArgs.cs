// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Iam.V1.Inputs
{

    /// <summary>
    /// A role in the Identity and Access Management API.
    /// </summary>
    public sealed class RoleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The current deleted state of the role. This field is read only. It will be ignored in calls to CreateRole and UpdateRole.
        /// </summary>
        [Input("deleted")]
        public Input<bool>? Deleted { get; set; }

        /// <summary>
        /// Optional. A human-readable description for the role.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Used to perform a consistent read-modify-write.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        [Input("includedPermissions")]
        private InputList<string>? _includedPermissions;

        /// <summary>
        /// The names of the permissions this role grants when bound in an IAM policy.
        /// </summary>
        public InputList<string> IncludedPermissions
        {
            get => _includedPermissions ?? (_includedPermissions = new InputList<string>());
            set => _includedPermissions = value;
        }

        /// <summary>
        /// The name of the role. When Role is used in CreateRole, the role name must not be set. When Role is used in output and other input such as UpdateRole, the role name is the complete path, e.g., roles/logging.viewer for predefined roles and organizations/{ORGANIZATION_ID}/roles/logging.viewer for custom roles.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The current launch stage of the role. If the `ALPHA` launch stage has been selected for a role, the `stage` field will not be included in the returned definition for the role.
        /// </summary>
        [Input("stage")]
        public Input<string>? Stage { get; set; }

        /// <summary>
        /// Optional. A human-readable title for the role. Typically this is limited to 100 UTF-8 bytes.
        /// </summary>
        [Input("title")]
        public Input<string>? Title { get; set; }

        public RoleArgs()
        {
        }
    }
}