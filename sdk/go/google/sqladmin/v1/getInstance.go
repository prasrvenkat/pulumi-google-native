// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves a resource containing information about a Cloud SQL instance.
func LookupInstance(ctx *pulumi.Context, args *LookupInstanceArgs, opts ...pulumi.InvokeOption) (*LookupInstanceResult, error) {
	var rv LookupInstanceResult
	err := ctx.Invoke("google-native:sqladmin/v1:getInstance", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupInstanceArgs struct {
	Instance string  `pulumi:"instance"`
	Project  *string `pulumi:"project"`
}

type LookupInstanceResult struct {
	// The backend type. **SECOND_GEN**: Cloud SQL database instance. **EXTERNAL**: A database server that is not managed by Google. This property is read-only; use the **tier** property in the **settings** object to determine the database type.
	BackendType string `pulumi:"backendType"`
	// Connection name of the Cloud SQL instance used in connection strings.
	ConnectionName string `pulumi:"connectionName"`
	// The time when the instance was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example **2012-11-15T16:19:00.094Z**.
	CreateTime string `pulumi:"createTime"`
	// The current disk usage of the instance in bytes. This property has been deprecated. Use the "cloudsql.googleapis.com/database/disk/bytes_used" metric in Cloud Monitoring API instead. Please see [this announcement](https://groups.google.com/d/msg/google-cloud-sql-announce/I_7-F9EBhT0/BtvFtdFeAgAJ) for details.
	CurrentDiskSize string `pulumi:"currentDiskSize"`
	// The databaseInstalledVersion stores the current fully resolved database version running on the instance including minor version such as MYSQL_5_6_50
	DatabaseInstalledVersion string `pulumi:"databaseInstalledVersion"`
	// The database engine type and version. The **databaseVersion** field cannot be changed after instance creation.
	DatabaseVersion string `pulumi:"databaseVersion"`
	// Disk encryption configuration specific to an instance.
	DiskEncryptionConfiguration DiskEncryptionConfigurationResponse `pulumi:"diskEncryptionConfiguration"`
	// Disk encryption status specific to an instance.
	DiskEncryptionStatus DiskEncryptionStatusResponse `pulumi:"diskEncryptionStatus"`
	// The name and status of the failover replica.
	FailoverReplica InstanceFailoverReplicaResponse `pulumi:"failoverReplica"`
	// The Compute Engine zone that the instance is currently serving from. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary zone.
	GceZone string `pulumi:"gceZone"`
	// The instance type.
	InstanceType string `pulumi:"instanceType"`
	// The assigned IP addresses for the instance.
	IpAddresses []IpMappingResponse `pulumi:"ipAddresses"`
	// This is always **sql#instance**.
	Kind string `pulumi:"kind"`
	// The name of the instance which will act as primary in the replication setup.
	MasterInstanceName string `pulumi:"masterInstanceName"`
	// The maximum disk size of the instance in bytes.
	MaxDiskSize string `pulumi:"maxDiskSize"`
	// Name of the Cloud SQL instance. This does not include the project ID.
	Name string `pulumi:"name"`
	// Configuration specific to on-premises instances.
	OnPremisesConfiguration OnPremisesConfigurationResponse `pulumi:"onPremisesConfiguration"`
	// This field represents the report generated by the proactive database wellness job for OutOfDisk issues. * Writers: * the proactive database wellness job for OOD. * Readers: * the proactive database wellness job
	OutOfDiskReport SqlOutOfDiskReportResponse `pulumi:"outOfDiskReport"`
	// The project ID of the project containing the Cloud SQL instance. The Google apps domain is prefixed if applicable.
	Project string `pulumi:"project"`
	// The geographical region. Can be: * **us-central** (**FIRST_GEN** instances only) * **us-central1** (**SECOND_GEN** instances only) * **asia-east1** or **europe-west1**. Defaults to **us-central** or **us-central1** depending on the instance type. The region cannot be changed after instance creation.
	Region string `pulumi:"region"`
	// Configuration specific to failover replicas and read replicas.
	ReplicaConfiguration ReplicaConfigurationResponse `pulumi:"replicaConfiguration"`
	// The replicas of the instance.
	ReplicaNames []string `pulumi:"replicaNames"`
	// Initial root password. Use only on creation.
	RootPassword string `pulumi:"rootPassword"`
	// The status indicating if instance satisfiesPzs. Reserved for future use.
	SatisfiesPzs bool `pulumi:"satisfiesPzs"`
	// The start time of any upcoming scheduled maintenance for this instance.
	ScheduledMaintenance SqlScheduledMaintenanceResponse `pulumi:"scheduledMaintenance"`
	// The Compute Engine zone that the failover instance is currently serving from for a regional instance. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary/failover zone. Reserved for future use.
	SecondaryGceZone string `pulumi:"secondaryGceZone"`
	// The URI of this resource.
	SelfLink string `pulumi:"selfLink"`
	// SSL configuration.
	ServerCaCert SslCertResponse `pulumi:"serverCaCert"`
	// The service account email address assigned to the instance. This property is read-only.
	ServiceAccountEmailAddress string `pulumi:"serviceAccountEmailAddress"`
	// The user settings.
	Settings SettingsResponse `pulumi:"settings"`
	// The current serving state of the Cloud SQL instance.
	State string `pulumi:"state"`
	// If the instance state is SUSPENDED, the reason for the suspension.
	SuspensionReason []string `pulumi:"suspensionReason"`
}

func LookupInstanceOutput(ctx *pulumi.Context, args LookupInstanceOutputArgs, opts ...pulumi.InvokeOption) LookupInstanceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupInstanceResult, error) {
			args := v.(LookupInstanceArgs)
			r, err := LookupInstance(ctx, &args, opts...)
			return *r, err
		}).(LookupInstanceResultOutput)
}

type LookupInstanceOutputArgs struct {
	Instance pulumi.StringInput    `pulumi:"instance"`
	Project  pulumi.StringPtrInput `pulumi:"project"`
}

func (LookupInstanceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInstanceArgs)(nil)).Elem()
}

type LookupInstanceResultOutput struct{ *pulumi.OutputState }

func (LookupInstanceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInstanceResult)(nil)).Elem()
}

func (o LookupInstanceResultOutput) ToLookupInstanceResultOutput() LookupInstanceResultOutput {
	return o
}

func (o LookupInstanceResultOutput) ToLookupInstanceResultOutputWithContext(ctx context.Context) LookupInstanceResultOutput {
	return o
}

// The backend type. **SECOND_GEN**: Cloud SQL database instance. **EXTERNAL**: A database server that is not managed by Google. This property is read-only; use the **tier** property in the **settings** object to determine the database type.
func (o LookupInstanceResultOutput) BackendType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.BackendType }).(pulumi.StringOutput)
}

// Connection name of the Cloud SQL instance used in connection strings.
func (o LookupInstanceResultOutput) ConnectionName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.ConnectionName }).(pulumi.StringOutput)
}

// The time when the instance was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example **2012-11-15T16:19:00.094Z**.
func (o LookupInstanceResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// The current disk usage of the instance in bytes. This property has been deprecated. Use the "cloudsql.googleapis.com/database/disk/bytes_used" metric in Cloud Monitoring API instead. Please see [this announcement](https://groups.google.com/d/msg/google-cloud-sql-announce/I_7-F9EBhT0/BtvFtdFeAgAJ) for details.
func (o LookupInstanceResultOutput) CurrentDiskSize() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.CurrentDiskSize }).(pulumi.StringOutput)
}

// The databaseInstalledVersion stores the current fully resolved database version running on the instance including minor version such as MYSQL_5_6_50
func (o LookupInstanceResultOutput) DatabaseInstalledVersion() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.DatabaseInstalledVersion }).(pulumi.StringOutput)
}

// The database engine type and version. The **databaseVersion** field cannot be changed after instance creation.
func (o LookupInstanceResultOutput) DatabaseVersion() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.DatabaseVersion }).(pulumi.StringOutput)
}

// Disk encryption configuration specific to an instance.
func (o LookupInstanceResultOutput) DiskEncryptionConfiguration() DiskEncryptionConfigurationResponseOutput {
	return o.ApplyT(func(v LookupInstanceResult) DiskEncryptionConfigurationResponse { return v.DiskEncryptionConfiguration }).(DiskEncryptionConfigurationResponseOutput)
}

// Disk encryption status specific to an instance.
func (o LookupInstanceResultOutput) DiskEncryptionStatus() DiskEncryptionStatusResponseOutput {
	return o.ApplyT(func(v LookupInstanceResult) DiskEncryptionStatusResponse { return v.DiskEncryptionStatus }).(DiskEncryptionStatusResponseOutput)
}

// The name and status of the failover replica.
func (o LookupInstanceResultOutput) FailoverReplica() InstanceFailoverReplicaResponseOutput {
	return o.ApplyT(func(v LookupInstanceResult) InstanceFailoverReplicaResponse { return v.FailoverReplica }).(InstanceFailoverReplicaResponseOutput)
}

// The Compute Engine zone that the instance is currently serving from. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary zone.
func (o LookupInstanceResultOutput) GceZone() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.GceZone }).(pulumi.StringOutput)
}

// The instance type.
func (o LookupInstanceResultOutput) InstanceType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.InstanceType }).(pulumi.StringOutput)
}

// The assigned IP addresses for the instance.
func (o LookupInstanceResultOutput) IpAddresses() IpMappingResponseArrayOutput {
	return o.ApplyT(func(v LookupInstanceResult) []IpMappingResponse { return v.IpAddresses }).(IpMappingResponseArrayOutput)
}

// This is always **sql#instance**.
func (o LookupInstanceResultOutput) Kind() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.Kind }).(pulumi.StringOutput)
}

// The name of the instance which will act as primary in the replication setup.
func (o LookupInstanceResultOutput) MasterInstanceName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.MasterInstanceName }).(pulumi.StringOutput)
}

// The maximum disk size of the instance in bytes.
func (o LookupInstanceResultOutput) MaxDiskSize() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.MaxDiskSize }).(pulumi.StringOutput)
}

// Name of the Cloud SQL instance. This does not include the project ID.
func (o LookupInstanceResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.Name }).(pulumi.StringOutput)
}

// Configuration specific to on-premises instances.
func (o LookupInstanceResultOutput) OnPremisesConfiguration() OnPremisesConfigurationResponseOutput {
	return o.ApplyT(func(v LookupInstanceResult) OnPremisesConfigurationResponse { return v.OnPremisesConfiguration }).(OnPremisesConfigurationResponseOutput)
}

// This field represents the report generated by the proactive database wellness job for OutOfDisk issues. * Writers: * the proactive database wellness job for OOD. * Readers: * the proactive database wellness job
func (o LookupInstanceResultOutput) OutOfDiskReport() SqlOutOfDiskReportResponseOutput {
	return o.ApplyT(func(v LookupInstanceResult) SqlOutOfDiskReportResponse { return v.OutOfDiskReport }).(SqlOutOfDiskReportResponseOutput)
}

// The project ID of the project containing the Cloud SQL instance. The Google apps domain is prefixed if applicable.
func (o LookupInstanceResultOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.Project }).(pulumi.StringOutput)
}

// The geographical region. Can be: * **us-central** (**FIRST_GEN** instances only) * **us-central1** (**SECOND_GEN** instances only) * **asia-east1** or **europe-west1**. Defaults to **us-central** or **us-central1** depending on the instance type. The region cannot be changed after instance creation.
func (o LookupInstanceResultOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.Region }).(pulumi.StringOutput)
}

// Configuration specific to failover replicas and read replicas.
func (o LookupInstanceResultOutput) ReplicaConfiguration() ReplicaConfigurationResponseOutput {
	return o.ApplyT(func(v LookupInstanceResult) ReplicaConfigurationResponse { return v.ReplicaConfiguration }).(ReplicaConfigurationResponseOutput)
}

// The replicas of the instance.
func (o LookupInstanceResultOutput) ReplicaNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupInstanceResult) []string { return v.ReplicaNames }).(pulumi.StringArrayOutput)
}

// Initial root password. Use only on creation.
func (o LookupInstanceResultOutput) RootPassword() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.RootPassword }).(pulumi.StringOutput)
}

// The status indicating if instance satisfiesPzs. Reserved for future use.
func (o LookupInstanceResultOutput) SatisfiesPzs() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupInstanceResult) bool { return v.SatisfiesPzs }).(pulumi.BoolOutput)
}

// The start time of any upcoming scheduled maintenance for this instance.
func (o LookupInstanceResultOutput) ScheduledMaintenance() SqlScheduledMaintenanceResponseOutput {
	return o.ApplyT(func(v LookupInstanceResult) SqlScheduledMaintenanceResponse { return v.ScheduledMaintenance }).(SqlScheduledMaintenanceResponseOutput)
}

// The Compute Engine zone that the failover instance is currently serving from for a regional instance. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary/failover zone. Reserved for future use.
func (o LookupInstanceResultOutput) SecondaryGceZone() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.SecondaryGceZone }).(pulumi.StringOutput)
}

// The URI of this resource.
func (o LookupInstanceResultOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.SelfLink }).(pulumi.StringOutput)
}

// SSL configuration.
func (o LookupInstanceResultOutput) ServerCaCert() SslCertResponseOutput {
	return o.ApplyT(func(v LookupInstanceResult) SslCertResponse { return v.ServerCaCert }).(SslCertResponseOutput)
}

// The service account email address assigned to the instance. This property is read-only.
func (o LookupInstanceResultOutput) ServiceAccountEmailAddress() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.ServiceAccountEmailAddress }).(pulumi.StringOutput)
}

// The user settings.
func (o LookupInstanceResultOutput) Settings() SettingsResponseOutput {
	return o.ApplyT(func(v LookupInstanceResult) SettingsResponse { return v.Settings }).(SettingsResponseOutput)
}

// The current serving state of the Cloud SQL instance.
func (o LookupInstanceResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceResult) string { return v.State }).(pulumi.StringOutput)
}

// If the instance state is SUSPENDED, the reason for the suspension.
func (o LookupInstanceResultOutput) SuspensionReason() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupInstanceResult) []string { return v.SuspensionReason }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupInstanceResultOutput{})
}