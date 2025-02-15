// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Integrations.V1Alpha.Outputs
{

    /// <summary>
    /// The task mock configuration details and assertions for functional tests. Next available id: 5
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudIntegrationsV1alphaTestTaskConfigResponse
    {
        /// <summary>
        /// Optional. List of conditions or expressions which should be evaluated to true unless there is a bug/problem in the integration. These are evaluated one the task execution is completed as per the mock strategy in test case
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleCloudIntegrationsV1alphaAssertionResponse> Assertions;
        /// <summary>
        /// Optional. Defines how to mock the given task during test execution
        /// </summary>
        public readonly Outputs.GoogleCloudIntegrationsV1alphaMockConfigResponse MockConfig;
        /// <summary>
        /// This defines in the test case, the task name in integration which will be mocked by this test task config
        /// </summary>
        public readonly string Task;
        /// <summary>
        /// This defines in the test case, the task in integration which will be mocked by this test task config
        /// </summary>
        public readonly string TaskNumber;

        [OutputConstructor]
        private GoogleCloudIntegrationsV1alphaTestTaskConfigResponse(
            ImmutableArray<Outputs.GoogleCloudIntegrationsV1alphaAssertionResponse> assertions,

            Outputs.GoogleCloudIntegrationsV1alphaMockConfigResponse mockConfig,

            string task,

            string taskNumber)
        {
            Assertions = assertions;
            MockConfig = mockConfig;
            Task = task;
            TaskNumber = taskNumber;
        }
    }
}
