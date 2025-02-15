// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a new empty dataset.
// Auto-naming is currently not supported for this resource.
type Dataset struct {
	pulumi.CustomResourceState

	// [Optional] An array of objects that define dataset access for one or more entities. You can set this property when inserting or updating a dataset in order to control who is allowed to access the data. If unspecified at dataset creation time, BigQuery adds default dataset access for the following entities: access.specialGroup: projectReaders; access.role: READER; access.specialGroup: projectWriters; access.role: WRITER; access.specialGroup: projectOwners; access.role: OWNER; access.userByEmail: [dataset creator email]; access.role: OWNER;
	Access DatasetAccessItemResponseArrayOutput `pulumi:"access"`
	// The time when this dataset was created, in milliseconds since the epoch.
	CreationTime pulumi.StringOutput `pulumi:"creationTime"`
	// [Required] A reference that identifies the dataset.
	DatasetReference DatasetReferenceResponseOutput `pulumi:"datasetReference"`
	// The default collation of the dataset.
	DefaultCollation               pulumi.StringOutput                   `pulumi:"defaultCollation"`
	DefaultEncryptionConfiguration EncryptionConfigurationResponseOutput `pulumi:"defaultEncryptionConfiguration"`
	// [Optional] The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set, all newly-created partitioned tables in the dataset will have an expirationMs property in the timePartitioning settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of defaultTableExpirationMs for partitioned tables: only one of defaultTableExpirationMs and defaultPartitionExpirationMs will be used for any new partitioned table. If you provide an explicit timePartitioning.expirationMs when creating or updating a partitioned table, that value takes precedence over the default partition expiration time indicated by this property.
	DefaultPartitionExpirationMs pulumi.StringOutput `pulumi:"defaultPartitionExpirationMs"`
	// The default rounding mode of the dataset.
	DefaultRoundingMode pulumi.StringOutput `pulumi:"defaultRoundingMode"`
	// [Optional] The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour). Once this property is set, all newly-created tables in the dataset will have an expirationTime property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the expirationTime for a given table is reached, that table will be deleted automatically. If a table's expirationTime is modified or removed before the table expires, or if you provide an explicit expirationTime when creating a table, that value takes precedence over the default expiration time indicated by this property.
	DefaultTableExpirationMs pulumi.StringOutput `pulumi:"defaultTableExpirationMs"`
	// [Optional] A user-friendly description of the dataset.
	Description pulumi.StringOutput `pulumi:"description"`
	// A hash of the resource.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// [Optional] Information about the external metadata storage where the dataset is defined. Filled out when the dataset type is EXTERNAL.
	ExternalDatasetReference ExternalDatasetReferenceResponseOutput `pulumi:"externalDatasetReference"`
	// [Optional] A descriptive name for the dataset.
	FriendlyName pulumi.StringOutput `pulumi:"friendlyName"`
	// [Optional] Indicates if table names are case insensitive in the dataset.
	IsCaseInsensitive pulumi.BoolOutput `pulumi:"isCaseInsensitive"`
	// The resource type.
	Kind pulumi.StringOutput `pulumi:"kind"`
	// The labels associated with this dataset. You can use these to organize and group your datasets. You can set this property when inserting or updating a dataset. See Creating and Updating Dataset Labels for more information.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.
	LastModifiedTime pulumi.StringOutput `pulumi:"lastModifiedTime"`
	// The geographic location where the dataset should reside. The default value is US. See details at https://cloud.google.com/bigquery/docs/locations.
	Location pulumi.StringOutput `pulumi:"location"`
	// [Optional] Number of hours for the max time travel for all tables in the dataset.
	MaxTimeTravelHours pulumi.StringOutput `pulumi:"maxTimeTravelHours"`
	Project            pulumi.StringOutput `pulumi:"project"`
	// Reserved for future use.
	SatisfiesPzs pulumi.BoolOutput `pulumi:"satisfiesPzs"`
	// A URL that can be used to access the resource again. You can use this URL in Get or Update requests to the resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// [Optional] Storage billing model to be used for all tables in the dataset. Can be set to PHYSICAL. Default is LOGICAL.
	StorageBillingModel pulumi.StringOutput `pulumi:"storageBillingModel"`
	// [Optional]The tags associated with this dataset. Tag keys are globally unique.
	Tags DatasetTagsItemResponseArrayOutput `pulumi:"tags"`
}

// NewDataset registers a new resource with the given unique name, arguments, and options.
func NewDataset(ctx *pulumi.Context,
	name string, args *DatasetArgs, opts ...pulumi.ResourceOption) (*Dataset, error) {
	if args == nil {
		args = &DatasetArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"project",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Dataset
	err := ctx.RegisterResource("google-native:bigquery/v2:Dataset", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDataset gets an existing Dataset resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDataset(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatasetState, opts ...pulumi.ResourceOption) (*Dataset, error) {
	var resource Dataset
	err := ctx.ReadResource("google-native:bigquery/v2:Dataset", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Dataset resources.
type datasetState struct {
}

type DatasetState struct {
}

func (DatasetState) ElementType() reflect.Type {
	return reflect.TypeOf((*datasetState)(nil)).Elem()
}

type datasetArgs struct {
	// [Optional] An array of objects that define dataset access for one or more entities. You can set this property when inserting or updating a dataset in order to control who is allowed to access the data. If unspecified at dataset creation time, BigQuery adds default dataset access for the following entities: access.specialGroup: projectReaders; access.role: READER; access.specialGroup: projectWriters; access.role: WRITER; access.specialGroup: projectOwners; access.role: OWNER; access.userByEmail: [dataset creator email]; access.role: OWNER;
	Access []DatasetAccessItem `pulumi:"access"`
	// [Required] A reference that identifies the dataset.
	DatasetReference               *DatasetReference        `pulumi:"datasetReference"`
	DefaultEncryptionConfiguration *EncryptionConfiguration `pulumi:"defaultEncryptionConfiguration"`
	// [Optional] The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set, all newly-created partitioned tables in the dataset will have an expirationMs property in the timePartitioning settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of defaultTableExpirationMs for partitioned tables: only one of defaultTableExpirationMs and defaultPartitionExpirationMs will be used for any new partitioned table. If you provide an explicit timePartitioning.expirationMs when creating or updating a partitioned table, that value takes precedence over the default partition expiration time indicated by this property.
	DefaultPartitionExpirationMs *string `pulumi:"defaultPartitionExpirationMs"`
	// [Optional] The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour). Once this property is set, all newly-created tables in the dataset will have an expirationTime property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the expirationTime for a given table is reached, that table will be deleted automatically. If a table's expirationTime is modified or removed before the table expires, or if you provide an explicit expirationTime when creating a table, that value takes precedence over the default expiration time indicated by this property.
	DefaultTableExpirationMs *string `pulumi:"defaultTableExpirationMs"`
	// [Optional] A user-friendly description of the dataset.
	Description *string `pulumi:"description"`
	// [Optional] Information about the external metadata storage where the dataset is defined. Filled out when the dataset type is EXTERNAL.
	ExternalDatasetReference *ExternalDatasetReference `pulumi:"externalDatasetReference"`
	// [Optional] A descriptive name for the dataset.
	FriendlyName *string `pulumi:"friendlyName"`
	// [Optional] Indicates if table names are case insensitive in the dataset.
	IsCaseInsensitive *bool `pulumi:"isCaseInsensitive"`
	// The labels associated with this dataset. You can use these to organize and group your datasets. You can set this property when inserting or updating a dataset. See Creating and Updating Dataset Labels for more information.
	Labels map[string]string `pulumi:"labels"`
	// The geographic location where the dataset should reside. The default value is US. See details at https://cloud.google.com/bigquery/docs/locations.
	Location *string `pulumi:"location"`
	// [Optional] Number of hours for the max time travel for all tables in the dataset.
	MaxTimeTravelHours *string `pulumi:"maxTimeTravelHours"`
	Project            *string `pulumi:"project"`
	// [Optional] Storage billing model to be used for all tables in the dataset. Can be set to PHYSICAL. Default is LOGICAL.
	StorageBillingModel *string `pulumi:"storageBillingModel"`
	// [Optional]The tags associated with this dataset. Tag keys are globally unique.
	Tags []DatasetTagsItem `pulumi:"tags"`
}

// The set of arguments for constructing a Dataset resource.
type DatasetArgs struct {
	// [Optional] An array of objects that define dataset access for one or more entities. You can set this property when inserting or updating a dataset in order to control who is allowed to access the data. If unspecified at dataset creation time, BigQuery adds default dataset access for the following entities: access.specialGroup: projectReaders; access.role: READER; access.specialGroup: projectWriters; access.role: WRITER; access.specialGroup: projectOwners; access.role: OWNER; access.userByEmail: [dataset creator email]; access.role: OWNER;
	Access DatasetAccessItemArrayInput
	// [Required] A reference that identifies the dataset.
	DatasetReference               DatasetReferencePtrInput
	DefaultEncryptionConfiguration EncryptionConfigurationPtrInput
	// [Optional] The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set, all newly-created partitioned tables in the dataset will have an expirationMs property in the timePartitioning settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of defaultTableExpirationMs for partitioned tables: only one of defaultTableExpirationMs and defaultPartitionExpirationMs will be used for any new partitioned table. If you provide an explicit timePartitioning.expirationMs when creating or updating a partitioned table, that value takes precedence over the default partition expiration time indicated by this property.
	DefaultPartitionExpirationMs pulumi.StringPtrInput
	// [Optional] The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour). Once this property is set, all newly-created tables in the dataset will have an expirationTime property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the expirationTime for a given table is reached, that table will be deleted automatically. If a table's expirationTime is modified or removed before the table expires, or if you provide an explicit expirationTime when creating a table, that value takes precedence over the default expiration time indicated by this property.
	DefaultTableExpirationMs pulumi.StringPtrInput
	// [Optional] A user-friendly description of the dataset.
	Description pulumi.StringPtrInput
	// [Optional] Information about the external metadata storage where the dataset is defined. Filled out when the dataset type is EXTERNAL.
	ExternalDatasetReference ExternalDatasetReferencePtrInput
	// [Optional] A descriptive name for the dataset.
	FriendlyName pulumi.StringPtrInput
	// [Optional] Indicates if table names are case insensitive in the dataset.
	IsCaseInsensitive pulumi.BoolPtrInput
	// The labels associated with this dataset. You can use these to organize and group your datasets. You can set this property when inserting or updating a dataset. See Creating and Updating Dataset Labels for more information.
	Labels pulumi.StringMapInput
	// The geographic location where the dataset should reside. The default value is US. See details at https://cloud.google.com/bigquery/docs/locations.
	Location pulumi.StringPtrInput
	// [Optional] Number of hours for the max time travel for all tables in the dataset.
	MaxTimeTravelHours pulumi.StringPtrInput
	Project            pulumi.StringPtrInput
	// [Optional] Storage billing model to be used for all tables in the dataset. Can be set to PHYSICAL. Default is LOGICAL.
	StorageBillingModel pulumi.StringPtrInput
	// [Optional]The tags associated with this dataset. Tag keys are globally unique.
	Tags DatasetTagsItemArrayInput
}

func (DatasetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*datasetArgs)(nil)).Elem()
}

type DatasetInput interface {
	pulumi.Input

	ToDatasetOutput() DatasetOutput
	ToDatasetOutputWithContext(ctx context.Context) DatasetOutput
}

func (*Dataset) ElementType() reflect.Type {
	return reflect.TypeOf((**Dataset)(nil)).Elem()
}

func (i *Dataset) ToDatasetOutput() DatasetOutput {
	return i.ToDatasetOutputWithContext(context.Background())
}

func (i *Dataset) ToDatasetOutputWithContext(ctx context.Context) DatasetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatasetOutput)
}

type DatasetOutput struct{ *pulumi.OutputState }

func (DatasetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Dataset)(nil)).Elem()
}

func (o DatasetOutput) ToDatasetOutput() DatasetOutput {
	return o
}

func (o DatasetOutput) ToDatasetOutputWithContext(ctx context.Context) DatasetOutput {
	return o
}

// [Optional] An array of objects that define dataset access for one or more entities. You can set this property when inserting or updating a dataset in order to control who is allowed to access the data. If unspecified at dataset creation time, BigQuery adds default dataset access for the following entities: access.specialGroup: projectReaders; access.role: READER; access.specialGroup: projectWriters; access.role: WRITER; access.specialGroup: projectOwners; access.role: OWNER; access.userByEmail: [dataset creator email]; access.role: OWNER;
func (o DatasetOutput) Access() DatasetAccessItemResponseArrayOutput {
	return o.ApplyT(func(v *Dataset) DatasetAccessItemResponseArrayOutput { return v.Access }).(DatasetAccessItemResponseArrayOutput)
}

// The time when this dataset was created, in milliseconds since the epoch.
func (o DatasetOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

// [Required] A reference that identifies the dataset.
func (o DatasetOutput) DatasetReference() DatasetReferenceResponseOutput {
	return o.ApplyT(func(v *Dataset) DatasetReferenceResponseOutput { return v.DatasetReference }).(DatasetReferenceResponseOutput)
}

// The default collation of the dataset.
func (o DatasetOutput) DefaultCollation() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.DefaultCollation }).(pulumi.StringOutput)
}

func (o DatasetOutput) DefaultEncryptionConfiguration() EncryptionConfigurationResponseOutput {
	return o.ApplyT(func(v *Dataset) EncryptionConfigurationResponseOutput { return v.DefaultEncryptionConfiguration }).(EncryptionConfigurationResponseOutput)
}

// [Optional] The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set, all newly-created partitioned tables in the dataset will have an expirationMs property in the timePartitioning settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of defaultTableExpirationMs for partitioned tables: only one of defaultTableExpirationMs and defaultPartitionExpirationMs will be used for any new partitioned table. If you provide an explicit timePartitioning.expirationMs when creating or updating a partitioned table, that value takes precedence over the default partition expiration time indicated by this property.
func (o DatasetOutput) DefaultPartitionExpirationMs() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.DefaultPartitionExpirationMs }).(pulumi.StringOutput)
}

// The default rounding mode of the dataset.
func (o DatasetOutput) DefaultRoundingMode() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.DefaultRoundingMode }).(pulumi.StringOutput)
}

// [Optional] The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour). Once this property is set, all newly-created tables in the dataset will have an expirationTime property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the expirationTime for a given table is reached, that table will be deleted automatically. If a table's expirationTime is modified or removed before the table expires, or if you provide an explicit expirationTime when creating a table, that value takes precedence over the default expiration time indicated by this property.
func (o DatasetOutput) DefaultTableExpirationMs() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.DefaultTableExpirationMs }).(pulumi.StringOutput)
}

// [Optional] A user-friendly description of the dataset.
func (o DatasetOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// A hash of the resource.
func (o DatasetOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

// [Optional] Information about the external metadata storage where the dataset is defined. Filled out when the dataset type is EXTERNAL.
func (o DatasetOutput) ExternalDatasetReference() ExternalDatasetReferenceResponseOutput {
	return o.ApplyT(func(v *Dataset) ExternalDatasetReferenceResponseOutput { return v.ExternalDatasetReference }).(ExternalDatasetReferenceResponseOutput)
}

// [Optional] A descriptive name for the dataset.
func (o DatasetOutput) FriendlyName() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.FriendlyName }).(pulumi.StringOutput)
}

// [Optional] Indicates if table names are case insensitive in the dataset.
func (o DatasetOutput) IsCaseInsensitive() pulumi.BoolOutput {
	return o.ApplyT(func(v *Dataset) pulumi.BoolOutput { return v.IsCaseInsensitive }).(pulumi.BoolOutput)
}

// The resource type.
func (o DatasetOutput) Kind() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.Kind }).(pulumi.StringOutput)
}

// The labels associated with this dataset. You can use these to organize and group your datasets. You can set this property when inserting or updating a dataset. See Creating and Updating Dataset Labels for more information.
func (o DatasetOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

// The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.
func (o DatasetOutput) LastModifiedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.LastModifiedTime }).(pulumi.StringOutput)
}

// The geographic location where the dataset should reside. The default value is US. See details at https://cloud.google.com/bigquery/docs/locations.
func (o DatasetOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// [Optional] Number of hours for the max time travel for all tables in the dataset.
func (o DatasetOutput) MaxTimeTravelHours() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.MaxTimeTravelHours }).(pulumi.StringOutput)
}

func (o DatasetOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// Reserved for future use.
func (o DatasetOutput) SatisfiesPzs() pulumi.BoolOutput {
	return o.ApplyT(func(v *Dataset) pulumi.BoolOutput { return v.SatisfiesPzs }).(pulumi.BoolOutput)
}

// A URL that can be used to access the resource again. You can use this URL in Get or Update requests to the resource.
func (o DatasetOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.SelfLink }).(pulumi.StringOutput)
}

// [Optional] Storage billing model to be used for all tables in the dataset. Can be set to PHYSICAL. Default is LOGICAL.
func (o DatasetOutput) StorageBillingModel() pulumi.StringOutput {
	return o.ApplyT(func(v *Dataset) pulumi.StringOutput { return v.StorageBillingModel }).(pulumi.StringOutput)
}

// [Optional]The tags associated with this dataset. Tag keys are globally unique.
func (o DatasetOutput) Tags() DatasetTagsItemResponseArrayOutput {
	return o.ApplyT(func(v *Dataset) DatasetTagsItemResponseArrayOutput { return v.Tags }).(DatasetTagsItemResponseArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetInput)(nil)).Elem(), &Dataset{})
	pulumi.RegisterOutputType(DatasetOutput{})
}
