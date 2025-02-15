// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.SQLAdmin.V1.Outputs
{

    /// <summary>
    /// Read-replica configuration for connecting to the primary instance.
    /// </summary>
    [OutputType]
    public sealed class ReplicaConfigurationResponse
    {
        /// <summary>
        /// Optional. Specifies if a SQL Server replica is a cascadable replica. A cascadable replica is a SQL Server cross region replica that supports replica(s) under it.
        /// </summary>
        public readonly bool CascadableReplica;
        /// <summary>
        /// Specifies if the replica is the failover target. If the field is set to `true`, the replica will be designated as a failover replica. In case the primary instance fails, the replica instance will be promoted as the new primary instance. Only one replica can be specified as failover target, and the replica has to be in different zone with the primary instance.
        /// </summary>
        public readonly bool FailoverTarget;
        /// <summary>
        /// This is always `sql#replicaConfiguration`.
        /// </summary>
        public readonly string Kind;
        /// <summary>
        /// MySQL specific configuration when replicating from a MySQL on-premises primary instance. Replication configuration information such as the username, password, certificates, and keys are not stored in the instance metadata. The configuration information is used only to set up the replication connection and is stored by MySQL in a file named `master.info` in the data directory.
        /// </summary>
        public readonly Outputs.MySqlReplicaConfigurationResponse MysqlReplicaConfiguration;

        [OutputConstructor]
        private ReplicaConfigurationResponse(
            bool cascadableReplica,

            bool failoverTarget,

            string kind,

            Outputs.MySqlReplicaConfigurationResponse mysqlReplicaConfiguration)
        {
            CascadableReplica = cascadableReplica;
            FailoverTarget = failoverTarget;
            Kind = kind;
            MysqlReplicaConfiguration = mysqlReplicaConfiguration;
        }
    }
}
