// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates an Index.
// Auto-naming is currently not supported for this resource.
type Index struct {
	pulumi.CustomResourceState

	// Timestamp when this Index was created.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// The pointers to DeployedIndexes created from this Index. An Index can be only deleted if all its DeployedIndexes had been undeployed first.
	DeployedIndexes GoogleCloudAiplatformV1beta1DeployedIndexRefResponseArrayOutput `pulumi:"deployedIndexes"`
	// The description of the Index.
	Description pulumi.StringOutput `pulumi:"description"`
	// The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// Immutable. Customer-managed encryption key spec for an Index. If set, this Index and all sub-resources of this Index will be secured by this key.
	EncryptionSpec GoogleCloudAiplatformV1beta1EncryptionSpecResponseOutput `pulumi:"encryptionSpec"`
	// Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// Stats of the index resource.
	IndexStats GoogleCloudAiplatformV1beta1IndexStatsResponseOutput `pulumi:"indexStats"`
	// Immutable. The update method to use with this Index. If not set, BATCH_UPDATE will be used by default.
	IndexUpdateMethod pulumi.StringOutput `pulumi:"indexUpdateMethod"`
	// The labels with user-defined metadata to organize your Indexes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
	Labels   pulumi.StringMapOutput `pulumi:"labels"`
	Location pulumi.StringOutput    `pulumi:"location"`
	// An additional information about the Index; the schema of the metadata can be found in metadata_schema.
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Index, that is specific to it. Unset if the Index does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.
	MetadataSchemaUri pulumi.StringOutput `pulumi:"metadataSchemaUri"`
	// The resource name of the Index.
	Name    pulumi.StringOutput `pulumi:"name"`
	Project pulumi.StringOutput `pulumi:"project"`
	// Timestamp when this Index was most recently updated. This also includes any update to the contents of the Index. Note that Operations working on this Index may have their Operations.metadata.generic_metadata.update_time a little after the value of this timestamp, yet that does not mean their results are not already reflected in the Index. Result of any successfully completed Operation on the Index is reflected in it.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
}

// NewIndex registers a new resource with the given unique name, arguments, and options.
func NewIndex(ctx *pulumi.Context,
	name string, args *IndexArgs, opts ...pulumi.ResourceOption) (*Index, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DisplayName == nil {
		return nil, errors.New("invalid value for required argument 'DisplayName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"location",
		"project",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Index
	err := ctx.RegisterResource("google-native:aiplatform/v1beta1:Index", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIndex gets an existing Index resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIndex(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IndexState, opts ...pulumi.ResourceOption) (*Index, error) {
	var resource Index
	err := ctx.ReadResource("google-native:aiplatform/v1beta1:Index", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Index resources.
type indexState struct {
}

type IndexState struct {
}

func (IndexState) ElementType() reflect.Type {
	return reflect.TypeOf((*indexState)(nil)).Elem()
}

type indexArgs struct {
	// The description of the Index.
	Description *string `pulumi:"description"`
	// The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.
	DisplayName string `pulumi:"displayName"`
	// Immutable. Customer-managed encryption key spec for an Index. If set, this Index and all sub-resources of this Index will be secured by this key.
	EncryptionSpec *GoogleCloudAiplatformV1beta1EncryptionSpec `pulumi:"encryptionSpec"`
	// Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
	Etag *string `pulumi:"etag"`
	// Immutable. The update method to use with this Index. If not set, BATCH_UPDATE will be used by default.
	IndexUpdateMethod *IndexIndexUpdateMethod `pulumi:"indexUpdateMethod"`
	// The labels with user-defined metadata to organize your Indexes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
	Labels   map[string]string `pulumi:"labels"`
	Location *string           `pulumi:"location"`
	// An additional information about the Index; the schema of the metadata can be found in metadata_schema.
	Metadata interface{} `pulumi:"metadata"`
	// Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Index, that is specific to it. Unset if the Index does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.
	MetadataSchemaUri *string `pulumi:"metadataSchemaUri"`
	Project           *string `pulumi:"project"`
}

// The set of arguments for constructing a Index resource.
type IndexArgs struct {
	// The description of the Index.
	Description pulumi.StringPtrInput
	// The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.
	DisplayName pulumi.StringInput
	// Immutable. Customer-managed encryption key spec for an Index. If set, this Index and all sub-resources of this Index will be secured by this key.
	EncryptionSpec GoogleCloudAiplatformV1beta1EncryptionSpecPtrInput
	// Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
	Etag pulumi.StringPtrInput
	// Immutable. The update method to use with this Index. If not set, BATCH_UPDATE will be used by default.
	IndexUpdateMethod IndexIndexUpdateMethodPtrInput
	// The labels with user-defined metadata to organize your Indexes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
	Labels   pulumi.StringMapInput
	Location pulumi.StringPtrInput
	// An additional information about the Index; the schema of the metadata can be found in metadata_schema.
	Metadata pulumi.Input
	// Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Index, that is specific to it. Unset if the Index does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.
	MetadataSchemaUri pulumi.StringPtrInput
	Project           pulumi.StringPtrInput
}

func (IndexArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*indexArgs)(nil)).Elem()
}

type IndexInput interface {
	pulumi.Input

	ToIndexOutput() IndexOutput
	ToIndexOutputWithContext(ctx context.Context) IndexOutput
}

func (*Index) ElementType() reflect.Type {
	return reflect.TypeOf((**Index)(nil)).Elem()
}

func (i *Index) ToIndexOutput() IndexOutput {
	return i.ToIndexOutputWithContext(context.Background())
}

func (i *Index) ToIndexOutputWithContext(ctx context.Context) IndexOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IndexOutput)
}

type IndexOutput struct{ *pulumi.OutputState }

func (IndexOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Index)(nil)).Elem()
}

func (o IndexOutput) ToIndexOutput() IndexOutput {
	return o
}

func (o IndexOutput) ToIndexOutputWithContext(ctx context.Context) IndexOutput {
	return o
}

// Timestamp when this Index was created.
func (o IndexOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Index) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// The pointers to DeployedIndexes created from this Index. An Index can be only deleted if all its DeployedIndexes had been undeployed first.
func (o IndexOutput) DeployedIndexes() GoogleCloudAiplatformV1beta1DeployedIndexRefResponseArrayOutput {
	return o.ApplyT(func(v *Index) GoogleCloudAiplatformV1beta1DeployedIndexRefResponseArrayOutput {
		return v.DeployedIndexes
	}).(GoogleCloudAiplatformV1beta1DeployedIndexRefResponseArrayOutput)
}

// The description of the Index.
func (o IndexOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *Index) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.
func (o IndexOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *Index) pulumi.StringOutput { return v.DisplayName }).(pulumi.StringOutput)
}

// Immutable. Customer-managed encryption key spec for an Index. If set, this Index and all sub-resources of this Index will be secured by this key.
func (o IndexOutput) EncryptionSpec() GoogleCloudAiplatformV1beta1EncryptionSpecResponseOutput {
	return o.ApplyT(func(v *Index) GoogleCloudAiplatformV1beta1EncryptionSpecResponseOutput { return v.EncryptionSpec }).(GoogleCloudAiplatformV1beta1EncryptionSpecResponseOutput)
}

// Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
func (o IndexOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *Index) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

// Stats of the index resource.
func (o IndexOutput) IndexStats() GoogleCloudAiplatformV1beta1IndexStatsResponseOutput {
	return o.ApplyT(func(v *Index) GoogleCloudAiplatformV1beta1IndexStatsResponseOutput { return v.IndexStats }).(GoogleCloudAiplatformV1beta1IndexStatsResponseOutput)
}

// Immutable. The update method to use with this Index. If not set, BATCH_UPDATE will be used by default.
func (o IndexOutput) IndexUpdateMethod() pulumi.StringOutput {
	return o.ApplyT(func(v *Index) pulumi.StringOutput { return v.IndexUpdateMethod }).(pulumi.StringOutput)
}

// The labels with user-defined metadata to organize your Indexes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
func (o IndexOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Index) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

func (o IndexOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *Index) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// An additional information about the Index; the schema of the metadata can be found in metadata_schema.
func (o IndexOutput) Metadata() pulumi.AnyOutput {
	return o.ApplyT(func(v *Index) pulumi.AnyOutput { return v.Metadata }).(pulumi.AnyOutput)
}

// Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Index, that is specific to it. Unset if the Index does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.
func (o IndexOutput) MetadataSchemaUri() pulumi.StringOutput {
	return o.ApplyT(func(v *Index) pulumi.StringOutput { return v.MetadataSchemaUri }).(pulumi.StringOutput)
}

// The resource name of the Index.
func (o IndexOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Index) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o IndexOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *Index) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// Timestamp when this Index was most recently updated. This also includes any update to the contents of the Index. Note that Operations working on this Index may have their Operations.metadata.generic_metadata.update_time a little after the value of this timestamp, yet that does not mean their results are not already reflected in the Index. Result of any successfully completed Operation on the Index is reflected in it.
func (o IndexOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Index) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IndexInput)(nil)).Elem(), &Index{})
	pulumi.RegisterOutputType(IndexOutput{})
}