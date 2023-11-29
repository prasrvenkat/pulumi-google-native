// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Returns the details of a fleet.
func LookupFleet(ctx *pulumi.Context, args *LookupFleetArgs, opts ...pulumi.InvokeOption) (*LookupFleetResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupFleetResult
	err := ctx.Invoke("google-native:gkehub/v1:getFleet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupFleetArgs struct {
	FleetId  string  `pulumi:"fleetId"`
	Location string  `pulumi:"location"`
	Project  *string `pulumi:"project"`
}

type LookupFleetResult struct {
	// When the Fleet was created.
	CreateTime string `pulumi:"createTime"`
	// Optional. The default cluster configurations to apply across the fleet.
	DefaultClusterConfig DefaultClusterConfigResponse `pulumi:"defaultClusterConfig"`
	// When the Fleet was deleted.
	DeleteTime string `pulumi:"deleteTime"`
	// Optional. A user-assigned display name of the Fleet. When present, it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. Example: `Production Fleet`
	DisplayName string `pulumi:"displayName"`
	// Optional. Labels for this Fleet.
	Labels map[string]string `pulumi:"labels"`
	// The full, unique resource name of this fleet in the format of `projects/{project}/locations/{location}/fleets/{fleet}`. Each Google Cloud project can have at most one fleet resource, named "default".
	Name string `pulumi:"name"`
	// State of the namespace resource.
	State FleetLifecycleStateResponse `pulumi:"state"`
	// Google-generated UUID for this resource. This is unique across all Fleet resources. If a Fleet resource is deleted and another resource with the same name is created, it gets a different uid.
	Uid string `pulumi:"uid"`
	// When the Fleet was last updated.
	UpdateTime string `pulumi:"updateTime"`
}

func LookupFleetOutput(ctx *pulumi.Context, args LookupFleetOutputArgs, opts ...pulumi.InvokeOption) LookupFleetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupFleetResult, error) {
			args := v.(LookupFleetArgs)
			r, err := LookupFleet(ctx, &args, opts...)
			var s LookupFleetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupFleetResultOutput)
}

type LookupFleetOutputArgs struct {
	FleetId  pulumi.StringInput    `pulumi:"fleetId"`
	Location pulumi.StringInput    `pulumi:"location"`
	Project  pulumi.StringPtrInput `pulumi:"project"`
}

func (LookupFleetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFleetArgs)(nil)).Elem()
}

type LookupFleetResultOutput struct{ *pulumi.OutputState }

func (LookupFleetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFleetResult)(nil)).Elem()
}

func (o LookupFleetResultOutput) ToLookupFleetResultOutput() LookupFleetResultOutput {
	return o
}

func (o LookupFleetResultOutput) ToLookupFleetResultOutputWithContext(ctx context.Context) LookupFleetResultOutput {
	return o
}

// When the Fleet was created.
func (o LookupFleetResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFleetResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// Optional. The default cluster configurations to apply across the fleet.
func (o LookupFleetResultOutput) DefaultClusterConfig() DefaultClusterConfigResponseOutput {
	return o.ApplyT(func(v LookupFleetResult) DefaultClusterConfigResponse { return v.DefaultClusterConfig }).(DefaultClusterConfigResponseOutput)
}

// When the Fleet was deleted.
func (o LookupFleetResultOutput) DeleteTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFleetResult) string { return v.DeleteTime }).(pulumi.StringOutput)
}

// Optional. A user-assigned display name of the Fleet. When present, it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. Example: `Production Fleet`
func (o LookupFleetResultOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFleetResult) string { return v.DisplayName }).(pulumi.StringOutput)
}

// Optional. Labels for this Fleet.
func (o LookupFleetResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupFleetResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

// The full, unique resource name of this fleet in the format of `projects/{project}/locations/{location}/fleets/{fleet}`. Each Google Cloud project can have at most one fleet resource, named "default".
func (o LookupFleetResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFleetResult) string { return v.Name }).(pulumi.StringOutput)
}

// State of the namespace resource.
func (o LookupFleetResultOutput) State() FleetLifecycleStateResponseOutput {
	return o.ApplyT(func(v LookupFleetResult) FleetLifecycleStateResponse { return v.State }).(FleetLifecycleStateResponseOutput)
}

// Google-generated UUID for this resource. This is unique across all Fleet resources. If a Fleet resource is deleted and another resource with the same name is created, it gets a different uid.
func (o LookupFleetResultOutput) Uid() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFleetResult) string { return v.Uid }).(pulumi.StringOutput)
}

// When the Fleet was last updated.
func (o LookupFleetResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFleetResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupFleetResultOutput{})
}