// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Testing.V1.Inputs
{

    /// <summary>
    /// A set of Android device configuration permutations is defined by the the cross-product of the given axes. Internally, the given AndroidMatrix will be expanded into a set of AndroidDevices. Only supported permutations will be instantiated. Invalid permutations (e.g., incompatible models/versions) are ignored.
    /// </summary>
    public sealed class AndroidMatrixArgs : Pulumi.ResourceArgs
    {
        [Input("androidModelIds")]
        private InputList<string>? _androidModelIds;

        /// <summary>
        /// Required. The ids of the set of Android device to be used. Use the TestEnvironmentDiscoveryService to get supported options.
        /// </summary>
        public InputList<string> AndroidModelIds
        {
            get => _androidModelIds ?? (_androidModelIds = new InputList<string>());
            set => _androidModelIds = value;
        }

        [Input("androidVersionIds")]
        private InputList<string>? _androidVersionIds;

        /// <summary>
        /// Required. The ids of the set of Android OS version to be used. Use the TestEnvironmentDiscoveryService to get supported options.
        /// </summary>
        public InputList<string> AndroidVersionIds
        {
            get => _androidVersionIds ?? (_androidVersionIds = new InputList<string>());
            set => _androidVersionIds = value;
        }

        [Input("locales")]
        private InputList<string>? _locales;

        /// <summary>
        /// Required. The set of locales the test device will enable for testing. Use the TestEnvironmentDiscoveryService to get supported options.
        /// </summary>
        public InputList<string> Locales
        {
            get => _locales ?? (_locales = new InputList<string>());
            set => _locales = value;
        }

        [Input("orientations")]
        private InputList<string>? _orientations;

        /// <summary>
        /// Required. The set of orientations to test with. Use the TestEnvironmentDiscoveryService to get supported options.
        /// </summary>
        public InputList<string> Orientations
        {
            get => _orientations ?? (_orientations = new InputList<string>());
            set => _orientations = value;
        }

        public AndroidMatrixArgs()
        {
        }
    }
}