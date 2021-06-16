// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a domain mapping on the specified site.
type Domain struct {
	pulumi.CustomResourceState

	// Required. The domain name of the association.
	DomainName pulumi.StringOutput `pulumi:"domainName"`
	// If set, the domain should redirect with the provided parameters.
	DomainRedirect DomainRedirectResponseOutput `pulumi:"domainRedirect"`
	// Information about the provisioning of certificates and the health of the DNS resolution for the domain.
	Provisioning DomainProvisioningResponseOutput `pulumi:"provisioning"`
	// Required. The site name of the association.
	Site pulumi.StringOutput `pulumi:"site"`
	// Additional status of the domain association.
	Status pulumi.StringOutput `pulumi:"status"`
	// The time at which the domain was last updated.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
}

// NewDomain registers a new resource with the given unique name, arguments, and options.
func NewDomain(ctx *pulumi.Context,
	name string, args *DomainArgs, opts ...pulumi.ResourceOption) (*Domain, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Project == nil {
		return nil, errors.New("invalid value for required argument 'Project'")
	}
	if args.SiteId == nil {
		return nil, errors.New("invalid value for required argument 'SiteId'")
	}
	var resource Domain
	err := ctx.RegisterResource("google-native:firebasehosting/v1beta1:Domain", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDomain gets an existing Domain resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDomain(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DomainState, opts ...pulumi.ResourceOption) (*Domain, error) {
	var resource Domain
	err := ctx.ReadResource("google-native:firebasehosting/v1beta1:Domain", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Domain resources.
type domainState struct {
	// Required. The domain name of the association.
	DomainName *string `pulumi:"domainName"`
	// If set, the domain should redirect with the provided parameters.
	DomainRedirect *DomainRedirectResponse `pulumi:"domainRedirect"`
	// Information about the provisioning of certificates and the health of the DNS resolution for the domain.
	Provisioning *DomainProvisioningResponse `pulumi:"provisioning"`
	// Required. The site name of the association.
	Site *string `pulumi:"site"`
	// Additional status of the domain association.
	Status *string `pulumi:"status"`
	// The time at which the domain was last updated.
	UpdateTime *string `pulumi:"updateTime"`
}

type DomainState struct {
	// Required. The domain name of the association.
	DomainName pulumi.StringPtrInput
	// If set, the domain should redirect with the provided parameters.
	DomainRedirect DomainRedirectResponsePtrInput
	// Information about the provisioning of certificates and the health of the DNS resolution for the domain.
	Provisioning DomainProvisioningResponsePtrInput
	// Required. The site name of the association.
	Site pulumi.StringPtrInput
	// Additional status of the domain association.
	Status pulumi.StringPtrInput
	// The time at which the domain was last updated.
	UpdateTime pulumi.StringPtrInput
}

func (DomainState) ElementType() reflect.Type {
	return reflect.TypeOf((*domainState)(nil)).Elem()
}

type domainArgs struct {
	// Required. The domain name of the association.
	DomainName *string `pulumi:"domainName"`
	// If set, the domain should redirect with the provided parameters.
	DomainRedirect *DomainRedirect `pulumi:"domainRedirect"`
	Project        string          `pulumi:"project"`
	// Information about the provisioning of certificates and the health of the DNS resolution for the domain.
	Provisioning *DomainProvisioning `pulumi:"provisioning"`
	// Required. The site name of the association.
	Site   *string `pulumi:"site"`
	SiteId string  `pulumi:"siteId"`
	// Additional status of the domain association.
	Status *string `pulumi:"status"`
	// The time at which the domain was last updated.
	UpdateTime *string `pulumi:"updateTime"`
}

// The set of arguments for constructing a Domain resource.
type DomainArgs struct {
	// Required. The domain name of the association.
	DomainName pulumi.StringPtrInput
	// If set, the domain should redirect with the provided parameters.
	DomainRedirect DomainRedirectPtrInput
	Project        pulumi.StringInput
	// Information about the provisioning of certificates and the health of the DNS resolution for the domain.
	Provisioning DomainProvisioningPtrInput
	// Required. The site name of the association.
	Site   pulumi.StringPtrInput
	SiteId pulumi.StringInput
	// Additional status of the domain association.
	Status *DomainStatus
	// The time at which the domain was last updated.
	UpdateTime pulumi.StringPtrInput
}

func (DomainArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*domainArgs)(nil)).Elem()
}

type DomainInput interface {
	pulumi.Input

	ToDomainOutput() DomainOutput
	ToDomainOutputWithContext(ctx context.Context) DomainOutput
}

func (*Domain) ElementType() reflect.Type {
	return reflect.TypeOf((*Domain)(nil))
}

func (i *Domain) ToDomainOutput() DomainOutput {
	return i.ToDomainOutputWithContext(context.Background())
}

func (i *Domain) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainOutput)
}

type DomainOutput struct {
	*pulumi.OutputState
}

func (DomainOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Domain)(nil))
}

func (o DomainOutput) ToDomainOutput() DomainOutput {
	return o
}

func (o DomainOutput) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DomainOutput{})
}