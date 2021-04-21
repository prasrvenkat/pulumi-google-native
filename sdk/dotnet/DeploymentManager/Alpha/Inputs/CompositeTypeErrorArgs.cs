// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DeploymentManager.Alpha.Inputs
{

    /// <summary>
    /// [Output Only] If errors are generated during processing of the operation, this field will be populated.
    /// </summary>
    public sealed class CompositeTypeErrorArgs : Pulumi.ResourceArgs
    {
        [Input("errors")]
        private InputList<Inputs.CompositeTypeErrorsItemArgs>? _errors;

        /// <summary>
        /// [Output Only] The array of errors encountered while processing this operation.
        /// </summary>
        public InputList<Inputs.CompositeTypeErrorsItemArgs> Errors
        {
            get => _errors ?? (_errors = new InputList<Inputs.CompositeTypeErrorsItemArgs>());
            set => _errors = value;
        }

        public CompositeTypeErrorArgs()
        {
        }
    }
}