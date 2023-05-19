// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Batch.V1.Inputs
{

    /// <summary>
    /// LifecyclePolicy describes how to deal with task failures based on different conditions.
    /// </summary>
    public sealed class LifecyclePolicyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Action to execute when ActionCondition is true. When RETRY_TASK is specified, we will retry failed tasks if we notice any exit code match and fail tasks if no match is found. Likewise, when FAIL_TASK is specified, we will fail tasks if we notice any exit code match and retry tasks if no match is found.
        /// </summary>
        [Input("action")]
        public Input<Pulumi.GoogleNative.Batch.V1.LifecyclePolicyAction>? Action { get; set; }

        /// <summary>
        /// Conditions that decide why a task failure is dealt with a specific action.
        /// </summary>
        [Input("actionCondition")]
        public Input<Inputs.ActionConditionArgs>? ActionCondition { get; set; }

        public LifecyclePolicyArgs()
        {
        }
        public static new LifecyclePolicyArgs Empty => new LifecyclePolicyArgs();
    }
}