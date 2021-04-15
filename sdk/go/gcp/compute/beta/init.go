// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package beta

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-gcp-native/sdk/go/gcp"
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
	case "gcp-native:compute/beta:Address":
		r = &Address{}
	case "gcp-native:compute/beta:Autoscaler":
		r = &Autoscaler{}
	case "gcp-native:compute/beta:BackendBucket":
		r = &BackendBucket{}
	case "gcp-native:compute/beta:BackendBucketIamPolicy":
		r = &BackendBucketIamPolicy{}
	case "gcp-native:compute/beta:BackendService":
		r = &BackendService{}
	case "gcp-native:compute/beta:Disk":
		r = &Disk{}
	case "gcp-native:compute/beta:DiskIamPolicy":
		r = &DiskIamPolicy{}
	case "gcp-native:compute/beta:ExternalVpnGateway":
		r = &ExternalVpnGateway{}
	case "gcp-native:compute/beta:Firewall":
		r = &Firewall{}
	case "gcp-native:compute/beta:FirewallPolicy":
		r = &FirewallPolicy{}
	case "gcp-native:compute/beta:FirewallPolicyIamPolicy":
		r = &FirewallPolicyIamPolicy{}
	case "gcp-native:compute/beta:ForwardingRule":
		r = &ForwardingRule{}
	case "gcp-native:compute/beta:GlobalAddress":
		r = &GlobalAddress{}
	case "gcp-native:compute/beta:GlobalForwardingRule":
		r = &GlobalForwardingRule{}
	case "gcp-native:compute/beta:GlobalNetworkEndpointGroup":
		r = &GlobalNetworkEndpointGroup{}
	case "gcp-native:compute/beta:GlobalPublicDelegatedPrefix":
		r = &GlobalPublicDelegatedPrefix{}
	case "gcp-native:compute/beta:HealthCheck":
		r = &HealthCheck{}
	case "gcp-native:compute/beta:HttpHealthCheck":
		r = &HttpHealthCheck{}
	case "gcp-native:compute/beta:HttpsHealthCheck":
		r = &HttpsHealthCheck{}
	case "gcp-native:compute/beta:Image":
		r = &Image{}
	case "gcp-native:compute/beta:ImageIamPolicy":
		r = &ImageIamPolicy{}
	case "gcp-native:compute/beta:Instance":
		r = &Instance{}
	case "gcp-native:compute/beta:InstanceGroup":
		r = &InstanceGroup{}
	case "gcp-native:compute/beta:InstanceGroupManager":
		r = &InstanceGroupManager{}
	case "gcp-native:compute/beta:InstanceIamPolicy":
		r = &InstanceIamPolicy{}
	case "gcp-native:compute/beta:InstanceTemplate":
		r = &InstanceTemplate{}
	case "gcp-native:compute/beta:InstanceTemplateIamPolicy":
		r = &InstanceTemplateIamPolicy{}
	case "gcp-native:compute/beta:Interconnect":
		r = &Interconnect{}
	case "gcp-native:compute/beta:InterconnectAttachment":
		r = &InterconnectAttachment{}
	case "gcp-native:compute/beta:License":
		r = &License{}
	case "gcp-native:compute/beta:LicenseIamPolicy":
		r = &LicenseIamPolicy{}
	case "gcp-native:compute/beta:MachineImage":
		r = &MachineImage{}
	case "gcp-native:compute/beta:MachineImageIamPolicy":
		r = &MachineImageIamPolicy{}
	case "gcp-native:compute/beta:Network":
		r = &Network{}
	case "gcp-native:compute/beta:NetworkEndpointGroup":
		r = &NetworkEndpointGroup{}
	case "gcp-native:compute/beta:NodeGroup":
		r = &NodeGroup{}
	case "gcp-native:compute/beta:NodeGroupIamPolicy":
		r = &NodeGroupIamPolicy{}
	case "gcp-native:compute/beta:NodeTemplate":
		r = &NodeTemplate{}
	case "gcp-native:compute/beta:NodeTemplateIamPolicy":
		r = &NodeTemplateIamPolicy{}
	case "gcp-native:compute/beta:OrganizationSecurityPolicy":
		r = &OrganizationSecurityPolicy{}
	case "gcp-native:compute/beta:PacketMirroring":
		r = &PacketMirroring{}
	case "gcp-native:compute/beta:PublicAdvertisedPrefix":
		r = &PublicAdvertisedPrefix{}
	case "gcp-native:compute/beta:PublicDelegatedPrefix":
		r = &PublicDelegatedPrefix{}
	case "gcp-native:compute/beta:RegionAutoscaler":
		r = &RegionAutoscaler{}
	case "gcp-native:compute/beta:RegionBackendService":
		r = &RegionBackendService{}
	case "gcp-native:compute/beta:RegionCommitment":
		r = &RegionCommitment{}
	case "gcp-native:compute/beta:RegionDisk":
		r = &RegionDisk{}
	case "gcp-native:compute/beta:RegionDiskIamPolicy":
		r = &RegionDiskIamPolicy{}
	case "gcp-native:compute/beta:RegionHealthCheck":
		r = &RegionHealthCheck{}
	case "gcp-native:compute/beta:RegionHealthCheckService":
		r = &RegionHealthCheckService{}
	case "gcp-native:compute/beta:RegionInstanceGroupManager":
		r = &RegionInstanceGroupManager{}
	case "gcp-native:compute/beta:RegionNetworkEndpointGroup":
		r = &RegionNetworkEndpointGroup{}
	case "gcp-native:compute/beta:RegionNotificationEndpoint":
		r = &RegionNotificationEndpoint{}
	case "gcp-native:compute/beta:RegionSslCertificate":
		r = &RegionSslCertificate{}
	case "gcp-native:compute/beta:RegionTargetHttpProxy":
		r = &RegionTargetHttpProxy{}
	case "gcp-native:compute/beta:RegionTargetHttpsProxy":
		r = &RegionTargetHttpsProxy{}
	case "gcp-native:compute/beta:RegionUrlMap":
		r = &RegionUrlMap{}
	case "gcp-native:compute/beta:Reservation":
		r = &Reservation{}
	case "gcp-native:compute/beta:ReservationIamPolicy":
		r = &ReservationIamPolicy{}
	case "gcp-native:compute/beta:ResourcePolicy":
		r = &ResourcePolicy{}
	case "gcp-native:compute/beta:ResourcePolicyIamPolicy":
		r = &ResourcePolicyIamPolicy{}
	case "gcp-native:compute/beta:Route":
		r = &Route{}
	case "gcp-native:compute/beta:Router":
		r = &Router{}
	case "gcp-native:compute/beta:SecurityPolicy":
		r = &SecurityPolicy{}
	case "gcp-native:compute/beta:ServiceAttachment":
		r = &ServiceAttachment{}
	case "gcp-native:compute/beta:ServiceAttachmentIamPolicy":
		r = &ServiceAttachmentIamPolicy{}
	case "gcp-native:compute/beta:Snapshot":
		r = &Snapshot{}
	case "gcp-native:compute/beta:SnapshotIamPolicy":
		r = &SnapshotIamPolicy{}
	case "gcp-native:compute/beta:SslCertificate":
		r = &SslCertificate{}
	case "gcp-native:compute/beta:SslPolicy":
		r = &SslPolicy{}
	case "gcp-native:compute/beta:Subnetwork":
		r = &Subnetwork{}
	case "gcp-native:compute/beta:SubnetworkIamPolicy":
		r = &SubnetworkIamPolicy{}
	case "gcp-native:compute/beta:TargetGrpcProxy":
		r = &TargetGrpcProxy{}
	case "gcp-native:compute/beta:TargetHttpProxy":
		r = &TargetHttpProxy{}
	case "gcp-native:compute/beta:TargetHttpsProxy":
		r = &TargetHttpsProxy{}
	case "gcp-native:compute/beta:TargetInstance":
		r = &TargetInstance{}
	case "gcp-native:compute/beta:TargetPool":
		r = &TargetPool{}
	case "gcp-native:compute/beta:TargetSslProxy":
		r = &TargetSslProxy{}
	case "gcp-native:compute/beta:TargetTcpProxy":
		r = &TargetTcpProxy{}
	case "gcp-native:compute/beta:TargetVpnGateway":
		r = &TargetVpnGateway{}
	case "gcp-native:compute/beta:UrlMap":
		r = &UrlMap{}
	case "gcp-native:compute/beta:VpnGateway":
		r = &VpnGateway{}
	case "gcp-native:compute/beta:VpnTunnel":
		r = &VpnTunnel{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := gcp.PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"gcp-native",
		"compute/beta",
		&module{version},
	)
}