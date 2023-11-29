// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets the catalog specified by the resource name.
func LookupCatalog(ctx *pulumi.Context, args *LookupCatalogArgs, opts ...pulumi.InvokeOption) (*LookupCatalogResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCatalogResult
	err := ctx.Invoke("google-native:biglake/v1:getCatalog", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupCatalogArgs struct {
	CatalogId string  `pulumi:"catalogId"`
	Location  string  `pulumi:"location"`
	Project   *string `pulumi:"project"`
}

type LookupCatalogResult struct {
	// The creation time of the catalog.
	CreateTime string `pulumi:"createTime"`
	// The deletion time of the catalog. Only set after the catalog is deleted.
	DeleteTime string `pulumi:"deleteTime"`
	// The time when this catalog is considered expired. Only set after the catalog is deleted.
	ExpireTime string `pulumi:"expireTime"`
	// The resource name. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
	Name string `pulumi:"name"`
	// The last modification time of the catalog.
	UpdateTime string `pulumi:"updateTime"`
}

func LookupCatalogOutput(ctx *pulumi.Context, args LookupCatalogOutputArgs, opts ...pulumi.InvokeOption) LookupCatalogResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCatalogResult, error) {
			args := v.(LookupCatalogArgs)
			r, err := LookupCatalog(ctx, &args, opts...)
			var s LookupCatalogResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCatalogResultOutput)
}

type LookupCatalogOutputArgs struct {
	CatalogId pulumi.StringInput    `pulumi:"catalogId"`
	Location  pulumi.StringInput    `pulumi:"location"`
	Project   pulumi.StringPtrInput `pulumi:"project"`
}

func (LookupCatalogOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCatalogArgs)(nil)).Elem()
}

type LookupCatalogResultOutput struct{ *pulumi.OutputState }

func (LookupCatalogResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCatalogResult)(nil)).Elem()
}

func (o LookupCatalogResultOutput) ToLookupCatalogResultOutput() LookupCatalogResultOutput {
	return o
}

func (o LookupCatalogResultOutput) ToLookupCatalogResultOutputWithContext(ctx context.Context) LookupCatalogResultOutput {
	return o
}

// The creation time of the catalog.
func (o LookupCatalogResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCatalogResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// The deletion time of the catalog. Only set after the catalog is deleted.
func (o LookupCatalogResultOutput) DeleteTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCatalogResult) string { return v.DeleteTime }).(pulumi.StringOutput)
}

// The time when this catalog is considered expired. Only set after the catalog is deleted.
func (o LookupCatalogResultOutput) ExpireTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCatalogResult) string { return v.ExpireTime }).(pulumi.StringOutput)
}

// The resource name. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
func (o LookupCatalogResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCatalogResult) string { return v.Name }).(pulumi.StringOutput)
}

// The last modification time of the catalog.
func (o LookupCatalogResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCatalogResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCatalogResultOutput{})
}