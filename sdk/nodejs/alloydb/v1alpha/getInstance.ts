// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets details of a single Instance.
 */
export function getInstance(args: GetInstanceArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:alloydb/v1alpha:getInstance", {
        "clusterId": args.clusterId,
        "instanceId": args.instanceId,
        "location": args.location,
        "project": args.project,
        "view": args.view,
    }, opts);
}

export interface GetInstanceArgs {
    clusterId: string;
    instanceId: string;
    location: string;
    project?: string;
    view?: string;
}

export interface GetInstanceResult {
    /**
     * Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128
     */
    readonly annotations: {[key: string]: string};
    /**
     * Availability type of an Instance. If empty, defaults to REGIONAL for primary instances. For read pools, availability_type is always UNSPECIFIED. Instances in the read pools are evenly distributed across available zones within the region (i.e. read pools with more than one node will have a node in at least two zones).
     */
    readonly availabilityType: string;
    /**
     * Optional. Client connection specific configurations
     */
    readonly clientConnectionConfig: outputs.alloydb.v1alpha.ClientConnectionConfigResponse;
    /**
     * Create time stamp
     */
    readonly createTime: string;
    /**
     * Database flags. Set at instance level. * They are copied from primary instance on read instance creation. * Read instances can set new or override existing flags that are relevant for reads, e.g. for enabling columnar cache on a read instance. Flags set on read instance may or may not be present on primary. This is a list of "key": "value" pairs. "key": The name of the flag. These flags are passed at instance setup time, so include both server options and system variables for Postgres. Flags are specified with underscores, not hyphens. "value": The value of the flag. Booleans are set to **on** for true and **off** for false. This field must be omitted if the flag doesn't take a value.
     */
    readonly databaseFlags: {[key: string]: string};
    /**
     * Delete time stamp
     */
    readonly deleteTime: string;
    /**
     * User-settable and human-readable display name for the Instance.
     */
    readonly displayName: string;
    /**
     * For Resource freshness validation (https://google.aip.dev/154)
     */
    readonly etag: string;
    /**
     * The Compute Engine zone that the instance should serve from, per https://cloud.google.com/compute/docs/regions-zones This can ONLY be specified for ZONAL instances. If present for a REGIONAL instance, an error will be thrown. If this is absent for a ZONAL instance, instance is created in a random zone with available capacity.
     */
    readonly gceZone: string;
    /**
     * The type of the instance. Specified at creation time.
     */
    readonly instanceType: string;
    /**
     * The IP address for the Instance. This is the connection endpoint for an end-user application.
     */
    readonly ipAddress: string;
    /**
     * Labels as key value pairs
     */
    readonly labels: {[key: string]: string};
    /**
     * Configurations for the machines that host the underlying database engine.
     */
    readonly machineConfig: outputs.alloydb.v1alpha.MachineConfigResponse;
    /**
     * The name of the instance resource with the format: * projects/{project}/locations/{region}/clusters/{cluster_id}/instances/{instance_id} where the cluster and instance ID segments should satisfy the regex expression `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`, e.g. 1-63 characters of lowercase letters, numbers, and dashes, starting with a letter, and ending with a letter or number. For more details see https://google.aip.dev/122. The prefix of the instance resource name is the name of the parent resource: * projects/{project}/locations/{region}/clusters/{cluster_id}
     */
    readonly name: string;
    /**
     * List of available read-only VMs in this instance, including the standby for a PRIMARY instance.
     */
    readonly nodes: outputs.alloydb.v1alpha.NodeResponse[];
    /**
     * Configuration for query insights.
     */
    readonly queryInsightsConfig: outputs.alloydb.v1alpha.QueryInsightsInstanceConfigResponse;
    /**
     * Read pool instance configuration. This is required if the value of instanceType is READ_POOL.
     */
    readonly readPoolConfig: outputs.alloydb.v1alpha.ReadPoolConfigResponse;
    /**
     * Reconciling (https://google.aip.dev/128#reconciliation). Set to true if the current state of Instance does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance.
     */
    readonly reconciling: boolean;
    /**
     * Reserved for future use.
     */
    readonly satisfiesPzs: boolean;
    /**
     * The current serving state of the instance.
     */
    readonly state: string;
    /**
     * The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted.
     */
    readonly uid: string;
    /**
     * Update policy that will be applied during instance update. This field is not persisted when you update the instance. To use a non-default update policy, you must specify explicitly specify the value in each update request.
     */
    readonly updatePolicy: outputs.alloydb.v1alpha.UpdatePolicyResponse;
    /**
     * Update time stamp
     */
    readonly updateTime: string;
    /**
     * This is set for the read-write VM of the PRIMARY instance only.
     */
    readonly writableNode: outputs.alloydb.v1alpha.NodeResponse;
}
/**
 * Gets details of a single Instance.
 */
export function getInstanceOutput(args: GetInstanceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInstanceResult> {
    return pulumi.output(args).apply((a: any) => getInstance(a, opts))
}

export interface GetInstanceOutputArgs {
    clusterId: pulumi.Input<string>;
    instanceId: pulumi.Input<string>;
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    view?: pulumi.Input<string>;
}
