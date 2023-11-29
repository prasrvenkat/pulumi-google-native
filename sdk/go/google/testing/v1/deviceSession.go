// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// POST /v1/projects/{project_id}/deviceSessions
// Note - this resource's API doesn't support deletion. When deleted, the resource will persist
// on Google Cloud even though it will be deleted from Pulumi state.
type DeviceSession struct {
	pulumi.CustomResourceState

	// The timestamp that the session first became ACTIVE.
	ActiveStartTime pulumi.StringOutput `pulumi:"activeStartTime"`
	// The requested device
	AndroidDevice AndroidDeviceResponseOutput `pulumi:"androidDevice"`
	// The time that the Session was created.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// The title of the DeviceSession to be presented in the UI.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// Optional. If the device is still in use at this time, any connections will be ended and the SessionState will transition from ACTIVE to FINISHED.
	ExpireTime pulumi.StringOutput `pulumi:"expireTime"`
	// The interval of time that this device must be interacted with before it transitions from ACTIVE to TIMEOUT_INACTIVITY.
	InactivityTimeout pulumi.StringOutput `pulumi:"inactivityTimeout"`
	// Optional. Name of the DeviceSession, e.g. "projects/{project_id}/deviceSessions/{session_id}"
	Name    pulumi.StringOutput `pulumi:"name"`
	Project pulumi.StringOutput `pulumi:"project"`
	// Current state of the DeviceSession.
	State pulumi.StringOutput `pulumi:"state"`
	// The historical state transitions of the session_state message including the current session state.
	StateHistories SessionStateEventResponseArrayOutput `pulumi:"stateHistories"`
	// Optional. The amount of time that a device will be initially allocated for. This can eventually be extended with the UpdateDeviceSession RPC. Default: 30 minutes.
	Ttl pulumi.StringOutput `pulumi:"ttl"`
}

// NewDeviceSession registers a new resource with the given unique name, arguments, and options.
func NewDeviceSession(ctx *pulumi.Context,
	name string, args *DeviceSessionArgs, opts ...pulumi.ResourceOption) (*DeviceSession, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AndroidDevice == nil {
		return nil, errors.New("invalid value for required argument 'AndroidDevice'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"project",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DeviceSession
	err := ctx.RegisterResource("google-native:testing/v1:DeviceSession", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDeviceSession gets an existing DeviceSession resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDeviceSession(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeviceSessionState, opts ...pulumi.ResourceOption) (*DeviceSession, error) {
	var resource DeviceSession
	err := ctx.ReadResource("google-native:testing/v1:DeviceSession", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DeviceSession resources.
type deviceSessionState struct {
}

type DeviceSessionState struct {
}

func (DeviceSessionState) ElementType() reflect.Type {
	return reflect.TypeOf((*deviceSessionState)(nil)).Elem()
}

type deviceSessionArgs struct {
	// The requested device
	AndroidDevice AndroidDevice `pulumi:"androidDevice"`
	// Optional. If the device is still in use at this time, any connections will be ended and the SessionState will transition from ACTIVE to FINISHED.
	ExpireTime *string `pulumi:"expireTime"`
	// Optional. Name of the DeviceSession, e.g. "projects/{project_id}/deviceSessions/{session_id}"
	Name    *string `pulumi:"name"`
	Project *string `pulumi:"project"`
	// Optional. The amount of time that a device will be initially allocated for. This can eventually be extended with the UpdateDeviceSession RPC. Default: 30 minutes.
	Ttl *string `pulumi:"ttl"`
}

// The set of arguments for constructing a DeviceSession resource.
type DeviceSessionArgs struct {
	// The requested device
	AndroidDevice AndroidDeviceInput
	// Optional. If the device is still in use at this time, any connections will be ended and the SessionState will transition from ACTIVE to FINISHED.
	ExpireTime pulumi.StringPtrInput
	// Optional. Name of the DeviceSession, e.g. "projects/{project_id}/deviceSessions/{session_id}"
	Name    pulumi.StringPtrInput
	Project pulumi.StringPtrInput
	// Optional. The amount of time that a device will be initially allocated for. This can eventually be extended with the UpdateDeviceSession RPC. Default: 30 minutes.
	Ttl pulumi.StringPtrInput
}

func (DeviceSessionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deviceSessionArgs)(nil)).Elem()
}

type DeviceSessionInput interface {
	pulumi.Input

	ToDeviceSessionOutput() DeviceSessionOutput
	ToDeviceSessionOutputWithContext(ctx context.Context) DeviceSessionOutput
}

func (*DeviceSession) ElementType() reflect.Type {
	return reflect.TypeOf((**DeviceSession)(nil)).Elem()
}

func (i *DeviceSession) ToDeviceSessionOutput() DeviceSessionOutput {
	return i.ToDeviceSessionOutputWithContext(context.Background())
}

func (i *DeviceSession) ToDeviceSessionOutputWithContext(ctx context.Context) DeviceSessionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeviceSessionOutput)
}

type DeviceSessionOutput struct{ *pulumi.OutputState }

func (DeviceSessionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DeviceSession)(nil)).Elem()
}

func (o DeviceSessionOutput) ToDeviceSessionOutput() DeviceSessionOutput {
	return o
}

func (o DeviceSessionOutput) ToDeviceSessionOutputWithContext(ctx context.Context) DeviceSessionOutput {
	return o
}

// The timestamp that the session first became ACTIVE.
func (o DeviceSessionOutput) ActiveStartTime() pulumi.StringOutput {
	return o.ApplyT(func(v *DeviceSession) pulumi.StringOutput { return v.ActiveStartTime }).(pulumi.StringOutput)
}

// The requested device
func (o DeviceSessionOutput) AndroidDevice() AndroidDeviceResponseOutput {
	return o.ApplyT(func(v *DeviceSession) AndroidDeviceResponseOutput { return v.AndroidDevice }).(AndroidDeviceResponseOutput)
}

// The time that the Session was created.
func (o DeviceSessionOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *DeviceSession) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// The title of the DeviceSession to be presented in the UI.
func (o DeviceSessionOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *DeviceSession) pulumi.StringOutput { return v.DisplayName }).(pulumi.StringOutput)
}

// Optional. If the device is still in use at this time, any connections will be ended and the SessionState will transition from ACTIVE to FINISHED.
func (o DeviceSessionOutput) ExpireTime() pulumi.StringOutput {
	return o.ApplyT(func(v *DeviceSession) pulumi.StringOutput { return v.ExpireTime }).(pulumi.StringOutput)
}

// The interval of time that this device must be interacted with before it transitions from ACTIVE to TIMEOUT_INACTIVITY.
func (o DeviceSessionOutput) InactivityTimeout() pulumi.StringOutput {
	return o.ApplyT(func(v *DeviceSession) pulumi.StringOutput { return v.InactivityTimeout }).(pulumi.StringOutput)
}

// Optional. Name of the DeviceSession, e.g. "projects/{project_id}/deviceSessions/{session_id}"
func (o DeviceSessionOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *DeviceSession) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o DeviceSessionOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *DeviceSession) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// Current state of the DeviceSession.
func (o DeviceSessionOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *DeviceSession) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// The historical state transitions of the session_state message including the current session state.
func (o DeviceSessionOutput) StateHistories() SessionStateEventResponseArrayOutput {
	return o.ApplyT(func(v *DeviceSession) SessionStateEventResponseArrayOutput { return v.StateHistories }).(SessionStateEventResponseArrayOutput)
}

// Optional. The amount of time that a device will be initially allocated for. This can eventually be extended with the UpdateDeviceSession RPC. Default: 30 minutes.
func (o DeviceSessionOutput) Ttl() pulumi.StringOutput {
	return o.ApplyT(func(v *DeviceSession) pulumi.StringOutput { return v.Ttl }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DeviceSessionInput)(nil)).Elem(), &DeviceSession{})
	pulumi.RegisterOutputType(DeviceSessionOutput{})
}