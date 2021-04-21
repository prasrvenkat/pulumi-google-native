// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Storage.V1.Inputs
{

    /// <summary>
    /// The bucket's lifecycle configuration. See lifecycle management for more information.
    /// </summary>
    public sealed class BucketLifecycleArgs : Pulumi.ResourceArgs
    {
        [Input("rule")]
        private InputList<Inputs.BucketRuleItemArgs>? _rule;

        /// <summary>
        /// A lifecycle management rule, which is made of an action to take and the condition(s) under which the action will be taken.
        /// </summary>
        public InputList<Inputs.BucketRuleItemArgs> Rule
        {
            get => _rule ?? (_rule = new InputList<Inputs.BucketRuleItemArgs>());
            set => _rule = value;
        }

        public BucketLifecycleArgs()
        {
        }
    }
}