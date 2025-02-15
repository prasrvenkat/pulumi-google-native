// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets an analysis.
 */
export function getAnalysis(args: GetAnalysisArgs, opts?: pulumi.InvokeOptions): Promise<GetAnalysisResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:contactcenterinsights/v1:getAnalysis", {
        "analysisId": args.analysisId,
        "conversationId": args.conversationId,
        "location": args.location,
        "project": args.project,
    }, opts);
}

export interface GetAnalysisArgs {
    analysisId: string;
    conversationId: string;
    location: string;
    project?: string;
}

export interface GetAnalysisResult {
    /**
     * The result of the analysis, which is populated when the analysis finishes.
     */
    readonly analysisResult: outputs.contactcenterinsights.v1.GoogleCloudContactcenterinsightsV1AnalysisResultResponse;
    /**
     * To select the annotators to run and the phrase matchers to use (if any). If not specified, all annotators will be run.
     */
    readonly annotatorSelector: outputs.contactcenterinsights.v1.GoogleCloudContactcenterinsightsV1AnnotatorSelectorResponse;
    /**
     * The time at which the analysis was created, which occurs when the long-running operation completes.
     */
    readonly createTime: string;
    /**
     * Immutable. The resource name of the analysis. Format: projects/{project}/locations/{location}/conversations/{conversation}/analyses/{analysis}
     */
    readonly name: string;
    /**
     * The time at which the analysis was requested.
     */
    readonly requestTime: string;
}
/**
 * Gets an analysis.
 */
export function getAnalysisOutput(args: GetAnalysisOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAnalysisResult> {
    return pulumi.output(args).apply((a: any) => getAnalysis(a, opts))
}

export interface GetAnalysisOutputArgs {
    analysisId: pulumi.Input<string>;
    conversationId: pulumi.Input<string>;
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
