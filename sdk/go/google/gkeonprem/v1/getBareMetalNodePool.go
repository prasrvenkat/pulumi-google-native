// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets details of a single bare metal node pool.
func LookupBareMetalNodePool(ctx *pulumi.Context, args *LookupBareMetalNodePoolArgs, opts ...pulumi.InvokeOption) (*LookupBareMetalNodePoolResult, error) {
	var rv LookupBareMetalNodePoolResult
	err := ctx.Invoke("google-native:gkeonprem/v1:getBareMetalNodePool", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupBareMetalNodePoolArgs struct {
	BareMetalClusterId  string  `pulumi:"bareMetalClusterId"`
	BareMetalNodePoolId string  `pulumi:"bareMetalNodePoolId"`
	Location            string  `pulumi:"location"`
	Project             *string `pulumi:"project"`
}

type LookupBareMetalNodePoolResult struct {
	// Annotations on the bare metal node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between.
	Annotations map[string]string `pulumi:"annotations"`
	// The time at which this bare metal node pool was created.
	CreateTime string `pulumi:"createTime"`
	// The time at which this bare metal node pool was deleted. If the resource is not deleted, this must be empty
	DeleteTime string `pulumi:"deleteTime"`
	// The display name for the bare metal node pool.
	DisplayName string `pulumi:"displayName"`
	// This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control.
	Etag string `pulumi:"etag"`
	// Immutable. The bare metal node pool resource name.
	Name string `pulumi:"name"`
	// Node pool configuration.
	NodePoolConfig BareMetalNodePoolConfigResponse `pulumi:"nodePoolConfig"`
	// If set, there are currently changes in flight to the bare metal node pool.
	Reconciling bool `pulumi:"reconciling"`
	// The current state of the bare metal node pool.
	State string `pulumi:"state"`
	// ResourceStatus representing the detailed node pool status.
	Status ResourceStatusResponse `pulumi:"status"`
	// The unique identifier of the bare metal node pool.
	Uid string `pulumi:"uid"`
	// The time at which this bare metal node pool was last updated.
	UpdateTime string `pulumi:"updateTime"`
}

func LookupBareMetalNodePoolOutput(ctx *pulumi.Context, args LookupBareMetalNodePoolOutputArgs, opts ...pulumi.InvokeOption) LookupBareMetalNodePoolResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupBareMetalNodePoolResult, error) {
			args := v.(LookupBareMetalNodePoolArgs)
			r, err := LookupBareMetalNodePool(ctx, &args, opts...)
			var s LookupBareMetalNodePoolResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupBareMetalNodePoolResultOutput)
}

type LookupBareMetalNodePoolOutputArgs struct {
	BareMetalClusterId  pulumi.StringInput    `pulumi:"bareMetalClusterId"`
	BareMetalNodePoolId pulumi.StringInput    `pulumi:"bareMetalNodePoolId"`
	Location            pulumi.StringInput    `pulumi:"location"`
	Project             pulumi.StringPtrInput `pulumi:"project"`
}

func (LookupBareMetalNodePoolOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBareMetalNodePoolArgs)(nil)).Elem()
}

type LookupBareMetalNodePoolResultOutput struct{ *pulumi.OutputState }

func (LookupBareMetalNodePoolResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBareMetalNodePoolResult)(nil)).Elem()
}

func (o LookupBareMetalNodePoolResultOutput) ToLookupBareMetalNodePoolResultOutput() LookupBareMetalNodePoolResultOutput {
	return o
}

func (o LookupBareMetalNodePoolResultOutput) ToLookupBareMetalNodePoolResultOutputWithContext(ctx context.Context) LookupBareMetalNodePoolResultOutput {
	return o
}

// Annotations on the bare metal node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between.
func (o LookupBareMetalNodePoolResultOutput) Annotations() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) map[string]string { return v.Annotations }).(pulumi.StringMapOutput)
}

// The time at which this bare metal node pool was created.
func (o LookupBareMetalNodePoolResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// The time at which this bare metal node pool was deleted. If the resource is not deleted, this must be empty
func (o LookupBareMetalNodePoolResultOutput) DeleteTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) string { return v.DeleteTime }).(pulumi.StringOutput)
}

// The display name for the bare metal node pool.
func (o LookupBareMetalNodePoolResultOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) string { return v.DisplayName }).(pulumi.StringOutput)
}

// This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control.
func (o LookupBareMetalNodePoolResultOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) string { return v.Etag }).(pulumi.StringOutput)
}

// Immutable. The bare metal node pool resource name.
func (o LookupBareMetalNodePoolResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) string { return v.Name }).(pulumi.StringOutput)
}

// Node pool configuration.
func (o LookupBareMetalNodePoolResultOutput) NodePoolConfig() BareMetalNodePoolConfigResponseOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) BareMetalNodePoolConfigResponse { return v.NodePoolConfig }).(BareMetalNodePoolConfigResponseOutput)
}

// If set, there are currently changes in flight to the bare metal node pool.
func (o LookupBareMetalNodePoolResultOutput) Reconciling() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) bool { return v.Reconciling }).(pulumi.BoolOutput)
}

// The current state of the bare metal node pool.
func (o LookupBareMetalNodePoolResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) string { return v.State }).(pulumi.StringOutput)
}

// ResourceStatus representing the detailed node pool status.
func (o LookupBareMetalNodePoolResultOutput) Status() ResourceStatusResponseOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) ResourceStatusResponse { return v.Status }).(ResourceStatusResponseOutput)
}

// The unique identifier of the bare metal node pool.
func (o LookupBareMetalNodePoolResultOutput) Uid() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) string { return v.Uid }).(pulumi.StringOutput)
}

// The time at which this bare metal node pool was last updated.
func (o LookupBareMetalNodePoolResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBareMetalNodePoolResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupBareMetalNodePoolResultOutput{})
}