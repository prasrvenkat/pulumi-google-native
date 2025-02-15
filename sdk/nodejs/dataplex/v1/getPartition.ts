// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Get a metadata partition of an entity.
 */
export function getPartition(args: GetPartitionArgs, opts?: pulumi.InvokeOptions): Promise<GetPartitionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:dataplex/v1:getPartition", {
        "entityId": args.entityId,
        "lakeId": args.lakeId,
        "location": args.location,
        "partitionId": args.partitionId,
        "project": args.project,
        "zone": args.zone,
    }, opts);
}

export interface GetPartitionArgs {
    entityId: string;
    lakeId: string;
    location: string;
    partitionId: string;
    project?: string;
    zone: string;
}

export interface GetPartitionResult {
    /**
     * Optional. The etag for this partition.
     */
    readonly etag: string;
    /**
     * Immutable. The location of the entity data within the partition, for example, gs://bucket/path/to/entity/key1=value1/key2=value2. Or projects//datasets//tables/
     */
    readonly location: string;
    /**
     * Partition values used in the HTTP URL must be double encoded. For example, url_encode(url_encode(value)) can be used to encode "US:CA/CA#Sunnyvale so that the request URL ends with "/partitions/US%253ACA/CA%2523Sunnyvale". The name field in the response retains the encoded format.
     */
    readonly name: string;
    /**
     * Immutable. The set of values representing the partition, which correspond to the partition schema defined in the parent entity.
     */
    readonly values: string[];
}
/**
 * Get a metadata partition of an entity.
 */
export function getPartitionOutput(args: GetPartitionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPartitionResult> {
    return pulumi.output(args).apply((a: any) => getPartition(a, opts))
}

export interface GetPartitionOutputArgs {
    entityId: pulumi.Input<string>;
    lakeId: pulumi.Input<string>;
    location: pulumi.Input<string>;
    partitionId: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    zone: pulumi.Input<string>;
}
