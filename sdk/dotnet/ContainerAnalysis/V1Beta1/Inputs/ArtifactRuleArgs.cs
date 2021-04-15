// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GcpNative.ContainerAnalysis.V1Beta1.Inputs
{

    /// <summary>
    /// Defines an object to declare an in-toto artifact rule
    /// </summary>
    public sealed class ArtifactRuleArgs : Pulumi.ResourceArgs
    {
        [Input("artifactRule")]
        private InputList<string>? _artifactRule;
        public InputList<string> ArtifactRule
        {
            get => _artifactRule ?? (_artifactRule = new InputList<string>());
            set => _artifactRule = value;
        }

        public ArtifactRuleArgs()
        {
        }
    }
}