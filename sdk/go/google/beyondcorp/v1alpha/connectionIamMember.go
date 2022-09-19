// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1alpha

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	iam "github.com/pulumi/pulumi-google-native/sdk/go/google/iam/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.
// Note - this resource's API doesn't support deletion. When deleted, the resource will persist
// on Google Cloud even though it will be deleted from Pulumi state.
type ConnectionIamMember struct {
	pulumi.CustomResourceState

	// An IAM Condition for a given binding. See https://cloud.google.com/iam/docs/conditions-overview for additional details.
	Condition iam.ConditionPtrOutput `pulumi:"condition"`
	// The etag of the resource's IAM policy.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// Identity that will be granted the privilege in role. The entry can have one of the following values:
	//
	//  * user:{emailid}: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
	//  * serviceAccount:{emailid}: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
	//  * group:{emailid}: An email address that represents a Google group. For example, admins@example.com.
	//  * domain:{domain}: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
	Member pulumi.StringOutput `pulumi:"member"`
	// The name of the resource to manage IAM policies for.
	Name pulumi.StringOutput `pulumi:"name"`
	// The project in which the resource belongs. If it is not provided, a default will be supplied.
	Project pulumi.StringOutput `pulumi:"project"`
	// The role that should be applied.
	Role pulumi.StringOutput `pulumi:"role"`
}

// NewConnectionIamMember registers a new resource with the given unique name, arguments, and options.
func NewConnectionIamMember(ctx *pulumi.Context,
	name string, args *ConnectionIamMemberArgs, opts ...pulumi.ResourceOption) (*ConnectionIamMember, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Member == nil {
		return nil, errors.New("invalid value for required argument 'Member'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.Role == nil {
		return nil, errors.New("invalid value for required argument 'Role'")
	}
	var resource ConnectionIamMember
	err := ctx.RegisterResource("google-native:beyondcorp/v1alpha:ConnectionIamMember", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConnectionIamMember gets an existing ConnectionIamMember resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConnectionIamMember(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConnectionIamMemberState, opts ...pulumi.ResourceOption) (*ConnectionIamMember, error) {
	var resource ConnectionIamMember
	err := ctx.ReadResource("google-native:beyondcorp/v1alpha:ConnectionIamMember", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConnectionIamMember resources.
type connectionIamMemberState struct {
}

type ConnectionIamMemberState struct {
}

func (ConnectionIamMemberState) ElementType() reflect.Type {
	return reflect.TypeOf((*connectionIamMemberState)(nil)).Elem()
}

type connectionIamMemberArgs struct {
	// An IAM Condition for a given binding.
	Condition *iam.Condition `pulumi:"condition"`
	// Identity that will be granted the privilege in role. The entry can have one of the following values:
	//
	//  * user:{emailid}: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
	//  * serviceAccount:{emailid}: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
	//  * group:{emailid}: An email address that represents a Google group. For example, admins@example.com.
	//  * domain:{domain}: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
	Member string `pulumi:"member"`
	// The name of the resource to manage IAM policies for.
	Name string `pulumi:"name"`
	// The role that should be applied.
	Role string `pulumi:"role"`
}

// The set of arguments for constructing a ConnectionIamMember resource.
type ConnectionIamMemberArgs struct {
	// An IAM Condition for a given binding.
	Condition iam.ConditionPtrInput
	// Identity that will be granted the privilege in role. The entry can have one of the following values:
	//
	//  * user:{emailid}: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
	//  * serviceAccount:{emailid}: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
	//  * group:{emailid}: An email address that represents a Google group. For example, admins@example.com.
	//  * domain:{domain}: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
	Member pulumi.StringInput
	// The name of the resource to manage IAM policies for.
	Name pulumi.StringInput
	// The role that should be applied.
	Role pulumi.StringInput
}

func (ConnectionIamMemberArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*connectionIamMemberArgs)(nil)).Elem()
}

type ConnectionIamMemberInput interface {
	pulumi.Input

	ToConnectionIamMemberOutput() ConnectionIamMemberOutput
	ToConnectionIamMemberOutputWithContext(ctx context.Context) ConnectionIamMemberOutput
}

func (*ConnectionIamMember) ElementType() reflect.Type {
	return reflect.TypeOf((**ConnectionIamMember)(nil)).Elem()
}

func (i *ConnectionIamMember) ToConnectionIamMemberOutput() ConnectionIamMemberOutput {
	return i.ToConnectionIamMemberOutputWithContext(context.Background())
}

func (i *ConnectionIamMember) ToConnectionIamMemberOutputWithContext(ctx context.Context) ConnectionIamMemberOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectionIamMemberOutput)
}

type ConnectionIamMemberOutput struct{ *pulumi.OutputState }

func (ConnectionIamMemberOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ConnectionIamMember)(nil)).Elem()
}

func (o ConnectionIamMemberOutput) ToConnectionIamMemberOutput() ConnectionIamMemberOutput {
	return o
}

func (o ConnectionIamMemberOutput) ToConnectionIamMemberOutputWithContext(ctx context.Context) ConnectionIamMemberOutput {
	return o
}

// An IAM Condition for a given binding. See https://cloud.google.com/iam/docs/conditions-overview for additional details.
func (o ConnectionIamMemberOutput) Condition() iam.ConditionPtrOutput {
	return o.ApplyT(func(v *ConnectionIamMember) iam.ConditionPtrOutput { return v.Condition }).(iam.ConditionPtrOutput)
}

// The etag of the resource's IAM policy.
func (o ConnectionIamMemberOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectionIamMember) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

// Identity that will be granted the privilege in role. The entry can have one of the following values:
//
//   - user:{emailid}: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
//   - serviceAccount:{emailid}: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
//   - group:{emailid}: An email address that represents a Google group. For example, admins@example.com.
//   - domain:{domain}: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
func (o ConnectionIamMemberOutput) Member() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectionIamMember) pulumi.StringOutput { return v.Member }).(pulumi.StringOutput)
}

// The name of the resource to manage IAM policies for.
func (o ConnectionIamMemberOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectionIamMember) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The project in which the resource belongs. If it is not provided, a default will be supplied.
func (o ConnectionIamMemberOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectionIamMember) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// The role that should be applied.
func (o ConnectionIamMemberOutput) Role() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectionIamMember) pulumi.StringOutput { return v.Role }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectionIamMemberInput)(nil)).Elem(), &ConnectionIamMember{})
	pulumi.RegisterOutputType(ConnectionIamMemberOutput{})
}