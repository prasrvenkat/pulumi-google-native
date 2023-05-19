// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Gets details of a single ServiceConnectionToken.
 */
export function getServiceConnectionToken(args: GetServiceConnectionTokenArgs, opts?: pulumi.InvokeOptions): Promise<GetServiceConnectionTokenResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:networkconnectivity/v1:getServiceConnectionToken", {
        "location": args.location,
        "project": args.project,
        "serviceConnectionTokenId": args.serviceConnectionTokenId,
    }, opts);
}

export interface GetServiceConnectionTokenArgs {
    location: string;
    project?: string;
    serviceConnectionTokenId: string;
}

export interface GetServiceConnectionTokenResult {
    /**
     * Time when the ServiceConnectionToken was created.
     */
    readonly createTime: string;
    /**
     * A description of this resource.
     */
    readonly description: string;
    /**
     * The time to which this token is valid.
     */
    readonly expireTime: string;
    /**
     * User-defined labels.
     */
    readonly labels: {[key: string]: string};
    /**
     * Immutable. The name of a ServiceConnectionToken. Format: projects/{project}/locations/{location}/ServiceConnectionTokens/{service_connection_token} See: https://google.aip.dev/122#fields-representing-resource-names
     */
    readonly name: string;
    /**
     * The resource path of the network associated with this token. Example: projects/{projectNumOrId}/global/networks/{resourceId}.
     */
    readonly network: string;
    /**
     * The token generated by Automation.
     */
    readonly token: string;
    /**
     * Time when the ServiceConnectionToken was updated.
     */
    readonly updateTime: string;
}
/**
 * Gets details of a single ServiceConnectionToken.
 */
export function getServiceConnectionTokenOutput(args: GetServiceConnectionTokenOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetServiceConnectionTokenResult> {
    return pulumi.output(args).apply((a: any) => getServiceConnectionToken(a, opts))
}

export interface GetServiceConnectionTokenOutputArgs {
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    serviceConnectionTokenId: pulumi.Input<string>;
}