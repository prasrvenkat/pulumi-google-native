// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a new data transfer configuration.
type TransferConfig struct {
	pulumi.CustomResourceState

	// The number of days to look back to automatically refresh the data. For example, if `data_refresh_window_days = 10`, then every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if the data source supports the feature. Set the value to 0 to use the default value.
	DataRefreshWindowDays pulumi.IntOutput `pulumi:"dataRefreshWindowDays"`
	// Data source id. Cannot be changed once data transfer is created.
	DataSourceId pulumi.StringOutput `pulumi:"dataSourceId"`
	// Region in which BigQuery dataset is located.
	DatasetRegion pulumi.StringOutput `pulumi:"datasetRegion"`
	// The BigQuery target dataset id.
	DestinationDatasetId pulumi.StringOutput `pulumi:"destinationDatasetId"`
	// Is this config disabled. When set to true, no runs are scheduled for a given transfer.
	Disabled pulumi.BoolOutput `pulumi:"disabled"`
	// User specified display name for the data transfer.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// Email notifications will be sent according to these preferences to the email address of the user who owns this transfer config.
	EmailPreferences EmailPreferencesResponseOutput `pulumi:"emailPreferences"`
	// The resource name of the transfer config. Transfer config names have the form `projects/{project_id}/locations/{region}/transferConfigs/{config_id}`. Where `config_id` is usually a uuid, even though it is not guaranteed or required. The name is ignored when creating a transfer config.
	Name pulumi.StringOutput `pulumi:"name"`
	// Next time when data transfer will run.
	NextRunTime pulumi.StringOutput `pulumi:"nextRunTime"`
	// Pub/Sub topic where notifications will be sent after transfer runs associated with this transfer config finish.
	NotificationPubsubTopic pulumi.StringOutput `pulumi:"notificationPubsubTopic"`
	// Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer' section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq
	Params pulumi.StringMapOutput `pulumi:"params"`
	// Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the default value for the data source will be used. The specified times are in UTC. Examples of valid format: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. See more explanation about the format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format NOTE: the granularity should be at least 8 hours, or less frequent.
	Schedule pulumi.StringOutput `pulumi:"schedule"`
	// Options customizing the data transfer schedule.
	ScheduleOptions ScheduleOptionsResponseOutput `pulumi:"scheduleOptions"`
	// State of the most recently updated transfer run.
	State pulumi.StringOutput `pulumi:"state"`
	// Data transfer modification time. Ignored by server on input.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
}

// NewTransferConfig registers a new resource with the given unique name, arguments, and options.
func NewTransferConfig(ctx *pulumi.Context,
	name string, args *TransferConfigArgs, opts ...pulumi.ResourceOption) (*TransferConfig, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ProjectsId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectsId'")
	}
	if args.TransferConfigsId == nil {
		return nil, errors.New("invalid value for required argument 'TransferConfigsId'")
	}
	var resource TransferConfig
	err := ctx.RegisterResource("google-native:bigquerydatatransfer/v1:TransferConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTransferConfig gets an existing TransferConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTransferConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TransferConfigState, opts ...pulumi.ResourceOption) (*TransferConfig, error) {
	var resource TransferConfig
	err := ctx.ReadResource("google-native:bigquerydatatransfer/v1:TransferConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TransferConfig resources.
type transferConfigState struct {
	// The number of days to look back to automatically refresh the data. For example, if `data_refresh_window_days = 10`, then every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if the data source supports the feature. Set the value to 0 to use the default value.
	DataRefreshWindowDays *int `pulumi:"dataRefreshWindowDays"`
	// Data source id. Cannot be changed once data transfer is created.
	DataSourceId *string `pulumi:"dataSourceId"`
	// Region in which BigQuery dataset is located.
	DatasetRegion *string `pulumi:"datasetRegion"`
	// The BigQuery target dataset id.
	DestinationDatasetId *string `pulumi:"destinationDatasetId"`
	// Is this config disabled. When set to true, no runs are scheduled for a given transfer.
	Disabled *bool `pulumi:"disabled"`
	// User specified display name for the data transfer.
	DisplayName *string `pulumi:"displayName"`
	// Email notifications will be sent according to these preferences to the email address of the user who owns this transfer config.
	EmailPreferences *EmailPreferencesResponse `pulumi:"emailPreferences"`
	// The resource name of the transfer config. Transfer config names have the form `projects/{project_id}/locations/{region}/transferConfigs/{config_id}`. Where `config_id` is usually a uuid, even though it is not guaranteed or required. The name is ignored when creating a transfer config.
	Name *string `pulumi:"name"`
	// Next time when data transfer will run.
	NextRunTime *string `pulumi:"nextRunTime"`
	// Pub/Sub topic where notifications will be sent after transfer runs associated with this transfer config finish.
	NotificationPubsubTopic *string `pulumi:"notificationPubsubTopic"`
	// Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer' section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq
	Params map[string]string `pulumi:"params"`
	// Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the default value for the data source will be used. The specified times are in UTC. Examples of valid format: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. See more explanation about the format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format NOTE: the granularity should be at least 8 hours, or less frequent.
	Schedule *string `pulumi:"schedule"`
	// Options customizing the data transfer schedule.
	ScheduleOptions *ScheduleOptionsResponse `pulumi:"scheduleOptions"`
	// State of the most recently updated transfer run.
	State *string `pulumi:"state"`
	// Data transfer modification time. Ignored by server on input.
	UpdateTime *string `pulumi:"updateTime"`
}

type TransferConfigState struct {
	// The number of days to look back to automatically refresh the data. For example, if `data_refresh_window_days = 10`, then every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if the data source supports the feature. Set the value to 0 to use the default value.
	DataRefreshWindowDays pulumi.IntPtrInput
	// Data source id. Cannot be changed once data transfer is created.
	DataSourceId pulumi.StringPtrInput
	// Region in which BigQuery dataset is located.
	DatasetRegion pulumi.StringPtrInput
	// The BigQuery target dataset id.
	DestinationDatasetId pulumi.StringPtrInput
	// Is this config disabled. When set to true, no runs are scheduled for a given transfer.
	Disabled pulumi.BoolPtrInput
	// User specified display name for the data transfer.
	DisplayName pulumi.StringPtrInput
	// Email notifications will be sent according to these preferences to the email address of the user who owns this transfer config.
	EmailPreferences EmailPreferencesResponsePtrInput
	// The resource name of the transfer config. Transfer config names have the form `projects/{project_id}/locations/{region}/transferConfigs/{config_id}`. Where `config_id` is usually a uuid, even though it is not guaranteed or required. The name is ignored when creating a transfer config.
	Name pulumi.StringPtrInput
	// Next time when data transfer will run.
	NextRunTime pulumi.StringPtrInput
	// Pub/Sub topic where notifications will be sent after transfer runs associated with this transfer config finish.
	NotificationPubsubTopic pulumi.StringPtrInput
	// Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer' section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq
	Params pulumi.StringMapInput
	// Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the default value for the data source will be used. The specified times are in UTC. Examples of valid format: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. See more explanation about the format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format NOTE: the granularity should be at least 8 hours, or less frequent.
	Schedule pulumi.StringPtrInput
	// Options customizing the data transfer schedule.
	ScheduleOptions ScheduleOptionsResponsePtrInput
	// State of the most recently updated transfer run.
	State pulumi.StringPtrInput
	// Data transfer modification time. Ignored by server on input.
	UpdateTime pulumi.StringPtrInput
}

func (TransferConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*transferConfigState)(nil)).Elem()
}

type transferConfigArgs struct {
	// The number of days to look back to automatically refresh the data. For example, if `data_refresh_window_days = 10`, then every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if the data source supports the feature. Set the value to 0 to use the default value.
	DataRefreshWindowDays *int `pulumi:"dataRefreshWindowDays"`
	// Data source id. Cannot be changed once data transfer is created.
	DataSourceId *string `pulumi:"dataSourceId"`
	// The BigQuery target dataset id.
	DestinationDatasetId *string `pulumi:"destinationDatasetId"`
	// Is this config disabled. When set to true, no runs are scheduled for a given transfer.
	Disabled *bool `pulumi:"disabled"`
	// User specified display name for the data transfer.
	DisplayName *string `pulumi:"displayName"`
	// Email notifications will be sent according to these preferences to the email address of the user who owns this transfer config.
	EmailPreferences *EmailPreferences `pulumi:"emailPreferences"`
	// The resource name of the transfer config. Transfer config names have the form `projects/{project_id}/locations/{region}/transferConfigs/{config_id}`. Where `config_id` is usually a uuid, even though it is not guaranteed or required. The name is ignored when creating a transfer config.
	Name *string `pulumi:"name"`
	// Pub/Sub topic where notifications will be sent after transfer runs associated with this transfer config finish.
	NotificationPubsubTopic *string `pulumi:"notificationPubsubTopic"`
	// Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer' section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq
	Params     map[string]string `pulumi:"params"`
	ProjectsId string            `pulumi:"projectsId"`
	// Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the default value for the data source will be used. The specified times are in UTC. Examples of valid format: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. See more explanation about the format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format NOTE: the granularity should be at least 8 hours, or less frequent.
	Schedule *string `pulumi:"schedule"`
	// Options customizing the data transfer schedule.
	ScheduleOptions   *ScheduleOptions `pulumi:"scheduleOptions"`
	TransferConfigsId string           `pulumi:"transferConfigsId"`
}

// The set of arguments for constructing a TransferConfig resource.
type TransferConfigArgs struct {
	// The number of days to look back to automatically refresh the data. For example, if `data_refresh_window_days = 10`, then every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if the data source supports the feature. Set the value to 0 to use the default value.
	DataRefreshWindowDays pulumi.IntPtrInput
	// Data source id. Cannot be changed once data transfer is created.
	DataSourceId pulumi.StringPtrInput
	// The BigQuery target dataset id.
	DestinationDatasetId pulumi.StringPtrInput
	// Is this config disabled. When set to true, no runs are scheduled for a given transfer.
	Disabled pulumi.BoolPtrInput
	// User specified display name for the data transfer.
	DisplayName pulumi.StringPtrInput
	// Email notifications will be sent according to these preferences to the email address of the user who owns this transfer config.
	EmailPreferences EmailPreferencesPtrInput
	// The resource name of the transfer config. Transfer config names have the form `projects/{project_id}/locations/{region}/transferConfigs/{config_id}`. Where `config_id` is usually a uuid, even though it is not guaranteed or required. The name is ignored when creating a transfer config.
	Name pulumi.StringPtrInput
	// Pub/Sub topic where notifications will be sent after transfer runs associated with this transfer config finish.
	NotificationPubsubTopic pulumi.StringPtrInput
	// Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer' section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq
	Params     pulumi.StringMapInput
	ProjectsId pulumi.StringInput
	// Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the default value for the data source will be used. The specified times are in UTC. Examples of valid format: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. See more explanation about the format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format NOTE: the granularity should be at least 8 hours, or less frequent.
	Schedule pulumi.StringPtrInput
	// Options customizing the data transfer schedule.
	ScheduleOptions   ScheduleOptionsPtrInput
	TransferConfigsId pulumi.StringInput
}

func (TransferConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*transferConfigArgs)(nil)).Elem()
}

type TransferConfigInput interface {
	pulumi.Input

	ToTransferConfigOutput() TransferConfigOutput
	ToTransferConfigOutputWithContext(ctx context.Context) TransferConfigOutput
}

func (*TransferConfig) ElementType() reflect.Type {
	return reflect.TypeOf((*TransferConfig)(nil))
}

func (i *TransferConfig) ToTransferConfigOutput() TransferConfigOutput {
	return i.ToTransferConfigOutputWithContext(context.Background())
}

func (i *TransferConfig) ToTransferConfigOutputWithContext(ctx context.Context) TransferConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TransferConfigOutput)
}

type TransferConfigOutput struct {
	*pulumi.OutputState
}

func (TransferConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TransferConfig)(nil))
}

func (o TransferConfigOutput) ToTransferConfigOutput() TransferConfigOutput {
	return o
}

func (o TransferConfigOutput) ToTransferConfigOutputWithContext(ctx context.Context) TransferConfigOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(TransferConfigOutput{})
}