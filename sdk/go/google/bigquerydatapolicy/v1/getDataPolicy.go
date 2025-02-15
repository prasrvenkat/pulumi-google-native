// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets the data policy specified by its resource name.
func LookupDataPolicy(ctx *pulumi.Context, args *LookupDataPolicyArgs, opts ...pulumi.InvokeOption) (*LookupDataPolicyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDataPolicyResult
	err := ctx.Invoke("google-native:bigquerydatapolicy/v1:getDataPolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDataPolicyArgs struct {
	DataPolicyId string  `pulumi:"dataPolicyId"`
	Location     string  `pulumi:"location"`
	Project      *string `pulumi:"project"`
}

type LookupDataPolicyResult struct {
	// The data masking policy that specifies the data masking rule to use.
	DataMaskingPolicy DataMaskingPolicyResponse `pulumi:"dataMaskingPolicy"`
	// User-assigned (human readable) ID of the data policy that needs to be unique within a project. Used as {data_policy_id} in part of the resource name.
	DataPolicyId string `pulumi:"dataPolicyId"`
	// Type of data policy.
	DataPolicyType string `pulumi:"dataPolicyType"`
	// Resource name of this data policy, in the format of `projects/{project_number}/locations/{location_id}/dataPolicies/{data_policy_id}`.
	Name string `pulumi:"name"`
	// Policy tag resource name, in the format of `projects/{project_number}/locations/{location_id}/taxonomies/{taxonomy_id}/policyTags/{policyTag_id}`.
	PolicyTag string `pulumi:"policyTag"`
}

func LookupDataPolicyOutput(ctx *pulumi.Context, args LookupDataPolicyOutputArgs, opts ...pulumi.InvokeOption) LookupDataPolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDataPolicyResult, error) {
			args := v.(LookupDataPolicyArgs)
			r, err := LookupDataPolicy(ctx, &args, opts...)
			var s LookupDataPolicyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDataPolicyResultOutput)
}

type LookupDataPolicyOutputArgs struct {
	DataPolicyId pulumi.StringInput    `pulumi:"dataPolicyId"`
	Location     pulumi.StringInput    `pulumi:"location"`
	Project      pulumi.StringPtrInput `pulumi:"project"`
}

func (LookupDataPolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataPolicyArgs)(nil)).Elem()
}

type LookupDataPolicyResultOutput struct{ *pulumi.OutputState }

func (LookupDataPolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataPolicyResult)(nil)).Elem()
}

func (o LookupDataPolicyResultOutput) ToLookupDataPolicyResultOutput() LookupDataPolicyResultOutput {
	return o
}

func (o LookupDataPolicyResultOutput) ToLookupDataPolicyResultOutputWithContext(ctx context.Context) LookupDataPolicyResultOutput {
	return o
}

// The data masking policy that specifies the data masking rule to use.
func (o LookupDataPolicyResultOutput) DataMaskingPolicy() DataMaskingPolicyResponseOutput {
	return o.ApplyT(func(v LookupDataPolicyResult) DataMaskingPolicyResponse { return v.DataMaskingPolicy }).(DataMaskingPolicyResponseOutput)
}

// User-assigned (human readable) ID of the data policy that needs to be unique within a project. Used as {data_policy_id} in part of the resource name.
func (o LookupDataPolicyResultOutput) DataPolicyId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataPolicyResult) string { return v.DataPolicyId }).(pulumi.StringOutput)
}

// Type of data policy.
func (o LookupDataPolicyResultOutput) DataPolicyType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataPolicyResult) string { return v.DataPolicyType }).(pulumi.StringOutput)
}

// Resource name of this data policy, in the format of `projects/{project_number}/locations/{location_id}/dataPolicies/{data_policy_id}`.
func (o LookupDataPolicyResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataPolicyResult) string { return v.Name }).(pulumi.StringOutput)
}

// Policy tag resource name, in the format of `projects/{project_number}/locations/{location_id}/taxonomies/{taxonomy_id}/policyTags/{policyTag_id}`.
func (o LookupDataPolicyResultOutput) PolicyTag() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDataPolicyResult) string { return v.PolicyTag }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDataPolicyResultOutput{})
}
