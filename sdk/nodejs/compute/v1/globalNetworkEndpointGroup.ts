// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../../types";
import * as utilities from "../../utilities";

/**
 * Creates a network endpoint group in the specified project using the parameters that are included in the request.
 */
export class GlobalNetworkEndpointGroup extends pulumi.CustomResource {
    /**
     * Get an existing GlobalNetworkEndpointGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): GlobalNetworkEndpointGroup {
        return new GlobalNetworkEndpointGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-cloud:compute/v1:GlobalNetworkEndpointGroup';

    /**
     * Returns true if the given object is an instance of GlobalNetworkEndpointGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GlobalNetworkEndpointGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GlobalNetworkEndpointGroup.__pulumiType;
    }

    /**
     * Metadata defined as annotations on the network endpoint group.
     */
    public readonly annotations!: pulumi.Output<{[key: string]: string}>;
    /**
     * Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
     */
    public readonly appEngine!: pulumi.Output<outputs.compute.v1.NetworkEndpointGroupAppEngineResponse>;
    /**
     * Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
     */
    public readonly cloudFunction!: pulumi.Output<outputs.compute.v1.NetworkEndpointGroupCloudFunctionResponse>;
    /**
     * Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
     */
    public readonly cloudRun!: pulumi.Output<outputs.compute.v1.NetworkEndpointGroupCloudRunResponse>;
    /**
     * [Output Only] Creation timestamp in RFC3339 text format.
     */
    public readonly creationTimestamp!: pulumi.Output<string>;
    /**
     * The default port used if the port number is not specified in the network endpoint.
     */
    public readonly defaultPort!: pulumi.Output<number>;
    /**
     * An optional description of this resource. Provide this property when you create the resource.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * [Output Only] Type of the resource. Always compute#networkEndpointGroup for network endpoint group.
     */
    public readonly kind!: pulumi.Output<string>;
    /**
     * Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The URL of the network to which all network endpoints in the NEG belong. Uses "default" project network if unspecified.
     */
    public readonly network!: pulumi.Output<string>;
    /**
     * Type of network endpoints in this network endpoint group. Can be one of GCE_VM_IP_PORT, NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT, INTERNET_IP_PORT, or SERVERLESS.
     */
    public readonly networkEndpointType!: pulumi.Output<string>;
    /**
     * [Output Only] The URL of the region where the network endpoint group is located.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * [Output Only] Server-defined URL for the resource.
     */
    public readonly selfLink!: pulumi.Output<string>;
    /**
     * [Output only] Number of network endpoints in the network endpoint group.
     */
    public readonly size!: pulumi.Output<number>;
    /**
     * Optional URL of the subnetwork to which all network endpoints in the NEG belong.
     */
    public readonly subnetwork!: pulumi.Output<string>;
    /**
     * [Output Only] The URL of the zone where the network endpoint group is located.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a GlobalNetworkEndpointGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GlobalNetworkEndpointGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.networkEndpointGroup === undefined) && !opts.urn) {
                throw new Error("Missing required property 'networkEndpointGroup'");
            }
            if ((!args || args.project === undefined) && !opts.urn) {
                throw new Error("Missing required property 'project'");
            }
            inputs["annotations"] = args ? args.annotations : undefined;
            inputs["appEngine"] = args ? args.appEngine : undefined;
            inputs["cloudFunction"] = args ? args.cloudFunction : undefined;
            inputs["cloudRun"] = args ? args.cloudRun : undefined;
            inputs["creationTimestamp"] = args ? args.creationTimestamp : undefined;
            inputs["defaultPort"] = args ? args.defaultPort : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["id"] = args ? args.id : undefined;
            inputs["kind"] = args ? args.kind : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["network"] = args ? args.network : undefined;
            inputs["networkEndpointGroup"] = args ? args.networkEndpointGroup : undefined;
            inputs["networkEndpointType"] = args ? args.networkEndpointType : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["selfLink"] = args ? args.selfLink : undefined;
            inputs["size"] = args ? args.size : undefined;
            inputs["subnetwork"] = args ? args.subnetwork : undefined;
            inputs["zone"] = args ? args.zone : undefined;
        } else {
            inputs["annotations"] = undefined /*out*/;
            inputs["appEngine"] = undefined /*out*/;
            inputs["cloudFunction"] = undefined /*out*/;
            inputs["cloudRun"] = undefined /*out*/;
            inputs["creationTimestamp"] = undefined /*out*/;
            inputs["defaultPort"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["kind"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["network"] = undefined /*out*/;
            inputs["networkEndpointType"] = undefined /*out*/;
            inputs["region"] = undefined /*out*/;
            inputs["selfLink"] = undefined /*out*/;
            inputs["size"] = undefined /*out*/;
            inputs["subnetwork"] = undefined /*out*/;
            inputs["zone"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(GlobalNetworkEndpointGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a GlobalNetworkEndpointGroup resource.
 */
export interface GlobalNetworkEndpointGroupArgs {
    /**
     * Metadata defined as annotations on the network endpoint group.
     */
    readonly annotations?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
     */
    readonly appEngine?: pulumi.Input<inputs.compute.v1.NetworkEndpointGroupAppEngine>;
    /**
     * Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
     */
    readonly cloudFunction?: pulumi.Input<inputs.compute.v1.NetworkEndpointGroupCloudFunction>;
    /**
     * Only valid when networkEndpointType is "SERVERLESS". Only one of cloudRun, appEngine or cloudFunction may be set.
     */
    readonly cloudRun?: pulumi.Input<inputs.compute.v1.NetworkEndpointGroupCloudRun>;
    /**
     * [Output Only] Creation timestamp in RFC3339 text format.
     */
    readonly creationTimestamp?: pulumi.Input<string>;
    /**
     * The default port used if the port number is not specified in the network endpoint.
     */
    readonly defaultPort?: pulumi.Input<number>;
    /**
     * An optional description of this resource. Provide this property when you create the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * [Output Only] The unique identifier for the resource. This identifier is defined by the server.
     */
    readonly id?: pulumi.Input<string>;
    /**
     * [Output Only] Type of the resource. Always compute#networkEndpointGroup for network endpoint group.
     */
    readonly kind?: pulumi.Input<string>;
    /**
     * Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The URL of the network to which all network endpoints in the NEG belong. Uses "default" project network if unspecified.
     */
    readonly network?: pulumi.Input<string>;
    readonly networkEndpointGroup: pulumi.Input<string>;
    /**
     * Type of network endpoints in this network endpoint group. Can be one of GCE_VM_IP_PORT, NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT, INTERNET_IP_PORT, or SERVERLESS.
     */
    readonly networkEndpointType?: pulumi.Input<string>;
    readonly project: pulumi.Input<string>;
    /**
     * [Output Only] The URL of the region where the network endpoint group is located.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * [Output Only] Server-defined URL for the resource.
     */
    readonly selfLink?: pulumi.Input<string>;
    /**
     * [Output only] Number of network endpoints in the network endpoint group.
     */
    readonly size?: pulumi.Input<number>;
    /**
     * Optional URL of the subnetwork to which all network endpoints in the NEG belong.
     */
    readonly subnetwork?: pulumi.Input<string>;
    /**
     * [Output Only] The URL of the zone where the network endpoint group is located.
     */
    readonly zone?: pulumi.Input<string>;
}