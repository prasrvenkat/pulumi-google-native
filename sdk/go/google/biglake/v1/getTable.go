// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets the table specified by the resource name.
func LookupTable(ctx *pulumi.Context, args *LookupTableArgs, opts ...pulumi.InvokeOption) (*LookupTableResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTableResult
	err := ctx.Invoke("google-native:biglake/v1:getTable", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTableArgs struct {
	CatalogId  string  `pulumi:"catalogId"`
	DatabaseId string  `pulumi:"databaseId"`
	Location   string  `pulumi:"location"`
	Project    *string `pulumi:"project"`
	TableId    string  `pulumi:"tableId"`
}

type LookupTableResult struct {
	// The creation time of the table.
	CreateTime string `pulumi:"createTime"`
	// The deletion time of the table. Only set after the table is deleted.
	DeleteTime string `pulumi:"deleteTime"`
	// The checksum of a table object computed by the server based on the value of other fields. It may be sent on update requests to ensure the client has an up-to-date value before proceeding. It is only checked for update table operations.
	Etag string `pulumi:"etag"`
	// The time when this table is considered expired. Only set after the table is deleted.
	ExpireTime string `pulumi:"expireTime"`
	// Options of a Hive table.
	HiveOptions HiveTableOptionsResponse `pulumi:"hiveOptions"`
	// The resource name. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
	Name string `pulumi:"name"`
	// The table type.
	Type string `pulumi:"type"`
	// The last modification time of the table.
	UpdateTime string `pulumi:"updateTime"`
}

func LookupTableOutput(ctx *pulumi.Context, args LookupTableOutputArgs, opts ...pulumi.InvokeOption) LookupTableResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTableResult, error) {
			args := v.(LookupTableArgs)
			r, err := LookupTable(ctx, &args, opts...)
			var s LookupTableResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTableResultOutput)
}

type LookupTableOutputArgs struct {
	CatalogId  pulumi.StringInput    `pulumi:"catalogId"`
	DatabaseId pulumi.StringInput    `pulumi:"databaseId"`
	Location   pulumi.StringInput    `pulumi:"location"`
	Project    pulumi.StringPtrInput `pulumi:"project"`
	TableId    pulumi.StringInput    `pulumi:"tableId"`
}

func (LookupTableOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTableArgs)(nil)).Elem()
}

type LookupTableResultOutput struct{ *pulumi.OutputState }

func (LookupTableResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTableResult)(nil)).Elem()
}

func (o LookupTableResultOutput) ToLookupTableResultOutput() LookupTableResultOutput {
	return o
}

func (o LookupTableResultOutput) ToLookupTableResultOutputWithContext(ctx context.Context) LookupTableResultOutput {
	return o
}

// The creation time of the table.
func (o LookupTableResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTableResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// The deletion time of the table. Only set after the table is deleted.
func (o LookupTableResultOutput) DeleteTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTableResult) string { return v.DeleteTime }).(pulumi.StringOutput)
}

// The checksum of a table object computed by the server based on the value of other fields. It may be sent on update requests to ensure the client has an up-to-date value before proceeding. It is only checked for update table operations.
func (o LookupTableResultOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTableResult) string { return v.Etag }).(pulumi.StringOutput)
}

// The time when this table is considered expired. Only set after the table is deleted.
func (o LookupTableResultOutput) ExpireTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTableResult) string { return v.ExpireTime }).(pulumi.StringOutput)
}

// Options of a Hive table.
func (o LookupTableResultOutput) HiveOptions() HiveTableOptionsResponseOutput {
	return o.ApplyT(func(v LookupTableResult) HiveTableOptionsResponse { return v.HiveOptions }).(HiveTableOptionsResponseOutput)
}

// The resource name. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
func (o LookupTableResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTableResult) string { return v.Name }).(pulumi.StringOutput)
}

// The table type.
func (o LookupTableResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTableResult) string { return v.Type }).(pulumi.StringOutput)
}

// The last modification time of the table.
func (o LookupTableResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTableResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTableResultOutput{})
}