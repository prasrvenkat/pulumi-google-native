// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DLP.V2.Outputs
{

    /// <summary>
    /// A type of transformation that is applied over images.
    /// </summary>
    [OutputType]
    public sealed class GooglePrivacyDlpV2ImageTransformationsResponse
    {
        public readonly ImmutableArray<Outputs.GooglePrivacyDlpV2ImageTransformationResponse> Transforms;

        [OutputConstructor]
        private GooglePrivacyDlpV2ImageTransformationsResponse(ImmutableArray<Outputs.GooglePrivacyDlpV2ImageTransformationResponse> transforms)
        {
            Transforms = transforms;
        }
    }
}