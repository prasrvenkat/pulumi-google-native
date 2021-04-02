// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../../types";
import * as utilities from "../../utilities";

/**
 * Creates a short Dynamic Link given either a valid long Dynamic Link or details such as Dynamic Link domain, Android and iOS app information. The created short Dynamic Link will not expire. Repeated calls with the same long Dynamic Link or Dynamic Link information will produce the same short Dynamic Link. The Dynamic Link domain in the request must be owned by requester's Firebase project.
 */
export class ShortLink extends pulumi.CustomResource {
    /**
     * Get an existing ShortLink resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ShortLink {
        return new ShortLink(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-cloud:firebasedynamiclinks/v1:ShortLink';

    /**
     * Returns true if the given object is an instance of ShortLink.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ShortLink {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ShortLink.__pulumiType;
    }


    /**
     * Create a ShortLink resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ShortLinkArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["dynamicLinkInfo"] = args ? args.dynamicLinkInfo : undefined;
            inputs["longDynamicLink"] = args ? args.longDynamicLink : undefined;
            inputs["sdkVersion"] = args ? args.sdkVersion : undefined;
            inputs["suffix"] = args ? args.suffix : undefined;
        } else {
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ShortLink.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ShortLink resource.
 */
export interface ShortLinkArgs {
    /**
     * Information about the Dynamic Link to be shortened. [Learn more](https://firebase.google.com/docs/reference/dynamic-links/link-shortener).
     */
    readonly dynamicLinkInfo?: pulumi.Input<inputs.firebasedynamiclinks.v1.DynamicLinkInfo>;
    /**
     * Full long Dynamic Link URL with desired query parameters specified. For example, "https://sample.app.goo.gl/?link=http://www.google.com&apn=com.sample", [Learn more](https://firebase.google.com/docs/reference/dynamic-links/link-shortener).
     */
    readonly longDynamicLink?: pulumi.Input<string>;
    /**
     * Google SDK version. Version takes the form "$major.$minor.$patch"
     */
    readonly sdkVersion?: pulumi.Input<string>;
    /**
     * Short Dynamic Link suffix. Optional.
     */
    readonly suffix?: pulumi.Input<inputs.firebasedynamiclinks.v1.Suffix>;
}