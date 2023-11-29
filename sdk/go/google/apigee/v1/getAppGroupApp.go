// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Returns the details for an AppGroup app.
func LookupAppGroupApp(ctx *pulumi.Context, args *LookupAppGroupAppArgs, opts ...pulumi.InvokeOption) (*LookupAppGroupAppResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAppGroupAppResult
	err := ctx.Invoke("google-native:apigee/v1:getAppGroupApp", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupAppGroupAppArgs struct {
	AppId          string `pulumi:"appId"`
	AppgroupId     string `pulumi:"appgroupId"`
	OrganizationId string `pulumi:"organizationId"`
}

type LookupAppGroupAppResult struct {
	// List of API products associated with the AppGroup app.
	ApiProducts []string `pulumi:"apiProducts"`
	// Immutable. Name of the parent AppGroup whose resource name format is of syntax (organizations/*/appgroups/*).
	AppGroup string `pulumi:"appGroup"`
	// Immutable. ID of the AppGroup app.
	AppId string `pulumi:"appId"`
	// List of attributes for the AppGroup app.
	Attributes []GoogleCloudApigeeV1AttributeResponse `pulumi:"attributes"`
	// Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to AppGroup apps.
	CallbackUrl string `pulumi:"callbackUrl"`
	// Time the AppGroup app was created in milliseconds since epoch.
	CreatedAt string `pulumi:"createdAt"`
	// Set of credentials for the AppGroup app consisting of the consumer key/secret pairs associated with the API products.
	Credentials []GoogleCloudApigeeV1CredentialResponse `pulumi:"credentials"`
	// Immutable. Expiration time, in seconds, for the consumer key that is generated for the AppGroup app. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set.
	KeyExpiresIn string `pulumi:"keyExpiresIn"`
	// Time the AppGroup app was modified in milliseconds since epoch.
	LastModifiedAt string `pulumi:"lastModifiedAt"`
	// Immutable. Name of the AppGroup app whose resource name format is of syntax (organizations/*/appgroups/*/apps/*).
	Name string `pulumi:"name"`
	// Scopes to apply to the AppGroup app. The specified scopes must already exist for the API product that you associate with the AppGroup app.
	Scopes []string `pulumi:"scopes"`
	// Status of the App. Valid values include `approved` or `revoked`.
	Status string `pulumi:"status"`
}

func LookupAppGroupAppOutput(ctx *pulumi.Context, args LookupAppGroupAppOutputArgs, opts ...pulumi.InvokeOption) LookupAppGroupAppResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAppGroupAppResult, error) {
			args := v.(LookupAppGroupAppArgs)
			r, err := LookupAppGroupApp(ctx, &args, opts...)
			var s LookupAppGroupAppResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAppGroupAppResultOutput)
}

type LookupAppGroupAppOutputArgs struct {
	AppId          pulumi.StringInput `pulumi:"appId"`
	AppgroupId     pulumi.StringInput `pulumi:"appgroupId"`
	OrganizationId pulumi.StringInput `pulumi:"organizationId"`
}

func (LookupAppGroupAppOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAppGroupAppArgs)(nil)).Elem()
}

type LookupAppGroupAppResultOutput struct{ *pulumi.OutputState }

func (LookupAppGroupAppResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAppGroupAppResult)(nil)).Elem()
}

func (o LookupAppGroupAppResultOutput) ToLookupAppGroupAppResultOutput() LookupAppGroupAppResultOutput {
	return o
}

func (o LookupAppGroupAppResultOutput) ToLookupAppGroupAppResultOutputWithContext(ctx context.Context) LookupAppGroupAppResultOutput {
	return o
}

// List of API products associated with the AppGroup app.
func (o LookupAppGroupAppResultOutput) ApiProducts() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) []string { return v.ApiProducts }).(pulumi.StringArrayOutput)
}

// Immutable. Name of the parent AppGroup whose resource name format is of syntax (organizations/*/appgroups/*).
func (o LookupAppGroupAppResultOutput) AppGroup() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) string { return v.AppGroup }).(pulumi.StringOutput)
}

// Immutable. ID of the AppGroup app.
func (o LookupAppGroupAppResultOutput) AppId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) string { return v.AppId }).(pulumi.StringOutput)
}

// List of attributes for the AppGroup app.
func (o LookupAppGroupAppResultOutput) Attributes() GoogleCloudApigeeV1AttributeResponseArrayOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) []GoogleCloudApigeeV1AttributeResponse { return v.Attributes }).(GoogleCloudApigeeV1AttributeResponseArrayOutput)
}

// Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to AppGroup apps.
func (o LookupAppGroupAppResultOutput) CallbackUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) string { return v.CallbackUrl }).(pulumi.StringOutput)
}

// Time the AppGroup app was created in milliseconds since epoch.
func (o LookupAppGroupAppResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// Set of credentials for the AppGroup app consisting of the consumer key/secret pairs associated with the API products.
func (o LookupAppGroupAppResultOutput) Credentials() GoogleCloudApigeeV1CredentialResponseArrayOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) []GoogleCloudApigeeV1CredentialResponse { return v.Credentials }).(GoogleCloudApigeeV1CredentialResponseArrayOutput)
}

// Immutable. Expiration time, in seconds, for the consumer key that is generated for the AppGroup app. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set.
func (o LookupAppGroupAppResultOutput) KeyExpiresIn() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) string { return v.KeyExpiresIn }).(pulumi.StringOutput)
}

// Time the AppGroup app was modified in milliseconds since epoch.
func (o LookupAppGroupAppResultOutput) LastModifiedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) string { return v.LastModifiedAt }).(pulumi.StringOutput)
}

// Immutable. Name of the AppGroup app whose resource name format is of syntax (organizations/*/appgroups/*/apps/*).
func (o LookupAppGroupAppResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) string { return v.Name }).(pulumi.StringOutput)
}

// Scopes to apply to the AppGroup app. The specified scopes must already exist for the API product that you associate with the AppGroup app.
func (o LookupAppGroupAppResultOutput) Scopes() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) []string { return v.Scopes }).(pulumi.StringArrayOutput)
}

// Status of the App. Valid values include `approved` or `revoked`.
func (o LookupAppGroupAppResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppGroupAppResult) string { return v.Status }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAppGroupAppResultOutput{})
}