// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v2beta1

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a new conversation. Conversations are auto-completed after 24 hours. Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage. For Automated Agent Stage, there will be a dialogflow agent responding to user queries. For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation. If Conversation.conversation_profile is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an Intent with Intent.live_agent_handoff is triggered, conversation will transfer to Assist Stage.
type Conversation struct {
	pulumi.CustomResourceState

	// Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: `projects//locations//conversationProfiles/`.
	ConversationProfile pulumi.StringOutput `pulumi:"conversationProfile"`
	// The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation. If the conversation is created with the conversation profile that has Dialogflow config set, defaults to ConversationStage.VIRTUAL_AGENT_STAGE; Otherwise, defaults to ConversationStage.HUMAN_ASSIST_STAGE. If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversation_stage to ConversationStage.HUMAN_ASSIST_STAGE, it skips ConversationStage.VIRTUAL_AGENT_STAGE stage and directly goes to ConversationStage.HUMAN_ASSIST_STAGE.
	ConversationStage pulumi.StringOutput `pulumi:"conversationStage"`
	// The time the conversation was finished.
	EndTime pulumi.StringOutput `pulumi:"endTime"`
	// The current state of the Conversation.
	LifecycleState pulumi.StringOutput `pulumi:"lifecycleState"`
	// The unique identifier of this conversation. Format: `projects//locations//conversations/`.
	Name pulumi.StringOutput `pulumi:"name"`
	// Required if the conversation is to be connected over telephony.
	PhoneNumber GoogleCloudDialogflowV2beta1ConversationPhoneNumberResponseOutput `pulumi:"phoneNumber"`
	// The time the conversation was started.
	StartTime pulumi.StringOutput `pulumi:"startTime"`
}

// NewConversation registers a new resource with the given unique name, arguments, and options.
func NewConversation(ctx *pulumi.Context,
	name string, args *ConversationArgs, opts ...pulumi.ResourceOption) (*Conversation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConversationsId == nil {
		return nil, errors.New("invalid value for required argument 'ConversationsId'")
	}
	if args.LocationsId == nil {
		return nil, errors.New("invalid value for required argument 'LocationsId'")
	}
	if args.ProjectsId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectsId'")
	}
	var resource Conversation
	err := ctx.RegisterResource("google-native:dialogflow/v2beta1:Conversation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConversation gets an existing Conversation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConversation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConversationState, opts ...pulumi.ResourceOption) (*Conversation, error) {
	var resource Conversation
	err := ctx.ReadResource("google-native:dialogflow/v2beta1:Conversation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Conversation resources.
type conversationState struct {
	// Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: `projects//locations//conversationProfiles/`.
	ConversationProfile *string `pulumi:"conversationProfile"`
	// The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation. If the conversation is created with the conversation profile that has Dialogflow config set, defaults to ConversationStage.VIRTUAL_AGENT_STAGE; Otherwise, defaults to ConversationStage.HUMAN_ASSIST_STAGE. If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversation_stage to ConversationStage.HUMAN_ASSIST_STAGE, it skips ConversationStage.VIRTUAL_AGENT_STAGE stage and directly goes to ConversationStage.HUMAN_ASSIST_STAGE.
	ConversationStage *string `pulumi:"conversationStage"`
	// The time the conversation was finished.
	EndTime *string `pulumi:"endTime"`
	// The current state of the Conversation.
	LifecycleState *string `pulumi:"lifecycleState"`
	// The unique identifier of this conversation. Format: `projects//locations//conversations/`.
	Name *string `pulumi:"name"`
	// Required if the conversation is to be connected over telephony.
	PhoneNumber *GoogleCloudDialogflowV2beta1ConversationPhoneNumberResponse `pulumi:"phoneNumber"`
	// The time the conversation was started.
	StartTime *string `pulumi:"startTime"`
}

type ConversationState struct {
	// Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: `projects//locations//conversationProfiles/`.
	ConversationProfile pulumi.StringPtrInput
	// The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation. If the conversation is created with the conversation profile that has Dialogflow config set, defaults to ConversationStage.VIRTUAL_AGENT_STAGE; Otherwise, defaults to ConversationStage.HUMAN_ASSIST_STAGE. If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversation_stage to ConversationStage.HUMAN_ASSIST_STAGE, it skips ConversationStage.VIRTUAL_AGENT_STAGE stage and directly goes to ConversationStage.HUMAN_ASSIST_STAGE.
	ConversationStage pulumi.StringPtrInput
	// The time the conversation was finished.
	EndTime pulumi.StringPtrInput
	// The current state of the Conversation.
	LifecycleState pulumi.StringPtrInput
	// The unique identifier of this conversation. Format: `projects//locations//conversations/`.
	Name pulumi.StringPtrInput
	// Required if the conversation is to be connected over telephony.
	PhoneNumber GoogleCloudDialogflowV2beta1ConversationPhoneNumberResponsePtrInput
	// The time the conversation was started.
	StartTime pulumi.StringPtrInput
}

func (ConversationState) ElementType() reflect.Type {
	return reflect.TypeOf((*conversationState)(nil)).Elem()
}

type conversationArgs struct {
	// Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: `projects//locations//conversationProfiles/`.
	ConversationProfile *string `pulumi:"conversationProfile"`
	// The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation. If the conversation is created with the conversation profile that has Dialogflow config set, defaults to ConversationStage.VIRTUAL_AGENT_STAGE; Otherwise, defaults to ConversationStage.HUMAN_ASSIST_STAGE. If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversation_stage to ConversationStage.HUMAN_ASSIST_STAGE, it skips ConversationStage.VIRTUAL_AGENT_STAGE stage and directly goes to ConversationStage.HUMAN_ASSIST_STAGE.
	ConversationStage *string `pulumi:"conversationStage"`
	ConversationsId   string  `pulumi:"conversationsId"`
	LocationsId       string  `pulumi:"locationsId"`
	ProjectsId        string  `pulumi:"projectsId"`
}

// The set of arguments for constructing a Conversation resource.
type ConversationArgs struct {
	// Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: `projects//locations//conversationProfiles/`.
	ConversationProfile pulumi.StringPtrInput
	// The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation. If the conversation is created with the conversation profile that has Dialogflow config set, defaults to ConversationStage.VIRTUAL_AGENT_STAGE; Otherwise, defaults to ConversationStage.HUMAN_ASSIST_STAGE. If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversation_stage to ConversationStage.HUMAN_ASSIST_STAGE, it skips ConversationStage.VIRTUAL_AGENT_STAGE stage and directly goes to ConversationStage.HUMAN_ASSIST_STAGE.
	ConversationStage pulumi.StringPtrInput
	ConversationsId   pulumi.StringInput
	LocationsId       pulumi.StringInput
	ProjectsId        pulumi.StringInput
}

func (ConversationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*conversationArgs)(nil)).Elem()
}

type ConversationInput interface {
	pulumi.Input

	ToConversationOutput() ConversationOutput
	ToConversationOutputWithContext(ctx context.Context) ConversationOutput
}

func (*Conversation) ElementType() reflect.Type {
	return reflect.TypeOf((*Conversation)(nil))
}

func (i *Conversation) ToConversationOutput() ConversationOutput {
	return i.ToConversationOutputWithContext(context.Background())
}

func (i *Conversation) ToConversationOutputWithContext(ctx context.Context) ConversationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConversationOutput)
}

type ConversationOutput struct {
	*pulumi.OutputState
}

func (ConversationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Conversation)(nil))
}

func (o ConversationOutput) ToConversationOutput() ConversationOutput {
	return o
}

func (o ConversationOutput) ToConversationOutputWithContext(ctx context.Context) ConversationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ConversationOutput{})
}