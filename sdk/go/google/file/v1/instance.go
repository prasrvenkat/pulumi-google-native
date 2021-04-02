// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Creates an instance. When creating from a backup, the capacity of the new instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier).
type Instance struct {
	pulumi.CustomResourceState

	// The time when the instance was created.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// The description of the instance (2048 characters or less).
	Description pulumi.StringOutput `pulumi:"description"`
	// Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// File system shares on the instance. For this version, only a single file share is supported.
	FileShares FileShareConfigResponseArrayOutput `pulumi:"fileShares"`
	// Resource labels to represent user provided metadata.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// The resource name of the instance, in the format projects/{project}/locations/{location}/instances/{instance}.
	Name pulumi.StringOutput `pulumi:"name"`
	// VPC networks to which the instance is connected. For this version, only a single network is supported.
	Networks NetworkConfigResponseArrayOutput `pulumi:"networks"`
	// The instance state.
	State pulumi.StringOutput `pulumi:"state"`
	// Additional information about the instance state, if available.
	StatusMessage pulumi.StringOutput `pulumi:"statusMessage"`
	// The service tier of the instance.
	Tier pulumi.StringOutput `pulumi:"tier"`
}

// NewInstance registers a new resource with the given unique name, arguments, and options.
func NewInstance(ctx *pulumi.Context,
	name string, args *InstanceArgs, opts ...pulumi.ResourceOption) (*Instance, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstancesId == nil {
		return nil, errors.New("invalid value for required argument 'InstancesId'")
	}
	if args.LocationsId == nil {
		return nil, errors.New("invalid value for required argument 'LocationsId'")
	}
	if args.ProjectsId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectsId'")
	}
	var resource Instance
	err := ctx.RegisterResource("google-cloud:file/v1:Instance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstance gets an existing Instance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceState, opts ...pulumi.ResourceOption) (*Instance, error) {
	var resource Instance
	err := ctx.ReadResource("google-cloud:file/v1:Instance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Instance resources.
type instanceState struct {
	// The time when the instance was created.
	CreateTime *string `pulumi:"createTime"`
	// The description of the instance (2048 characters or less).
	Description *string `pulumi:"description"`
	// Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.
	Etag *string `pulumi:"etag"`
	// File system shares on the instance. For this version, only a single file share is supported.
	FileShares []FileShareConfigResponse `pulumi:"fileShares"`
	// Resource labels to represent user provided metadata.
	Labels map[string]string `pulumi:"labels"`
	// The resource name of the instance, in the format projects/{project}/locations/{location}/instances/{instance}.
	Name *string `pulumi:"name"`
	// VPC networks to which the instance is connected. For this version, only a single network is supported.
	Networks []NetworkConfigResponse `pulumi:"networks"`
	// The instance state.
	State *string `pulumi:"state"`
	// Additional information about the instance state, if available.
	StatusMessage *string `pulumi:"statusMessage"`
	// The service tier of the instance.
	Tier *string `pulumi:"tier"`
}

type InstanceState struct {
	// The time when the instance was created.
	CreateTime pulumi.StringPtrInput
	// The description of the instance (2048 characters or less).
	Description pulumi.StringPtrInput
	// Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.
	Etag pulumi.StringPtrInput
	// File system shares on the instance. For this version, only a single file share is supported.
	FileShares FileShareConfigResponseArrayInput
	// Resource labels to represent user provided metadata.
	Labels pulumi.StringMapInput
	// The resource name of the instance, in the format projects/{project}/locations/{location}/instances/{instance}.
	Name pulumi.StringPtrInput
	// VPC networks to which the instance is connected. For this version, only a single network is supported.
	Networks NetworkConfigResponseArrayInput
	// The instance state.
	State pulumi.StringPtrInput
	// Additional information about the instance state, if available.
	StatusMessage pulumi.StringPtrInput
	// The service tier of the instance.
	Tier pulumi.StringPtrInput
}

func (InstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceState)(nil)).Elem()
}

type instanceArgs struct {
	// The description of the instance (2048 characters or less).
	Description *string `pulumi:"description"`
	// Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.
	Etag *string `pulumi:"etag"`
	// File system shares on the instance. For this version, only a single file share is supported.
	FileShares  []FileShareConfig `pulumi:"fileShares"`
	InstancesId string            `pulumi:"instancesId"`
	// Resource labels to represent user provided metadata.
	Labels      map[string]string `pulumi:"labels"`
	LocationsId string            `pulumi:"locationsId"`
	// VPC networks to which the instance is connected. For this version, only a single network is supported.
	Networks   []NetworkConfig `pulumi:"networks"`
	ProjectsId string          `pulumi:"projectsId"`
	// The service tier of the instance.
	Tier *string `pulumi:"tier"`
}

// The set of arguments for constructing a Instance resource.
type InstanceArgs struct {
	// The description of the instance (2048 characters or less).
	Description pulumi.StringPtrInput
	// Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.
	Etag pulumi.StringPtrInput
	// File system shares on the instance. For this version, only a single file share is supported.
	FileShares  FileShareConfigArrayInput
	InstancesId pulumi.StringInput
	// Resource labels to represent user provided metadata.
	Labels      pulumi.StringMapInput
	LocationsId pulumi.StringInput
	// VPC networks to which the instance is connected. For this version, only a single network is supported.
	Networks   NetworkConfigArrayInput
	ProjectsId pulumi.StringInput
	// The service tier of the instance.
	Tier pulumi.StringPtrInput
}

func (InstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceArgs)(nil)).Elem()
}

type InstanceInput interface {
	pulumi.Input

	ToInstanceOutput() InstanceOutput
	ToInstanceOutputWithContext(ctx context.Context) InstanceOutput
}

func (*Instance) ElementType() reflect.Type {
	return reflect.TypeOf((*Instance)(nil))
}

func (i *Instance) ToInstanceOutput() InstanceOutput {
	return i.ToInstanceOutputWithContext(context.Background())
}

func (i *Instance) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceOutput)
}

type InstanceOutput struct {
	*pulumi.OutputState
}

func (InstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Instance)(nil))
}

func (o InstanceOutput) ToInstanceOutput() InstanceOutput {
	return o
}

func (o InstanceOutput) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(InstanceOutput{})
}