// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets a view on a log bucket.
func LookupFolderBucketView(ctx *pulumi.Context, args *LookupFolderBucketViewArgs, opts ...pulumi.InvokeOption) (*LookupFolderBucketViewResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupFolderBucketViewResult
	err := ctx.Invoke("google-native:logging/v2:getFolderBucketView", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupFolderBucketViewArgs struct {
	BucketId string `pulumi:"bucketId"`
	FolderId string `pulumi:"folderId"`
	Location string `pulumi:"location"`
	ViewId   string `pulumi:"viewId"`
}

type LookupFolderBucketViewResult struct {
	// The creation timestamp of the view.
	CreateTime string `pulumi:"createTime"`
	// Describes this view.
	Description string `pulumi:"description"`
	// Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout")
	Filter string `pulumi:"filter"`
	// The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view
	Name string `pulumi:"name"`
	// The last update timestamp of the view.
	UpdateTime string `pulumi:"updateTime"`
}

func LookupFolderBucketViewOutput(ctx *pulumi.Context, args LookupFolderBucketViewOutputArgs, opts ...pulumi.InvokeOption) LookupFolderBucketViewResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupFolderBucketViewResult, error) {
			args := v.(LookupFolderBucketViewArgs)
			r, err := LookupFolderBucketView(ctx, &args, opts...)
			var s LookupFolderBucketViewResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupFolderBucketViewResultOutput)
}

type LookupFolderBucketViewOutputArgs struct {
	BucketId pulumi.StringInput `pulumi:"bucketId"`
	FolderId pulumi.StringInput `pulumi:"folderId"`
	Location pulumi.StringInput `pulumi:"location"`
	ViewId   pulumi.StringInput `pulumi:"viewId"`
}

func (LookupFolderBucketViewOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFolderBucketViewArgs)(nil)).Elem()
}

type LookupFolderBucketViewResultOutput struct{ *pulumi.OutputState }

func (LookupFolderBucketViewResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFolderBucketViewResult)(nil)).Elem()
}

func (o LookupFolderBucketViewResultOutput) ToLookupFolderBucketViewResultOutput() LookupFolderBucketViewResultOutput {
	return o
}

func (o LookupFolderBucketViewResultOutput) ToLookupFolderBucketViewResultOutputWithContext(ctx context.Context) LookupFolderBucketViewResultOutput {
	return o
}

// The creation timestamp of the view.
func (o LookupFolderBucketViewResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFolderBucketViewResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// Describes this view.
func (o LookupFolderBucketViewResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFolderBucketViewResult) string { return v.Description }).(pulumi.StringOutput)
}

// Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout")
func (o LookupFolderBucketViewResultOutput) Filter() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFolderBucketViewResult) string { return v.Filter }).(pulumi.StringOutput)
}

// The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view
func (o LookupFolderBucketViewResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFolderBucketViewResult) string { return v.Name }).(pulumi.StringOutput)
}

// The last update timestamp of the view.
func (o LookupFolderBucketViewResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFolderBucketViewResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupFolderBucketViewResultOutput{})
}
