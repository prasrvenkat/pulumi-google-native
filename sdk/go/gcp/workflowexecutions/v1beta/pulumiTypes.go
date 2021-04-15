// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Error describes why the execution was abnormally terminated.
type ErrorResponse struct {
	// Human readable stack trace string.
	Context string `pulumi:"context"`
	// Error message and data returned represented as a JSON string.
	Payload string `pulumi:"payload"`
	// Stack trace with detailed information of where error was generated.
	StackTrace StackTraceResponse `pulumi:"stackTrace"`
}

// ErrorResponseInput is an input type that accepts ErrorResponseArgs and ErrorResponseOutput values.
// You can construct a concrete instance of `ErrorResponseInput` via:
//
//          ErrorResponseArgs{...}
type ErrorResponseInput interface {
	pulumi.Input

	ToErrorResponseOutput() ErrorResponseOutput
	ToErrorResponseOutputWithContext(context.Context) ErrorResponseOutput
}

// Error describes why the execution was abnormally terminated.
type ErrorResponseArgs struct {
	// Human readable stack trace string.
	Context pulumi.StringInput `pulumi:"context"`
	// Error message and data returned represented as a JSON string.
	Payload pulumi.StringInput `pulumi:"payload"`
	// Stack trace with detailed information of where error was generated.
	StackTrace StackTraceResponseInput `pulumi:"stackTrace"`
}

func (ErrorResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ErrorResponse)(nil)).Elem()
}

func (i ErrorResponseArgs) ToErrorResponseOutput() ErrorResponseOutput {
	return i.ToErrorResponseOutputWithContext(context.Background())
}

func (i ErrorResponseArgs) ToErrorResponseOutputWithContext(ctx context.Context) ErrorResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ErrorResponseOutput)
}

func (i ErrorResponseArgs) ToErrorResponsePtrOutput() ErrorResponsePtrOutput {
	return i.ToErrorResponsePtrOutputWithContext(context.Background())
}

func (i ErrorResponseArgs) ToErrorResponsePtrOutputWithContext(ctx context.Context) ErrorResponsePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ErrorResponseOutput).ToErrorResponsePtrOutputWithContext(ctx)
}

// ErrorResponsePtrInput is an input type that accepts ErrorResponseArgs, ErrorResponsePtr and ErrorResponsePtrOutput values.
// You can construct a concrete instance of `ErrorResponsePtrInput` via:
//
//          ErrorResponseArgs{...}
//
//  or:
//
//          nil
type ErrorResponsePtrInput interface {
	pulumi.Input

	ToErrorResponsePtrOutput() ErrorResponsePtrOutput
	ToErrorResponsePtrOutputWithContext(context.Context) ErrorResponsePtrOutput
}

type errorResponsePtrType ErrorResponseArgs

func ErrorResponsePtr(v *ErrorResponseArgs) ErrorResponsePtrInput {
	return (*errorResponsePtrType)(v)
}

func (*errorResponsePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ErrorResponse)(nil)).Elem()
}

func (i *errorResponsePtrType) ToErrorResponsePtrOutput() ErrorResponsePtrOutput {
	return i.ToErrorResponsePtrOutputWithContext(context.Background())
}

func (i *errorResponsePtrType) ToErrorResponsePtrOutputWithContext(ctx context.Context) ErrorResponsePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ErrorResponsePtrOutput)
}

// Error describes why the execution was abnormally terminated.
type ErrorResponseOutput struct{ *pulumi.OutputState }

func (ErrorResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ErrorResponse)(nil)).Elem()
}

func (o ErrorResponseOutput) ToErrorResponseOutput() ErrorResponseOutput {
	return o
}

func (o ErrorResponseOutput) ToErrorResponseOutputWithContext(ctx context.Context) ErrorResponseOutput {
	return o
}

func (o ErrorResponseOutput) ToErrorResponsePtrOutput() ErrorResponsePtrOutput {
	return o.ToErrorResponsePtrOutputWithContext(context.Background())
}

func (o ErrorResponseOutput) ToErrorResponsePtrOutputWithContext(ctx context.Context) ErrorResponsePtrOutput {
	return o.ApplyT(func(v ErrorResponse) *ErrorResponse {
		return &v
	}).(ErrorResponsePtrOutput)
}

// Human readable stack trace string.
func (o ErrorResponseOutput) Context() pulumi.StringOutput {
	return o.ApplyT(func(v ErrorResponse) string { return v.Context }).(pulumi.StringOutput)
}

// Error message and data returned represented as a JSON string.
func (o ErrorResponseOutput) Payload() pulumi.StringOutput {
	return o.ApplyT(func(v ErrorResponse) string { return v.Payload }).(pulumi.StringOutput)
}

// Stack trace with detailed information of where error was generated.
func (o ErrorResponseOutput) StackTrace() StackTraceResponseOutput {
	return o.ApplyT(func(v ErrorResponse) StackTraceResponse { return v.StackTrace }).(StackTraceResponseOutput)
}

type ErrorResponsePtrOutput struct{ *pulumi.OutputState }

func (ErrorResponsePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ErrorResponse)(nil)).Elem()
}

func (o ErrorResponsePtrOutput) ToErrorResponsePtrOutput() ErrorResponsePtrOutput {
	return o
}

func (o ErrorResponsePtrOutput) ToErrorResponsePtrOutputWithContext(ctx context.Context) ErrorResponsePtrOutput {
	return o
}

func (o ErrorResponsePtrOutput) Elem() ErrorResponseOutput {
	return o.ApplyT(func(v *ErrorResponse) ErrorResponse { return *v }).(ErrorResponseOutput)
}

// Human readable stack trace string.
func (o ErrorResponsePtrOutput) Context() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ErrorResponse) *string {
		if v == nil {
			return nil
		}
		return &v.Context
	}).(pulumi.StringPtrOutput)
}

// Error message and data returned represented as a JSON string.
func (o ErrorResponsePtrOutput) Payload() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ErrorResponse) *string {
		if v == nil {
			return nil
		}
		return &v.Payload
	}).(pulumi.StringPtrOutput)
}

// Stack trace with detailed information of where error was generated.
func (o ErrorResponsePtrOutput) StackTrace() StackTraceResponsePtrOutput {
	return o.ApplyT(func(v *ErrorResponse) *StackTraceResponse {
		if v == nil {
			return nil
		}
		return &v.StackTrace
	}).(StackTraceResponsePtrOutput)
}

// Position contains source position information about the stack trace element such as line number, column number and length of the code block in bytes.
type PositionResponse struct {
	// The source code column position (of the line) the current instruction was generated from.
	Column string `pulumi:"column"`
	// The length in bytes of text in this character group, e.g. digits of a number, string length, or AST (abstract syntax tree) node.
	Length string `pulumi:"length"`
	// The source code line number the current instruction was generated from.
	Line string `pulumi:"line"`
}

// PositionResponseInput is an input type that accepts PositionResponseArgs and PositionResponseOutput values.
// You can construct a concrete instance of `PositionResponseInput` via:
//
//          PositionResponseArgs{...}
type PositionResponseInput interface {
	pulumi.Input

	ToPositionResponseOutput() PositionResponseOutput
	ToPositionResponseOutputWithContext(context.Context) PositionResponseOutput
}

// Position contains source position information about the stack trace element such as line number, column number and length of the code block in bytes.
type PositionResponseArgs struct {
	// The source code column position (of the line) the current instruction was generated from.
	Column pulumi.StringInput `pulumi:"column"`
	// The length in bytes of text in this character group, e.g. digits of a number, string length, or AST (abstract syntax tree) node.
	Length pulumi.StringInput `pulumi:"length"`
	// The source code line number the current instruction was generated from.
	Line pulumi.StringInput `pulumi:"line"`
}

func (PositionResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PositionResponse)(nil)).Elem()
}

func (i PositionResponseArgs) ToPositionResponseOutput() PositionResponseOutput {
	return i.ToPositionResponseOutputWithContext(context.Background())
}

func (i PositionResponseArgs) ToPositionResponseOutputWithContext(ctx context.Context) PositionResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PositionResponseOutput)
}

// Position contains source position information about the stack trace element such as line number, column number and length of the code block in bytes.
type PositionResponseOutput struct{ *pulumi.OutputState }

func (PositionResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PositionResponse)(nil)).Elem()
}

func (o PositionResponseOutput) ToPositionResponseOutput() PositionResponseOutput {
	return o
}

func (o PositionResponseOutput) ToPositionResponseOutputWithContext(ctx context.Context) PositionResponseOutput {
	return o
}

// The source code column position (of the line) the current instruction was generated from.
func (o PositionResponseOutput) Column() pulumi.StringOutput {
	return o.ApplyT(func(v PositionResponse) string { return v.Column }).(pulumi.StringOutput)
}

// The length in bytes of text in this character group, e.g. digits of a number, string length, or AST (abstract syntax tree) node.
func (o PositionResponseOutput) Length() pulumi.StringOutput {
	return o.ApplyT(func(v PositionResponse) string { return v.Length }).(pulumi.StringOutput)
}

// The source code line number the current instruction was generated from.
func (o PositionResponseOutput) Line() pulumi.StringOutput {
	return o.ApplyT(func(v PositionResponse) string { return v.Line }).(pulumi.StringOutput)
}

// A single stack element (frame) where an error occurred.
type StackTraceElementResponse struct {
	// The source position information of the stacktrace element.
	Position PositionResponse `pulumi:"position"`
	// The routine where the error occurred.
	Routine string `pulumi:"routine"`
	// The step the error occurred at.
	Step string `pulumi:"step"`
}

// StackTraceElementResponseInput is an input type that accepts StackTraceElementResponseArgs and StackTraceElementResponseOutput values.
// You can construct a concrete instance of `StackTraceElementResponseInput` via:
//
//          StackTraceElementResponseArgs{...}
type StackTraceElementResponseInput interface {
	pulumi.Input

	ToStackTraceElementResponseOutput() StackTraceElementResponseOutput
	ToStackTraceElementResponseOutputWithContext(context.Context) StackTraceElementResponseOutput
}

// A single stack element (frame) where an error occurred.
type StackTraceElementResponseArgs struct {
	// The source position information of the stacktrace element.
	Position PositionResponseInput `pulumi:"position"`
	// The routine where the error occurred.
	Routine pulumi.StringInput `pulumi:"routine"`
	// The step the error occurred at.
	Step pulumi.StringInput `pulumi:"step"`
}

func (StackTraceElementResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*StackTraceElementResponse)(nil)).Elem()
}

func (i StackTraceElementResponseArgs) ToStackTraceElementResponseOutput() StackTraceElementResponseOutput {
	return i.ToStackTraceElementResponseOutputWithContext(context.Background())
}

func (i StackTraceElementResponseArgs) ToStackTraceElementResponseOutputWithContext(ctx context.Context) StackTraceElementResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StackTraceElementResponseOutput)
}

// StackTraceElementResponseArrayInput is an input type that accepts StackTraceElementResponseArray and StackTraceElementResponseArrayOutput values.
// You can construct a concrete instance of `StackTraceElementResponseArrayInput` via:
//
//          StackTraceElementResponseArray{ StackTraceElementResponseArgs{...} }
type StackTraceElementResponseArrayInput interface {
	pulumi.Input

	ToStackTraceElementResponseArrayOutput() StackTraceElementResponseArrayOutput
	ToStackTraceElementResponseArrayOutputWithContext(context.Context) StackTraceElementResponseArrayOutput
}

type StackTraceElementResponseArray []StackTraceElementResponseInput

func (StackTraceElementResponseArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]StackTraceElementResponse)(nil)).Elem()
}

func (i StackTraceElementResponseArray) ToStackTraceElementResponseArrayOutput() StackTraceElementResponseArrayOutput {
	return i.ToStackTraceElementResponseArrayOutputWithContext(context.Background())
}

func (i StackTraceElementResponseArray) ToStackTraceElementResponseArrayOutputWithContext(ctx context.Context) StackTraceElementResponseArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StackTraceElementResponseArrayOutput)
}

// A single stack element (frame) where an error occurred.
type StackTraceElementResponseOutput struct{ *pulumi.OutputState }

func (StackTraceElementResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*StackTraceElementResponse)(nil)).Elem()
}

func (o StackTraceElementResponseOutput) ToStackTraceElementResponseOutput() StackTraceElementResponseOutput {
	return o
}

func (o StackTraceElementResponseOutput) ToStackTraceElementResponseOutputWithContext(ctx context.Context) StackTraceElementResponseOutput {
	return o
}

// The source position information of the stacktrace element.
func (o StackTraceElementResponseOutput) Position() PositionResponseOutput {
	return o.ApplyT(func(v StackTraceElementResponse) PositionResponse { return v.Position }).(PositionResponseOutput)
}

// The routine where the error occurred.
func (o StackTraceElementResponseOutput) Routine() pulumi.StringOutput {
	return o.ApplyT(func(v StackTraceElementResponse) string { return v.Routine }).(pulumi.StringOutput)
}

// The step the error occurred at.
func (o StackTraceElementResponseOutput) Step() pulumi.StringOutput {
	return o.ApplyT(func(v StackTraceElementResponse) string { return v.Step }).(pulumi.StringOutput)
}

type StackTraceElementResponseArrayOutput struct{ *pulumi.OutputState }

func (StackTraceElementResponseArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]StackTraceElementResponse)(nil)).Elem()
}

func (o StackTraceElementResponseArrayOutput) ToStackTraceElementResponseArrayOutput() StackTraceElementResponseArrayOutput {
	return o
}

func (o StackTraceElementResponseArrayOutput) ToStackTraceElementResponseArrayOutputWithContext(ctx context.Context) StackTraceElementResponseArrayOutput {
	return o
}

func (o StackTraceElementResponseArrayOutput) Index(i pulumi.IntInput) StackTraceElementResponseOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) StackTraceElementResponse {
		return vs[0].([]StackTraceElementResponse)[vs[1].(int)]
	}).(StackTraceElementResponseOutput)
}

// A collection of stack elements (frames) where an error occurred.
type StackTraceResponse struct {
	// An array of Stack elements.
	Elements []StackTraceElementResponse `pulumi:"elements"`
}

// StackTraceResponseInput is an input type that accepts StackTraceResponseArgs and StackTraceResponseOutput values.
// You can construct a concrete instance of `StackTraceResponseInput` via:
//
//          StackTraceResponseArgs{...}
type StackTraceResponseInput interface {
	pulumi.Input

	ToStackTraceResponseOutput() StackTraceResponseOutput
	ToStackTraceResponseOutputWithContext(context.Context) StackTraceResponseOutput
}

// A collection of stack elements (frames) where an error occurred.
type StackTraceResponseArgs struct {
	// An array of Stack elements.
	Elements StackTraceElementResponseArrayInput `pulumi:"elements"`
}

func (StackTraceResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*StackTraceResponse)(nil)).Elem()
}

func (i StackTraceResponseArgs) ToStackTraceResponseOutput() StackTraceResponseOutput {
	return i.ToStackTraceResponseOutputWithContext(context.Background())
}

func (i StackTraceResponseArgs) ToStackTraceResponseOutputWithContext(ctx context.Context) StackTraceResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StackTraceResponseOutput)
}

func (i StackTraceResponseArgs) ToStackTraceResponsePtrOutput() StackTraceResponsePtrOutput {
	return i.ToStackTraceResponsePtrOutputWithContext(context.Background())
}

func (i StackTraceResponseArgs) ToStackTraceResponsePtrOutputWithContext(ctx context.Context) StackTraceResponsePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StackTraceResponseOutput).ToStackTraceResponsePtrOutputWithContext(ctx)
}

// StackTraceResponsePtrInput is an input type that accepts StackTraceResponseArgs, StackTraceResponsePtr and StackTraceResponsePtrOutput values.
// You can construct a concrete instance of `StackTraceResponsePtrInput` via:
//
//          StackTraceResponseArgs{...}
//
//  or:
//
//          nil
type StackTraceResponsePtrInput interface {
	pulumi.Input

	ToStackTraceResponsePtrOutput() StackTraceResponsePtrOutput
	ToStackTraceResponsePtrOutputWithContext(context.Context) StackTraceResponsePtrOutput
}

type stackTraceResponsePtrType StackTraceResponseArgs

func StackTraceResponsePtr(v *StackTraceResponseArgs) StackTraceResponsePtrInput {
	return (*stackTraceResponsePtrType)(v)
}

func (*stackTraceResponsePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**StackTraceResponse)(nil)).Elem()
}

func (i *stackTraceResponsePtrType) ToStackTraceResponsePtrOutput() StackTraceResponsePtrOutput {
	return i.ToStackTraceResponsePtrOutputWithContext(context.Background())
}

func (i *stackTraceResponsePtrType) ToStackTraceResponsePtrOutputWithContext(ctx context.Context) StackTraceResponsePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StackTraceResponsePtrOutput)
}

// A collection of stack elements (frames) where an error occurred.
type StackTraceResponseOutput struct{ *pulumi.OutputState }

func (StackTraceResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*StackTraceResponse)(nil)).Elem()
}

func (o StackTraceResponseOutput) ToStackTraceResponseOutput() StackTraceResponseOutput {
	return o
}

func (o StackTraceResponseOutput) ToStackTraceResponseOutputWithContext(ctx context.Context) StackTraceResponseOutput {
	return o
}

func (o StackTraceResponseOutput) ToStackTraceResponsePtrOutput() StackTraceResponsePtrOutput {
	return o.ToStackTraceResponsePtrOutputWithContext(context.Background())
}

func (o StackTraceResponseOutput) ToStackTraceResponsePtrOutputWithContext(ctx context.Context) StackTraceResponsePtrOutput {
	return o.ApplyT(func(v StackTraceResponse) *StackTraceResponse {
		return &v
	}).(StackTraceResponsePtrOutput)
}

// An array of Stack elements.
func (o StackTraceResponseOutput) Elements() StackTraceElementResponseArrayOutput {
	return o.ApplyT(func(v StackTraceResponse) []StackTraceElementResponse { return v.Elements }).(StackTraceElementResponseArrayOutput)
}

type StackTraceResponsePtrOutput struct{ *pulumi.OutputState }

func (StackTraceResponsePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StackTraceResponse)(nil)).Elem()
}

func (o StackTraceResponsePtrOutput) ToStackTraceResponsePtrOutput() StackTraceResponsePtrOutput {
	return o
}

func (o StackTraceResponsePtrOutput) ToStackTraceResponsePtrOutputWithContext(ctx context.Context) StackTraceResponsePtrOutput {
	return o
}

func (o StackTraceResponsePtrOutput) Elem() StackTraceResponseOutput {
	return o.ApplyT(func(v *StackTraceResponse) StackTraceResponse { return *v }).(StackTraceResponseOutput)
}

// An array of Stack elements.
func (o StackTraceResponsePtrOutput) Elements() StackTraceElementResponseArrayOutput {
	return o.ApplyT(func(v *StackTraceResponse) []StackTraceElementResponse {
		if v == nil {
			return nil
		}
		return v.Elements
	}).(StackTraceElementResponseArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(ErrorResponseOutput{})
	pulumi.RegisterOutputType(ErrorResponsePtrOutput{})
	pulumi.RegisterOutputType(PositionResponseOutput{})
	pulumi.RegisterOutputType(StackTraceElementResponseOutput{})
	pulumi.RegisterOutputType(StackTraceElementResponseArrayOutput{})
	pulumi.RegisterOutputType(StackTraceResponseOutput{})
	pulumi.RegisterOutputType(StackTraceResponsePtrOutput{})
}