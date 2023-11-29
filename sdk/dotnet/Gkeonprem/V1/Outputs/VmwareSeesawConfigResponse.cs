// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Gkeonprem.V1.Outputs
{

    /// <summary>
    /// VmwareSeesawConfig represents configuration parameters for an already existing Seesaw load balancer. IMPORTANT: Please note that the Anthos On-Prem API will not generate or update Seesaw configurations it can only bind a pre-existing configuration to a new user cluster. IMPORTANT: When attempting to create a user cluster with a pre-existing Seesaw load balancer you will need to follow some preparation steps before calling the 'CreateVmwareCluster' API method. First you will need to create the user cluster's namespace via kubectl. The namespace will need to use the following naming convention : -gke-onprem-mgmt or -gke-onprem-mgmt depending on whether you used the 'VmwareCluster.local_name' to disambiguate collisions; for more context see the documentation of 'VmwareCluster.local_name'. Once the namespace is created you will need to create a secret resource via kubectl. This secret will contain copies of your Seesaw credentials. The Secret must be called 'user-cluster-creds' and contain Seesaw's SSH and Cert credentials. The credentials must be keyed with the following names: 'seesaw-ssh-private-key', 'seesaw-ssh-public-key', 'seesaw-ssh-ca-key', 'seesaw-ssh-ca-cert'.
    /// </summary>
    [OutputType]
    public sealed class VmwareSeesawConfigResponse
    {
        /// <summary>
        /// Enable two load balancer VMs to achieve a highly-available Seesaw load balancer.
        /// </summary>
        public readonly bool EnableHa;
        /// <summary>
        /// In general the following format should be used for the Seesaw group name: seesaw-for-[cluster_name].
        /// </summary>
        public readonly string Group;
        /// <summary>
        /// The IP Blocks to be used by the Seesaw load balancer
        /// </summary>
        public readonly ImmutableArray<Outputs.VmwareIpBlockResponse> IpBlocks;
        /// <summary>
        /// MasterIP is the IP announced by the master of Seesaw group.
        /// </summary>
        public readonly string MasterIp;
        /// <summary>
        /// Name to be used by Stackdriver.
        /// </summary>
        public readonly string StackdriverName;
        /// <summary>
        /// Names of the VMs created for this Seesaw group.
        /// </summary>
        public readonly ImmutableArray<string> Vms;

        [OutputConstructor]
        private VmwareSeesawConfigResponse(
            bool enableHa,

            string group,

            ImmutableArray<Outputs.VmwareIpBlockResponse> ipBlocks,

            string masterIp,

            string stackdriverName,

            ImmutableArray<string> vms)
        {
            EnableHa = enableHa;
            Group = group;
            IpBlocks = ipBlocks;
            MasterIp = masterIp;
            StackdriverName = stackdriverName;
            Vms = vms;
        }
    }
}