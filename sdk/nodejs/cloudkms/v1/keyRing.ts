// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Create a new KeyRing in a given Project and Location.
 */
export class KeyRing extends pulumi.CustomResource {
    /**
     * Get an existing KeyRing resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): KeyRing {
        return new KeyRing(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-cloud:cloudkms/v1:KeyRing';

    /**
     * Returns true if the given object is an instance of KeyRing.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is KeyRing {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === KeyRing.__pulumiType;
    }

    /**
     * The time at which this KeyRing was created.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * The resource name for the KeyRing in the format `projects/*&#47;locations/*&#47;keyRings/*`.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;

    /**
     * Create a KeyRing resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: KeyRingArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.keyRingsId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'keyRingsId'");
            }
            if ((!args || args.locationsId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'locationsId'");
            }
            if ((!args || args.projectsId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectsId'");
            }
            inputs["keyRingsId"] = args ? args.keyRingsId : undefined;
            inputs["locationsId"] = args ? args.locationsId : undefined;
            inputs["projectsId"] = args ? args.projectsId : undefined;
            inputs["createTime"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
        } else {
            inputs["createTime"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(KeyRing.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a KeyRing resource.
 */
export interface KeyRingArgs {
    readonly keyRingsId: pulumi.Input<string>;
    readonly locationsId: pulumi.Input<string>;
    readonly projectsId: pulumi.Input<string>;
}