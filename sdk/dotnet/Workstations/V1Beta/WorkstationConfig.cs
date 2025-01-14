// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Workstations.V1Beta
{
    /// <summary>
    /// Creates a new workstation configuration.
    /// </summary>
    [GoogleNativeResourceType("google-native:workstations/v1beta:WorkstationConfig")]
    public partial class WorkstationConfig : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Optional. Client-specified annotations.
        /// </summary>
        [Output("annotations")]
        public Output<ImmutableDictionary<string, string>> Annotations { get; private set; } = null!;

        /// <summary>
        /// Status conditions describing the current resource state.
        /// </summary>
        [Output("conditions")]
        public Output<ImmutableArray<Outputs.StatusResponse>> Conditions { get; private set; } = null!;

        /// <summary>
        /// Optional. Container that runs upon startup for each workstation using this workstation configuration.
        /// </summary>
        [Output("container")]
        public Output<Outputs.ContainerResponse> Container { get; private set; } = null!;

        /// <summary>
        /// Time when this workstation configuration was created.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Whether this resource is degraded, in which case it may require user action to restore full functionality. See also the conditions field.
        /// </summary>
        [Output("degraded")]
        public Output<bool> Degraded { get; private set; } = null!;

        /// <summary>
        /// Time when this workstation configuration was soft-deleted.
        /// </summary>
        [Output("deleteTime")]
        public Output<string> DeleteTime { get; private set; } = null!;

        /// <summary>
        /// Optional. Disables support for plain TCP connections in the workstation. By default the service supports TCP connections via a websocket relay. Setting this option to true disables that relay, which prevents the usage of services that require plain tcp connections, such as ssh. When enabled, all communication must occur over https or wss.
        /// </summary>
        [Output("disableTcpConnections")]
        public Output<bool> DisableTcpConnections { get; private set; } = null!;

        /// <summary>
        /// Optional. Human-readable name for this workstation configuration.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Optional. Whether to enable Linux `auditd` logging on the workstation. When enabled, a service account must also be specified that has `logging.buckets.write` permission on the project. Operating system audit logging is distinct from [Cloud Audit Logs](https://cloud.google.com/workstations/docs/audit-logging).
        /// </summary>
        [Output("enableAuditAgent")]
        public Output<bool> EnableAuditAgent { get; private set; } = null!;

        /// <summary>
        /// Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK). If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata. If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost. If the encryption key is revoked, the workstation session automatically stops within 7 hours. Immutable after the workstation configuration is created.
        /// </summary>
        [Output("encryptionKey")]
        public Output<Outputs.CustomerEncryptionKeyResponse> EncryptionKey { get; private set; } = null!;

        /// <summary>
        /// Optional. Ephemeral directories which won't persist across workstation sessions.
        /// </summary>
        [Output("ephemeralDirectories")]
        public Output<ImmutableArray<Outputs.EphemeralDirectoryResponse>> EphemeralDirectories { get; private set; } = null!;

        /// <summary>
        /// Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// Optional. Runtime host for the workstation.
        /// </summary>
        [Output("host")]
        public Output<Outputs.HostResponse> Host { get; private set; } = null!;

        /// <summary>
        /// Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic. A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).
        /// </summary>
        [Output("idleTimeout")]
        public Output<string> IdleTimeout { get; private set; } = null!;

        /// <summary>
        /// Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// Identifier. Full name of this workstation configuration.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Optional. Directories to persist across workstation sessions.
        /// </summary>
        [Output("persistentDirectories")]
        public Output<ImmutableArray<Outputs.PersistentDirectoryResponse>> PersistentDirectories { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.
        /// </summary>
        [Output("readinessChecks")]
        public Output<ImmutableArray<Outputs.ReadinessCheckResponse>> ReadinessChecks { get; private set; } = null!;

        /// <summary>
        /// Indicates whether this workstation configuration is currently being updated to match its intended state.
        /// </summary>
        [Output("reconciling")]
        public Output<bool> Reconciling { get; private set; } = null!;

        /// <summary>
        /// Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used. Immutable after the workstation configuration is created.
        /// </summary>
        [Output("replicaZones")]
        public Output<ImmutableArray<string>> ReplicaZones { get; private set; } = null!;

        /// <summary>
        /// Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle. Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours). Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.
        /// </summary>
        [Output("runningTimeout")]
        public Output<string> RunningTimeout { get; private set; } = null!;

        /// <summary>
        /// A system-assigned unique identifier for this workstation configuration.
        /// </summary>
        [Output("uid")]
        public Output<string> Uid { get; private set; } = null!;

        /// <summary>
        /// Time when this workstation configuration was most recently updated.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;

        [Output("workstationClusterId")]
        public Output<string> WorkstationClusterId { get; private set; } = null!;

        /// <summary>
        /// Required. ID to use for the workstation configuration.
        /// </summary>
        [Output("workstationConfigId")]
        public Output<string> WorkstationConfigId { get; private set; } = null!;


        /// <summary>
        /// Create a WorkstationConfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public WorkstationConfig(string name, WorkstationConfigArgs args, CustomResourceOptions? options = null)
            : base("google-native:workstations/v1beta:WorkstationConfig", name, args ?? new WorkstationConfigArgs(), MakeResourceOptions(options, ""))
        {
        }

        private WorkstationConfig(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:workstations/v1beta:WorkstationConfig", name, null, MakeResourceOptions(options, id))
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
                    "workstationClusterId",
                    "workstationConfigId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing WorkstationConfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static WorkstationConfig Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new WorkstationConfig(name, id, options);
        }
    }

    public sealed class WorkstationConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("annotations")]
        private InputMap<string>? _annotations;

        /// <summary>
        /// Optional. Client-specified annotations.
        /// </summary>
        public InputMap<string> Annotations
        {
            get => _annotations ?? (_annotations = new InputMap<string>());
            set => _annotations = value;
        }

        /// <summary>
        /// Optional. Container that runs upon startup for each workstation using this workstation configuration.
        /// </summary>
        [Input("container")]
        public Input<Inputs.ContainerArgs>? Container { get; set; }

        /// <summary>
        /// Optional. Disables support for plain TCP connections in the workstation. By default the service supports TCP connections via a websocket relay. Setting this option to true disables that relay, which prevents the usage of services that require plain tcp connections, such as ssh. When enabled, all communication must occur over https or wss.
        /// </summary>
        [Input("disableTcpConnections")]
        public Input<bool>? DisableTcpConnections { get; set; }

        /// <summary>
        /// Optional. Human-readable name for this workstation configuration.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Optional. Whether to enable Linux `auditd` logging on the workstation. When enabled, a service account must also be specified that has `logging.buckets.write` permission on the project. Operating system audit logging is distinct from [Cloud Audit Logs](https://cloud.google.com/workstations/docs/audit-logging).
        /// </summary>
        [Input("enableAuditAgent")]
        public Input<bool>? EnableAuditAgent { get; set; }

        /// <summary>
        /// Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK). If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata. If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost. If the encryption key is revoked, the workstation session automatically stops within 7 hours. Immutable after the workstation configuration is created.
        /// </summary>
        [Input("encryptionKey")]
        public Input<Inputs.CustomerEncryptionKeyArgs>? EncryptionKey { get; set; }

        [Input("ephemeralDirectories")]
        private InputList<Inputs.EphemeralDirectoryArgs>? _ephemeralDirectories;

        /// <summary>
        /// Optional. Ephemeral directories which won't persist across workstation sessions.
        /// </summary>
        public InputList<Inputs.EphemeralDirectoryArgs> EphemeralDirectories
        {
            get => _ephemeralDirectories ?? (_ephemeralDirectories = new InputList<Inputs.EphemeralDirectoryArgs>());
            set => _ephemeralDirectories = value;
        }

        /// <summary>
        /// Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// Optional. Runtime host for the workstation.
        /// </summary>
        [Input("host")]
        public Input<Inputs.HostArgs>? Host { get; set; }

        /// <summary>
        /// Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic. A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).
        /// </summary>
        [Input("idleTimeout")]
        public Input<string>? IdleTimeout { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Identifier. Full name of this workstation configuration.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("persistentDirectories")]
        private InputList<Inputs.PersistentDirectoryArgs>? _persistentDirectories;

        /// <summary>
        /// Optional. Directories to persist across workstation sessions.
        /// </summary>
        public InputList<Inputs.PersistentDirectoryArgs> PersistentDirectories
        {
            get => _persistentDirectories ?? (_persistentDirectories = new InputList<Inputs.PersistentDirectoryArgs>());
            set => _persistentDirectories = value;
        }

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("readinessChecks")]
        private InputList<Inputs.ReadinessCheckArgs>? _readinessChecks;

        /// <summary>
        /// Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.
        /// </summary>
        public InputList<Inputs.ReadinessCheckArgs> ReadinessChecks
        {
            get => _readinessChecks ?? (_readinessChecks = new InputList<Inputs.ReadinessCheckArgs>());
            set => _readinessChecks = value;
        }

        [Input("replicaZones")]
        private InputList<string>? _replicaZones;

        /// <summary>
        /// Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used. Immutable after the workstation configuration is created.
        /// </summary>
        public InputList<string> ReplicaZones
        {
            get => _replicaZones ?? (_replicaZones = new InputList<string>());
            set => _replicaZones = value;
        }

        /// <summary>
        /// Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle. Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours). Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.
        /// </summary>
        [Input("runningTimeout")]
        public Input<string>? RunningTimeout { get; set; }

        [Input("workstationClusterId", required: true)]
        public Input<string> WorkstationClusterId { get; set; } = null!;

        /// <summary>
        /// Required. ID to use for the workstation configuration.
        /// </summary>
        [Input("workstationConfigId", required: true)]
        public Input<string> WorkstationConfigId { get; set; } = null!;

        public WorkstationConfigArgs()
        {
        }
        public static new WorkstationConfigArgs Empty => new WorkstationConfigArgs();
    }
}
