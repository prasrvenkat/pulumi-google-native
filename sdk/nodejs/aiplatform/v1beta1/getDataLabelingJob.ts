// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets a DataLabelingJob.
 */
export function getDataLabelingJob(args: GetDataLabelingJobArgs, opts?: pulumi.InvokeOptions): Promise<GetDataLabelingJobResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:aiplatform/v1beta1:getDataLabelingJob", {
        "dataLabelingJobId": args.dataLabelingJobId,
        "location": args.location,
        "project": args.project,
    }, opts);
}

export interface GetDataLabelingJobArgs {
    dataLabelingJobId: string;
    location: string;
    project?: string;
}

export interface GetDataLabelingJobResult {
    /**
     * Parameters that configure the active learning pipeline. Active learning will label the data incrementally via several iterations. For every iteration, it will select a batch of data based on the sampling strategy.
     */
    readonly activeLearningConfig: outputs.aiplatform.v1beta1.GoogleCloudAiplatformV1beta1ActiveLearningConfigResponse;
    /**
     * Labels to assign to annotations generated by this DataLabelingJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
     */
    readonly annotationLabels: {[key: string]: string};
    /**
     * Timestamp when this DataLabelingJob was created.
     */
    readonly createTime: string;
    /**
     * Estimated cost(in US dollars) that the DataLabelingJob has incurred to date.
     */
    readonly currentSpend: outputs.aiplatform.v1beta1.GoogleTypeMoneyResponse;
    /**
     * Dataset resource names. Right now we only support labeling from a single Dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
     */
    readonly datasets: string[];
    /**
     * The user-defined name of the DataLabelingJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a DataLabelingJob.
     */
    readonly displayName: string;
    /**
     * Customer-managed encryption key spec for a DataLabelingJob. If set, this DataLabelingJob will be secured by this key. Note: Annotations created in the DataLabelingJob are associated with the EncryptionSpec of the Dataset they are exported to.
     */
    readonly encryptionSpec: outputs.aiplatform.v1beta1.GoogleCloudAiplatformV1beta1EncryptionSpecResponse;
    /**
     * DataLabelingJob errors. It is only populated when job's state is `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.
     */
    readonly error: outputs.aiplatform.v1beta1.GoogleRpcStatusResponse;
    /**
     * Input config parameters for the DataLabelingJob.
     */
    readonly inputs: any;
    /**
     * Points to a YAML file stored on Google Cloud Storage describing the config for a specific type of DataLabelingJob. The schema files that can be used here are found in the https://storage.googleapis.com/google-cloud-aiplatform bucket in the /schema/datalabelingjob/inputs/ folder.
     */
    readonly inputsSchemaUri: string;
    /**
     * The Google Cloud Storage location of the instruction pdf. This pdf is shared with labelers, and provides detailed description on how to label DataItems in Datasets.
     */
    readonly instructionUri: string;
    /**
     * Number of labelers to work on each DataItem.
     */
    readonly labelerCount: number;
    /**
     * Current labeling job progress percentage scaled in interval [0, 100], indicating the percentage of DataItems that has been finished.
     */
    readonly labelingProgress: number;
    /**
     * The labels with user-defined metadata to organize your DataLabelingJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each DataLabelingJob: * "aiplatform.googleapis.com/schema": output only, its value is the inputs_schema's title.
     */
    readonly labels: {[key: string]: string};
    /**
     * Resource name of the DataLabelingJob.
     */
    readonly name: string;
    /**
     * The SpecialistPools' resource names associated with this job.
     */
    readonly specialistPools: string[];
    /**
     * The detailed state of the job.
     */
    readonly state: string;
    /**
     * Timestamp when this DataLabelingJob was updated most recently.
     */
    readonly updateTime: string;
}
/**
 * Gets a DataLabelingJob.
 */
export function getDataLabelingJobOutput(args: GetDataLabelingJobOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDataLabelingJobResult> {
    return pulumi.output(args).apply((a: any) => getDataLabelingJob(a, opts))
}

export interface GetDataLabelingJobOutputArgs {
    dataLabelingJobId: pulumi.Input<string>;
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}