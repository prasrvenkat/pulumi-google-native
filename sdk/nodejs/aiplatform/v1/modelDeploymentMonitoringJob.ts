// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval.
 * Auto-naming is currently not supported for this resource.
 */
export class ModelDeploymentMonitoringJob extends pulumi.CustomResource {
    /**
     * Get an existing ModelDeploymentMonitoringJob resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ModelDeploymentMonitoringJob {
        return new ModelDeploymentMonitoringJob(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:aiplatform/v1:ModelDeploymentMonitoringJob';

    /**
     * Returns true if the given object is an instance of ModelDeploymentMonitoringJob.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ModelDeploymentMonitoringJob {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ModelDeploymentMonitoringJob.__pulumiType;
    }

    /**
     * YAML schema file uri describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze. If this field is empty, all the feature data types are inferred from predict_instance_schema_uri, meaning that TFDV will use the data in the exact format(data type) as prediction request/response. If there are any data type differences between predict instance and TFDV instance, this field can be used to override the schema. For models trained with Vertex AI, this field must be set as all the fields in predict instance formatted as string.
     */
    public readonly analysisInstanceSchemaUri!: pulumi.Output<string>;
    /**
     * The created bigquery tables for the job under customer project. Customer could do their own query & analysis. There could be 4 log tables in maximum: 1. Training data logging predict request/response 2. Serving data logging predict request/response
     */
    public /*out*/ readonly bigqueryTables!: pulumi.Output<outputs.aiplatform.v1.GoogleCloudAiplatformV1ModelDeploymentMonitoringBigQueryTableResponse[]>;
    /**
     * Timestamp when this ModelDeploymentMonitoringJob was created.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * The user-defined name of the ModelDeploymentMonitoringJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a ModelDeploymentMonitoringJob.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * If true, the scheduled monitoring pipeline logs are sent to Google Cloud Logging, including pipeline status and anomalies detected. Please note the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging#pricing).
     */
    public readonly enableMonitoringPipelineLogs!: pulumi.Output<boolean>;
    /**
     * Customer-managed encryption key spec for a ModelDeploymentMonitoringJob. If set, this ModelDeploymentMonitoringJob and all sub-resources of this ModelDeploymentMonitoringJob will be secured by this key.
     */
    public readonly encryptionSpec!: pulumi.Output<outputs.aiplatform.v1.GoogleCloudAiplatformV1EncryptionSpecResponse>;
    /**
     * Endpoint resource name. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
     */
    public readonly endpoint!: pulumi.Output<string>;
    /**
     * Only populated when the job's state is `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.
     */
    public /*out*/ readonly error!: pulumi.Output<outputs.aiplatform.v1.GoogleRpcStatusResponse>;
    /**
     * The labels with user-defined metadata to organize your ModelDeploymentMonitoringJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string}>;
    /**
     * Latest triggered monitoring pipeline metadata.
     */
    public /*out*/ readonly latestMonitoringPipelineMetadata!: pulumi.Output<outputs.aiplatform.v1.GoogleCloudAiplatformV1ModelDeploymentMonitoringJobLatestMonitoringPipelineMetadataResponse>;
    public readonly location!: pulumi.Output<string>;
    /**
     * The TTL of BigQuery tables in user projects which stores logs. A day is the basic unit of the TTL and we take the ceil of TTL/86400(a day). e.g. { second: 3600} indicates ttl = 1 day.
     */
    public readonly logTtl!: pulumi.Output<string>;
    /**
     * Sample Strategy for logging.
     */
    public readonly loggingSamplingStrategy!: pulumi.Output<outputs.aiplatform.v1.GoogleCloudAiplatformV1SamplingStrategyResponse>;
    /**
     * The config for monitoring objectives. This is a per DeployedModel config. Each DeployedModel needs to be configured separately.
     */
    public readonly modelDeploymentMonitoringObjectiveConfigs!: pulumi.Output<outputs.aiplatform.v1.GoogleCloudAiplatformV1ModelDeploymentMonitoringObjectiveConfigResponse[]>;
    /**
     * Schedule config for running the monitoring job.
     */
    public readonly modelDeploymentMonitoringScheduleConfig!: pulumi.Output<outputs.aiplatform.v1.GoogleCloudAiplatformV1ModelDeploymentMonitoringScheduleConfigResponse>;
    /**
     * Alert config for model monitoring.
     */
    public readonly modelMonitoringAlertConfig!: pulumi.Output<outputs.aiplatform.v1.GoogleCloudAiplatformV1ModelMonitoringAlertConfigResponse>;
    /**
     * Resource name of a ModelDeploymentMonitoringJob.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * Timestamp when this monitoring pipeline will be scheduled to run for the next round.
     */
    public /*out*/ readonly nextScheduleTime!: pulumi.Output<string>;
    /**
     * YAML schema file uri describing the format of a single instance, which are given to format this Endpoint's prediction (and explanation). If not set, we will generate predict schema from collected predict requests.
     */
    public readonly predictInstanceSchemaUri!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    /**
     * Sample Predict instance, same format as PredictRequest.instances, this can be set as a replacement of ModelDeploymentMonitoringJob.predict_instance_schema_uri. If not set, we will generate predict schema from collected predict requests.
     */
    public readonly samplePredictInstance!: pulumi.Output<any>;
    /**
     * Schedule state when the monitoring job is in Running state.
     */
    public /*out*/ readonly scheduleState!: pulumi.Output<string>;
    /**
     * The detailed state of the monitoring job. When the job is still creating, the state will be 'PENDING'. Once the job is successfully created, the state will be 'RUNNING'. Pause the job, the state will be 'PAUSED'. Resume the job, the state will return to 'RUNNING'.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * Stats anomalies base folder path.
     */
    public readonly statsAnomaliesBaseDirectory!: pulumi.Output<outputs.aiplatform.v1.GoogleCloudAiplatformV1GcsDestinationResponse>;
    /**
     * Timestamp when this ModelDeploymentMonitoringJob was updated most recently.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a ModelDeploymentMonitoringJob resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ModelDeploymentMonitoringJobArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.displayName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'displayName'");
            }
            if ((!args || args.endpoint === undefined) && !opts.urn) {
                throw new Error("Missing required property 'endpoint'");
            }
            if ((!args || args.loggingSamplingStrategy === undefined) && !opts.urn) {
                throw new Error("Missing required property 'loggingSamplingStrategy'");
            }
            if ((!args || args.modelDeploymentMonitoringObjectiveConfigs === undefined) && !opts.urn) {
                throw new Error("Missing required property 'modelDeploymentMonitoringObjectiveConfigs'");
            }
            if ((!args || args.modelDeploymentMonitoringScheduleConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'modelDeploymentMonitoringScheduleConfig'");
            }
            resourceInputs["analysisInstanceSchemaUri"] = args ? args.analysisInstanceSchemaUri : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["enableMonitoringPipelineLogs"] = args ? args.enableMonitoringPipelineLogs : undefined;
            resourceInputs["encryptionSpec"] = args ? args.encryptionSpec : undefined;
            resourceInputs["endpoint"] = args ? args.endpoint : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["logTtl"] = args ? args.logTtl : undefined;
            resourceInputs["loggingSamplingStrategy"] = args ? args.loggingSamplingStrategy : undefined;
            resourceInputs["modelDeploymentMonitoringObjectiveConfigs"] = args ? args.modelDeploymentMonitoringObjectiveConfigs : undefined;
            resourceInputs["modelDeploymentMonitoringScheduleConfig"] = args ? args.modelDeploymentMonitoringScheduleConfig : undefined;
            resourceInputs["modelMonitoringAlertConfig"] = args ? args.modelMonitoringAlertConfig : undefined;
            resourceInputs["predictInstanceSchemaUri"] = args ? args.predictInstanceSchemaUri : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["samplePredictInstance"] = args ? args.samplePredictInstance : undefined;
            resourceInputs["statsAnomaliesBaseDirectory"] = args ? args.statsAnomaliesBaseDirectory : undefined;
            resourceInputs["bigqueryTables"] = undefined /*out*/;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["error"] = undefined /*out*/;
            resourceInputs["latestMonitoringPipelineMetadata"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["nextScheduleTime"] = undefined /*out*/;
            resourceInputs["scheduleState"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["analysisInstanceSchemaUri"] = undefined /*out*/;
            resourceInputs["bigqueryTables"] = undefined /*out*/;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["displayName"] = undefined /*out*/;
            resourceInputs["enableMonitoringPipelineLogs"] = undefined /*out*/;
            resourceInputs["encryptionSpec"] = undefined /*out*/;
            resourceInputs["endpoint"] = undefined /*out*/;
            resourceInputs["error"] = undefined /*out*/;
            resourceInputs["labels"] = undefined /*out*/;
            resourceInputs["latestMonitoringPipelineMetadata"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["logTtl"] = undefined /*out*/;
            resourceInputs["loggingSamplingStrategy"] = undefined /*out*/;
            resourceInputs["modelDeploymentMonitoringObjectiveConfigs"] = undefined /*out*/;
            resourceInputs["modelDeploymentMonitoringScheduleConfig"] = undefined /*out*/;
            resourceInputs["modelMonitoringAlertConfig"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["nextScheduleTime"] = undefined /*out*/;
            resourceInputs["predictInstanceSchemaUri"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["samplePredictInstance"] = undefined /*out*/;
            resourceInputs["scheduleState"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["statsAnomaliesBaseDirectory"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["location", "project"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ModelDeploymentMonitoringJob.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ModelDeploymentMonitoringJob resource.
 */
export interface ModelDeploymentMonitoringJobArgs {
    /**
     * YAML schema file uri describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze. If this field is empty, all the feature data types are inferred from predict_instance_schema_uri, meaning that TFDV will use the data in the exact format(data type) as prediction request/response. If there are any data type differences between predict instance and TFDV instance, this field can be used to override the schema. For models trained with Vertex AI, this field must be set as all the fields in predict instance formatted as string.
     */
    analysisInstanceSchemaUri?: pulumi.Input<string>;
    /**
     * The user-defined name of the ModelDeploymentMonitoringJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a ModelDeploymentMonitoringJob.
     */
    displayName: pulumi.Input<string>;
    /**
     * If true, the scheduled monitoring pipeline logs are sent to Google Cloud Logging, including pipeline status and anomalies detected. Please note the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging#pricing).
     */
    enableMonitoringPipelineLogs?: pulumi.Input<boolean>;
    /**
     * Customer-managed encryption key spec for a ModelDeploymentMonitoringJob. If set, this ModelDeploymentMonitoringJob and all sub-resources of this ModelDeploymentMonitoringJob will be secured by this key.
     */
    encryptionSpec?: pulumi.Input<inputs.aiplatform.v1.GoogleCloudAiplatformV1EncryptionSpecArgs>;
    /**
     * Endpoint resource name. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
     */
    endpoint: pulumi.Input<string>;
    /**
     * The labels with user-defined metadata to organize your ModelDeploymentMonitoringJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    location?: pulumi.Input<string>;
    /**
     * The TTL of BigQuery tables in user projects which stores logs. A day is the basic unit of the TTL and we take the ceil of TTL/86400(a day). e.g. { second: 3600} indicates ttl = 1 day.
     */
    logTtl?: pulumi.Input<string>;
    /**
     * Sample Strategy for logging.
     */
    loggingSamplingStrategy: pulumi.Input<inputs.aiplatform.v1.GoogleCloudAiplatformV1SamplingStrategyArgs>;
    /**
     * The config for monitoring objectives. This is a per DeployedModel config. Each DeployedModel needs to be configured separately.
     */
    modelDeploymentMonitoringObjectiveConfigs: pulumi.Input<pulumi.Input<inputs.aiplatform.v1.GoogleCloudAiplatformV1ModelDeploymentMonitoringObjectiveConfigArgs>[]>;
    /**
     * Schedule config for running the monitoring job.
     */
    modelDeploymentMonitoringScheduleConfig: pulumi.Input<inputs.aiplatform.v1.GoogleCloudAiplatformV1ModelDeploymentMonitoringScheduleConfigArgs>;
    /**
     * Alert config for model monitoring.
     */
    modelMonitoringAlertConfig?: pulumi.Input<inputs.aiplatform.v1.GoogleCloudAiplatformV1ModelMonitoringAlertConfigArgs>;
    /**
     * YAML schema file uri describing the format of a single instance, which are given to format this Endpoint's prediction (and explanation). If not set, we will generate predict schema from collected predict requests.
     */
    predictInstanceSchemaUri?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    /**
     * Sample Predict instance, same format as PredictRequest.instances, this can be set as a replacement of ModelDeploymentMonitoringJob.predict_instance_schema_uri. If not set, we will generate predict schema from collected predict requests.
     */
    samplePredictInstance?: any;
    /**
     * Stats anomalies base folder path.
     */
    statsAnomaliesBaseDirectory?: pulumi.Input<inputs.aiplatform.v1.GoogleCloudAiplatformV1GcsDestinationArgs>;
}
