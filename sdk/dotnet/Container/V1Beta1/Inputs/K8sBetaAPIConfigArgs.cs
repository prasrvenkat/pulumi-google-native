// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Container.V1Beta1.Inputs
{

    /// <summary>
    /// Kubernetes open source beta apis enabled on the cluster.
    /// </summary>
    public sealed class K8sBetaAPIConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("enabledApis")]
        private InputList<string>? _enabledApis;

        /// <summary>
        /// api name, e.g. storage.k8s.io/v1beta1/csistoragecapacities.
        /// </summary>
        public InputList<string> EnabledApis
        {
            get => _enabledApis ?? (_enabledApis = new InputList<string>());
            set => _enabledApis = value;
        }

        public K8sBetaAPIConfigArgs()
        {
        }
        public static new K8sBetaAPIConfigArgs Empty => new K8sBetaAPIConfigArgs();
    }
}