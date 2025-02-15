// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V3Beta1.Outputs
{

    /// <summary>
    /// Settings for connecting to Git repository for an agent.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettingsResponse
    {
        /// <summary>
        /// GitHub settings.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettingsGithubSettingsResponse GithubSettings;

        [OutputConstructor]
        private GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettingsResponse(Outputs.GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettingsGithubSettingsResponse githubSettings)
        {
            GithubSettings = githubSettings;
        }
    }
}
