// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Sets the access control policy on the specified resource. Replaces any existing policy.Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.
type RegionAutoscalingPolicyIamPolicy struct {
	pulumi.CustomResourceState

	// Associates a list of members to a role. Optionally, may specify a condition that determines how and when the bindings are applied. Each of the bindings must contain at least one member.
	Bindings BindingResponseArrayOutput `pulumi:"bindings"`
	// etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An etag is returned in the response to getIamPolicy, and systems are expected to put that etag in the request to setIamPolicy to ensure that their change will be applied to the same version of the policy.Important: If you use IAM Conditions, you must include the etag field whenever you call setIamPolicy. If you omit this field, then IAM allows you to overwrite a version 3 policy with a version 1 policy, and all of the conditions in the version 3 policy are lost.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// Specifies the format of the policy.Valid values are 0, 1, and 3. Requests that specify an invalid value are rejected.Any operation that affects conditional role bindings must specify version 3. This requirement applies to the following operations: Getting a policy that includes a conditional role binding Adding a conditional role binding to a policy Changing a conditional role binding in a policy Removing any role binding, with or without a condition, from a policy that includes conditionsImportant: If you use IAM Conditions, you must include the etag field whenever you call setIamPolicy. If you omit this field, then IAM allows you to overwrite a version 3 policy with a version 1 policy, and all of the conditions in the version 3 policy are lost.If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset.To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).
	Version pulumi.IntOutput `pulumi:"version"`
}

// NewRegionAutoscalingPolicyIamPolicy registers a new resource with the given unique name, arguments, and options.
func NewRegionAutoscalingPolicyIamPolicy(ctx *pulumi.Context,
	name string, args *RegionAutoscalingPolicyIamPolicyArgs, opts ...pulumi.ResourceOption) (*RegionAutoscalingPolicyIamPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AutoscalingPoliciesId == nil {
		return nil, errors.New("invalid value for required argument 'AutoscalingPoliciesId'")
	}
	if args.ProjectsId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectsId'")
	}
	if args.RegionsId == nil {
		return nil, errors.New("invalid value for required argument 'RegionsId'")
	}
	var resource RegionAutoscalingPolicyIamPolicy
	err := ctx.RegisterResource("google-cloud:dataproc/v1beta2:RegionAutoscalingPolicyIamPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRegionAutoscalingPolicyIamPolicy gets an existing RegionAutoscalingPolicyIamPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRegionAutoscalingPolicyIamPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RegionAutoscalingPolicyIamPolicyState, opts ...pulumi.ResourceOption) (*RegionAutoscalingPolicyIamPolicy, error) {
	var resource RegionAutoscalingPolicyIamPolicy
	err := ctx.ReadResource("google-cloud:dataproc/v1beta2:RegionAutoscalingPolicyIamPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RegionAutoscalingPolicyIamPolicy resources.
type regionAutoscalingPolicyIamPolicyState struct {
	// Associates a list of members to a role. Optionally, may specify a condition that determines how and when the bindings are applied. Each of the bindings must contain at least one member.
	Bindings []BindingResponse `pulumi:"bindings"`
	// etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An etag is returned in the response to getIamPolicy, and systems are expected to put that etag in the request to setIamPolicy to ensure that their change will be applied to the same version of the policy.Important: If you use IAM Conditions, you must include the etag field whenever you call setIamPolicy. If you omit this field, then IAM allows you to overwrite a version 3 policy with a version 1 policy, and all of the conditions in the version 3 policy are lost.
	Etag *string `pulumi:"etag"`
	// Specifies the format of the policy.Valid values are 0, 1, and 3. Requests that specify an invalid value are rejected.Any operation that affects conditional role bindings must specify version 3. This requirement applies to the following operations: Getting a policy that includes a conditional role binding Adding a conditional role binding to a policy Changing a conditional role binding in a policy Removing any role binding, with or without a condition, from a policy that includes conditionsImportant: If you use IAM Conditions, you must include the etag field whenever you call setIamPolicy. If you omit this field, then IAM allows you to overwrite a version 3 policy with a version 1 policy, and all of the conditions in the version 3 policy are lost.If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset.To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).
	Version *int `pulumi:"version"`
}

type RegionAutoscalingPolicyIamPolicyState struct {
	// Associates a list of members to a role. Optionally, may specify a condition that determines how and when the bindings are applied. Each of the bindings must contain at least one member.
	Bindings BindingResponseArrayInput
	// etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An etag is returned in the response to getIamPolicy, and systems are expected to put that etag in the request to setIamPolicy to ensure that their change will be applied to the same version of the policy.Important: If you use IAM Conditions, you must include the etag field whenever you call setIamPolicy. If you omit this field, then IAM allows you to overwrite a version 3 policy with a version 1 policy, and all of the conditions in the version 3 policy are lost.
	Etag pulumi.StringPtrInput
	// Specifies the format of the policy.Valid values are 0, 1, and 3. Requests that specify an invalid value are rejected.Any operation that affects conditional role bindings must specify version 3. This requirement applies to the following operations: Getting a policy that includes a conditional role binding Adding a conditional role binding to a policy Changing a conditional role binding in a policy Removing any role binding, with or without a condition, from a policy that includes conditionsImportant: If you use IAM Conditions, you must include the etag field whenever you call setIamPolicy. If you omit this field, then IAM allows you to overwrite a version 3 policy with a version 1 policy, and all of the conditions in the version 3 policy are lost.If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset.To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).
	Version pulumi.IntPtrInput
}

func (RegionAutoscalingPolicyIamPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*regionAutoscalingPolicyIamPolicyState)(nil)).Elem()
}

type regionAutoscalingPolicyIamPolicyArgs struct {
	AutoscalingPoliciesId string `pulumi:"autoscalingPoliciesId"`
	// REQUIRED: The complete policy to be applied to the resource. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.
	Policy     *Policy `pulumi:"policy"`
	ProjectsId string  `pulumi:"projectsId"`
	RegionsId  string  `pulumi:"regionsId"`
}

// The set of arguments for constructing a RegionAutoscalingPolicyIamPolicy resource.
type RegionAutoscalingPolicyIamPolicyArgs struct {
	AutoscalingPoliciesId pulumi.StringInput
	// REQUIRED: The complete policy to be applied to the resource. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.
	Policy     PolicyPtrInput
	ProjectsId pulumi.StringInput
	RegionsId  pulumi.StringInput
}

func (RegionAutoscalingPolicyIamPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*regionAutoscalingPolicyIamPolicyArgs)(nil)).Elem()
}

type RegionAutoscalingPolicyIamPolicyInput interface {
	pulumi.Input

	ToRegionAutoscalingPolicyIamPolicyOutput() RegionAutoscalingPolicyIamPolicyOutput
	ToRegionAutoscalingPolicyIamPolicyOutputWithContext(ctx context.Context) RegionAutoscalingPolicyIamPolicyOutput
}

func (*RegionAutoscalingPolicyIamPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((*RegionAutoscalingPolicyIamPolicy)(nil))
}

func (i *RegionAutoscalingPolicyIamPolicy) ToRegionAutoscalingPolicyIamPolicyOutput() RegionAutoscalingPolicyIamPolicyOutput {
	return i.ToRegionAutoscalingPolicyIamPolicyOutputWithContext(context.Background())
}

func (i *RegionAutoscalingPolicyIamPolicy) ToRegionAutoscalingPolicyIamPolicyOutputWithContext(ctx context.Context) RegionAutoscalingPolicyIamPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RegionAutoscalingPolicyIamPolicyOutput)
}

type RegionAutoscalingPolicyIamPolicyOutput struct {
	*pulumi.OutputState
}

func (RegionAutoscalingPolicyIamPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RegionAutoscalingPolicyIamPolicy)(nil))
}

func (o RegionAutoscalingPolicyIamPolicyOutput) ToRegionAutoscalingPolicyIamPolicyOutput() RegionAutoscalingPolicyIamPolicyOutput {
	return o
}

func (o RegionAutoscalingPolicyIamPolicyOutput) ToRegionAutoscalingPolicyIamPolicyOutputWithContext(ctx context.Context) RegionAutoscalingPolicyIamPolicyOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(RegionAutoscalingPolicyIamPolicyOutput{})
}