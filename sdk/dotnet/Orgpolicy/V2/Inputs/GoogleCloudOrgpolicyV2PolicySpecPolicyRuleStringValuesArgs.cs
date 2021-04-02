// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Orgpolicy.V2.Inputs
{

    /// <summary>
    /// A message that holds specific allowed and denied values. This message can define specific values and subtrees of Cloud Resource Manager resource hierarchy (`Organizations`, `Folders`, `Projects`) that are allowed or denied. This is achieved by using the `under:` and optional `is:` prefixes. The `under:` prefix is used to denote resource subtree values. The `is:` prefix is used to denote specific values, and is required only if the value contains a ":". Values prefixed with "is:" are treated the same as values with no prefix. Ancestry subtrees must be in one of the following formats: - "projects/", e.g. "projects/tokyo-rain-123" - "folders/", e.g. "folders/1234" - "organizations/", e.g. "organizations/1234" The `supports_under` field of the associated `Constraint` defines whether ancestry prefixes can be used.
    /// </summary>
    public sealed class GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesArgs : Pulumi.ResourceArgs
    {
        [Input("allowedValues")]
        private InputList<string>? _allowedValues;

        /// <summary>
        /// List of values allowed at this resource.
        /// </summary>
        public InputList<string> AllowedValues
        {
            get => _allowedValues ?? (_allowedValues = new InputList<string>());
            set => _allowedValues = value;
        }

        [Input("deniedValues")]
        private InputList<string>? _deniedValues;

        /// <summary>
        /// List of values denied at this resource.
        /// </summary>
        public InputList<string> DeniedValues
        {
            get => _deniedValues ?? (_deniedValues = new InputList<string>());
            set => _deniedValues = value;
        }

        public GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesArgs()
        {
        }
    }
}