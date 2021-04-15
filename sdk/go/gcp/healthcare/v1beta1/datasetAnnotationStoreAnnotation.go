// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a new Annotation record. It is valid to create Annotation objects for the same source more than once since a unique ID is assigned to each record by this service.
type DatasetAnnotationStoreAnnotation struct {
	pulumi.CustomResourceState

	// Details of the source.
	AnnotationSource AnnotationSourceResponseOutput `pulumi:"annotationSource"`
	// Additional information for this annotation record, such as annotator and verifier information or study campaign.
	CustomData pulumi.StringMapOutput `pulumi:"customData"`
	// Annotations for images. For example, bounding polygons.
	ImageAnnotation ImageAnnotationResponseOutput `pulumi:"imageAnnotation"`
	// Resource name of the Annotation, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/annotationStores/{annotation_store_id}/annotations/{annotation_id}`.
	Name pulumi.StringOutput `pulumi:"name"`
	// Annotations for resource. For example, classification tags.
	ResourceAnnotation ResourceAnnotationResponseOutput `pulumi:"resourceAnnotation"`
	// Annotations for sensitive texts. For example, a range that describes the location of sensitive text.
	TextAnnotation SensitiveTextAnnotationResponseOutput `pulumi:"textAnnotation"`
}

// NewDatasetAnnotationStoreAnnotation registers a new resource with the given unique name, arguments, and options.
func NewDatasetAnnotationStoreAnnotation(ctx *pulumi.Context,
	name string, args *DatasetAnnotationStoreAnnotationArgs, opts ...pulumi.ResourceOption) (*DatasetAnnotationStoreAnnotation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AnnotationStoresId == nil {
		return nil, errors.New("invalid value for required argument 'AnnotationStoresId'")
	}
	if args.AnnotationsId == nil {
		return nil, errors.New("invalid value for required argument 'AnnotationsId'")
	}
	if args.DatasetsId == nil {
		return nil, errors.New("invalid value for required argument 'DatasetsId'")
	}
	if args.LocationsId == nil {
		return nil, errors.New("invalid value for required argument 'LocationsId'")
	}
	if args.ProjectsId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectsId'")
	}
	var resource DatasetAnnotationStoreAnnotation
	err := ctx.RegisterResource("gcp-native:healthcare/v1beta1:DatasetAnnotationStoreAnnotation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatasetAnnotationStoreAnnotation gets an existing DatasetAnnotationStoreAnnotation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatasetAnnotationStoreAnnotation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatasetAnnotationStoreAnnotationState, opts ...pulumi.ResourceOption) (*DatasetAnnotationStoreAnnotation, error) {
	var resource DatasetAnnotationStoreAnnotation
	err := ctx.ReadResource("gcp-native:healthcare/v1beta1:DatasetAnnotationStoreAnnotation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DatasetAnnotationStoreAnnotation resources.
type datasetAnnotationStoreAnnotationState struct {
	// Details of the source.
	AnnotationSource *AnnotationSourceResponse `pulumi:"annotationSource"`
	// Additional information for this annotation record, such as annotator and verifier information or study campaign.
	CustomData map[string]string `pulumi:"customData"`
	// Annotations for images. For example, bounding polygons.
	ImageAnnotation *ImageAnnotationResponse `pulumi:"imageAnnotation"`
	// Resource name of the Annotation, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/annotationStores/{annotation_store_id}/annotations/{annotation_id}`.
	Name *string `pulumi:"name"`
	// Annotations for resource. For example, classification tags.
	ResourceAnnotation *ResourceAnnotationResponse `pulumi:"resourceAnnotation"`
	// Annotations for sensitive texts. For example, a range that describes the location of sensitive text.
	TextAnnotation *SensitiveTextAnnotationResponse `pulumi:"textAnnotation"`
}

type DatasetAnnotationStoreAnnotationState struct {
	// Details of the source.
	AnnotationSource AnnotationSourceResponsePtrInput
	// Additional information for this annotation record, such as annotator and verifier information or study campaign.
	CustomData pulumi.StringMapInput
	// Annotations for images. For example, bounding polygons.
	ImageAnnotation ImageAnnotationResponsePtrInput
	// Resource name of the Annotation, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/annotationStores/{annotation_store_id}/annotations/{annotation_id}`.
	Name pulumi.StringPtrInput
	// Annotations for resource. For example, classification tags.
	ResourceAnnotation ResourceAnnotationResponsePtrInput
	// Annotations for sensitive texts. For example, a range that describes the location of sensitive text.
	TextAnnotation SensitiveTextAnnotationResponsePtrInput
}

func (DatasetAnnotationStoreAnnotationState) ElementType() reflect.Type {
	return reflect.TypeOf((*datasetAnnotationStoreAnnotationState)(nil)).Elem()
}

type datasetAnnotationStoreAnnotationArgs struct {
	// Details of the source.
	AnnotationSource   *AnnotationSource `pulumi:"annotationSource"`
	AnnotationStoresId string            `pulumi:"annotationStoresId"`
	AnnotationsId      string            `pulumi:"annotationsId"`
	// Additional information for this annotation record, such as annotator and verifier information or study campaign.
	CustomData map[string]string `pulumi:"customData"`
	DatasetsId string            `pulumi:"datasetsId"`
	// Annotations for images. For example, bounding polygons.
	ImageAnnotation *ImageAnnotation `pulumi:"imageAnnotation"`
	LocationsId     string           `pulumi:"locationsId"`
	// Resource name of the Annotation, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/annotationStores/{annotation_store_id}/annotations/{annotation_id}`.
	Name       *string `pulumi:"name"`
	ProjectsId string  `pulumi:"projectsId"`
	// Annotations for resource. For example, classification tags.
	ResourceAnnotation *ResourceAnnotation `pulumi:"resourceAnnotation"`
	// Annotations for sensitive texts. For example, a range that describes the location of sensitive text.
	TextAnnotation *SensitiveTextAnnotation `pulumi:"textAnnotation"`
}

// The set of arguments for constructing a DatasetAnnotationStoreAnnotation resource.
type DatasetAnnotationStoreAnnotationArgs struct {
	// Details of the source.
	AnnotationSource   AnnotationSourcePtrInput
	AnnotationStoresId pulumi.StringInput
	AnnotationsId      pulumi.StringInput
	// Additional information for this annotation record, such as annotator and verifier information or study campaign.
	CustomData pulumi.StringMapInput
	DatasetsId pulumi.StringInput
	// Annotations for images. For example, bounding polygons.
	ImageAnnotation ImageAnnotationPtrInput
	LocationsId     pulumi.StringInput
	// Resource name of the Annotation, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/annotationStores/{annotation_store_id}/annotations/{annotation_id}`.
	Name       pulumi.StringPtrInput
	ProjectsId pulumi.StringInput
	// Annotations for resource. For example, classification tags.
	ResourceAnnotation ResourceAnnotationPtrInput
	// Annotations for sensitive texts. For example, a range that describes the location of sensitive text.
	TextAnnotation SensitiveTextAnnotationPtrInput
}

func (DatasetAnnotationStoreAnnotationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*datasetAnnotationStoreAnnotationArgs)(nil)).Elem()
}

type DatasetAnnotationStoreAnnotationInput interface {
	pulumi.Input

	ToDatasetAnnotationStoreAnnotationOutput() DatasetAnnotationStoreAnnotationOutput
	ToDatasetAnnotationStoreAnnotationOutputWithContext(ctx context.Context) DatasetAnnotationStoreAnnotationOutput
}

func (*DatasetAnnotationStoreAnnotation) ElementType() reflect.Type {
	return reflect.TypeOf((*DatasetAnnotationStoreAnnotation)(nil))
}

func (i *DatasetAnnotationStoreAnnotation) ToDatasetAnnotationStoreAnnotationOutput() DatasetAnnotationStoreAnnotationOutput {
	return i.ToDatasetAnnotationStoreAnnotationOutputWithContext(context.Background())
}

func (i *DatasetAnnotationStoreAnnotation) ToDatasetAnnotationStoreAnnotationOutputWithContext(ctx context.Context) DatasetAnnotationStoreAnnotationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatasetAnnotationStoreAnnotationOutput)
}

type DatasetAnnotationStoreAnnotationOutput struct {
	*pulumi.OutputState
}

func (DatasetAnnotationStoreAnnotationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DatasetAnnotationStoreAnnotation)(nil))
}

func (o DatasetAnnotationStoreAnnotationOutput) ToDatasetAnnotationStoreAnnotationOutput() DatasetAnnotationStoreAnnotationOutput {
	return o
}

func (o DatasetAnnotationStoreAnnotationOutput) ToDatasetAnnotationStoreAnnotationOutputWithContext(ctx context.Context) DatasetAnnotationStoreAnnotationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DatasetAnnotationStoreAnnotationOutput{})
}