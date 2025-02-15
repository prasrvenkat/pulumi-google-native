// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets an IndexEndpoint.
func LookupIndexEndpoint(ctx *pulumi.Context, args *LookupIndexEndpointArgs, opts ...pulumi.InvokeOption) (*LookupIndexEndpointResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupIndexEndpointResult
	err := ctx.Invoke("google-native:aiplatform/v1:getIndexEndpoint", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupIndexEndpointArgs struct {
	IndexEndpointId string  `pulumi:"indexEndpointId"`
	Location        string  `pulumi:"location"`
	Project         *string `pulumi:"project"`
}

type LookupIndexEndpointResult struct {
	// Timestamp when this IndexEndpoint was created.
	CreateTime string `pulumi:"createTime"`
	// The indexes deployed in this endpoint.
	DeployedIndexes []GoogleCloudAiplatformV1DeployedIndexResponse `pulumi:"deployedIndexes"`
	// The description of the IndexEndpoint.
	Description string `pulumi:"description"`
	// The display name of the IndexEndpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters.
	DisplayName string `pulumi:"displayName"`
	// Optional. Deprecated: If true, expose the IndexEndpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.
	//
	// Deprecated: Optional. Deprecated: If true, expose the IndexEndpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.
	EnablePrivateServiceConnect bool `pulumi:"enablePrivateServiceConnect"`
	// Immutable. Customer-managed encryption key spec for an IndexEndpoint. If set, this IndexEndpoint and all sub-resources of this IndexEndpoint will be secured by this key.
	EncryptionSpec GoogleCloudAiplatformV1EncryptionSpecResponse `pulumi:"encryptionSpec"`
	// Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
	Etag string `pulumi:"etag"`
	// The labels with user-defined metadata to organize your IndexEndpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
	Labels map[string]string `pulumi:"labels"`
	// The resource name of the IndexEndpoint.
	Name string `pulumi:"name"`
	// Optional. The full name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the IndexEndpoint should be peered. Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network. network and private_service_connect_config are mutually exclusive. [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where {project} is a project number, as in '12345', and {network} is network name.
	Network string `pulumi:"network"`
	// Optional. Configuration for private service connect. network and private_service_connect_config are mutually exclusive.
	PrivateServiceConnectConfig GoogleCloudAiplatformV1PrivateServiceConnectConfigResponse `pulumi:"privateServiceConnectConfig"`
	// If public_endpoint_enabled is true, this field will be populated with the domain name to use for this index endpoint.
	PublicEndpointDomainName string `pulumi:"publicEndpointDomainName"`
	// Optional. If true, the deployed index will be accessible through public endpoint.
	PublicEndpointEnabled bool `pulumi:"publicEndpointEnabled"`
	// Timestamp when this IndexEndpoint was last updated. This timestamp is not updated when the endpoint's DeployedIndexes are updated, e.g. due to updates of the original Indexes they are the deployments of.
	UpdateTime string `pulumi:"updateTime"`
}

func LookupIndexEndpointOutput(ctx *pulumi.Context, args LookupIndexEndpointOutputArgs, opts ...pulumi.InvokeOption) LookupIndexEndpointResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupIndexEndpointResult, error) {
			args := v.(LookupIndexEndpointArgs)
			r, err := LookupIndexEndpoint(ctx, &args, opts...)
			var s LookupIndexEndpointResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupIndexEndpointResultOutput)
}

type LookupIndexEndpointOutputArgs struct {
	IndexEndpointId pulumi.StringInput    `pulumi:"indexEndpointId"`
	Location        pulumi.StringInput    `pulumi:"location"`
	Project         pulumi.StringPtrInput `pulumi:"project"`
}

func (LookupIndexEndpointOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIndexEndpointArgs)(nil)).Elem()
}

type LookupIndexEndpointResultOutput struct{ *pulumi.OutputState }

func (LookupIndexEndpointResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIndexEndpointResult)(nil)).Elem()
}

func (o LookupIndexEndpointResultOutput) ToLookupIndexEndpointResultOutput() LookupIndexEndpointResultOutput {
	return o
}

func (o LookupIndexEndpointResultOutput) ToLookupIndexEndpointResultOutputWithContext(ctx context.Context) LookupIndexEndpointResultOutput {
	return o
}

// Timestamp when this IndexEndpoint was created.
func (o LookupIndexEndpointResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// The indexes deployed in this endpoint.
func (o LookupIndexEndpointResultOutput) DeployedIndexes() GoogleCloudAiplatformV1DeployedIndexResponseArrayOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) []GoogleCloudAiplatformV1DeployedIndexResponse {
		return v.DeployedIndexes
	}).(GoogleCloudAiplatformV1DeployedIndexResponseArrayOutput)
}

// The description of the IndexEndpoint.
func (o LookupIndexEndpointResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) string { return v.Description }).(pulumi.StringOutput)
}

// The display name of the IndexEndpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters.
func (o LookupIndexEndpointResultOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) string { return v.DisplayName }).(pulumi.StringOutput)
}

// Optional. Deprecated: If true, expose the IndexEndpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.
//
// Deprecated: Optional. Deprecated: If true, expose the IndexEndpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.
func (o LookupIndexEndpointResultOutput) EnablePrivateServiceConnect() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) bool { return v.EnablePrivateServiceConnect }).(pulumi.BoolOutput)
}

// Immutable. Customer-managed encryption key spec for an IndexEndpoint. If set, this IndexEndpoint and all sub-resources of this IndexEndpoint will be secured by this key.
func (o LookupIndexEndpointResultOutput) EncryptionSpec() GoogleCloudAiplatformV1EncryptionSpecResponseOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) GoogleCloudAiplatformV1EncryptionSpecResponse {
		return v.EncryptionSpec
	}).(GoogleCloudAiplatformV1EncryptionSpecResponseOutput)
}

// Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
func (o LookupIndexEndpointResultOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) string { return v.Etag }).(pulumi.StringOutput)
}

// The labels with user-defined metadata to organize your IndexEndpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
func (o LookupIndexEndpointResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

// The resource name of the IndexEndpoint.
func (o LookupIndexEndpointResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) string { return v.Name }).(pulumi.StringOutput)
}

// Optional. The full name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the IndexEndpoint should be peered. Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network. network and private_service_connect_config are mutually exclusive. [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where {project} is a project number, as in '12345', and {network} is network name.
func (o LookupIndexEndpointResultOutput) Network() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) string { return v.Network }).(pulumi.StringOutput)
}

// Optional. Configuration for private service connect. network and private_service_connect_config are mutually exclusive.
func (o LookupIndexEndpointResultOutput) PrivateServiceConnectConfig() GoogleCloudAiplatformV1PrivateServiceConnectConfigResponseOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) GoogleCloudAiplatformV1PrivateServiceConnectConfigResponse {
		return v.PrivateServiceConnectConfig
	}).(GoogleCloudAiplatformV1PrivateServiceConnectConfigResponseOutput)
}

// If public_endpoint_enabled is true, this field will be populated with the domain name to use for this index endpoint.
func (o LookupIndexEndpointResultOutput) PublicEndpointDomainName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) string { return v.PublicEndpointDomainName }).(pulumi.StringOutput)
}

// Optional. If true, the deployed index will be accessible through public endpoint.
func (o LookupIndexEndpointResultOutput) PublicEndpointEnabled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) bool { return v.PublicEndpointEnabled }).(pulumi.BoolOutput)
}

// Timestamp when this IndexEndpoint was last updated. This timestamp is not updated when the endpoint's DeployedIndexes are updated, e.g. due to updates of the original Indexes they are the deployments of.
func (o LookupIndexEndpointResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIndexEndpointResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupIndexEndpointResultOutput{})
}
