// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package beta

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a new resize request that starts provisioning VMs immediately or queues VM creation.
type InstanceGroupManagerResizeRequest struct {
	pulumi.CustomResourceState

	// The count of instances to create as part of this resize request.
	Count pulumi.IntOutput `pulumi:"count"`
	// The creation timestamp for this resize request in RFC3339 text format.
	CreationTimestamp pulumi.StringOutput `pulumi:"creationTimestamp"`
	// An optional description of this resource.
	Description          pulumi.StringOutput `pulumi:"description"`
	InstanceGroupManager pulumi.StringOutput `pulumi:"instanceGroupManager"`
	// The resource type, which is always compute#instanceGroupManagerResizeRequest for resize requests.
	Kind pulumi.StringOutput `pulumi:"kind"`
	// The name of this resize request. The name must be 1-63 characters long, and comply with RFC1035.
	Name    pulumi.StringOutput `pulumi:"name"`
	Project pulumi.StringOutput `pulumi:"project"`
	// An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
	RequestId pulumi.StringPtrOutput `pulumi:"requestId"`
	// Requested run duration for instances that will be created by this request. At the end of the run duration instance will be deleted.
	RequestedRunDuration DurationResponseOutput `pulumi:"requestedRunDuration"`
	// The number of instances to be created by this resize request. The group's target size will be increased by this number.
	ResizeBy pulumi.IntOutput `pulumi:"resizeBy"`
	// The URL for this resize request. The server defines this URL.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// Server-defined URL for this resource with the resource id.
	SelfLinkWithId pulumi.StringOutput `pulumi:"selfLinkWithId"`
	// [Output only] Current state of the request.
	State pulumi.StringOutput `pulumi:"state"`
	// [Output only] Status of the request.
	Status InstanceGroupManagerResizeRequestStatusResponseOutput `pulumi:"status"`
	Zone   pulumi.StringOutput                                   `pulumi:"zone"`
}

// NewInstanceGroupManagerResizeRequest registers a new resource with the given unique name, arguments, and options.
func NewInstanceGroupManagerResizeRequest(ctx *pulumi.Context,
	name string, args *InstanceGroupManagerResizeRequestArgs, opts ...pulumi.ResourceOption) (*InstanceGroupManagerResizeRequest, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceGroupManager == nil {
		return nil, errors.New("invalid value for required argument 'InstanceGroupManager'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"instanceGroupManager",
		"project",
		"zone",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource InstanceGroupManagerResizeRequest
	err := ctx.RegisterResource("google-native:compute/beta:InstanceGroupManagerResizeRequest", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstanceGroupManagerResizeRequest gets an existing InstanceGroupManagerResizeRequest resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstanceGroupManagerResizeRequest(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceGroupManagerResizeRequestState, opts ...pulumi.ResourceOption) (*InstanceGroupManagerResizeRequest, error) {
	var resource InstanceGroupManagerResizeRequest
	err := ctx.ReadResource("google-native:compute/beta:InstanceGroupManagerResizeRequest", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering InstanceGroupManagerResizeRequest resources.
type instanceGroupManagerResizeRequestState struct {
}

type InstanceGroupManagerResizeRequestState struct {
}

func (InstanceGroupManagerResizeRequestState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceGroupManagerResizeRequestState)(nil)).Elem()
}

type instanceGroupManagerResizeRequestArgs struct {
	// The count of instances to create as part of this resize request.
	Count *int `pulumi:"count"`
	// An optional description of this resource.
	Description          *string `pulumi:"description"`
	InstanceGroupManager string  `pulumi:"instanceGroupManager"`
	// The name of this resize request. The name must be 1-63 characters long, and comply with RFC1035.
	Name    *string `pulumi:"name"`
	Project *string `pulumi:"project"`
	// An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
	RequestId *string `pulumi:"requestId"`
	// Requested run duration for instances that will be created by this request. At the end of the run duration instance will be deleted.
	RequestedRunDuration *Duration `pulumi:"requestedRunDuration"`
	// The number of instances to be created by this resize request. The group's target size will be increased by this number.
	ResizeBy *int    `pulumi:"resizeBy"`
	Zone     *string `pulumi:"zone"`
}

// The set of arguments for constructing a InstanceGroupManagerResizeRequest resource.
type InstanceGroupManagerResizeRequestArgs struct {
	// The count of instances to create as part of this resize request.
	Count pulumi.IntPtrInput
	// An optional description of this resource.
	Description          pulumi.StringPtrInput
	InstanceGroupManager pulumi.StringInput
	// The name of this resize request. The name must be 1-63 characters long, and comply with RFC1035.
	Name    pulumi.StringPtrInput
	Project pulumi.StringPtrInput
	// An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
	RequestId pulumi.StringPtrInput
	// Requested run duration for instances that will be created by this request. At the end of the run duration instance will be deleted.
	RequestedRunDuration DurationPtrInput
	// The number of instances to be created by this resize request. The group's target size will be increased by this number.
	ResizeBy pulumi.IntPtrInput
	Zone     pulumi.StringPtrInput
}

func (InstanceGroupManagerResizeRequestArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceGroupManagerResizeRequestArgs)(nil)).Elem()
}

type InstanceGroupManagerResizeRequestInput interface {
	pulumi.Input

	ToInstanceGroupManagerResizeRequestOutput() InstanceGroupManagerResizeRequestOutput
	ToInstanceGroupManagerResizeRequestOutputWithContext(ctx context.Context) InstanceGroupManagerResizeRequestOutput
}

func (*InstanceGroupManagerResizeRequest) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceGroupManagerResizeRequest)(nil)).Elem()
}

func (i *InstanceGroupManagerResizeRequest) ToInstanceGroupManagerResizeRequestOutput() InstanceGroupManagerResizeRequestOutput {
	return i.ToInstanceGroupManagerResizeRequestOutputWithContext(context.Background())
}

func (i *InstanceGroupManagerResizeRequest) ToInstanceGroupManagerResizeRequestOutputWithContext(ctx context.Context) InstanceGroupManagerResizeRequestOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceGroupManagerResizeRequestOutput)
}

type InstanceGroupManagerResizeRequestOutput struct{ *pulumi.OutputState }

func (InstanceGroupManagerResizeRequestOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceGroupManagerResizeRequest)(nil)).Elem()
}

func (o InstanceGroupManagerResizeRequestOutput) ToInstanceGroupManagerResizeRequestOutput() InstanceGroupManagerResizeRequestOutput {
	return o
}

func (o InstanceGroupManagerResizeRequestOutput) ToInstanceGroupManagerResizeRequestOutputWithContext(ctx context.Context) InstanceGroupManagerResizeRequestOutput {
	return o
}

// The count of instances to create as part of this resize request.
func (o InstanceGroupManagerResizeRequestOutput) Count() pulumi.IntOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.IntOutput { return v.Count }).(pulumi.IntOutput)
}

// The creation timestamp for this resize request in RFC3339 text format.
func (o InstanceGroupManagerResizeRequestOutput) CreationTimestamp() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.StringOutput { return v.CreationTimestamp }).(pulumi.StringOutput)
}

// An optional description of this resource.
func (o InstanceGroupManagerResizeRequestOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

func (o InstanceGroupManagerResizeRequestOutput) InstanceGroupManager() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.StringOutput { return v.InstanceGroupManager }).(pulumi.StringOutput)
}

// The resource type, which is always compute#instanceGroupManagerResizeRequest for resize requests.
func (o InstanceGroupManagerResizeRequestOutput) Kind() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.StringOutput { return v.Kind }).(pulumi.StringOutput)
}

// The name of this resize request. The name must be 1-63 characters long, and comply with RFC1035.
func (o InstanceGroupManagerResizeRequestOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o InstanceGroupManagerResizeRequestOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
func (o InstanceGroupManagerResizeRequestOutput) RequestId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.StringPtrOutput { return v.RequestId }).(pulumi.StringPtrOutput)
}

// Requested run duration for instances that will be created by this request. At the end of the run duration instance will be deleted.
func (o InstanceGroupManagerResizeRequestOutput) RequestedRunDuration() DurationResponseOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) DurationResponseOutput { return v.RequestedRunDuration }).(DurationResponseOutput)
}

// The number of instances to be created by this resize request. The group's target size will be increased by this number.
func (o InstanceGroupManagerResizeRequestOutput) ResizeBy() pulumi.IntOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.IntOutput { return v.ResizeBy }).(pulumi.IntOutput)
}

// The URL for this resize request. The server defines this URL.
func (o InstanceGroupManagerResizeRequestOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.StringOutput { return v.SelfLink }).(pulumi.StringOutput)
}

// Server-defined URL for this resource with the resource id.
func (o InstanceGroupManagerResizeRequestOutput) SelfLinkWithId() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.StringOutput { return v.SelfLinkWithId }).(pulumi.StringOutput)
}

// [Output only] Current state of the request.
func (o InstanceGroupManagerResizeRequestOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// [Output only] Status of the request.
func (o InstanceGroupManagerResizeRequestOutput) Status() InstanceGroupManagerResizeRequestStatusResponseOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) InstanceGroupManagerResizeRequestStatusResponseOutput {
		return v.Status
	}).(InstanceGroupManagerResizeRequestStatusResponseOutput)
}

func (o InstanceGroupManagerResizeRequestOutput) Zone() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceGroupManagerResizeRequest) pulumi.StringOutput { return v.Zone }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceGroupManagerResizeRequestInput)(nil)).Elem(), &InstanceGroupManagerResizeRequest{})
	pulumi.RegisterOutputType(InstanceGroupManagerResizeRequestOutput{})
}