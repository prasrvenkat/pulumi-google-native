// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Containeranalysis.V1alpha1.Inputs
{

    /// <summary>
    /// The Upgrade Distribution represents metadata about the Upgrade for each operating system (CPE). Some distributions have additional metadata around updates, classifying them into various categories and severities.
    /// </summary>
    public sealed class UpgradeDistributionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The operating system classification of this Upgrade, as specified by the upstream operating system upgrade feed.
        /// </summary>
        [Input("classification")]
        public Input<string>? Classification { get; set; }

        /// <summary>
        /// Required - The specific operating system this metadata applies to. See https://cpe.mitre.org/specification/.
        /// </summary>
        [Input("cpeUri")]
        public Input<string>? CpeUri { get; set; }

        [Input("cve")]
        private InputList<string>? _cve;

        /// <summary>
        /// The cve that would be resolved by this upgrade.
        /// </summary>
        public InputList<string> Cve
        {
            get => _cve ?? (_cve = new InputList<string>());
            set => _cve = value;
        }

        /// <summary>
        /// The severity as specified by the upstream operating system.
        /// </summary>
        [Input("severity")]
        public Input<string>? Severity { get; set; }

        public UpgradeDistributionArgs()
        {
        }
    }
}