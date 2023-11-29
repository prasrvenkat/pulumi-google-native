// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets the details of a specific Redis cluster.
 */
export function getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:redis/v1beta1:getCluster", {
        "clusterId": args.clusterId,
        "location": args.location,
        "project": args.project,
    }, opts);
}

export interface GetClusterArgs {
    clusterId: string;
    location: string;
    project?: string;
}

export interface GetClusterResult {
    /**
     * Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster.
     */
    readonly authorizationMode: string;
    /**
     * The timestamp associated with the cluster creation request.
     */
    readonly createTime: string;
    /**
     * Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported.
     */
    readonly discoveryEndpoints: outputs.redis.v1beta1.DiscoveryEndpointResponse[];
    /**
     * Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}`
     */
    readonly name: string;
    /**
     * Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.
     */
    readonly pscConfigs: outputs.redis.v1beta1.PscConfigResponse[];
    /**
     * PSC connections for discovery of the cluster topology and accessing the cluster.
     */
    readonly pscConnections: outputs.redis.v1beta1.PscConnectionResponse[];
    /**
     * Optional. The number of replica nodes per shard.
     */
    readonly replicaCount: number;
    /**
     * Number of shards for the Redis cluster.
     */
    readonly shardCount: number;
    /**
     * Redis memory size in GB for the entire cluster.
     */
    readonly sizeGb: number;
    /**
     * The current state of this cluster. Can be CREATING, READY, UPDATING, DELETING and SUSPENDED
     */
    readonly state: string;
    /**
     * Additional information about the current state of the cluster.
     */
    readonly stateInfo: outputs.redis.v1beta1.StateInfoResponse;
    /**
     * Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster.
     */
    readonly transitEncryptionMode: string;
    /**
     * System assigned, unique identifier for the cluster.
     */
    readonly uid: string;
}
/**
 * Gets the details of a specific Redis cluster.
 */
export function getClusterOutput(args: GetClusterOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetClusterResult> {
    return pulumi.output(args).apply((a: any) => getCluster(a, opts))
}

export interface GetClusterOutputArgs {
    clusterId: pulumi.Input<string>;
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}