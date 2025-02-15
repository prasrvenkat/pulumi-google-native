// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Returns the specified HttpHealthCheck resource.
 */
export function getHttpHealthCheck(args: GetHttpHealthCheckArgs, opts?: pulumi.InvokeOptions): Promise<GetHttpHealthCheckResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:compute/alpha:getHttpHealthCheck", {
        "httpHealthCheck": args.httpHealthCheck,
        "project": args.project,
    }, opts);
}

export interface GetHttpHealthCheckArgs {
    httpHealthCheck: string;
    project?: string;
}

export interface GetHttpHealthCheckResult {
    /**
     * How often (in seconds) to send a health check. The default value is 5 seconds.
     */
    readonly checkIntervalSec: number;
    /**
     * Creation timestamp in RFC3339 text format.
     */
    readonly creationTimestamp: string;
    /**
     * An optional description of this resource. Provide this property when you create the resource.
     */
    readonly description: string;
    /**
     * A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.
     */
    readonly healthyThreshold: number;
    /**
     * The value of the host header in the HTTP health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used.
     */
    readonly host: string;
    /**
     * Type of the resource. Always compute#httpHealthCheck for HTTP health checks.
     */
    readonly kind: string;
    /**
     * Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
     */
    readonly name: string;
    /**
     * The TCP port number for the HTTP health check request. The default value is 80.
     */
    readonly port: number;
    /**
     * The request path of the HTTP health check request. The default value is /. This field does not support query parameters. Must comply with RFC3986.
     */
    readonly requestPath: string;
    /**
     * Server-defined URL for the resource.
     */
    readonly selfLink: string;
    /**
     * Server-defined URL for this resource with the resource id.
     */
    readonly selfLinkWithId: string;
    /**
     * How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.
     */
    readonly timeoutSec: number;
    /**
     * A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.
     */
    readonly unhealthyThreshold: number;
}
/**
 * Returns the specified HttpHealthCheck resource.
 */
export function getHttpHealthCheckOutput(args: GetHttpHealthCheckOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetHttpHealthCheckResult> {
    return pulumi.output(args).apply((a: any) => getHttpHealthCheck(a, opts))
}

export interface GetHttpHealthCheckOutputArgs {
    httpHealthCheck: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
