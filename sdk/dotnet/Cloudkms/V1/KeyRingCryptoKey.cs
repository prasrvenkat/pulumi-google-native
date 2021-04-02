// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Cloudkms.V1
{
    /// <summary>
    /// Create a new CryptoKey within a KeyRing. CryptoKey.purpose and CryptoKey.version_template.algorithm are required.
    /// </summary>
    [GoogleCloudResourceType("google-cloud:cloudkms/v1:KeyRingCryptoKey")]
    public partial class KeyRingCryptoKey : Pulumi.CustomResource
    {
        /// <summary>
        /// The time at which this CryptoKey was created.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys).
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        /// <summary>
        /// The resource name for this CryptoKey in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*`.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// At next_rotation_time, the Key Management Service will automatically: 1. Create a new version of this CryptoKey. 2. Mark the new version as primary. Key rotations performed manually via CreateCryptoKeyVersion and UpdateCryptoKeyPrimaryVersion do not affect next_rotation_time. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        /// </summary>
        [Output("nextRotationTime")]
        public Output<string> NextRotationTime { get; private set; } = null!;

        /// <summary>
        /// A copy of the "primary" CryptoKeyVersion that will be used by Encrypt when this CryptoKey is given in EncryptRequest.name. The CryptoKey's primary version can be updated via UpdateCryptoKeyPrimaryVersion. Keys with purpose ENCRYPT_DECRYPT may have a primary. For other keys, this field will be omitted.
        /// </summary>
        [Output("primary")]
        public Output<Outputs.CryptoKeyVersionResponse> Primary { get; private set; } = null!;

        /// <summary>
        /// Immutable. The immutable purpose of this CryptoKey.
        /// </summary>
        [Output("purpose")]
        public Output<string> Purpose { get; private set; } = null!;

        /// <summary>
        /// next_rotation_time will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours. If rotation_period is set, next_rotation_time must also be set. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        /// </summary>
        [Output("rotationPeriod")]
        public Output<string> RotationPeriod { get; private set; } = null!;

        /// <summary>
        /// A template describing settings for new CryptoKeyVersion instances. The properties of new CryptoKeyVersion instances created by either CreateCryptoKeyVersion or auto-rotation are controlled by this template.
        /// </summary>
        [Output("versionTemplate")]
        public Output<Outputs.CryptoKeyVersionTemplateResponse> VersionTemplate { get; private set; } = null!;


        /// <summary>
        /// Create a KeyRingCryptoKey resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public KeyRingCryptoKey(string name, KeyRingCryptoKeyArgs args, CustomResourceOptions? options = null)
            : base("google-cloud:cloudkms/v1:KeyRingCryptoKey", name, args ?? new KeyRingCryptoKeyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private KeyRingCryptoKey(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-cloud:cloudkms/v1:KeyRingCryptoKey", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing KeyRingCryptoKey resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static KeyRingCryptoKey Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new KeyRingCryptoKey(name, id, options);
        }
    }

    public sealed class KeyRingCryptoKeyArgs : Pulumi.ResourceArgs
    {
        [Input("cryptoKeysId", required: true)]
        public Input<string> CryptoKeysId { get; set; } = null!;

        [Input("keyRingsId", required: true)]
        public Input<string> KeyRingsId { get; set; } = null!;

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys).
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("locationsId", required: true)]
        public Input<string> LocationsId { get; set; } = null!;

        /// <summary>
        /// At next_rotation_time, the Key Management Service will automatically: 1. Create a new version of this CryptoKey. 2. Mark the new version as primary. Key rotations performed manually via CreateCryptoKeyVersion and UpdateCryptoKeyPrimaryVersion do not affect next_rotation_time. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        /// </summary>
        [Input("nextRotationTime")]
        public Input<string>? NextRotationTime { get; set; }

        [Input("projectsId", required: true)]
        public Input<string> ProjectsId { get; set; } = null!;

        /// <summary>
        /// Immutable. The immutable purpose of this CryptoKey.
        /// </summary>
        [Input("purpose")]
        public Input<string>? Purpose { get; set; }

        /// <summary>
        /// next_rotation_time will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours. If rotation_period is set, next_rotation_time must also be set. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        /// </summary>
        [Input("rotationPeriod")]
        public Input<string>? RotationPeriod { get; set; }

        /// <summary>
        /// A template describing settings for new CryptoKeyVersion instances. The properties of new CryptoKeyVersion instances created by either CreateCryptoKeyVersion or auto-rotation are controlled by this template.
        /// </summary>
        [Input("versionTemplate")]
        public Input<Inputs.CryptoKeyVersionTemplateArgs>? VersionTemplate { get; set; }

        public KeyRingCryptoKeyArgs()
        {
        }
    }
}