// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Retrieves information about the specified future reservation.
 */
export function getFutureReservation(args: GetFutureReservationArgs, opts?: pulumi.InvokeOptions): Promise<GetFutureReservationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:compute/alpha:getFutureReservation", {
        "futureReservation": args.futureReservation,
        "project": args.project,
        "zone": args.zone,
    }, opts);
}

export interface GetFutureReservationArgs {
    futureReservation: string;
    project?: string;
    zone: string;
}

export interface GetFutureReservationResult {
    /**
     * Future timestamp when the FR auto-created reservations will be deleted by GCE. Format of this field must be a valid href="https://www.ietf.org/rfc/rfc3339.txt">RFC3339 value.
     */
    readonly autoCreatedReservationsDeleteTime: string;
    /**
     * Specifies the duration of auto-created reservations. It represents relative time to future reservation start_time when auto-created reservations will be automatically deleted by GCE. Duration time unit is represented as a count of seconds and fractions of seconds at nanosecond resolution.
     */
    readonly autoCreatedReservationsDuration: outputs.compute.alpha.DurationResponse;
    /**
     * Setting for enabling or disabling automatic deletion for auto-created reservation. If set to true, auto-created reservations will be deleted at Future Reservation's end time (default) or at user's defined timestamp if any of the [auto_created_reservations_delete_time, auto_created_reservations_duration] values is specified. For keeping auto-created reservation indefinitely, this value should be set to false.
     */
    readonly autoDeleteAutoCreatedReservations: boolean;
    /**
     * The creation timestamp for this future reservation in RFC3339 text format.
     */
    readonly creationTimestamp: string;
    /**
     * An optional description of this resource. Provide this property when you create the future reservation.
     */
    readonly description: string;
    /**
     * Type of the resource. Always compute#futureReservation for future reservations.
     */
    readonly kind: string;
    /**
     * The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
     */
    readonly name: string;
    /**
     * Name prefix for the reservations to be created at the time of delivery. The name prefix must comply with RFC1035. Maximum allowed length for name prefix is 20. Automatically created reservations name format will be -date-####.
     */
    readonly namePrefix: string;
    /**
     * Planning state before being submitted for evaluation
     */
    readonly planningStatus: string;
    /**
     * Server-defined fully-qualified URL for this resource.
     */
    readonly selfLink: string;
    /**
     * Server-defined URL for this resource with the resource id.
     */
    readonly selfLinkWithId: string;
    /**
     * List of Projects/Folders to share with.
     */
    readonly shareSettings: outputs.compute.alpha.ShareSettingsResponse;
    /**
     * Future Reservation configuration to indicate instance properties and total count.
     */
    readonly specificSkuProperties: outputs.compute.alpha.FutureReservationSpecificSKUPropertiesResponse;
    /**
     * [Output only] Status of the Future Reservation
     */
    readonly status: outputs.compute.alpha.FutureReservationStatusResponse;
    /**
     * Time window for this Future Reservation.
     */
    readonly timeWindow: outputs.compute.alpha.FutureReservationTimeWindowResponse;
    /**
     * URL of the Zone where this future reservation resides.
     */
    readonly zone: string;
}
/**
 * Retrieves information about the specified future reservation.
 */
export function getFutureReservationOutput(args: GetFutureReservationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetFutureReservationResult> {
    return pulumi.output(args).apply((a: any) => getFutureReservation(a, opts))
}

export interface GetFutureReservationOutputArgs {
    futureReservation: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    zone: pulumi.Input<string>;
}
