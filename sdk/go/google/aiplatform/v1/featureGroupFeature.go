// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a new Feature in a given FeatureGroup.
// Auto-naming is currently not supported for this resource.
type FeatureGroupFeature struct {
	pulumi.CustomResourceState

	// Only applicable for Vertex AI Feature Store (Legacy). Timestamp when this EntityType was created.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Description of the Feature.
	Description pulumi.StringOutput `pulumi:"description"`
	// Optional. Only applicable for Vertex AI Feature Store (Legacy). If not set, use the monitoring_config defined for the EntityType this Feature belongs to. Only Features with type (Feature.ValueType) BOOL, STRING, DOUBLE or INT64 can enable monitoring. If set to true, all types of data monitoring are disabled despite the config on EntityType.
	DisableMonitoring pulumi.BoolOutput `pulumi:"disableMonitoring"`
	// Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
	Etag           pulumi.StringOutput `pulumi:"etag"`
	FeatureGroupId pulumi.StringOutput `pulumi:"featureGroupId"`
	// Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.
	FeatureId pulumi.StringOutput `pulumi:"featureId"`
	// Optional. The labels with user-defined metadata to organize your Features. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one Feature (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
	Labels   pulumi.StringMapOutput `pulumi:"labels"`
	Location pulumi.StringOutput    `pulumi:"location"`
	// Only applicable for Vertex AI Feature Store (Legacy). The list of historical stats and anomalies with specified objectives.
	MonitoringStatsAnomalies GoogleCloudAiplatformV1FeatureMonitoringStatsAnomalyResponseArrayOutput `pulumi:"monitoringStatsAnomalies"`
	// Immutable. Name of the Feature. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}` The last part feature is assigned by the client. The feature can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given an entity type.
	Name    pulumi.StringOutput `pulumi:"name"`
	Project pulumi.StringOutput `pulumi:"project"`
	// Only applicable for Vertex AI Feature Store (Legacy). Timestamp when this EntityType was most recently updated.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
	// Immutable. Only applicable for Vertex AI Feature Store (Legacy). Type of Feature value.
	ValueType pulumi.StringOutput `pulumi:"valueType"`
	// Only applicable for Vertex AI Feature Store. The name of the BigQuery Table/View columnn hosting data for this version. If no value is provided, will use feature_id.
	VersionColumnName pulumi.StringOutput `pulumi:"versionColumnName"`
}

// NewFeatureGroupFeature registers a new resource with the given unique name, arguments, and options.
func NewFeatureGroupFeature(ctx *pulumi.Context,
	name string, args *FeatureGroupFeatureArgs, opts ...pulumi.ResourceOption) (*FeatureGroupFeature, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FeatureGroupId == nil {
		return nil, errors.New("invalid value for required argument 'FeatureGroupId'")
	}
	if args.FeatureId == nil {
		return nil, errors.New("invalid value for required argument 'FeatureId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"featureGroupId",
		"featureId",
		"location",
		"project",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource FeatureGroupFeature
	err := ctx.RegisterResource("google-native:aiplatform/v1:FeatureGroupFeature", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFeatureGroupFeature gets an existing FeatureGroupFeature resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFeatureGroupFeature(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FeatureGroupFeatureState, opts ...pulumi.ResourceOption) (*FeatureGroupFeature, error) {
	var resource FeatureGroupFeature
	err := ctx.ReadResource("google-native:aiplatform/v1:FeatureGroupFeature", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FeatureGroupFeature resources.
type featureGroupFeatureState struct {
}

type FeatureGroupFeatureState struct {
}

func (FeatureGroupFeatureState) ElementType() reflect.Type {
	return reflect.TypeOf((*featureGroupFeatureState)(nil)).Elem()
}

type featureGroupFeatureArgs struct {
	// Description of the Feature.
	Description *string `pulumi:"description"`
	// Optional. Only applicable for Vertex AI Feature Store (Legacy). If not set, use the monitoring_config defined for the EntityType this Feature belongs to. Only Features with type (Feature.ValueType) BOOL, STRING, DOUBLE or INT64 can enable monitoring. If set to true, all types of data monitoring are disabled despite the config on EntityType.
	DisableMonitoring *bool `pulumi:"disableMonitoring"`
	// Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
	Etag           *string `pulumi:"etag"`
	FeatureGroupId string  `pulumi:"featureGroupId"`
	// Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.
	FeatureId string `pulumi:"featureId"`
	// Optional. The labels with user-defined metadata to organize your Features. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one Feature (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
	Labels   map[string]string `pulumi:"labels"`
	Location *string           `pulumi:"location"`
	// Immutable. Name of the Feature. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}` The last part feature is assigned by the client. The feature can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given an entity type.
	Name    *string `pulumi:"name"`
	Project *string `pulumi:"project"`
	// Immutable. Only applicable for Vertex AI Feature Store (Legacy). Type of Feature value.
	ValueType *FeatureGroupFeatureValueType `pulumi:"valueType"`
	// Only applicable for Vertex AI Feature Store. The name of the BigQuery Table/View columnn hosting data for this version. If no value is provided, will use feature_id.
	VersionColumnName *string `pulumi:"versionColumnName"`
}

// The set of arguments for constructing a FeatureGroupFeature resource.
type FeatureGroupFeatureArgs struct {
	// Description of the Feature.
	Description pulumi.StringPtrInput
	// Optional. Only applicable for Vertex AI Feature Store (Legacy). If not set, use the monitoring_config defined for the EntityType this Feature belongs to. Only Features with type (Feature.ValueType) BOOL, STRING, DOUBLE or INT64 can enable monitoring. If set to true, all types of data monitoring are disabled despite the config on EntityType.
	DisableMonitoring pulumi.BoolPtrInput
	// Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
	Etag           pulumi.StringPtrInput
	FeatureGroupId pulumi.StringInput
	// Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.
	FeatureId pulumi.StringInput
	// Optional. The labels with user-defined metadata to organize your Features. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one Feature (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
	Labels   pulumi.StringMapInput
	Location pulumi.StringPtrInput
	// Immutable. Name of the Feature. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}` The last part feature is assigned by the client. The feature can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given an entity type.
	Name    pulumi.StringPtrInput
	Project pulumi.StringPtrInput
	// Immutable. Only applicable for Vertex AI Feature Store (Legacy). Type of Feature value.
	ValueType FeatureGroupFeatureValueTypePtrInput
	// Only applicable for Vertex AI Feature Store. The name of the BigQuery Table/View columnn hosting data for this version. If no value is provided, will use feature_id.
	VersionColumnName pulumi.StringPtrInput
}

func (FeatureGroupFeatureArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*featureGroupFeatureArgs)(nil)).Elem()
}

type FeatureGroupFeatureInput interface {
	pulumi.Input

	ToFeatureGroupFeatureOutput() FeatureGroupFeatureOutput
	ToFeatureGroupFeatureOutputWithContext(ctx context.Context) FeatureGroupFeatureOutput
}

func (*FeatureGroupFeature) ElementType() reflect.Type {
	return reflect.TypeOf((**FeatureGroupFeature)(nil)).Elem()
}

func (i *FeatureGroupFeature) ToFeatureGroupFeatureOutput() FeatureGroupFeatureOutput {
	return i.ToFeatureGroupFeatureOutputWithContext(context.Background())
}

func (i *FeatureGroupFeature) ToFeatureGroupFeatureOutputWithContext(ctx context.Context) FeatureGroupFeatureOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FeatureGroupFeatureOutput)
}

type FeatureGroupFeatureOutput struct{ *pulumi.OutputState }

func (FeatureGroupFeatureOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**FeatureGroupFeature)(nil)).Elem()
}

func (o FeatureGroupFeatureOutput) ToFeatureGroupFeatureOutput() FeatureGroupFeatureOutput {
	return o
}

func (o FeatureGroupFeatureOutput) ToFeatureGroupFeatureOutputWithContext(ctx context.Context) FeatureGroupFeatureOutput {
	return o
}

// Only applicable for Vertex AI Feature Store (Legacy). Timestamp when this EntityType was created.
func (o FeatureGroupFeatureOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Description of the Feature.
func (o FeatureGroupFeatureOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Optional. Only applicable for Vertex AI Feature Store (Legacy). If not set, use the monitoring_config defined for the EntityType this Feature belongs to. Only Features with type (Feature.ValueType) BOOL, STRING, DOUBLE or INT64 can enable monitoring. If set to true, all types of data monitoring are disabled despite the config on EntityType.
func (o FeatureGroupFeatureOutput) DisableMonitoring() pulumi.BoolOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.BoolOutput { return v.DisableMonitoring }).(pulumi.BoolOutput)
}

// Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
func (o FeatureGroupFeatureOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

func (o FeatureGroupFeatureOutput) FeatureGroupId() pulumi.StringOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringOutput { return v.FeatureGroupId }).(pulumi.StringOutput)
}

// Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.
func (o FeatureGroupFeatureOutput) FeatureId() pulumi.StringOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringOutput { return v.FeatureId }).(pulumi.StringOutput)
}

// Optional. The labels with user-defined metadata to organize your Features. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one Feature (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
func (o FeatureGroupFeatureOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

func (o FeatureGroupFeatureOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// Only applicable for Vertex AI Feature Store (Legacy). The list of historical stats and anomalies with specified objectives.
func (o FeatureGroupFeatureOutput) MonitoringStatsAnomalies() GoogleCloudAiplatformV1FeatureMonitoringStatsAnomalyResponseArrayOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) GoogleCloudAiplatformV1FeatureMonitoringStatsAnomalyResponseArrayOutput {
		return v.MonitoringStatsAnomalies
	}).(GoogleCloudAiplatformV1FeatureMonitoringStatsAnomalyResponseArrayOutput)
}

// Immutable. Name of the Feature. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}` The last part feature is assigned by the client. The feature can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given an entity type.
func (o FeatureGroupFeatureOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o FeatureGroupFeatureOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// Only applicable for Vertex AI Feature Store (Legacy). Timestamp when this EntityType was most recently updated.
func (o FeatureGroupFeatureOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

// Immutable. Only applicable for Vertex AI Feature Store (Legacy). Type of Feature value.
func (o FeatureGroupFeatureOutput) ValueType() pulumi.StringOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringOutput { return v.ValueType }).(pulumi.StringOutput)
}

// Only applicable for Vertex AI Feature Store. The name of the BigQuery Table/View columnn hosting data for this version. If no value is provided, will use feature_id.
func (o FeatureGroupFeatureOutput) VersionColumnName() pulumi.StringOutput {
	return o.ApplyT(func(v *FeatureGroupFeature) pulumi.StringOutput { return v.VersionColumnName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FeatureGroupFeatureInput)(nil)).Elem(), &FeatureGroupFeature{})
	pulumi.RegisterOutputType(FeatureGroupFeatureOutput{})
}