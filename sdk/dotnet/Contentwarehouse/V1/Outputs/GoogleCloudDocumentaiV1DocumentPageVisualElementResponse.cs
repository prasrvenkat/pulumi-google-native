// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Contentwarehouse.V1.Outputs
{

    /// <summary>
    /// Detected non-text visual elements e.g. checkbox, signature etc. on the page.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDocumentaiV1DocumentPageVisualElementResponse
    {
        /// <summary>
        /// A list of detected languages together with confidence.
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleCloudDocumentaiV1DocumentPageDetectedLanguageResponse> DetectedLanguages;
        /// <summary>
        /// Layout for VisualElement.
        /// </summary>
        public readonly Outputs.GoogleCloudDocumentaiV1DocumentPageLayoutResponse Layout;
        /// <summary>
        /// Type of the VisualElement.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GoogleCloudDocumentaiV1DocumentPageVisualElementResponse(
            ImmutableArray<Outputs.GoogleCloudDocumentaiV1DocumentPageDetectedLanguageResponse> detectedLanguages,

            Outputs.GoogleCloudDocumentaiV1DocumentPageLayoutResponse layout,

            string type)
        {
            DetectedLanguages = detectedLanguages;
            Layout = layout;
            Type = type;
        }
    }
}
