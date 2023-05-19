// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a new workstation cluster.
type WorkstationCluster struct {
	pulumi.CustomResourceState

	// Client-specified annotations.
	Annotations pulumi.StringMapOutput `pulumi:"annotations"`
	// Status conditions describing the current resource state.
	Conditions StatusResponseArrayOutput `pulumi:"conditions"`
	// The private IP address of the control plane for this cluster. Workstation VMs need access to this IP address to work with the service, so make sure that your firewall rules allow egress from the workstation VMs to this address.
	ControlPlaneIp pulumi.StringOutput `pulumi:"controlPlaneIp"`
	// Time when this resource was created.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Whether this resource is in degraded mode, in which case it may require user action to restore full functionality. Details can be found in the `conditions` field.
	Degraded pulumi.BoolOutput `pulumi:"degraded"`
	// Time when this resource was soft-deleted.
	DeleteTime pulumi.StringOutput `pulumi:"deleteTime"`
	// Human-readable name for this resource.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// Client-specified labels that are applied to the resource and that are also propagated to the underlying Compute Engine resources.
	Labels   pulumi.StringMapOutput `pulumi:"labels"`
	Location pulumi.StringOutput    `pulumi:"location"`
	// Full name of this resource.
	Name pulumi.StringOutput `pulumi:"name"`
	// Immutable. Name of the Compute Engine network in which instances associated with this cluster will be created.
	Network pulumi.StringOutput `pulumi:"network"`
	// Configuration for private cluster.
	PrivateClusterConfig PrivateClusterConfigResponseOutput `pulumi:"privateClusterConfig"`
	Project              pulumi.StringOutput                `pulumi:"project"`
	// Indicates whether this resource is currently being updated to match its intended state.
	Reconciling pulumi.BoolOutput `pulumi:"reconciling"`
	// Immutable. Name of the Compute Engine subnetwork in which instances associated with this cluster will be created. Must be part of the subnetwork specified for this cluster.
	Subnetwork pulumi.StringOutput `pulumi:"subnetwork"`
	// A system-assigned unique identified for this resource.
	Uid pulumi.StringOutput `pulumi:"uid"`
	// Time when this resource was most recently updated.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
	// Required. ID to use for the workstation cluster.
	WorkstationClusterId pulumi.StringOutput `pulumi:"workstationClusterId"`
}

// NewWorkstationCluster registers a new resource with the given unique name, arguments, and options.
func NewWorkstationCluster(ctx *pulumi.Context,
	name string, args *WorkstationClusterArgs, opts ...pulumi.ResourceOption) (*WorkstationCluster, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.WorkstationClusterId == nil {
		return nil, errors.New("invalid value for required argument 'WorkstationClusterId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"location",
		"project",
		"workstationClusterId",
	})
	opts = append(opts, replaceOnChanges)
	var resource WorkstationCluster
	err := ctx.RegisterResource("google-native:workstations/v1beta:WorkstationCluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWorkstationCluster gets an existing WorkstationCluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWorkstationCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WorkstationClusterState, opts ...pulumi.ResourceOption) (*WorkstationCluster, error) {
	var resource WorkstationCluster
	err := ctx.ReadResource("google-native:workstations/v1beta:WorkstationCluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WorkstationCluster resources.
type workstationClusterState struct {
}

type WorkstationClusterState struct {
}

func (WorkstationClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*workstationClusterState)(nil)).Elem()
}

type workstationClusterArgs struct {
	// Client-specified annotations.
	Annotations map[string]string `pulumi:"annotations"`
	// Human-readable name for this resource.
	DisplayName *string `pulumi:"displayName"`
	// Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.
	Etag *string `pulumi:"etag"`
	// Client-specified labels that are applied to the resource and that are also propagated to the underlying Compute Engine resources.
	Labels   map[string]string `pulumi:"labels"`
	Location *string           `pulumi:"location"`
	// Full name of this resource.
	Name *string `pulumi:"name"`
	// Immutable. Name of the Compute Engine network in which instances associated with this cluster will be created.
	Network *string `pulumi:"network"`
	// Configuration for private cluster.
	PrivateClusterConfig *PrivateClusterConfig `pulumi:"privateClusterConfig"`
	Project              *string               `pulumi:"project"`
	// Immutable. Name of the Compute Engine subnetwork in which instances associated with this cluster will be created. Must be part of the subnetwork specified for this cluster.
	Subnetwork *string `pulumi:"subnetwork"`
	// Required. ID to use for the workstation cluster.
	WorkstationClusterId string `pulumi:"workstationClusterId"`
}

// The set of arguments for constructing a WorkstationCluster resource.
type WorkstationClusterArgs struct {
	// Client-specified annotations.
	Annotations pulumi.StringMapInput
	// Human-readable name for this resource.
	DisplayName pulumi.StringPtrInput
	// Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.
	Etag pulumi.StringPtrInput
	// Client-specified labels that are applied to the resource and that are also propagated to the underlying Compute Engine resources.
	Labels   pulumi.StringMapInput
	Location pulumi.StringPtrInput
	// Full name of this resource.
	Name pulumi.StringPtrInput
	// Immutable. Name of the Compute Engine network in which instances associated with this cluster will be created.
	Network pulumi.StringPtrInput
	// Configuration for private cluster.
	PrivateClusterConfig PrivateClusterConfigPtrInput
	Project              pulumi.StringPtrInput
	// Immutable. Name of the Compute Engine subnetwork in which instances associated with this cluster will be created. Must be part of the subnetwork specified for this cluster.
	Subnetwork pulumi.StringPtrInput
	// Required. ID to use for the workstation cluster.
	WorkstationClusterId pulumi.StringInput
}

func (WorkstationClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*workstationClusterArgs)(nil)).Elem()
}

type WorkstationClusterInput interface {
	pulumi.Input

	ToWorkstationClusterOutput() WorkstationClusterOutput
	ToWorkstationClusterOutputWithContext(ctx context.Context) WorkstationClusterOutput
}

func (*WorkstationCluster) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkstationCluster)(nil)).Elem()
}

func (i *WorkstationCluster) ToWorkstationClusterOutput() WorkstationClusterOutput {
	return i.ToWorkstationClusterOutputWithContext(context.Background())
}

func (i *WorkstationCluster) ToWorkstationClusterOutputWithContext(ctx context.Context) WorkstationClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkstationClusterOutput)
}

type WorkstationClusterOutput struct{ *pulumi.OutputState }

func (WorkstationClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkstationCluster)(nil)).Elem()
}

func (o WorkstationClusterOutput) ToWorkstationClusterOutput() WorkstationClusterOutput {
	return o
}

func (o WorkstationClusterOutput) ToWorkstationClusterOutputWithContext(ctx context.Context) WorkstationClusterOutput {
	return o
}

// Client-specified annotations.
func (o WorkstationClusterOutput) Annotations() pulumi.StringMapOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringMapOutput { return v.Annotations }).(pulumi.StringMapOutput)
}

// Status conditions describing the current resource state.
func (o WorkstationClusterOutput) Conditions() StatusResponseArrayOutput {
	return o.ApplyT(func(v *WorkstationCluster) StatusResponseArrayOutput { return v.Conditions }).(StatusResponseArrayOutput)
}

// The private IP address of the control plane for this cluster. Workstation VMs need access to this IP address to work with the service, so make sure that your firewall rules allow egress from the workstation VMs to this address.
func (o WorkstationClusterOutput) ControlPlaneIp() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.ControlPlaneIp }).(pulumi.StringOutput)
}

// Time when this resource was created.
func (o WorkstationClusterOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Whether this resource is in degraded mode, in which case it may require user action to restore full functionality. Details can be found in the `conditions` field.
func (o WorkstationClusterOutput) Degraded() pulumi.BoolOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.BoolOutput { return v.Degraded }).(pulumi.BoolOutput)
}

// Time when this resource was soft-deleted.
func (o WorkstationClusterOutput) DeleteTime() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.DeleteTime }).(pulumi.StringOutput)
}

// Human-readable name for this resource.
func (o WorkstationClusterOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.DisplayName }).(pulumi.StringOutput)
}

// Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.
func (o WorkstationClusterOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

// Client-specified labels that are applied to the resource and that are also propagated to the underlying Compute Engine resources.
func (o WorkstationClusterOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

func (o WorkstationClusterOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// Full name of this resource.
func (o WorkstationClusterOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Immutable. Name of the Compute Engine network in which instances associated with this cluster will be created.
func (o WorkstationClusterOutput) Network() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.Network }).(pulumi.StringOutput)
}

// Configuration for private cluster.
func (o WorkstationClusterOutput) PrivateClusterConfig() PrivateClusterConfigResponseOutput {
	return o.ApplyT(func(v *WorkstationCluster) PrivateClusterConfigResponseOutput { return v.PrivateClusterConfig }).(PrivateClusterConfigResponseOutput)
}

func (o WorkstationClusterOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// Indicates whether this resource is currently being updated to match its intended state.
func (o WorkstationClusterOutput) Reconciling() pulumi.BoolOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.BoolOutput { return v.Reconciling }).(pulumi.BoolOutput)
}

// Immutable. Name of the Compute Engine subnetwork in which instances associated with this cluster will be created. Must be part of the subnetwork specified for this cluster.
func (o WorkstationClusterOutput) Subnetwork() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.Subnetwork }).(pulumi.StringOutput)
}

// A system-assigned unique identified for this resource.
func (o WorkstationClusterOutput) Uid() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.Uid }).(pulumi.StringOutput)
}

// Time when this resource was most recently updated.
func (o WorkstationClusterOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

// Required. ID to use for the workstation cluster.
func (o WorkstationClusterOutput) WorkstationClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkstationCluster) pulumi.StringOutput { return v.WorkstationClusterId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WorkstationClusterInput)(nil)).Elem(), &WorkstationCluster{})
	pulumi.RegisterOutputType(WorkstationClusterOutput{})
}