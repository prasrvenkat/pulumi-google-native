// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates an app profile within an instance.
type AppProfile struct {
	pulumi.CustomResourceState

	// Long form description of the use case for this AppProfile.
	Description pulumi.StringOutput `pulumi:"description"`
	// Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// Use a multi-cluster routing policy.
	MultiClusterRoutingUseAny MultiClusterRoutingUseAnyResponseOutput `pulumi:"multiClusterRoutingUseAny"`
	// The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.
	Name pulumi.StringOutput `pulumi:"name"`
	// Use a single-cluster routing policy.
	SingleClusterRouting SingleClusterRoutingResponseOutput `pulumi:"singleClusterRouting"`
}

// NewAppProfile registers a new resource with the given unique name, arguments, and options.
func NewAppProfile(ctx *pulumi.Context,
	name string, args *AppProfileArgs, opts ...pulumi.ResourceOption) (*AppProfile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AppProfileId == nil {
		return nil, errors.New("invalid value for required argument 'AppProfileId'")
	}
	if args.InstanceId == nil {
		return nil, errors.New("invalid value for required argument 'InstanceId'")
	}
	if args.Project == nil {
		return nil, errors.New("invalid value for required argument 'Project'")
	}
	var resource AppProfile
	err := ctx.RegisterResource("google-native:bigtableadmin/v2:AppProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAppProfile gets an existing AppProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAppProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AppProfileState, opts ...pulumi.ResourceOption) (*AppProfile, error) {
	var resource AppProfile
	err := ctx.ReadResource("google-native:bigtableadmin/v2:AppProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AppProfile resources.
type appProfileState struct {
	// Long form description of the use case for this AppProfile.
	Description *string `pulumi:"description"`
	// Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.
	Etag *string `pulumi:"etag"`
	// Use a multi-cluster routing policy.
	MultiClusterRoutingUseAny *MultiClusterRoutingUseAnyResponse `pulumi:"multiClusterRoutingUseAny"`
	// The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.
	Name *string `pulumi:"name"`
	// Use a single-cluster routing policy.
	SingleClusterRouting *SingleClusterRoutingResponse `pulumi:"singleClusterRouting"`
}

type AppProfileState struct {
	// Long form description of the use case for this AppProfile.
	Description pulumi.StringPtrInput
	// Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.
	Etag pulumi.StringPtrInput
	// Use a multi-cluster routing policy.
	MultiClusterRoutingUseAny MultiClusterRoutingUseAnyResponsePtrInput
	// The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.
	Name pulumi.StringPtrInput
	// Use a single-cluster routing policy.
	SingleClusterRouting SingleClusterRoutingResponsePtrInput
}

func (AppProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*appProfileState)(nil)).Elem()
}

type appProfileArgs struct {
	AppProfileId string `pulumi:"appProfileId"`
	// Long form description of the use case for this AppProfile.
	Description *string `pulumi:"description"`
	// Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.
	Etag           *string `pulumi:"etag"`
	IgnoreWarnings *string `pulumi:"ignoreWarnings"`
	InstanceId     string  `pulumi:"instanceId"`
	// Use a multi-cluster routing policy.
	MultiClusterRoutingUseAny *MultiClusterRoutingUseAny `pulumi:"multiClusterRoutingUseAny"`
	// The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.
	Name    *string `pulumi:"name"`
	Project string  `pulumi:"project"`
	// Use a single-cluster routing policy.
	SingleClusterRouting *SingleClusterRouting `pulumi:"singleClusterRouting"`
}

// The set of arguments for constructing a AppProfile resource.
type AppProfileArgs struct {
	AppProfileId pulumi.StringInput
	// Long form description of the use case for this AppProfile.
	Description pulumi.StringPtrInput
	// Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.
	Etag           pulumi.StringPtrInput
	IgnoreWarnings pulumi.StringPtrInput
	InstanceId     pulumi.StringInput
	// Use a multi-cluster routing policy.
	MultiClusterRoutingUseAny MultiClusterRoutingUseAnyPtrInput
	// The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.
	Name    pulumi.StringPtrInput
	Project pulumi.StringInput
	// Use a single-cluster routing policy.
	SingleClusterRouting SingleClusterRoutingPtrInput
}

func (AppProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*appProfileArgs)(nil)).Elem()
}

type AppProfileInput interface {
	pulumi.Input

	ToAppProfileOutput() AppProfileOutput
	ToAppProfileOutputWithContext(ctx context.Context) AppProfileOutput
}

func (*AppProfile) ElementType() reflect.Type {
	return reflect.TypeOf((*AppProfile)(nil))
}

func (i *AppProfile) ToAppProfileOutput() AppProfileOutput {
	return i.ToAppProfileOutputWithContext(context.Background())
}

func (i *AppProfile) ToAppProfileOutputWithContext(ctx context.Context) AppProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AppProfileOutput)
}

type AppProfileOutput struct {
	*pulumi.OutputState
}

func (AppProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AppProfile)(nil))
}

func (o AppProfileOutput) ToAppProfileOutput() AppProfileOutput {
	return o
}

func (o AppProfileOutput) ToAppProfileOutputWithContext(ctx context.Context) AppProfileOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(AppProfileOutput{})
}