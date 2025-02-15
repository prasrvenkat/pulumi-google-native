// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.IdentityToolkit.V2
{
    public static class GetTenant
    {
        /// <summary>
        /// Get a tenant. Requires read permission on the Tenant resource.
        /// </summary>
        public static Task<GetTenantResult> InvokeAsync(GetTenantArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetTenantResult>("google-native:identitytoolkit/v2:getTenant", args ?? new GetTenantArgs(), options.WithDefaults());

        /// <summary>
        /// Get a tenant. Requires read permission on the Tenant resource.
        /// </summary>
        public static Output<GetTenantResult> Invoke(GetTenantInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetTenantResult>("google-native:identitytoolkit/v2:getTenant", args ?? new GetTenantInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTenantArgs : global::Pulumi.InvokeArgs
    {
        [Input("project")]
        public string? Project { get; set; }

        [Input("tenantId", required: true)]
        public string TenantId { get; set; } = null!;

        public GetTenantArgs()
        {
        }
        public static new GetTenantArgs Empty => new GetTenantArgs();
    }

    public sealed class GetTenantInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("tenantId", required: true)]
        public Input<string> TenantId { get; set; } = null!;

        public GetTenantInvokeArgs()
        {
        }
        public static new GetTenantInvokeArgs Empty => new GetTenantInvokeArgs();
    }


    [OutputType]
    public sealed class GetTenantResult
    {
        /// <summary>
        /// Whether to allow email/password user authentication.
        /// </summary>
        public readonly bool AllowPasswordSignup;
        /// <summary>
        /// Whether anonymous users will be auto-deleted after a period of 30 days.
        /// </summary>
        public readonly bool AutodeleteAnonymousUsers;
        /// <summary>
        /// Options related to how clients making requests on behalf of a project should be configured.
        /// </summary>
        public readonly Outputs.GoogleCloudIdentitytoolkitAdminV2ClientPermissionConfigResponse Client;
        /// <summary>
        /// Whether authentication is disabled for the tenant. If true, the users under the disabled tenant are not allowed to sign-in. Admins of the disabled tenant are not able to manage its users.
        /// </summary>
        public readonly bool DisableAuth;
        /// <summary>
        /// Display name of the tenant.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// Configuration for settings related to email privacy and public visibility.
        /// </summary>
        public readonly Outputs.GoogleCloudIdentitytoolkitAdminV2EmailPrivacyConfigResponse EmailPrivacyConfig;
        /// <summary>
        /// Whether to enable anonymous user authentication.
        /// </summary>
        public readonly bool EnableAnonymousUser;
        /// <summary>
        /// Whether to enable email link user authentication.
        /// </summary>
        public readonly bool EnableEmailLinkSignin;
        /// <summary>
        /// Hash config information of a tenant for display on Pantheon. This can only be displayed on Pantheon to avoid the sensitive information to get accidentally leaked. Only returned in GetTenant response to restrict reading of this information. Requires firebaseauth.configs.getHashConfig permission on the agent project for returning this field.
        /// </summary>
        public readonly Outputs.GoogleCloudIdentitytoolkitAdminV2HashConfigResponse HashConfig;
        /// <summary>
        /// Specify the settings that the tenant could inherit.
        /// </summary>
        public readonly Outputs.GoogleCloudIdentitytoolkitAdminV2InheritanceResponse Inheritance;
        /// <summary>
        /// The tenant-level configuration of MFA options.
        /// </summary>
        public readonly Outputs.GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfigResponse MfaConfig;
        /// <summary>
        /// Configuration related to monitoring project activity.
        /// </summary>
        public readonly Outputs.GoogleCloudIdentitytoolkitAdminV2MonitoringConfigResponse Monitoring;
        /// <summary>
        /// Resource name of a tenant. For example: "projects/{project-id}/tenants/{tenant-id}"
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The tenant-level password policy config
        /// </summary>
        public readonly Outputs.GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfigResponse PasswordPolicyConfig;
        /// <summary>
        /// The tenant-level reCAPTCHA config.
        /// </summary>
        public readonly Outputs.GoogleCloudIdentitytoolkitAdminV2RecaptchaConfigResponse RecaptchaConfig;
        /// <summary>
        /// Configures which regions are enabled for SMS verification code sending.
        /// </summary>
        public readonly Outputs.GoogleCloudIdentitytoolkitAdminV2SmsRegionConfigResponse SmsRegionConfig;
        /// <summary>
        /// A map of pairs that can be used for MFA. The phone number should be in E.164 format (https://www.itu.int/rec/T-REC-E.164/) and a maximum of 10 pairs can be added (error will be thrown once exceeded).
        /// </summary>
        public readonly ImmutableDictionary<string, string> TestPhoneNumbers;

        [OutputConstructor]
        private GetTenantResult(
            bool allowPasswordSignup,

            bool autodeleteAnonymousUsers,

            Outputs.GoogleCloudIdentitytoolkitAdminV2ClientPermissionConfigResponse client,

            bool disableAuth,

            string displayName,

            Outputs.GoogleCloudIdentitytoolkitAdminV2EmailPrivacyConfigResponse emailPrivacyConfig,

            bool enableAnonymousUser,

            bool enableEmailLinkSignin,

            Outputs.GoogleCloudIdentitytoolkitAdminV2HashConfigResponse hashConfig,

            Outputs.GoogleCloudIdentitytoolkitAdminV2InheritanceResponse inheritance,

            Outputs.GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfigResponse mfaConfig,

            Outputs.GoogleCloudIdentitytoolkitAdminV2MonitoringConfigResponse monitoring,

            string name,

            Outputs.GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfigResponse passwordPolicyConfig,

            Outputs.GoogleCloudIdentitytoolkitAdminV2RecaptchaConfigResponse recaptchaConfig,

            Outputs.GoogleCloudIdentitytoolkitAdminV2SmsRegionConfigResponse smsRegionConfig,

            ImmutableDictionary<string, string> testPhoneNumbers)
        {
            AllowPasswordSignup = allowPasswordSignup;
            AutodeleteAnonymousUsers = autodeleteAnonymousUsers;
            Client = client;
            DisableAuth = disableAuth;
            DisplayName = displayName;
            EmailPrivacyConfig = emailPrivacyConfig;
            EnableAnonymousUser = enableAnonymousUser;
            EnableEmailLinkSignin = enableEmailLinkSignin;
            HashConfig = hashConfig;
            Inheritance = inheritance;
            MfaConfig = mfaConfig;
            Monitoring = monitoring;
            Name = name;
            PasswordPolicyConfig = passwordPolicyConfig;
            RecaptchaConfig = recaptchaConfig;
            SmsRegionConfig = smsRegionConfig;
            TestPhoneNumbers = testPhoneNumbers;
        }
    }
}
