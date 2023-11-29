// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a TrainingPipeline. A created TrainingPipeline right away will be attempted to be run.
 * Auto-naming is currently not supported for this resource.
 */
export class TrainingPipeline extends pulumi.CustomResource {
    /**
     * Get an existing TrainingPipeline resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): TrainingPipeline {
        return new TrainingPipeline(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:aiplatform/v1:TrainingPipeline';

    /**
     * Returns true if the given object is an instance of TrainingPipeline.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TrainingPipeline {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TrainingPipeline.__pulumiType;
    }

    /**
     * Time when the TrainingPipeline was created.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * The user-defined name of this TrainingPipeline.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * Customer-managed encryption key spec for a TrainingPipeline. If set, this TrainingPipeline will be secured by this key. Note: Model trained by this TrainingPipeline is also secured by this key if model_to_upload is not set separately.
     */
    public readonly encryptionSpec!: pulumi.Output<outputs.aiplatform.v1.GoogleCloudAiplatformV1EncryptionSpecResponse>;
    /**
     * Time when the TrainingPipeline entered any of the following states: `PIPELINE_STATE_SUCCEEDED`, `PIPELINE_STATE_FAILED`, `PIPELINE_STATE_CANCELLED`.
     */
    public /*out*/ readonly endTime!: pulumi.Output<string>;
    /**
     * Only populated when the pipeline's state is `PIPELINE_STATE_FAILED` or `PIPELINE_STATE_CANCELLED`.
     */
    public /*out*/ readonly error!: pulumi.Output<outputs.aiplatform.v1.GoogleRpcStatusResponse>;
    /**
     * Specifies Vertex AI owned input data that may be used for training the Model. The TrainingPipeline's training_task_definition should make clear whether this config is used and if there are any special requirements on how it should be filled. If nothing about this config is mentioned in the training_task_definition, then it should be assumed that the TrainingPipeline does not depend on this configuration.
     */
    public readonly inputDataConfig!: pulumi.Output<outputs.aiplatform.v1.GoogleCloudAiplatformV1InputDataConfigResponse>;
    /**
     * The labels with user-defined metadata to organize TrainingPipelines. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string}>;
    public readonly location!: pulumi.Output<string>;
    /**
     * Optional. The ID to use for the uploaded Model, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.
     */
    public readonly modelId!: pulumi.Output<string>;
    /**
     * Describes the Model that may be uploaded (via ModelService.UploadModel) by this TrainingPipeline. The TrainingPipeline's training_task_definition should make clear whether this Model description should be populated, and if there are any special requirements regarding how it should be filled. If nothing is mentioned in the training_task_definition, then it should be assumed that this field should not be filled and the training task either uploads the Model without a need of this information, or that training task does not support uploading a Model as part of the pipeline. When the Pipeline's state becomes `PIPELINE_STATE_SUCCEEDED` and the trained Model had been uploaded into Vertex AI, then the model_to_upload's resource name is populated. The Model is always uploaded into the Project and Location in which this pipeline is.
     */
    public readonly modelToUpload!: pulumi.Output<outputs.aiplatform.v1.GoogleCloudAiplatformV1ModelResponse>;
    /**
     * Resource name of the TrainingPipeline.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * Optional. When specify this field, the `model_to_upload` will not be uploaded as a new model, instead, it will become a new version of this `parent_model`.
     */
    public readonly parentModel!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    /**
     * Time when the TrainingPipeline for the first time entered the `PIPELINE_STATE_RUNNING` state.
     */
    public /*out*/ readonly startTime!: pulumi.Output<string>;
    /**
     * The detailed state of the pipeline.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * A Google Cloud Storage path to the YAML file that defines the training task which is responsible for producing the model artifact, and may also include additional auxiliary work. The definition files that can be used here are found in gs://google-cloud-aiplatform/schema/trainingjob/definition/. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.
     */
    public readonly trainingTaskDefinition!: pulumi.Output<string>;
    /**
     * The training task's parameter(s), as specified in the training_task_definition's `inputs`.
     */
    public readonly trainingTaskInputs!: pulumi.Output<any>;
    /**
     * The metadata information as specified in the training_task_definition's `metadata`. This metadata is an auxiliary runtime and final information about the training task. While the pipeline is running this information is populated only at a best effort basis. Only present if the pipeline's training_task_definition contains `metadata` object.
     */
    public /*out*/ readonly trainingTaskMetadata!: pulumi.Output<any>;
    /**
     * Time when the TrainingPipeline was most recently updated.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a TrainingPipeline resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TrainingPipelineArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.displayName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'displayName'");
            }
            if ((!args || args.trainingTaskDefinition === undefined) && !opts.urn) {
                throw new Error("Missing required property 'trainingTaskDefinition'");
            }
            if ((!args || args.trainingTaskInputs === undefined) && !opts.urn) {
                throw new Error("Missing required property 'trainingTaskInputs'");
            }
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["encryptionSpec"] = args ? args.encryptionSpec : undefined;
            resourceInputs["inputDataConfig"] = args ? args.inputDataConfig : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["modelId"] = args ? args.modelId : undefined;
            resourceInputs["modelToUpload"] = args ? args.modelToUpload : undefined;
            resourceInputs["parentModel"] = args ? args.parentModel : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["trainingTaskDefinition"] = args ? args.trainingTaskDefinition : undefined;
            resourceInputs["trainingTaskInputs"] = args ? args.trainingTaskInputs : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["endTime"] = undefined /*out*/;
            resourceInputs["error"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["startTime"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["trainingTaskMetadata"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["displayName"] = undefined /*out*/;
            resourceInputs["encryptionSpec"] = undefined /*out*/;
            resourceInputs["endTime"] = undefined /*out*/;
            resourceInputs["error"] = undefined /*out*/;
            resourceInputs["inputDataConfig"] = undefined /*out*/;
            resourceInputs["labels"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["modelId"] = undefined /*out*/;
            resourceInputs["modelToUpload"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["parentModel"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["startTime"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["trainingTaskDefinition"] = undefined /*out*/;
            resourceInputs["trainingTaskInputs"] = undefined /*out*/;
            resourceInputs["trainingTaskMetadata"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["location", "project"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(TrainingPipeline.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a TrainingPipeline resource.
 */
export interface TrainingPipelineArgs {
    /**
     * The user-defined name of this TrainingPipeline.
     */
    displayName: pulumi.Input<string>;
    /**
     * Customer-managed encryption key spec for a TrainingPipeline. If set, this TrainingPipeline will be secured by this key. Note: Model trained by this TrainingPipeline is also secured by this key if model_to_upload is not set separately.
     */
    encryptionSpec?: pulumi.Input<inputs.aiplatform.v1.GoogleCloudAiplatformV1EncryptionSpecArgs>;
    /**
     * Specifies Vertex AI owned input data that may be used for training the Model. The TrainingPipeline's training_task_definition should make clear whether this config is used and if there are any special requirements on how it should be filled. If nothing about this config is mentioned in the training_task_definition, then it should be assumed that the TrainingPipeline does not depend on this configuration.
     */
    inputDataConfig?: pulumi.Input<inputs.aiplatform.v1.GoogleCloudAiplatformV1InputDataConfigArgs>;
    /**
     * The labels with user-defined metadata to organize TrainingPipelines. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    location?: pulumi.Input<string>;
    /**
     * Optional. The ID to use for the uploaded Model, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.
     */
    modelId?: pulumi.Input<string>;
    /**
     * Describes the Model that may be uploaded (via ModelService.UploadModel) by this TrainingPipeline. The TrainingPipeline's training_task_definition should make clear whether this Model description should be populated, and if there are any special requirements regarding how it should be filled. If nothing is mentioned in the training_task_definition, then it should be assumed that this field should not be filled and the training task either uploads the Model without a need of this information, or that training task does not support uploading a Model as part of the pipeline. When the Pipeline's state becomes `PIPELINE_STATE_SUCCEEDED` and the trained Model had been uploaded into Vertex AI, then the model_to_upload's resource name is populated. The Model is always uploaded into the Project and Location in which this pipeline is.
     */
    modelToUpload?: pulumi.Input<inputs.aiplatform.v1.GoogleCloudAiplatformV1ModelArgs>;
    /**
     * Optional. When specify this field, the `model_to_upload` will not be uploaded as a new model, instead, it will become a new version of this `parent_model`.
     */
    parentModel?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    /**
     * A Google Cloud Storage path to the YAML file that defines the training task which is responsible for producing the model artifact, and may also include additional auxiliary work. The definition files that can be used here are found in gs://google-cloud-aiplatform/schema/trainingjob/definition/. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.
     */
    trainingTaskDefinition: pulumi.Input<string>;
    /**
     * The training task's parameter(s), as specified in the training_task_definition's `inputs`.
     */
    trainingTaskInputs: any;
}