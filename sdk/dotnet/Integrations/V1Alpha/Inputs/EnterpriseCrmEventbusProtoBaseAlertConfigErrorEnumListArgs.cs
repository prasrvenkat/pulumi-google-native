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
    /// List of error enums for alerts.
    /// </summary>
    public sealed class EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListArgs : global::Pulumi.ResourceArgs
    {
        [Input("enumStrings")]
        private InputList<string>? _enumStrings;
        public InputList<string> EnumStrings
        {
            get => _enumStrings ?? (_enumStrings = new InputList<string>());
            set => _enumStrings = value;
        }

        [Input("filterType")]
        public Input<Pulumi.GoogleNative.Integrations.V1Alpha.EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListFilterType>? FilterType { get; set; }

        public EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListArgs()
        {
        }
        public static new EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListArgs Empty => new EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListArgs();
    }
}
