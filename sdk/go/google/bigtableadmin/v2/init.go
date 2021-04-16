// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v2

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-google-native/sdk/go/google"
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
	case "google-native:bigtableadmin/v2:Instance":
		r = &Instance{}
	case "google-native:bigtableadmin/v2:InstanceAppProfile":
		r = &InstanceAppProfile{}
	case "google-native:bigtableadmin/v2:InstanceCluster":
		r = &InstanceCluster{}
	case "google-native:bigtableadmin/v2:InstanceClusterBackup":
		r = &InstanceClusterBackup{}
	case "google-native:bigtableadmin/v2:InstanceClusterBackupIamPolicy":
		r = &InstanceClusterBackupIamPolicy{}
	case "google-native:bigtableadmin/v2:InstanceIamPolicy":
		r = &InstanceIamPolicy{}
	case "google-native:bigtableadmin/v2:InstanceTable":
		r = &InstanceTable{}
	case "google-native:bigtableadmin/v2:InstanceTableIamPolicy":
		r = &InstanceTableIamPolicy{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := google.PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"google-native",
		"bigtableadmin/v2",
		&module{version},
	)
}