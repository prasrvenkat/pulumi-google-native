// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Securitycenter.V1.Inputs
{

    /// <summary>
    /// Resource for selecting resource type.
    /// </summary>
    public sealed class GoogleCloudSecuritycenterV1ResourceSelectorArgs : global::Pulumi.ResourceArgs
    {
        [Input("resourceTypes")]
        private InputList<string>? _resourceTypes;

        /// <summary>
        /// The resource types to run the detector on.
        /// </summary>
        public InputList<string> ResourceTypes
        {
            get => _resourceTypes ?? (_resourceTypes = new InputList<string>());
            set => _resourceTypes = value;
        }

        public GoogleCloudSecuritycenterV1ResourceSelectorArgs()
        {
        }
        public static new GoogleCloudSecuritycenterV1ResourceSelectorArgs Empty => new GoogleCloudSecuritycenterV1ResourceSelectorArgs();
    }
}