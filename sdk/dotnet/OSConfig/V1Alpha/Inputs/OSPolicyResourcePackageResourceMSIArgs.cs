// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.OSConfig.V1Alpha.Inputs
{

    /// <summary>
    /// An MSI package. MSI packages only support INSTALLED state.
    /// </summary>
    public sealed class OSPolicyResourcePackageResourceMSIArgs : global::Pulumi.ResourceArgs
    {
        [Input("properties")]
        private InputList<string>? _properties;

        /// <summary>
        /// Additional properties to use during installation. This should be in the format of Property=Setting. Appended to the defaults of `ACTION=INSTALL REBOOT=ReallySuppress`.
        /// </summary>
        public InputList<string> Properties
        {
            get => _properties ?? (_properties = new InputList<string>());
            set => _properties = value;
        }

        /// <summary>
        /// The MSI package.
        /// </summary>
        [Input("source", required: true)]
        public Input<Inputs.OSPolicyResourceFileArgs> Source { get; set; } = null!;

        public OSPolicyResourcePackageResourceMSIArgs()
        {
        }
        public static new OSPolicyResourcePackageResourceMSIArgs Empty => new OSPolicyResourcePackageResourceMSIArgs();
    }
}
