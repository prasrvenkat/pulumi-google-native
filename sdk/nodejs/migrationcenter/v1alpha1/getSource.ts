// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Gets the details of a source.
 */
export function getSource(args: GetSourceArgs, opts?: pulumi.InvokeOptions): Promise<GetSourceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:migrationcenter/v1alpha1:getSource", {
        "location": args.location,
        "project": args.project,
        "sourceId": args.sourceId,
    }, opts);
}

export interface GetSourceArgs {
    location: string;
    project?: string;
    sourceId: string;
}

export interface GetSourceResult {
    /**
     * The timestamp when the source was created.
     */
    readonly createTime: string;
    /**
     * Free-text description.
     */
    readonly description: string;
    /**
     * User-friendly display name.
     */
    readonly displayName: string;
    /**
     * The number of frames that were reported by the source and contained errors.
     */
    readonly errorFrameCount: number;
    /**
     * If `true`, the source is managed by other service(s).
     */
    readonly isManaged: boolean;
    /**
     * The full name of the source.
     */
    readonly name: string;
    /**
     * Number of frames that are still being processed.
     */
    readonly pendingFrameCount: number;
    /**
     * The information confidence of the source. The higher the value, the higher the confidence.
     */
    readonly priority: number;
    /**
     * The state of the source.
     */
    readonly state: string;
    /**
     * Data source type.
     */
    readonly type: string;
    /**
     * The timestamp when the source was last updated.
     */
    readonly updateTime: string;
}
/**
 * Gets the details of a source.
 */
export function getSourceOutput(args: GetSourceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSourceResult> {
    return pulumi.output(args).apply((a: any) => getSource(a, opts))
}

export interface GetSourceOutputArgs {
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    sourceId: pulumi.Input<string>;
}
