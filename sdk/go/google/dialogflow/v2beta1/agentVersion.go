// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v2beta1

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates an agent version. The new version points to the agent instance in the "default" environment.
type AgentVersion struct {
	pulumi.CustomResourceState

	// The creation time of this version. This field is read-only, i.e., it cannot be set by create and update methods.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Optional. The developer-provided description of this version.
	Description pulumi.StringOutput `pulumi:"description"`
	// The unique identifier of this agent version. Supported formats: - `projects//agent/versions/` - `projects//locations//agent/versions/`
	Name pulumi.StringOutput `pulumi:"name"`
	// The status of this version. This field is read-only and cannot be set by create and update methods.
	Status pulumi.StringOutput `pulumi:"status"`
	// The sequential number of this version. This field is read-only which means it cannot be set by create and update methods.
	VersionNumber pulumi.IntOutput `pulumi:"versionNumber"`
}

// NewAgentVersion registers a new resource with the given unique name, arguments, and options.
func NewAgentVersion(ctx *pulumi.Context,
	name string, args *AgentVersionArgs, opts ...pulumi.ResourceOption) (*AgentVersion, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.LocationsId == nil {
		return nil, errors.New("invalid value for required argument 'LocationsId'")
	}
	if args.ProjectsId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectsId'")
	}
	if args.VersionsId == nil {
		return nil, errors.New("invalid value for required argument 'VersionsId'")
	}
	var resource AgentVersion
	err := ctx.RegisterResource("google-native:dialogflow/v2beta1:AgentVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAgentVersion gets an existing AgentVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAgentVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AgentVersionState, opts ...pulumi.ResourceOption) (*AgentVersion, error) {
	var resource AgentVersion
	err := ctx.ReadResource("google-native:dialogflow/v2beta1:AgentVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AgentVersion resources.
type agentVersionState struct {
	// The creation time of this version. This field is read-only, i.e., it cannot be set by create and update methods.
	CreateTime *string `pulumi:"createTime"`
	// Optional. The developer-provided description of this version.
	Description *string `pulumi:"description"`
	// The unique identifier of this agent version. Supported formats: - `projects//agent/versions/` - `projects//locations//agent/versions/`
	Name *string `pulumi:"name"`
	// The status of this version. This field is read-only and cannot be set by create and update methods.
	Status *string `pulumi:"status"`
	// The sequential number of this version. This field is read-only which means it cannot be set by create and update methods.
	VersionNumber *int `pulumi:"versionNumber"`
}

type AgentVersionState struct {
	// The creation time of this version. This field is read-only, i.e., it cannot be set by create and update methods.
	CreateTime pulumi.StringPtrInput
	// Optional. The developer-provided description of this version.
	Description pulumi.StringPtrInput
	// The unique identifier of this agent version. Supported formats: - `projects//agent/versions/` - `projects//locations//agent/versions/`
	Name pulumi.StringPtrInput
	// The status of this version. This field is read-only and cannot be set by create and update methods.
	Status pulumi.StringPtrInput
	// The sequential number of this version. This field is read-only which means it cannot be set by create and update methods.
	VersionNumber pulumi.IntPtrInput
}

func (AgentVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*agentVersionState)(nil)).Elem()
}

type agentVersionArgs struct {
	// Optional. The developer-provided description of this version.
	Description *string `pulumi:"description"`
	LocationsId string  `pulumi:"locationsId"`
	ProjectsId  string  `pulumi:"projectsId"`
	VersionsId  string  `pulumi:"versionsId"`
}

// The set of arguments for constructing a AgentVersion resource.
type AgentVersionArgs struct {
	// Optional. The developer-provided description of this version.
	Description pulumi.StringPtrInput
	LocationsId pulumi.StringInput
	ProjectsId  pulumi.StringInput
	VersionsId  pulumi.StringInput
}

func (AgentVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*agentVersionArgs)(nil)).Elem()
}

type AgentVersionInput interface {
	pulumi.Input

	ToAgentVersionOutput() AgentVersionOutput
	ToAgentVersionOutputWithContext(ctx context.Context) AgentVersionOutput
}

func (*AgentVersion) ElementType() reflect.Type {
	return reflect.TypeOf((*AgentVersion)(nil))
}

func (i *AgentVersion) ToAgentVersionOutput() AgentVersionOutput {
	return i.ToAgentVersionOutputWithContext(context.Background())
}

func (i *AgentVersion) ToAgentVersionOutputWithContext(ctx context.Context) AgentVersionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AgentVersionOutput)
}

type AgentVersionOutput struct {
	*pulumi.OutputState
}

func (AgentVersionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AgentVersion)(nil))
}

func (o AgentVersionOutput) ToAgentVersionOutput() AgentVersionOutput {
	return o
}

func (o AgentVersionOutput) ToAgentVersionOutputWithContext(ctx context.Context) AgentVersionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(AgentVersionOutput{})
}