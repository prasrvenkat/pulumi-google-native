// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dataproc.V1
{
    /// <summary>
    /// Create an interactive session asynchronously.
    /// </summary>
    [GoogleNativeResourceType("google-native:dataproc/v1:Session")]
    public partial class Session : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The time when the session was created.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// The email address of the user who created the session.
        /// </summary>
        [Output("creator")]
        public Output<string> Creator { get; private set; } = null!;

        /// <summary>
        /// Optional. Environment configuration for the session execution.
        /// </summary>
        [Output("environmentConfig")]
        public Output<Outputs.EnvironmentConfigResponse> EnvironmentConfig { get; private set; } = null!;

        /// <summary>
        /// Optional. Jupyter session config.
        /// </summary>
        [Output("jupyterSession")]
        public Output<Outputs.JupyterConfigResponse> JupyterSession { get; private set; } = null!;

        /// <summary>
        /// Optional. The labels to associate with the session. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The resource name of the session.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// Optional. A unique ID used to identify the request. If the service receives two CreateSessionRequests (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.CreateSessionRequest)s with the same ID, the second request is ignored, and the first Session is created and stored in the backend.Recommendation: Set this value to a UUID (https://en.wikipedia.org/wiki/Universally_unique_identifier).The value must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters.
        /// </summary>
        [Output("requestId")]
        public Output<string?> RequestId { get; private set; } = null!;

        /// <summary>
        /// Optional. Runtime configuration for the session execution.
        /// </summary>
        [Output("runtimeConfig")]
        public Output<Outputs.RuntimeConfigResponse> RuntimeConfig { get; private set; } = null!;

        /// <summary>
        /// Runtime information about session execution.
        /// </summary>
        [Output("runtimeInfo")]
        public Output<Outputs.RuntimeInfoResponse> RuntimeInfo { get; private set; } = null!;

        /// <summary>
        /// Required. The ID to use for the session, which becomes the final component of the session's resource name.This value must be 4-63 characters. Valid characters are /a-z-/.
        /// </summary>
        [Output("sessionId")]
        public Output<string> SessionId { get; private set; } = null!;

        /// <summary>
        /// Optional. The session template used by the session.Only resource names, including project ID and location, are valid.Example: * https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id] * projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id]The template must be in the same project and Dataproc region as the session.
        /// </summary>
        [Output("sessionTemplate")]
        public Output<string> SessionTemplate { get; private set; } = null!;

        /// <summary>
        /// A state of the session.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// Historical state information for the session.
        /// </summary>
        [Output("stateHistory")]
        public Output<ImmutableArray<Outputs.SessionStateHistoryResponse>> StateHistory { get; private set; } = null!;

        /// <summary>
        /// Session state details, such as the failure description if the state is FAILED.
        /// </summary>
        [Output("stateMessage")]
        public Output<string> StateMessage { get; private set; } = null!;

        /// <summary>
        /// The time when the session entered the current state.
        /// </summary>
        [Output("stateTime")]
        public Output<string> StateTime { get; private set; } = null!;

        /// <summary>
        /// Optional. The email address of the user who owns the session.
        /// </summary>
        [Output("user")]
        public Output<string> User { get; private set; } = null!;

        /// <summary>
        /// A session UUID (Unique Universal Identifier). The service generates this value when it creates the session.
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;


        /// <summary>
        /// Create a Session resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Session(string name, SessionArgs args, CustomResourceOptions? options = null)
            : base("google-native:dataproc/v1:Session", name, args ?? new SessionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Session(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:dataproc/v1:Session", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "location",
                    "project",
                    "sessionId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Session resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Session Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Session(name, id, options);
        }
    }

    public sealed class SessionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. Environment configuration for the session execution.
        /// </summary>
        [Input("environmentConfig")]
        public Input<Inputs.EnvironmentConfigArgs>? EnvironmentConfig { get; set; }

        /// <summary>
        /// Optional. Jupyter session config.
        /// </summary>
        [Input("jupyterSession")]
        public Input<Inputs.JupyterConfigArgs>? JupyterSession { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Optional. The labels to associate with the session. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The resource name of the session.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// Optional. A unique ID used to identify the request. If the service receives two CreateSessionRequests (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.CreateSessionRequest)s with the same ID, the second request is ignored, and the first Session is created and stored in the backend.Recommendation: Set this value to a UUID (https://en.wikipedia.org/wiki/Universally_unique_identifier).The value must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters.
        /// </summary>
        [Input("requestId")]
        public Input<string>? RequestId { get; set; }

        /// <summary>
        /// Optional. Runtime configuration for the session execution.
        /// </summary>
        [Input("runtimeConfig")]
        public Input<Inputs.RuntimeConfigArgs>? RuntimeConfig { get; set; }

        /// <summary>
        /// Required. The ID to use for the session, which becomes the final component of the session's resource name.This value must be 4-63 characters. Valid characters are /a-z-/.
        /// </summary>
        [Input("sessionId", required: true)]
        public Input<string> SessionId { get; set; } = null!;

        /// <summary>
        /// Optional. The session template used by the session.Only resource names, including project ID and location, are valid.Example: * https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id] * projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id]The template must be in the same project and Dataproc region as the session.
        /// </summary>
        [Input("sessionTemplate")]
        public Input<string>? SessionTemplate { get; set; }

        /// <summary>
        /// Optional. The email address of the user who owns the session.
        /// </summary>
        [Input("user")]
        public Input<string>? User { get; set; }

        public SessionArgs()
        {
        }
        public static new SessionArgs Empty => new SessionArgs();
    }
}
