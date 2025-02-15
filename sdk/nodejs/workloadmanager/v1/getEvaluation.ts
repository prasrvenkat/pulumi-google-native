// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets details of a single Evaluation.
 */
export function getEvaluation(args: GetEvaluationArgs, opts?: pulumi.InvokeOptions): Promise<GetEvaluationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:workloadmanager/v1:getEvaluation", {
        "evaluationId": args.evaluationId,
        "location": args.location,
        "project": args.project,
    }, opts);
}

export interface GetEvaluationArgs {
    evaluationId: string;
    location: string;
    project?: string;
}

export interface GetEvaluationResult {
    /**
     * [Output only] Create time stamp
     */
    readonly createTime: string;
    /**
     * The Cloud Storage bucket name for custom rules.
     */
    readonly customRulesBucket: string;
    /**
     * Description of the Evaluation
     */
    readonly description: string;
    /**
     * Labels as key value pairs
     */
    readonly labels: {[key: string]: string};
    /**
     * name of resource names have the form 'projects/{project_id}/locations/{location_id}/evaluations/{evaluation_id}'
     */
    readonly name: string;
    /**
     * annotations as key value pairs
     */
    readonly resourceFilter: outputs.workloadmanager.v1.ResourceFilterResponse;
    /**
     * [Output only] The updated rule ids if exist.
     */
    readonly resourceStatus: outputs.workloadmanager.v1.ResourceStatusResponse;
    /**
     * the name of the rule
     */
    readonly ruleNames: string[];
    /**
     * [Output only] The updated rule ids if exist.
     */
    readonly ruleVersions: string[];
    /**
     * crontab format schedule for scheduled evaluation, currently only support the following schedule: "0 *&#47;1 * * *", "0 *&#47;6 * * *", "0 *&#47;12 * * *", "0 0 *&#47;1 * *", "0 0 *&#47;7 * *",
     */
    readonly schedule: string;
    /**
     * [Output only] Update time stamp
     */
    readonly updateTime: string;
}
/**
 * Gets details of a single Evaluation.
 */
export function getEvaluationOutput(args: GetEvaluationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEvaluationResult> {
    return pulumi.output(args).apply((a: any) => getEvaluation(a, opts))
}

export interface GetEvaluationOutputArgs {
    evaluationId: pulumi.Input<string>;
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
