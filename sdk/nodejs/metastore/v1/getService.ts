// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets the details of a single service.
 */
export function getService(args: GetServiceArgs, opts?: pulumi.InvokeOptions): Promise<GetServiceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:metastore/v1:getService", {
        "location": args.location,
        "project": args.project,
        "serviceId": args.serviceId,
    }, opts);
}

export interface GetServiceArgs {
    location: string;
    project?: string;
    serviceId: string;
}

export interface GetServiceResult {
    /**
     * A Cloud Storage URI (starting with gs://) that specifies where artifacts related to the metastore service are stored.
     */
    readonly artifactGcsUri: string;
    /**
     * The time when the metastore service was created.
     */
    readonly createTime: string;
    /**
     * Immutable. The database type that the Metastore service stores its data.
     */
    readonly databaseType: string;
    /**
     * Immutable. Information used to configure the Dataproc Metastore service to encrypt customer data at rest. Cannot be updated.
     */
    readonly encryptionConfig: outputs.metastore.v1.EncryptionConfigResponse;
    /**
     * The URI of the endpoint used to access the metastore service.
     */
    readonly endpointUri: string;
    /**
     * Configuration information specific to running Hive metastore software as the metastore service.
     */
    readonly hiveMetastoreConfig: outputs.metastore.v1.HiveMetastoreConfigResponse;
    /**
     * User-defined labels for the metastore service.
     */
    readonly labels: {[key: string]: string};
    /**
     * The one hour maintenance window of the metastore service. This specifies when the service can be restarted for maintenance purposes in UTC time. Maintenance window is not needed for services with the SPANNER database type.
     */
    readonly maintenanceWindow: outputs.metastore.v1.MaintenanceWindowResponse;
    /**
     * The metadata management activities of the metastore service.
     */
    readonly metadataManagementActivity: outputs.metastore.v1.MetadataManagementActivityResponse;
    /**
     * Immutable. The relative resource name of the metastore service, in the following format:projects/{project_number}/locations/{location_id}/services/{service_id}.
     */
    readonly name: string;
    /**
     * Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:projects/{project_number}/global/networks/{network_id}.
     */
    readonly network: string;
    /**
     * The configuration specifying the network settings for the Dataproc Metastore service.
     */
    readonly networkConfig: outputs.metastore.v1.NetworkConfigResponse;
    /**
     * The TCP port at which the metastore service is reached. Default: 9083.
     */
    readonly port: number;
    /**
     * Immutable. The release channel of the service. If unspecified, defaults to STABLE.
     */
    readonly releaseChannel: string;
    /**
     * Scaling configuration of the metastore service.
     */
    readonly scalingConfig: outputs.metastore.v1.ScalingConfigResponse;
    /**
     * The current state of the metastore service.
     */
    readonly state: string;
    /**
     * Additional information about the current state of the metastore service, if available.
     */
    readonly stateMessage: string;
    /**
     * The configuration specifying telemetry settings for the Dataproc Metastore service. If unspecified defaults to JSON.
     */
    readonly telemetryConfig: outputs.metastore.v1.TelemetryConfigResponse;
    /**
     * The tier of the service.
     */
    readonly tier: string;
    /**
     * The globally unique resource identifier of the metastore service.
     */
    readonly uid: string;
    /**
     * The time when the metastore service was last updated.
     */
    readonly updateTime: string;
}
/**
 * Gets the details of a single service.
 */
export function getServiceOutput(args: GetServiceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetServiceResult> {
    return pulumi.output(args).apply((a: any) => getService(a, opts))
}

export interface GetServiceOutputArgs {
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    serviceId: pulumi.Input<string>;
}