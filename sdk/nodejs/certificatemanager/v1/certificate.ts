// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../../types";
import * as utilities from "../../utilities";

/**
 * Creates a new Certificate in a given project and location.
 */
export class Certificate extends pulumi.CustomResource {
    /**
     * Get an existing Certificate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Certificate {
        return new Certificate(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:certificatemanager/v1:Certificate';

    /**
     * Returns true if the given object is an instance of Certificate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Certificate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Certificate.__pulumiType;
    }

    /**
     * The creation timestamp of a Certificate.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * One or more paragraphs of text description of a certificate.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The expiry timestamp of a Certificate.
     */
    public /*out*/ readonly expireTime!: pulumi.Output<string>;
    /**
     * Set of labels associated with a Certificate.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string}>;
    /**
     * If set, contains configuration and state of a managed certificate.
     */
    public readonly managed!: pulumi.Output<outputs.certificatemanager.v1.ManagedCertificateResponse>;
    /**
     * A user-defined name of the certificate. Certificate names must be unique globally and match pattern `projects/*&#47;locations/*&#47;certificates/*`.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The PEM-encoded certificate chain.
     */
    public /*out*/ readonly pemCertificate!: pulumi.Output<string>;
    /**
     * The list of Subject Alternative Names of dnsName type defined in the certificate (see RFC 5280 4.2.1.6)
     */
    public /*out*/ readonly sanDnsnames!: pulumi.Output<string[]>;
    /**
     * Immutable. The scope of the certificate.
     */
    public readonly scope!: pulumi.Output<string>;
    /**
     * If set, defines data of a self-managed certificate.
     */
    public readonly selfManaged!: pulumi.Output<outputs.certificatemanager.v1.SelfManagedCertificateResponse>;
    /**
     * The last update timestamp of a Certificate.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a Certificate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CertificateArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.certificateId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'certificateId'");
            }
            resourceInputs["certificateId"] = args ? args.certificateId : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["managed"] = args ? args.managed : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["scope"] = args ? args.scope : undefined;
            resourceInputs["selfManaged"] = args ? args.selfManaged : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["expireTime"] = undefined /*out*/;
            resourceInputs["pemCertificate"] = undefined /*out*/;
            resourceInputs["sanDnsnames"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["expireTime"] = undefined /*out*/;
            resourceInputs["labels"] = undefined /*out*/;
            resourceInputs["managed"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["pemCertificate"] = undefined /*out*/;
            resourceInputs["sanDnsnames"] = undefined /*out*/;
            resourceInputs["scope"] = undefined /*out*/;
            resourceInputs["selfManaged"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Certificate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Certificate resource.
 */
export interface CertificateArgs {
    certificateId: pulumi.Input<string>;
    /**
     * One or more paragraphs of text description of a certificate.
     */
    description?: pulumi.Input<string>;
    /**
     * Set of labels associated with a Certificate.
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    location?: pulumi.Input<string>;
    /**
     * If set, contains configuration and state of a managed certificate.
     */
    managed?: pulumi.Input<inputs.certificatemanager.v1.ManagedCertificateArgs>;
    /**
     * A user-defined name of the certificate. Certificate names must be unique globally and match pattern `projects/*&#47;locations/*&#47;certificates/*`.
     */
    name?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    /**
     * Immutable. The scope of the certificate.
     */
    scope?: pulumi.Input<enums.certificatemanager.v1.CertificateScope>;
    /**
     * If set, defines data of a self-managed certificate.
     */
    selfManaged?: pulumi.Input<inputs.certificatemanager.v1.SelfManagedCertificateArgs>;
}