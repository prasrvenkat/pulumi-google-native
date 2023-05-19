// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Gkeonprem.V1.Inputs
{

    /// <summary>
    /// BareMetalAdminStorageConfig specifies the cluster storage configuration.
    /// </summary>
    public sealed class BareMetalAdminStorageConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the config for local PersistentVolumes backed by mounted node disks. These disks need to be formatted and mounted by the user, which can be done before or after cluster creation.
        /// </summary>
        [Input("lvpNodeMountsConfig", required: true)]
        public Input<Inputs.BareMetalLvpConfigArgs> LvpNodeMountsConfig { get; set; } = null!;

        /// <summary>
        /// Specifies the config for local PersistentVolumes backed by subdirectories in a shared filesystem. These subdirectores are automatically created during cluster creation.
        /// </summary>
        [Input("lvpShareConfig", required: true)]
        public Input<Inputs.BareMetalLvpShareConfigArgs> LvpShareConfig { get; set; } = null!;

        public BareMetalAdminStorageConfigArgs()
        {
        }
        public static new BareMetalAdminStorageConfigArgs Empty => new BareMetalAdminStorageConfigArgs();
    }
}