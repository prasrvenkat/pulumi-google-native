// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// GetSecurityProfile gets the specified security profile. Returns NOT_FOUND if security profile is not present for the specified organization.
func LookupSecurityProfile(ctx *pulumi.Context, args *LookupSecurityProfileArgs, opts ...pulumi.InvokeOption) (*LookupSecurityProfileResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSecurityProfileResult
	err := ctx.Invoke("google-native:apigee/v1:getSecurityProfile", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSecurityProfileArgs struct {
	OrganizationId    string `pulumi:"organizationId"`
	SecurityProfileId string `pulumi:"securityProfileId"`
}

type LookupSecurityProfileResult struct {
	// Description of the security profile.
	Description string `pulumi:"description"`
	// Display name of the security profile.
	DisplayName string `pulumi:"displayName"`
	// List of environments attached to security profile.
	Environments []GoogleCloudApigeeV1SecurityProfileEnvironmentResponse `pulumi:"environments"`
	// Maximum security score that can be generated by this profile.
	MaxScore int `pulumi:"maxScore"`
	// Minimum security score that can be generated by this profile.
	MinScore int `pulumi:"minScore"`
	// Immutable. Name of the security profile resource. Format: organizations/{org}/securityProfiles/{profile}
	Name string `pulumi:"name"`
	// Customized profile configuration that computes the security score.
	ProfileConfig GoogleCloudApigeeV1ProfileConfigResponse `pulumi:"profileConfig"`
	// The time when revision was created.
	RevisionCreateTime string `pulumi:"revisionCreateTime"`
	// Revision ID of the security profile.
	RevisionId string `pulumi:"revisionId"`
	// The time when revision was published. Once published, the security profile revision cannot be updated further and can be attached to environments.
	RevisionPublishTime string `pulumi:"revisionPublishTime"`
	// The time when revision was updated.
	RevisionUpdateTime string `pulumi:"revisionUpdateTime"`
	// List of profile scoring configs in this revision.
	ScoringConfigs []GoogleCloudApigeeV1SecurityProfileScoringConfigResponse `pulumi:"scoringConfigs"`
}

func LookupSecurityProfileOutput(ctx *pulumi.Context, args LookupSecurityProfileOutputArgs, opts ...pulumi.InvokeOption) LookupSecurityProfileResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSecurityProfileResult, error) {
			args := v.(LookupSecurityProfileArgs)
			r, err := LookupSecurityProfile(ctx, &args, opts...)
			var s LookupSecurityProfileResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSecurityProfileResultOutput)
}

type LookupSecurityProfileOutputArgs struct {
	OrganizationId    pulumi.StringInput `pulumi:"organizationId"`
	SecurityProfileId pulumi.StringInput `pulumi:"securityProfileId"`
}

func (LookupSecurityProfileOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSecurityProfileArgs)(nil)).Elem()
}

type LookupSecurityProfileResultOutput struct{ *pulumi.OutputState }

func (LookupSecurityProfileResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSecurityProfileResult)(nil)).Elem()
}

func (o LookupSecurityProfileResultOutput) ToLookupSecurityProfileResultOutput() LookupSecurityProfileResultOutput {
	return o
}

func (o LookupSecurityProfileResultOutput) ToLookupSecurityProfileResultOutputWithContext(ctx context.Context) LookupSecurityProfileResultOutput {
	return o
}

// Description of the security profile.
func (o LookupSecurityProfileResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) string { return v.Description }).(pulumi.StringOutput)
}

// Display name of the security profile.
func (o LookupSecurityProfileResultOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) string { return v.DisplayName }).(pulumi.StringOutput)
}

// List of environments attached to security profile.
func (o LookupSecurityProfileResultOutput) Environments() GoogleCloudApigeeV1SecurityProfileEnvironmentResponseArrayOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) []GoogleCloudApigeeV1SecurityProfileEnvironmentResponse {
		return v.Environments
	}).(GoogleCloudApigeeV1SecurityProfileEnvironmentResponseArrayOutput)
}

// Maximum security score that can be generated by this profile.
func (o LookupSecurityProfileResultOutput) MaxScore() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) int { return v.MaxScore }).(pulumi.IntOutput)
}

// Minimum security score that can be generated by this profile.
func (o LookupSecurityProfileResultOutput) MinScore() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) int { return v.MinScore }).(pulumi.IntOutput)
}

// Immutable. Name of the security profile resource. Format: organizations/{org}/securityProfiles/{profile}
func (o LookupSecurityProfileResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) string { return v.Name }).(pulumi.StringOutput)
}

// Customized profile configuration that computes the security score.
func (o LookupSecurityProfileResultOutput) ProfileConfig() GoogleCloudApigeeV1ProfileConfigResponseOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) GoogleCloudApigeeV1ProfileConfigResponse { return v.ProfileConfig }).(GoogleCloudApigeeV1ProfileConfigResponseOutput)
}

// The time when revision was created.
func (o LookupSecurityProfileResultOutput) RevisionCreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) string { return v.RevisionCreateTime }).(pulumi.StringOutput)
}

// Revision ID of the security profile.
func (o LookupSecurityProfileResultOutput) RevisionId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) string { return v.RevisionId }).(pulumi.StringOutput)
}

// The time when revision was published. Once published, the security profile revision cannot be updated further and can be attached to environments.
func (o LookupSecurityProfileResultOutput) RevisionPublishTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) string { return v.RevisionPublishTime }).(pulumi.StringOutput)
}

// The time when revision was updated.
func (o LookupSecurityProfileResultOutput) RevisionUpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) string { return v.RevisionUpdateTime }).(pulumi.StringOutput)
}

// List of profile scoring configs in this revision.
func (o LookupSecurityProfileResultOutput) ScoringConfigs() GoogleCloudApigeeV1SecurityProfileScoringConfigResponseArrayOutput {
	return o.ApplyT(func(v LookupSecurityProfileResult) []GoogleCloudApigeeV1SecurityProfileScoringConfigResponse {
		return v.ScoringConfigs
	}).(GoogleCloudApigeeV1SecurityProfileScoringConfigResponseArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSecurityProfileResultOutput{})
}
