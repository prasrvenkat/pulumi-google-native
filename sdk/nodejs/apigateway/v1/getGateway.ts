// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Gets details of a single Gateway.
 */
export function getGateway(args: GetGatewayArgs, opts?: pulumi.InvokeOptions): Promise<GetGatewayResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:apigateway/v1:getGateway", {
        "gatewayId": args.gatewayId,
        "location": args.location,
        "project": args.project,
    }, opts);
}

export interface GetGatewayArgs {
    gatewayId: string;
    location: string;
    project?: string;
}

export interface GetGatewayResult {
    /**
     * Resource name of the API Config for this Gateway. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig}
     */
    readonly apiConfig: string;
    /**
     * Created time.
     */
    readonly createTime: string;
    /**
     * The default API Gateway host name of the form `{gateway_id}-{hash}.{region_code}.gateway.dev`.
     */
    readonly defaultHostname: string;
    /**
     * Optional. Display name.
     */
    readonly displayName: string;
    /**
     * Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources
     */
    readonly labels: {[key: string]: string};
    /**
     * Resource name of the Gateway. Format: projects/{project}/locations/{location}/gateways/{gateway}
     */
    readonly name: string;
    /**
     * The current state of the Gateway.
     */
    readonly state: string;
    /**
     * Updated time.
     */
    readonly updateTime: string;
}
/**
 * Gets details of a single Gateway.
 */
export function getGatewayOutput(args: GetGatewayOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetGatewayResult> {
    return pulumi.output(args).apply((a: any) => getGateway(a, opts))
}

export interface GetGatewayOutputArgs {
    gatewayId: pulumi.Input<string>;
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
