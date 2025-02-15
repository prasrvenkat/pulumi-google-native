// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Transcoder.V1.Inputs
{

    /// <summary>
    /// Encoding of a text stream. For example, closed captions or subtitles.
    /// </summary>
    public sealed class TextStreamArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The codec for this text stream. The default is `webvtt`. Supported text codecs: - `srt` - `ttml` - `cea608` - `cea708` - `webvtt`
        /// </summary>
        [Input("codec")]
        public Input<string>? Codec { get; set; }

        /// <summary>
        /// The name for this particular text stream that will be added to the HLS/DASH manifest. Not supported in MP4 files.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// The BCP-47 language code, such as `en-US` or `sr-Latn`. For more information, see https://www.unicode.org/reports/tr35/#Unicode_locale_identifier. Not supported in MP4 files.
        /// </summary>
        [Input("languageCode")]
        public Input<string>? LanguageCode { get; set; }

        [Input("mapping")]
        private InputList<Inputs.TextMappingArgs>? _mapping;

        /// <summary>
        /// The mapping for the JobConfig.edit_list atoms with text EditAtom.inputs.
        /// </summary>
        public InputList<Inputs.TextMappingArgs> Mapping
        {
            get => _mapping ?? (_mapping = new InputList<Inputs.TextMappingArgs>());
            set => _mapping = value;
        }

        public TextStreamArgs()
        {
        }
        public static new TextStreamArgs Empty => new TextStreamArgs();
    }
}
