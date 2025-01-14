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
    /// Settings for connecting to Git repository for an agent.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowCxV3AgentGitIntegrationSettingsResponse
    {
        /// <summary>
        /// GitHub settings.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowCxV3AgentGitIntegrationSettingsGithubSettingsResponse GithubSettings;

        [OutputConstructor]
        private GoogleCloudDialogflowCxV3AgentGitIntegrationSettingsResponse(Outputs.GoogleCloudDialogflowCxV3AgentGitIntegrationSettingsGithubSettingsResponse githubSettings)
        {
            GithubSettings = githubSettings;
        }
    }
}
