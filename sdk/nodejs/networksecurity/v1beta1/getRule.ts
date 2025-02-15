// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Gets details of a single GatewaySecurityPolicyRule.
 */
export function getRule(args: GetRuleArgs, opts?: pulumi.InvokeOptions): Promise<GetRuleResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:networksecurity/v1beta1:getRule", {
        "gatewaySecurityPolicyId": args.gatewaySecurityPolicyId,
        "location": args.location,
        "project": args.project,
        "ruleId": args.ruleId,
    }, opts);
}

export interface GetRuleArgs {
    gatewaySecurityPolicyId: string;
    location: string;
    project?: string;
    ruleId: string;
}

export interface GetRuleResult {
    /**
     * Optional. CEL expression for matching on L7/application level criteria.
     */
    readonly applicationMatcher: string;
    /**
     * Profile which tells what the primitive action should be.
     */
    readonly basicProfile: string;
    /**
     * Time when the rule was created.
     */
    readonly createTime: string;
    /**
     * Optional. Free-text description of the resource.
     */
    readonly description: string;
    /**
     * Whether the rule is enforced.
     */
    readonly enabled: boolean;
    /**
     * Immutable. Name of the resource. ame is the full resource name so projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy}/rules/{rule} rule should match the pattern: (^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$).
     */
    readonly name: string;
    /**
     * Priority of the rule. Lower number corresponds to higher precedence.
     */
    readonly priority: number;
    /**
     * CEL expression for matching on session criteria.
     */
    readonly sessionMatcher: string;
    /**
     * Optional. Flag to enable TLS inspection of traffic matching on , can only be true if the parent GatewaySecurityPolicy references a TLSInspectionConfig.
     */
    readonly tlsInspectionEnabled: boolean;
    /**
     * Time when the rule was updated.
     */
    readonly updateTime: string;
}
/**
 * Gets details of a single GatewaySecurityPolicyRule.
 */
export function getRuleOutput(args: GetRuleOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetRuleResult> {
    return pulumi.output(args).apply((a: any) => getRule(a, opts))
}

export interface GetRuleOutputArgs {
    gatewaySecurityPolicyId: pulumi.Input<string>;
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    ruleId: pulumi.Input<string>;
}
