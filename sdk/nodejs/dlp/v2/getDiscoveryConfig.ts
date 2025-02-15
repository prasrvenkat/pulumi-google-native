// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets a discovery configuration.
 */
export function getDiscoveryConfig(args: GetDiscoveryConfigArgs, opts?: pulumi.InvokeOptions): Promise<GetDiscoveryConfigResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:dlp/v2:getDiscoveryConfig", {
        "discoveryConfigId": args.discoveryConfigId,
        "location": args.location,
        "project": args.project,
    }, opts);
}

export interface GetDiscoveryConfigArgs {
    discoveryConfigId: string;
    location: string;
    project?: string;
}

export interface GetDiscoveryConfigResult {
    /**
     * Actions to execute at the completion of scanning.
     */
    readonly actions: outputs.dlp.v2.GooglePrivacyDlpV2DataProfileActionResponse[];
    /**
     * The creation timestamp of a DiscoveryConfig.
     */
    readonly createTime: string;
    /**
     * Display name (max 100 chars)
     */
    readonly displayName: string;
    /**
     * A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.
     */
    readonly errors: outputs.dlp.v2.GooglePrivacyDlpV2ErrorResponse[];
    /**
     * Detection logic for profile generation. Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery. Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned. For more information, see https://cloud.google.com/dlp/docs/data-profiles#data-residency.
     */
    readonly inspectTemplates: string[];
    /**
     * The timestamp of the last time this config was executed.
     */
    readonly lastRunTime: string;
    /**
     * Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example `projects/dlp-test-project/locations/global/discoveryConfigs/53234423`.
     */
    readonly name: string;
    /**
     * Only set when the parent is an org.
     */
    readonly orgConfig: outputs.dlp.v2.GooglePrivacyDlpV2OrgConfigResponse;
    /**
     * A status for this configuration.
     */
    readonly status: string;
    /**
     * Target to match against for determining what to scan and how frequently.
     */
    readonly targets: outputs.dlp.v2.GooglePrivacyDlpV2DiscoveryTargetResponse[];
    /**
     * The last update timestamp of a DiscoveryConfig.
     */
    readonly updateTime: string;
}
/**
 * Gets a discovery configuration.
 */
export function getDiscoveryConfigOutput(args: GetDiscoveryConfigOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDiscoveryConfigResult> {
    return pulumi.output(args).apply((a: any) => getDiscoveryConfig(a, opts))
}

export interface GetDiscoveryConfigOutputArgs {
    discoveryConfigId: pulumi.Input<string>;
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
