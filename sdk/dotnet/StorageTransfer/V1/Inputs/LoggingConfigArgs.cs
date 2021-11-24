// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.StorageTransfer.V1.Inputs
{

    /// <summary>
    /// Logging configuration.
    /// </summary>
    public sealed class LoggingConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enables the Cloud Storage transfer logs for this transfer. This is only supported for transfer jobs with PosixFilesystem sources. The default is that logs are not generated for this transfer.
        /// </summary>
        [Input("enableOnpremGcsTransferLogs")]
        public Input<bool>? EnableOnpremGcsTransferLogs { get; set; }

        [Input("logActionStates")]
        private InputList<Pulumi.GoogleNative.StorageTransfer.V1.LoggingConfigLogActionStatesItem>? _logActionStates;

        /// <summary>
        /// States in which `log_actions` are logged. If empty, no logs are generated. This is not yet supported for transfers with PosixFilesystem data sources.
        /// </summary>
        public InputList<Pulumi.GoogleNative.StorageTransfer.V1.LoggingConfigLogActionStatesItem> LogActionStates
        {
            get => _logActionStates ?? (_logActionStates = new InputList<Pulumi.GoogleNative.StorageTransfer.V1.LoggingConfigLogActionStatesItem>());
            set => _logActionStates = value;
        }

        [Input("logActions")]
        private InputList<Pulumi.GoogleNative.StorageTransfer.V1.LoggingConfigLogActionsItem>? _logActions;

        /// <summary>
        /// Actions to be logged. If empty, no logs are generated. This is not yet supported for transfers with PosixFilesystem data sources.
        /// </summary>
        public InputList<Pulumi.GoogleNative.StorageTransfer.V1.LoggingConfigLogActionsItem> LogActions
        {
            get => _logActions ?? (_logActions = new InputList<Pulumi.GoogleNative.StorageTransfer.V1.LoggingConfigLogActionsItem>());
            set => _logActions = value;
        }

        public LoggingConfigArgs()
        {
        }
    }
}