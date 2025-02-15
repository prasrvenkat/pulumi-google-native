// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates an analysis. The long running operation is done when the analysis has completed.
 */
export class Analysis extends pulumi.CustomResource {
    /**
     * Get an existing Analysis resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Analysis {
        return new Analysis(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:contactcenterinsights/v1:Analysis';

    /**
     * Returns true if the given object is an instance of Analysis.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Analysis {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Analysis.__pulumiType;
    }

    /**
     * The result of the analysis, which is populated when the analysis finishes.
     */
    public /*out*/ readonly analysisResult!: pulumi.Output<outputs.contactcenterinsights.v1.GoogleCloudContactcenterinsightsV1AnalysisResultResponse>;
    /**
     * To select the annotators to run and the phrase matchers to use (if any). If not specified, all annotators will be run.
     */
    public readonly annotatorSelector!: pulumi.Output<outputs.contactcenterinsights.v1.GoogleCloudContactcenterinsightsV1AnnotatorSelectorResponse>;
    public readonly conversationId!: pulumi.Output<string>;
    /**
     * The time at which the analysis was created, which occurs when the long-running operation completes.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    public readonly location!: pulumi.Output<string>;
    /**
     * Immutable. The resource name of the analysis. Format: projects/{project}/locations/{location}/conversations/{conversation}/analyses/{analysis}
     */
    public readonly name!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    /**
     * The time at which the analysis was requested.
     */
    public /*out*/ readonly requestTime!: pulumi.Output<string>;

    /**
     * Create a Analysis resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AnalysisArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.conversationId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'conversationId'");
            }
            resourceInputs["annotatorSelector"] = args ? args.annotatorSelector : undefined;
            resourceInputs["conversationId"] = args ? args.conversationId : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["analysisResult"] = undefined /*out*/;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["requestTime"] = undefined /*out*/;
        } else {
            resourceInputs["analysisResult"] = undefined /*out*/;
            resourceInputs["annotatorSelector"] = undefined /*out*/;
            resourceInputs["conversationId"] = undefined /*out*/;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["requestTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["conversationId", "location", "project"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Analysis.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Analysis resource.
 */
export interface AnalysisArgs {
    /**
     * To select the annotators to run and the phrase matchers to use (if any). If not specified, all annotators will be run.
     */
    annotatorSelector?: pulumi.Input<inputs.contactcenterinsights.v1.GoogleCloudContactcenterinsightsV1AnnotatorSelectorArgs>;
    conversationId: pulumi.Input<string>;
    location?: pulumi.Input<string>;
    /**
     * Immutable. The resource name of the analysis. Format: projects/{project}/locations/{location}/conversations/{conversation}/analyses/{analysis}
     */
    name?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
