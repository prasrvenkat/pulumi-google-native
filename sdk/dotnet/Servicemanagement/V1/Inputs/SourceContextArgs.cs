// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Servicemanagement.V1.Inputs
{

    /// <summary>
    /// `SourceContext` represents information about the source of a protobuf element, like the file in which it is defined.
    /// </summary>
    public sealed class SourceContextArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The path-qualified name of the .proto file that contained the associated protobuf element. For example: `"google/protobuf/source_context.proto"`.
        /// </summary>
        [Input("fileName")]
        public Input<string>? FileName { get; set; }

        public SourceContextArgs()
        {
        }
    }
}