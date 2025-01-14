// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Create an NFS share.
 */
export class NfsShare extends pulumi.CustomResource {
    /**
     * Get an existing NfsShare resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): NfsShare {
        return new NfsShare(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:baremetalsolution/v2:NfsShare';

    /**
     * Returns true if the given object is an instance of NfsShare.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NfsShare {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NfsShare.__pulumiType;
    }

    /**
     * List of allowed access points.
     */
    public readonly allowedClients!: pulumi.Output<outputs.baremetalsolution.v2.AllowedClientResponse[]>;
    /**
     * Labels as key value pairs.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string}>;
    public readonly location!: pulumi.Output<string>;
    /**
     * Immutable. The name of the NFS share.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * An identifier for the NFS share, generated by the backend. This field will be deprecated in the future, use `id` instead.
     */
    public /*out*/ readonly nfsShareId!: pulumi.Output<string>;
    /**
     * Immutable. Pod name. Pod is an independent part of infrastructure. NFSShare can only be connected to the assets (networks, instances) allocated in the same pod.
     */
    public readonly pod!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    /**
     * The requested size, in GiB.
     */
    public readonly requestedSizeGib!: pulumi.Output<string>;
    /**
     * The state of the NFS share.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * Immutable. The storage type of the underlying volume.
     */
    public readonly storageType!: pulumi.Output<string>;
    /**
     * The underlying volume of the share. Created automatically during provisioning.
     */
    public /*out*/ readonly volume!: pulumi.Output<string>;

    /**
     * Create a NfsShare resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: NfsShareArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["allowedClients"] = args ? args.allowedClients : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["pod"] = args ? args.pod : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["requestedSizeGib"] = args ? args.requestedSizeGib : undefined;
            resourceInputs["storageType"] = args ? args.storageType : undefined;
            resourceInputs["nfsShareId"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["volume"] = undefined /*out*/;
        } else {
            resourceInputs["allowedClients"] = undefined /*out*/;
            resourceInputs["labels"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["nfsShareId"] = undefined /*out*/;
            resourceInputs["pod"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["requestedSizeGib"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["storageType"] = undefined /*out*/;
            resourceInputs["volume"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["location", "project"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(NfsShare.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a NfsShare resource.
 */
export interface NfsShareArgs {
    /**
     * List of allowed access points.
     */
    allowedClients?: pulumi.Input<pulumi.Input<inputs.baremetalsolution.v2.AllowedClientArgs>[]>;
    /**
     * Labels as key value pairs.
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    location?: pulumi.Input<string>;
    /**
     * Immutable. The name of the NFS share.
     */
    name?: pulumi.Input<string>;
    /**
     * Immutable. Pod name. Pod is an independent part of infrastructure. NFSShare can only be connected to the assets (networks, instances) allocated in the same pod.
     */
    pod?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    /**
     * The requested size, in GiB.
     */
    requestedSizeGib?: pulumi.Input<string>;
    /**
     * Immutable. The storage type of the underlying volume.
     */
    storageType?: pulumi.Input<enums.baremetalsolution.v2.NfsShareStorageType>;
}
