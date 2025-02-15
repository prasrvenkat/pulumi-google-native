// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets the details of a preference set.
func LookupPreferenceSet(ctx *pulumi.Context, args *LookupPreferenceSetArgs, opts ...pulumi.InvokeOption) (*LookupPreferenceSetResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPreferenceSetResult
	err := ctx.Invoke("google-native:migrationcenter/v1:getPreferenceSet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupPreferenceSetArgs struct {
	Location        string  `pulumi:"location"`
	PreferenceSetId string  `pulumi:"preferenceSetId"`
	Project         *string `pulumi:"project"`
}

type LookupPreferenceSetResult struct {
	// The timestamp when the preference set was created.
	CreateTime string `pulumi:"createTime"`
	// A description of the preference set.
	Description string `pulumi:"description"`
	// User-friendly display name. Maximum length is 63 characters.
	DisplayName string `pulumi:"displayName"`
	// Name of the preference set.
	Name string `pulumi:"name"`
	// The timestamp when the preference set was last updated.
	UpdateTime string `pulumi:"updateTime"`
	// A set of preferences that applies to all virtual machines in the context.
	VirtualMachinePreferences VirtualMachinePreferencesResponse `pulumi:"virtualMachinePreferences"`
}

func LookupPreferenceSetOutput(ctx *pulumi.Context, args LookupPreferenceSetOutputArgs, opts ...pulumi.InvokeOption) LookupPreferenceSetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPreferenceSetResult, error) {
			args := v.(LookupPreferenceSetArgs)
			r, err := LookupPreferenceSet(ctx, &args, opts...)
			var s LookupPreferenceSetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPreferenceSetResultOutput)
}

type LookupPreferenceSetOutputArgs struct {
	Location        pulumi.StringInput    `pulumi:"location"`
	PreferenceSetId pulumi.StringInput    `pulumi:"preferenceSetId"`
	Project         pulumi.StringPtrInput `pulumi:"project"`
}

func (LookupPreferenceSetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPreferenceSetArgs)(nil)).Elem()
}

type LookupPreferenceSetResultOutput struct{ *pulumi.OutputState }

func (LookupPreferenceSetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPreferenceSetResult)(nil)).Elem()
}

func (o LookupPreferenceSetResultOutput) ToLookupPreferenceSetResultOutput() LookupPreferenceSetResultOutput {
	return o
}

func (o LookupPreferenceSetResultOutput) ToLookupPreferenceSetResultOutputWithContext(ctx context.Context) LookupPreferenceSetResultOutput {
	return o
}

// The timestamp when the preference set was created.
func (o LookupPreferenceSetResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPreferenceSetResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// A description of the preference set.
func (o LookupPreferenceSetResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPreferenceSetResult) string { return v.Description }).(pulumi.StringOutput)
}

// User-friendly display name. Maximum length is 63 characters.
func (o LookupPreferenceSetResultOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPreferenceSetResult) string { return v.DisplayName }).(pulumi.StringOutput)
}

// Name of the preference set.
func (o LookupPreferenceSetResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPreferenceSetResult) string { return v.Name }).(pulumi.StringOutput)
}

// The timestamp when the preference set was last updated.
func (o LookupPreferenceSetResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPreferenceSetResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

// A set of preferences that applies to all virtual machines in the context.
func (o LookupPreferenceSetResultOutput) VirtualMachinePreferences() VirtualMachinePreferencesResponseOutput {
	return o.ApplyT(func(v LookupPreferenceSetResult) VirtualMachinePreferencesResponse {
		return v.VirtualMachinePreferences
	}).(VirtualMachinePreferencesResponseOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPreferenceSetResultOutput{})
}
