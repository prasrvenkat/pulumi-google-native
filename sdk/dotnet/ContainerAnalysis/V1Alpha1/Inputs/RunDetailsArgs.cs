// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ContainerAnalysis.V1Alpha1.Inputs
{

    public sealed class RunDetailsArgs : global::Pulumi.ResourceArgs
    {
        [Input("builder")]
        public Input<Inputs.ProvenanceBuilderArgs>? Builder { get; set; }

        [Input("byproducts")]
        private InputList<Inputs.ResourceDescriptorArgs>? _byproducts;
        public InputList<Inputs.ResourceDescriptorArgs> Byproducts
        {
            get => _byproducts ?? (_byproducts = new InputList<Inputs.ResourceDescriptorArgs>());
            set => _byproducts = value;
        }

        [Input("metadata")]
        public Input<Inputs.BuildMetadataArgs>? Metadata { get; set; }

        public RunDetailsArgs()
        {
        }
        public static new RunDetailsArgs Empty => new RunDetailsArgs();
    }
}
