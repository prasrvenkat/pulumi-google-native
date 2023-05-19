// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a new Evaluation in a given project and location.
// Note - this resource's API doesn't support deletion. When deleted, the resource will persist
// on Google Cloud even though it will be deleted from Pulumi state.
type Evaluation struct {
	pulumi.CustomResourceState

	// [Output only] Create time stamp
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Description of the Evaluation
	Description pulumi.StringOutput `pulumi:"description"`
	// Required. Id of the requesting object
	EvaluationId pulumi.StringOutput `pulumi:"evaluationId"`
	// Labels as key value pairs
	Labels   pulumi.StringMapOutput `pulumi:"labels"`
	Location pulumi.StringOutput    `pulumi:"location"`
	// name of resource names have the form 'projects/{project_id}/locations/{location_id}/evaluations/{evaluation_id}'
	Name    pulumi.StringOutput `pulumi:"name"`
	Project pulumi.StringOutput `pulumi:"project"`
	// Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
	RequestId pulumi.StringPtrOutput `pulumi:"requestId"`
	// annotations as key value pairs
	ResourceFilter ResourceFilterResponseOutput `pulumi:"resourceFilter"`
	// [Output only] The updated rule ids if exist.
	ResourceStatus ResourceStatusResponseOutput `pulumi:"resourceStatus"`
	// the name of the rule
	RuleNames pulumi.StringArrayOutput `pulumi:"ruleNames"`
	// [Output only] The updated rule ids if exist.
	RuleVersions pulumi.StringArrayOutput `pulumi:"ruleVersions"`
	// crontab format schedule for scheduled evaluation, example: 0 */3 * * *
	Schedule pulumi.StringOutput `pulumi:"schedule"`
	// [Output only] Update time stamp
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
}

// NewEvaluation registers a new resource with the given unique name, arguments, and options.
func NewEvaluation(ctx *pulumi.Context,
	name string, args *EvaluationArgs, opts ...pulumi.ResourceOption) (*Evaluation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.EvaluationId == nil {
		return nil, errors.New("invalid value for required argument 'EvaluationId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"evaluationId",
		"location",
		"project",
	})
	opts = append(opts, replaceOnChanges)
	var resource Evaluation
	err := ctx.RegisterResource("google-native:workloadmanager/v1:Evaluation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEvaluation gets an existing Evaluation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEvaluation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EvaluationState, opts ...pulumi.ResourceOption) (*Evaluation, error) {
	var resource Evaluation
	err := ctx.ReadResource("google-native:workloadmanager/v1:Evaluation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Evaluation resources.
type evaluationState struct {
}

type EvaluationState struct {
}

func (EvaluationState) ElementType() reflect.Type {
	return reflect.TypeOf((*evaluationState)(nil)).Elem()
}

type evaluationArgs struct {
	// Description of the Evaluation
	Description *string `pulumi:"description"`
	// Required. Id of the requesting object
	EvaluationId string `pulumi:"evaluationId"`
	// Labels as key value pairs
	Labels   map[string]string `pulumi:"labels"`
	Location *string           `pulumi:"location"`
	// name of resource names have the form 'projects/{project_id}/locations/{location_id}/evaluations/{evaluation_id}'
	Name    *string `pulumi:"name"`
	Project *string `pulumi:"project"`
	// Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
	RequestId *string `pulumi:"requestId"`
	// annotations as key value pairs
	ResourceFilter *ResourceFilter `pulumi:"resourceFilter"`
	// the name of the rule
	RuleNames []string `pulumi:"ruleNames"`
	// crontab format schedule for scheduled evaluation, example: 0 */3 * * *
	Schedule *string `pulumi:"schedule"`
}

// The set of arguments for constructing a Evaluation resource.
type EvaluationArgs struct {
	// Description of the Evaluation
	Description pulumi.StringPtrInput
	// Required. Id of the requesting object
	EvaluationId pulumi.StringInput
	// Labels as key value pairs
	Labels   pulumi.StringMapInput
	Location pulumi.StringPtrInput
	// name of resource names have the form 'projects/{project_id}/locations/{location_id}/evaluations/{evaluation_id}'
	Name    pulumi.StringPtrInput
	Project pulumi.StringPtrInput
	// Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
	RequestId pulumi.StringPtrInput
	// annotations as key value pairs
	ResourceFilter ResourceFilterPtrInput
	// the name of the rule
	RuleNames pulumi.StringArrayInput
	// crontab format schedule for scheduled evaluation, example: 0 */3 * * *
	Schedule pulumi.StringPtrInput
}

func (EvaluationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*evaluationArgs)(nil)).Elem()
}

type EvaluationInput interface {
	pulumi.Input

	ToEvaluationOutput() EvaluationOutput
	ToEvaluationOutputWithContext(ctx context.Context) EvaluationOutput
}

func (*Evaluation) ElementType() reflect.Type {
	return reflect.TypeOf((**Evaluation)(nil)).Elem()
}

func (i *Evaluation) ToEvaluationOutput() EvaluationOutput {
	return i.ToEvaluationOutputWithContext(context.Background())
}

func (i *Evaluation) ToEvaluationOutputWithContext(ctx context.Context) EvaluationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EvaluationOutput)
}

type EvaluationOutput struct{ *pulumi.OutputState }

func (EvaluationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Evaluation)(nil)).Elem()
}

func (o EvaluationOutput) ToEvaluationOutput() EvaluationOutput {
	return o
}

func (o EvaluationOutput) ToEvaluationOutputWithContext(ctx context.Context) EvaluationOutput {
	return o
}

// [Output only] Create time stamp
func (o EvaluationOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Description of the Evaluation
func (o EvaluationOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Required. Id of the requesting object
func (o EvaluationOutput) EvaluationId() pulumi.StringOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringOutput { return v.EvaluationId }).(pulumi.StringOutput)
}

// Labels as key value pairs
func (o EvaluationOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

func (o EvaluationOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// name of resource names have the form 'projects/{project_id}/locations/{location_id}/evaluations/{evaluation_id}'
func (o EvaluationOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o EvaluationOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
func (o EvaluationOutput) RequestId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringPtrOutput { return v.RequestId }).(pulumi.StringPtrOutput)
}

// annotations as key value pairs
func (o EvaluationOutput) ResourceFilter() ResourceFilterResponseOutput {
	return o.ApplyT(func(v *Evaluation) ResourceFilterResponseOutput { return v.ResourceFilter }).(ResourceFilterResponseOutput)
}

// [Output only] The updated rule ids if exist.
func (o EvaluationOutput) ResourceStatus() ResourceStatusResponseOutput {
	return o.ApplyT(func(v *Evaluation) ResourceStatusResponseOutput { return v.ResourceStatus }).(ResourceStatusResponseOutput)
}

// the name of the rule
func (o EvaluationOutput) RuleNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringArrayOutput { return v.RuleNames }).(pulumi.StringArrayOutput)
}

// [Output only] The updated rule ids if exist.
func (o EvaluationOutput) RuleVersions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringArrayOutput { return v.RuleVersions }).(pulumi.StringArrayOutput)
}

// crontab format schedule for scheduled evaluation, example: 0 */3 * * *
func (o EvaluationOutput) Schedule() pulumi.StringOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringOutput { return v.Schedule }).(pulumi.StringOutput)
}

// [Output only] Update time stamp
func (o EvaluationOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Evaluation) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EvaluationInput)(nil)).Elem(), &Evaluation{})
	pulumi.RegisterOutputType(EvaluationOutput{})
}