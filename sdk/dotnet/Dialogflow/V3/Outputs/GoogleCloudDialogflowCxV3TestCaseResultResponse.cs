// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V3.Outputs
{

    /// <summary>
    /// Represents a result from running a test case in an agent environment.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowCxV3TestCaseResultResponse
    {
        /// <summary>
        /// The conversation turns uttered during the test case replay in chronological order.
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleCloudDialogflowCxV3ConversationTurnResponse> ConversationTurns;
        /// <summary>
        /// Environment where the test was run. If not set, it indicates the draft environment.
        /// </summary>
        public readonly string Environment;
        /// <summary>
        /// The resource name for the test case result. Format: `projects//locations//agents//testCases/ /results/`.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Whether the test case passed in the agent environment.
        /// </summary>
        public readonly string TestResult;
        /// <summary>
        /// The time that the test was run.
        /// </summary>
        public readonly string TestTime;

        [OutputConstructor]
        private GoogleCloudDialogflowCxV3TestCaseResultResponse(
            ImmutableArray<Outputs.GoogleCloudDialogflowCxV3ConversationTurnResponse> conversationTurns,

            string environment,

            string name,

            string testResult,

            string testTime)
        {
            ConversationTurns = conversationTurns;
            Environment = environment;
            Name = name;
            TestResult = testResult;
            TestTime = testTime;
        }
    }
}
