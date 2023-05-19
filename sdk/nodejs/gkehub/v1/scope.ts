// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a Scope.
 * Auto-naming is currently not supported for this resource.
 */
export class Scope extends pulumi.CustomResource {
    /**
     * Get an existing Scope resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Scope {
        return new Scope(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:gkehub/v1:Scope';

    /**
     * Returns true if the given object is an instance of Scope.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Scope {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Scope.__pulumiType;
    }

    /**
     * If true, all Memberships in the Fleet bind to this Scope.
     */
    public readonly allMemberships!: pulumi.Output<boolean>;
    /**
     * When the scope was created.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * When the scope was deleted.
     */
    public /*out*/ readonly deleteTime!: pulumi.Output<string>;
    public readonly location!: pulumi.Output<string>;
    /**
     * The resource name for the scope `projects/{project}/locations/{location}/scopes/{scope}`
     */
    public readonly name!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    /**
     * Required. Client chosen ID for the Scope. `scope_id` must be a ????
     */
    public readonly scopeId!: pulumi.Output<string>;
    /**
     * State of the scope resource.
     */
    public /*out*/ readonly state!: pulumi.Output<outputs.gkehub.v1.ScopeLifecycleStateResponse>;
    /**
     * Google-generated UUID for this resource. This is unique across all scope resources. If a scope resource is deleted and another resource with the same name is created, it gets a different uid.
     */
    public /*out*/ readonly uid!: pulumi.Output<string>;
    /**
     * When the scope was last updated.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a Scope resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ScopeArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.scopeId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'scopeId'");
            }
            resourceInputs["allMemberships"] = args ? args.allMemberships : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["scopeId"] = args ? args.scopeId : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["deleteTime"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["uid"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["allMemberships"] = undefined /*out*/;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["deleteTime"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["scopeId"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["uid"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["location", "project", "scopeId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Scope.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Scope resource.
 */
export interface ScopeArgs {
    /**
     * If true, all Memberships in the Fleet bind to this Scope.
     */
    allMemberships?: pulumi.Input<boolean>;
    location?: pulumi.Input<string>;
    /**
     * The resource name for the scope `projects/{project}/locations/{location}/scopes/{scope}`
     */
    name?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    /**
     * Required. Client chosen ID for the Scope. `scope_id` must be a ????
     */
    scopeId: pulumi.Input<string>;
}