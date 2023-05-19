// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BigQuery.V2.Inputs
{

    /// <summary>
    /// [Optional] The primary key of the table.
    /// </summary>
    public sealed class TableConstraintsPrimaryKeyArgs : global::Pulumi.ResourceArgs
    {
        [Input("columns")]
        private InputList<string>? _columns;
        public InputList<string> Columns
        {
            get => _columns ?? (_columns = new InputList<string>());
            set => _columns = value;
        }

        public TableConstraintsPrimaryKeyArgs()
        {
        }
        public static new TableConstraintsPrimaryKeyArgs Empty => new TableConstraintsPrimaryKeyArgs();
    }
}