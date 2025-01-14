// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Creates a new `ExternalAddress` resource in a given private cloud. The network policy that corresponds to the private cloud must have the external IP address network service enabled (`NetworkPolicy.external_ip`).
 * Auto-naming is currently not supported for this resource.
 */
export class ExternalAddress extends pulumi.CustomResource {
    /**
     * Get an existing ExternalAddress resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ExternalAddress {
        return new ExternalAddress(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:vmwareengine/v1:ExternalAddress';

    /**
     * Returns true if the given object is an instance of ExternalAddress.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ExternalAddress {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ExternalAddress.__pulumiType;
    }

    /**
     * Creation time of this resource.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * User-provided description for this resource.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * Required. The user-provided identifier of the `ExternalAddress` to be created. This identifier must be unique among `ExternalAddress` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
     */
    public readonly externalAddressId!: pulumi.Output<string>;
    /**
     * The external IP address of a workload VM.
     */
    public /*out*/ readonly externalIp!: pulumi.Output<string>;
    /**
     * The internal IP address of a workload VM.
     */
    public readonly internalIp!: pulumi.Output<string>;
    public readonly location!: pulumi.Output<string>;
    /**
     * The resource name of this external IP address. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-address`
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    public readonly privateCloudId!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    /**
     * Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
     */
    public readonly requestId!: pulumi.Output<string | undefined>;
    /**
     * The state of the resource.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * System-generated unique identifier for the resource.
     */
    public /*out*/ readonly uid!: pulumi.Output<string>;
    /**
     * Last update time of this resource.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a ExternalAddress resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ExternalAddressArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.externalAddressId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'externalAddressId'");
            }
            if ((!args || args.privateCloudId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'privateCloudId'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["externalAddressId"] = args ? args.externalAddressId : undefined;
            resourceInputs["internalIp"] = args ? args.internalIp : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["privateCloudId"] = args ? args.privateCloudId : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["requestId"] = args ? args.requestId : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["externalIp"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["uid"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["externalAddressId"] = undefined /*out*/;
            resourceInputs["externalIp"] = undefined /*out*/;
            resourceInputs["internalIp"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["privateCloudId"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["requestId"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["uid"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["externalAddressId", "location", "privateCloudId", "project"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ExternalAddress.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ExternalAddress resource.
 */
export interface ExternalAddressArgs {
    /**
     * User-provided description for this resource.
     */
    description?: pulumi.Input<string>;
    /**
     * Required. The user-provided identifier of the `ExternalAddress` to be created. This identifier must be unique among `ExternalAddress` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
     */
    externalAddressId: pulumi.Input<string>;
    /**
     * The internal IP address of a workload VM.
     */
    internalIp?: pulumi.Input<string>;
    location?: pulumi.Input<string>;
    privateCloudId: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    /**
     * Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
     */
    requestId?: pulumi.Input<string>;
}
