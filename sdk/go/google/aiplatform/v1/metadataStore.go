// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Initializes a MetadataStore, including allocation of resources.
// Auto-naming is currently not supported for this resource.
type MetadataStore struct {
	pulumi.CustomResourceState

	// Timestamp when this MetadataStore was created.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Description of the MetadataStore.
	Description pulumi.StringOutput `pulumi:"description"`
	// Customer-managed encryption key spec for a Metadata Store. If set, this Metadata Store and all sub-resources of this Metadata Store are secured using this key.
	EncryptionSpec GoogleCloudAiplatformV1EncryptionSpecResponseOutput `pulumi:"encryptionSpec"`
	Location       pulumi.StringOutput                                 `pulumi:"location"`
	// The {metadatastore} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all MetadataStores in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataStore.)
	MetadataStoreId pulumi.StringPtrOutput `pulumi:"metadataStoreId"`
	// The resource name of the MetadataStore instance.
	Name    pulumi.StringOutput `pulumi:"name"`
	Project pulumi.StringOutput `pulumi:"project"`
	// State information of the MetadataStore.
	State GoogleCloudAiplatformV1MetadataStoreMetadataStoreStateResponseOutput `pulumi:"state"`
	// Timestamp when this MetadataStore was last updated.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
}

// NewMetadataStore registers a new resource with the given unique name, arguments, and options.
func NewMetadataStore(ctx *pulumi.Context,
	name string, args *MetadataStoreArgs, opts ...pulumi.ResourceOption) (*MetadataStore, error) {
	if args == nil {
		args = &MetadataStoreArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"location",
		"project",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource MetadataStore
	err := ctx.RegisterResource("google-native:aiplatform/v1:MetadataStore", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMetadataStore gets an existing MetadataStore resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMetadataStore(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MetadataStoreState, opts ...pulumi.ResourceOption) (*MetadataStore, error) {
	var resource MetadataStore
	err := ctx.ReadResource("google-native:aiplatform/v1:MetadataStore", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MetadataStore resources.
type metadataStoreState struct {
}

type MetadataStoreState struct {
}

func (MetadataStoreState) ElementType() reflect.Type {
	return reflect.TypeOf((*metadataStoreState)(nil)).Elem()
}

type metadataStoreArgs struct {
	// Description of the MetadataStore.
	Description *string `pulumi:"description"`
	// Customer-managed encryption key spec for a Metadata Store. If set, this Metadata Store and all sub-resources of this Metadata Store are secured using this key.
	EncryptionSpec *GoogleCloudAiplatformV1EncryptionSpec `pulumi:"encryptionSpec"`
	Location       *string                                `pulumi:"location"`
	// The {metadatastore} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all MetadataStores in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataStore.)
	MetadataStoreId *string `pulumi:"metadataStoreId"`
	Project         *string `pulumi:"project"`
}

// The set of arguments for constructing a MetadataStore resource.
type MetadataStoreArgs struct {
	// Description of the MetadataStore.
	Description pulumi.StringPtrInput
	// Customer-managed encryption key spec for a Metadata Store. If set, this Metadata Store and all sub-resources of this Metadata Store are secured using this key.
	EncryptionSpec GoogleCloudAiplatformV1EncryptionSpecPtrInput
	Location       pulumi.StringPtrInput
	// The {metadatastore} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all MetadataStores in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataStore.)
	MetadataStoreId pulumi.StringPtrInput
	Project         pulumi.StringPtrInput
}

func (MetadataStoreArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*metadataStoreArgs)(nil)).Elem()
}

type MetadataStoreInput interface {
	pulumi.Input

	ToMetadataStoreOutput() MetadataStoreOutput
	ToMetadataStoreOutputWithContext(ctx context.Context) MetadataStoreOutput
}

func (*MetadataStore) ElementType() reflect.Type {
	return reflect.TypeOf((**MetadataStore)(nil)).Elem()
}

func (i *MetadataStore) ToMetadataStoreOutput() MetadataStoreOutput {
	return i.ToMetadataStoreOutputWithContext(context.Background())
}

func (i *MetadataStore) ToMetadataStoreOutputWithContext(ctx context.Context) MetadataStoreOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MetadataStoreOutput)
}

type MetadataStoreOutput struct{ *pulumi.OutputState }

func (MetadataStoreOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**MetadataStore)(nil)).Elem()
}

func (o MetadataStoreOutput) ToMetadataStoreOutput() MetadataStoreOutput {
	return o
}

func (o MetadataStoreOutput) ToMetadataStoreOutputWithContext(ctx context.Context) MetadataStoreOutput {
	return o
}

// Timestamp when this MetadataStore was created.
func (o MetadataStoreOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *MetadataStore) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Description of the MetadataStore.
func (o MetadataStoreOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *MetadataStore) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Customer-managed encryption key spec for a Metadata Store. If set, this Metadata Store and all sub-resources of this Metadata Store are secured using this key.
func (o MetadataStoreOutput) EncryptionSpec() GoogleCloudAiplatformV1EncryptionSpecResponseOutput {
	return o.ApplyT(func(v *MetadataStore) GoogleCloudAiplatformV1EncryptionSpecResponseOutput { return v.EncryptionSpec }).(GoogleCloudAiplatformV1EncryptionSpecResponseOutput)
}

func (o MetadataStoreOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *MetadataStore) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// The {metadatastore} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all MetadataStores in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataStore.)
func (o MetadataStoreOutput) MetadataStoreId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *MetadataStore) pulumi.StringPtrOutput { return v.MetadataStoreId }).(pulumi.StringPtrOutput)
}

// The resource name of the MetadataStore instance.
func (o MetadataStoreOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *MetadataStore) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o MetadataStoreOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *MetadataStore) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// State information of the MetadataStore.
func (o MetadataStoreOutput) State() GoogleCloudAiplatformV1MetadataStoreMetadataStoreStateResponseOutput {
	return o.ApplyT(func(v *MetadataStore) GoogleCloudAiplatformV1MetadataStoreMetadataStoreStateResponseOutput {
		return v.State
	}).(GoogleCloudAiplatformV1MetadataStoreMetadataStoreStateResponseOutput)
}

// Timestamp when this MetadataStore was last updated.
func (o MetadataStoreOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *MetadataStore) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MetadataStoreInput)(nil)).Elem(), &MetadataStore{})
	pulumi.RegisterOutputType(MetadataStoreOutput{})
}