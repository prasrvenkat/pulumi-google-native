// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates an evaluation job.
// Auto-naming is currently not supported for this resource.
type EvaluationJob struct {
	pulumi.CustomResourceState

	// Name of the AnnotationSpecSet describing all the labels that your machine learning model outputs. You must create this resource before you create an evaluation job and provide its name in the following format: "projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}"
	AnnotationSpecSet pulumi.StringOutput `pulumi:"annotationSpecSet"`
	// Every time the evaluation job runs and an error occurs, the failed attempt is appended to this array.
	Attempts GoogleCloudDatalabelingV1beta1AttemptResponseArrayOutput `pulumi:"attempts"`
	// Timestamp of when this evaluation job was created.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Description of the job. The description can be up to 25,000 characters long.
	Description pulumi.StringOutput `pulumi:"description"`
	// Configuration details for the evaluation job.
	EvaluationJobConfig GoogleCloudDatalabelingV1beta1EvaluationJobConfigResponseOutput `pulumi:"evaluationJobConfig"`
	// Whether you want Data Labeling Service to provide ground truth labels for prediction input. If you want the service to assign human labelers to annotate your data, set this to `true`. If you want to provide your own ground truth labels in the evaluation job's BigQuery table, set this to `false`.
	LabelMissingGroundTruth pulumi.BoolOutput `pulumi:"labelMissingGroundTruth"`
	// The [AI Platform Prediction model version](/ml-engine/docs/prediction-overview) to be evaluated. Prediction input and output is sampled from this model version. When creating an evaluation job, specify the model version in the following format: "projects/{project_id}/models/{model_name}/versions/{version_name}" There can only be one evaluation job per model version.
	ModelVersion pulumi.StringOutput `pulumi:"modelVersion"`
	// After you create a job, Data Labeling Service assigns a name to the job with the following format: "projects/{project_id}/evaluationJobs/ {evaluation_job_id}"
	Name    pulumi.StringOutput `pulumi:"name"`
	Project pulumi.StringOutput `pulumi:"project"`
	// Describes the interval at which the job runs. This interval must be at least 1 day, and it is rounded to the nearest day. For example, if you specify a 50-hour interval, the job runs every 2 days. You can provide the schedule in [crontab format](/scheduler/docs/configuring/cron-job-schedules) or in an [English-like format](/appengine/docs/standard/python/config/cronref#schedule_format). Regardless of what you specify, the job will run at 10:00 AM UTC. Only the interval from this schedule is used, not the specific time of day.
	Schedule pulumi.StringOutput `pulumi:"schedule"`
	// Describes the current state of the job.
	State pulumi.StringOutput `pulumi:"state"`
}

// NewEvaluationJob registers a new resource with the given unique name, arguments, and options.
func NewEvaluationJob(ctx *pulumi.Context,
	name string, args *EvaluationJobArgs, opts ...pulumi.ResourceOption) (*EvaluationJob, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AnnotationSpecSet == nil {
		return nil, errors.New("invalid value for required argument 'AnnotationSpecSet'")
	}
	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.EvaluationJobConfig == nil {
		return nil, errors.New("invalid value for required argument 'EvaluationJobConfig'")
	}
	if args.LabelMissingGroundTruth == nil {
		return nil, errors.New("invalid value for required argument 'LabelMissingGroundTruth'")
	}
	if args.ModelVersion == nil {
		return nil, errors.New("invalid value for required argument 'ModelVersion'")
	}
	if args.Schedule == nil {
		return nil, errors.New("invalid value for required argument 'Schedule'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"project",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource EvaluationJob
	err := ctx.RegisterResource("google-native:datalabeling/v1beta1:EvaluationJob", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEvaluationJob gets an existing EvaluationJob resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEvaluationJob(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EvaluationJobState, opts ...pulumi.ResourceOption) (*EvaluationJob, error) {
	var resource EvaluationJob
	err := ctx.ReadResource("google-native:datalabeling/v1beta1:EvaluationJob", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EvaluationJob resources.
type evaluationJobState struct {
}

type EvaluationJobState struct {
}

func (EvaluationJobState) ElementType() reflect.Type {
	return reflect.TypeOf((*evaluationJobState)(nil)).Elem()
}

type evaluationJobArgs struct {
	// Name of the AnnotationSpecSet describing all the labels that your machine learning model outputs. You must create this resource before you create an evaluation job and provide its name in the following format: "projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}"
	AnnotationSpecSet string `pulumi:"annotationSpecSet"`
	// Description of the job. The description can be up to 25,000 characters long.
	Description string `pulumi:"description"`
	// Configuration details for the evaluation job.
	EvaluationJobConfig GoogleCloudDatalabelingV1beta1EvaluationJobConfig `pulumi:"evaluationJobConfig"`
	// Whether you want Data Labeling Service to provide ground truth labels for prediction input. If you want the service to assign human labelers to annotate your data, set this to `true`. If you want to provide your own ground truth labels in the evaluation job's BigQuery table, set this to `false`.
	LabelMissingGroundTruth bool `pulumi:"labelMissingGroundTruth"`
	// The [AI Platform Prediction model version](/ml-engine/docs/prediction-overview) to be evaluated. Prediction input and output is sampled from this model version. When creating an evaluation job, specify the model version in the following format: "projects/{project_id}/models/{model_name}/versions/{version_name}" There can only be one evaluation job per model version.
	ModelVersion string  `pulumi:"modelVersion"`
	Project      *string `pulumi:"project"`
	// Describes the interval at which the job runs. This interval must be at least 1 day, and it is rounded to the nearest day. For example, if you specify a 50-hour interval, the job runs every 2 days. You can provide the schedule in [crontab format](/scheduler/docs/configuring/cron-job-schedules) or in an [English-like format](/appengine/docs/standard/python/config/cronref#schedule_format). Regardless of what you specify, the job will run at 10:00 AM UTC. Only the interval from this schedule is used, not the specific time of day.
	Schedule string `pulumi:"schedule"`
}

// The set of arguments for constructing a EvaluationJob resource.
type EvaluationJobArgs struct {
	// Name of the AnnotationSpecSet describing all the labels that your machine learning model outputs. You must create this resource before you create an evaluation job and provide its name in the following format: "projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}"
	AnnotationSpecSet pulumi.StringInput
	// Description of the job. The description can be up to 25,000 characters long.
	Description pulumi.StringInput
	// Configuration details for the evaluation job.
	EvaluationJobConfig GoogleCloudDatalabelingV1beta1EvaluationJobConfigInput
	// Whether you want Data Labeling Service to provide ground truth labels for prediction input. If you want the service to assign human labelers to annotate your data, set this to `true`. If you want to provide your own ground truth labels in the evaluation job's BigQuery table, set this to `false`.
	LabelMissingGroundTruth pulumi.BoolInput
	// The [AI Platform Prediction model version](/ml-engine/docs/prediction-overview) to be evaluated. Prediction input and output is sampled from this model version. When creating an evaluation job, specify the model version in the following format: "projects/{project_id}/models/{model_name}/versions/{version_name}" There can only be one evaluation job per model version.
	ModelVersion pulumi.StringInput
	Project      pulumi.StringPtrInput
	// Describes the interval at which the job runs. This interval must be at least 1 day, and it is rounded to the nearest day. For example, if you specify a 50-hour interval, the job runs every 2 days. You can provide the schedule in [crontab format](/scheduler/docs/configuring/cron-job-schedules) or in an [English-like format](/appengine/docs/standard/python/config/cronref#schedule_format). Regardless of what you specify, the job will run at 10:00 AM UTC. Only the interval from this schedule is used, not the specific time of day.
	Schedule pulumi.StringInput
}

func (EvaluationJobArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*evaluationJobArgs)(nil)).Elem()
}

type EvaluationJobInput interface {
	pulumi.Input

	ToEvaluationJobOutput() EvaluationJobOutput
	ToEvaluationJobOutputWithContext(ctx context.Context) EvaluationJobOutput
}

func (*EvaluationJob) ElementType() reflect.Type {
	return reflect.TypeOf((**EvaluationJob)(nil)).Elem()
}

func (i *EvaluationJob) ToEvaluationJobOutput() EvaluationJobOutput {
	return i.ToEvaluationJobOutputWithContext(context.Background())
}

func (i *EvaluationJob) ToEvaluationJobOutputWithContext(ctx context.Context) EvaluationJobOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EvaluationJobOutput)
}

type EvaluationJobOutput struct{ *pulumi.OutputState }

func (EvaluationJobOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EvaluationJob)(nil)).Elem()
}

func (o EvaluationJobOutput) ToEvaluationJobOutput() EvaluationJobOutput {
	return o
}

func (o EvaluationJobOutput) ToEvaluationJobOutputWithContext(ctx context.Context) EvaluationJobOutput {
	return o
}

// Name of the AnnotationSpecSet describing all the labels that your machine learning model outputs. You must create this resource before you create an evaluation job and provide its name in the following format: "projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}"
func (o EvaluationJobOutput) AnnotationSpecSet() pulumi.StringOutput {
	return o.ApplyT(func(v *EvaluationJob) pulumi.StringOutput { return v.AnnotationSpecSet }).(pulumi.StringOutput)
}

// Every time the evaluation job runs and an error occurs, the failed attempt is appended to this array.
func (o EvaluationJobOutput) Attempts() GoogleCloudDatalabelingV1beta1AttemptResponseArrayOutput {
	return o.ApplyT(func(v *EvaluationJob) GoogleCloudDatalabelingV1beta1AttemptResponseArrayOutput { return v.Attempts }).(GoogleCloudDatalabelingV1beta1AttemptResponseArrayOutput)
}

// Timestamp of when this evaluation job was created.
func (o EvaluationJobOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *EvaluationJob) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Description of the job. The description can be up to 25,000 characters long.
func (o EvaluationJobOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *EvaluationJob) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Configuration details for the evaluation job.
func (o EvaluationJobOutput) EvaluationJobConfig() GoogleCloudDatalabelingV1beta1EvaluationJobConfigResponseOutput {
	return o.ApplyT(func(v *EvaluationJob) GoogleCloudDatalabelingV1beta1EvaluationJobConfigResponseOutput {
		return v.EvaluationJobConfig
	}).(GoogleCloudDatalabelingV1beta1EvaluationJobConfigResponseOutput)
}

// Whether you want Data Labeling Service to provide ground truth labels for prediction input. If you want the service to assign human labelers to annotate your data, set this to `true`. If you want to provide your own ground truth labels in the evaluation job's BigQuery table, set this to `false`.
func (o EvaluationJobOutput) LabelMissingGroundTruth() pulumi.BoolOutput {
	return o.ApplyT(func(v *EvaluationJob) pulumi.BoolOutput { return v.LabelMissingGroundTruth }).(pulumi.BoolOutput)
}

// The [AI Platform Prediction model version](/ml-engine/docs/prediction-overview) to be evaluated. Prediction input and output is sampled from this model version. When creating an evaluation job, specify the model version in the following format: "projects/{project_id}/models/{model_name}/versions/{version_name}" There can only be one evaluation job per model version.
func (o EvaluationJobOutput) ModelVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *EvaluationJob) pulumi.StringOutput { return v.ModelVersion }).(pulumi.StringOutput)
}

// After you create a job, Data Labeling Service assigns a name to the job with the following format: "projects/{project_id}/evaluationJobs/ {evaluation_job_id}"
func (o EvaluationJobOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *EvaluationJob) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o EvaluationJobOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *EvaluationJob) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// Describes the interval at which the job runs. This interval must be at least 1 day, and it is rounded to the nearest day. For example, if you specify a 50-hour interval, the job runs every 2 days. You can provide the schedule in [crontab format](/scheduler/docs/configuring/cron-job-schedules) or in an [English-like format](/appengine/docs/standard/python/config/cronref#schedule_format). Regardless of what you specify, the job will run at 10:00 AM UTC. Only the interval from this schedule is used, not the specific time of day.
func (o EvaluationJobOutput) Schedule() pulumi.StringOutput {
	return o.ApplyT(func(v *EvaluationJob) pulumi.StringOutput { return v.Schedule }).(pulumi.StringOutput)
}

// Describes the current state of the job.
func (o EvaluationJobOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *EvaluationJob) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EvaluationJobInput)(nil)).Elem(), &EvaluationJob{})
	pulumi.RegisterOutputType(EvaluationJobOutput{})
}
