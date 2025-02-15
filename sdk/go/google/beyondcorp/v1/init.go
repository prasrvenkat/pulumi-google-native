// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "google-native:beyondcorp/v1:AppConnection":
		r = &AppConnection{}
	case "google-native:beyondcorp/v1:AppConnectionIamBinding":
		r = &AppConnectionIamBinding{}
	case "google-native:beyondcorp/v1:AppConnectionIamMember":
		r = &AppConnectionIamMember{}
	case "google-native:beyondcorp/v1:AppConnectionIamPolicy":
		r = &AppConnectionIamPolicy{}
	case "google-native:beyondcorp/v1:AppConnector":
		r = &AppConnector{}
	case "google-native:beyondcorp/v1:AppConnectorIamBinding":
		r = &AppConnectorIamBinding{}
	case "google-native:beyondcorp/v1:AppConnectorIamMember":
		r = &AppConnectorIamMember{}
	case "google-native:beyondcorp/v1:AppConnectorIamPolicy":
		r = &AppConnectorIamPolicy{}
	case "google-native:beyondcorp/v1:AppGateway":
		r = &AppGateway{}
	case "google-native:beyondcorp/v1:AppGatewayIamBinding":
		r = &AppGatewayIamBinding{}
	case "google-native:beyondcorp/v1:AppGatewayIamMember":
		r = &AppGatewayIamMember{}
	case "google-native:beyondcorp/v1:AppGatewayIamPolicy":
		r = &AppGatewayIamPolicy{}
	case "google-native:beyondcorp/v1:ClientConnectorServiceIamBinding":
		r = &ClientConnectorServiceIamBinding{}
	case "google-native:beyondcorp/v1:ClientConnectorServiceIamMember":
		r = &ClientConnectorServiceIamMember{}
	case "google-native:beyondcorp/v1:ClientConnectorServiceIamPolicy":
		r = &ClientConnectorServiceIamPolicy{}
	case "google-native:beyondcorp/v1:ClientGatewayIamBinding":
		r = &ClientGatewayIamBinding{}
	case "google-native:beyondcorp/v1:ClientGatewayIamMember":
		r = &ClientGatewayIamMember{}
	case "google-native:beyondcorp/v1:ClientGatewayIamPolicy":
		r = &ClientGatewayIamPolicy{}
	case "google-native:beyondcorp/v1:OrganizationPartnerTenantBrowserDlpRuleIamBinding":
		r = &OrganizationPartnerTenantBrowserDlpRuleIamBinding{}
	case "google-native:beyondcorp/v1:OrganizationPartnerTenantBrowserDlpRuleIamMember":
		r = &OrganizationPartnerTenantBrowserDlpRuleIamMember{}
	case "google-native:beyondcorp/v1:OrganizationPartnerTenantBrowserDlpRuleIamPolicy":
		r = &OrganizationPartnerTenantBrowserDlpRuleIamPolicy{}
	case "google-native:beyondcorp/v1:OrganizationPartnerTenantIamBinding":
		r = &OrganizationPartnerTenantIamBinding{}
	case "google-native:beyondcorp/v1:OrganizationPartnerTenantIamMember":
		r = &OrganizationPartnerTenantIamMember{}
	case "google-native:beyondcorp/v1:OrganizationPartnerTenantIamPolicy":
		r = &OrganizationPartnerTenantIamPolicy{}
	case "google-native:beyondcorp/v1:OrganizationPartnerTenantProxyConfigIamBinding":
		r = &OrganizationPartnerTenantProxyConfigIamBinding{}
	case "google-native:beyondcorp/v1:OrganizationPartnerTenantProxyConfigIamMember":
		r = &OrganizationPartnerTenantProxyConfigIamMember{}
	case "google-native:beyondcorp/v1:OrganizationPartnerTenantProxyConfigIamPolicy":
		r = &OrganizationPartnerTenantProxyConfigIamPolicy{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"google-native",
		"beyondcorp/v1",
		&module{version},
	)
}
