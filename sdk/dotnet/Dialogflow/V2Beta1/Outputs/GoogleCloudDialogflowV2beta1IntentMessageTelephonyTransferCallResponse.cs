// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V2Beta1.Outputs
{

    /// <summary>
    /// Transfers the call in Telephony Gateway.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallResponse
    {
        /// <summary>
        /// The phone number to transfer the call to in [E.164 format](https://en.wikipedia.org/wiki/E.164). We currently only allow transferring to US numbers (+1xxxyyyzzzz).
        /// </summary>
        public readonly string PhoneNumber;

        [OutputConstructor]
        private GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCallResponse(string phoneNumber)
        {
            PhoneNumber = phoneNumber;
        }
    }
}
