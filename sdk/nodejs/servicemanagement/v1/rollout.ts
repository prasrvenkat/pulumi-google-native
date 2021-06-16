// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../../types";
import * as utilities from "../../utilities";

/**
 * Creates a new service configuration rollout. Based on rollout, the Google Service Management will roll out the service configurations to different backend services. For example, the logging configuration will be pushed to Google Cloud Logging. Please note that any previous pending and running Rollouts and associated Operations will be automatically cancelled so that the latest Rollout will not be blocked by previous Rollouts. Only the 100 most recent (in any state) and the last 10 successful (if not already part of the set of 100 most recent) rollouts are kept for each service. The rest will be deleted eventually. Operation
 */
export class Rollout extends pulumi.CustomResource {
    /**
     * Get an existing Rollout resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Rollout {
        return new Rollout(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:servicemanagement/v1:Rollout';

    /**
     * Returns true if the given object is an instance of Rollout.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Rollout {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Rollout.__pulumiType;
    }

    /**
     * Creation time of the rollout. Readonly.
     */
    public readonly createTime!: pulumi.Output<string>;
    /**
     * The strategy associated with a rollout to delete a `ManagedService`. Readonly.
     */
    public readonly deleteServiceStrategy!: pulumi.Output<outputs.servicemanagement.v1.DeleteServiceStrategyResponse>;
    /**
     * Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'
     */
    public readonly rolloutId!: pulumi.Output<string>;
    /**
     * The name of the service associated with this Rollout.
     */
    public readonly serviceName!: pulumi.Output<string>;
    /**
     * The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly.
     */
    public readonly status!: pulumi.Output<string>;
    /**
     * Google Service Control selects service configurations based on traffic percentage.
     */
    public readonly trafficPercentStrategy!: pulumi.Output<outputs.servicemanagement.v1.TrafficPercentStrategyResponse>;

    /**
     * Create a Rollout resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RolloutArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            inputs["createTime"] = args ? args.createTime : undefined;
            inputs["deleteServiceStrategy"] = args ? args.deleteServiceStrategy : undefined;
            inputs["rolloutId"] = args ? args.rolloutId : undefined;
            inputs["serviceName"] = args ? args.serviceName : undefined;
            inputs["status"] = args ? args.status : undefined;
            inputs["trafficPercentStrategy"] = args ? args.trafficPercentStrategy : undefined;
        } else {
            inputs["createTime"] = undefined /*out*/;
            inputs["deleteServiceStrategy"] = undefined /*out*/;
            inputs["rolloutId"] = undefined /*out*/;
            inputs["serviceName"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
            inputs["trafficPercentStrategy"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Rollout.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Rollout resource.
 */
export interface RolloutArgs {
    /**
     * Creation time of the rollout. Readonly.
     */
    createTime?: pulumi.Input<string>;
    /**
     * The strategy associated with a rollout to delete a `ManagedService`. Readonly.
     */
    deleteServiceStrategy?: pulumi.Input<inputs.servicemanagement.v1.DeleteServiceStrategyArgs>;
    /**
     * Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'
     */
    rolloutId?: pulumi.Input<string>;
    /**
     * The name of the service associated with this Rollout.
     */
    serviceName: pulumi.Input<string>;
    /**
     * The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly.
     */
    status?: pulumi.Input<enums.servicemanagement.v1.RolloutStatus>;
    /**
     * Google Service Control selects service configurations based on traffic percentage.
     */
    trafficPercentStrategy?: pulumi.Input<inputs.servicemanagement.v1.TrafficPercentStrategyArgs>;
}