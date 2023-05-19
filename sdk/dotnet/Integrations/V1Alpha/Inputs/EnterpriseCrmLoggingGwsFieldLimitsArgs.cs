// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Integrations.V1Alpha.Inputs
{

    /// <summary>
    /// Describes string and array limits when writing to logs. When a limit is exceeded the *shortener_type* describes how to shorten the field. next_id: 6
    /// </summary>
    public sealed class EnterpriseCrmLoggingGwsFieldLimitsArgs : global::Pulumi.ResourceArgs
    {
        [Input("logAction")]
        public Input<Pulumi.GoogleNative.Integrations.V1Alpha.EnterpriseCrmLoggingGwsFieldLimitsLogAction>? LogAction { get; set; }

        [Input("logType")]
        private InputList<Pulumi.GoogleNative.Integrations.V1Alpha.EnterpriseCrmLoggingGwsFieldLimitsLogTypeItem>? _logType;

        /// <summary>
        /// To which type(s) of logs the limits apply.
        /// </summary>
        public InputList<Pulumi.GoogleNative.Integrations.V1Alpha.EnterpriseCrmLoggingGwsFieldLimitsLogTypeItem> LogType
        {
            get => _logType ?? (_logType = new InputList<Pulumi.GoogleNative.Integrations.V1Alpha.EnterpriseCrmLoggingGwsFieldLimitsLogTypeItem>());
            set => _logType = value;
        }

        /// <summary>
        /// maximum array size. If the array exceds this size, the field (list) is truncated.
        /// </summary>
        [Input("maxArraySize")]
        public Input<int>? MaxArraySize { get; set; }

        /// <summary>
        /// maximum string length. If the field exceeds this amount the field is shortened.
        /// </summary>
        [Input("maxStringLength")]
        public Input<int>? MaxStringLength { get; set; }

        [Input("shortenerType")]
        public Input<Pulumi.GoogleNative.Integrations.V1Alpha.EnterpriseCrmLoggingGwsFieldLimitsShortenerType>? ShortenerType { get; set; }

        public EnterpriseCrmLoggingGwsFieldLimitsArgs()
        {
        }
        public static new EnterpriseCrmLoggingGwsFieldLimitsArgs Empty => new EnterpriseCrmLoggingGwsFieldLimitsArgs();
    }
}