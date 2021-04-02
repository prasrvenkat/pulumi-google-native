// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../../types";
import * as utilities from "../../utilities";

/**
 * Creates a new `Note`.
 */
export class ProviderNote extends pulumi.CustomResource {
    /**
     * Get an existing ProviderNote resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ProviderNote {
        return new ProviderNote(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-cloud:containeranalysis/v1alpha1:ProviderNote';

    /**
     * Returns true if the given object is an instance of ProviderNote.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ProviderNote {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ProviderNote.__pulumiType;
    }

    /**
     * A note describing an attestation role.
     */
    public readonly attestationAuthority!: pulumi.Output<outputs.containeranalysis.v1alpha1.AttestationAuthorityResponse>;
    /**
     * A note describing a base image.
     */
    public readonly baseImage!: pulumi.Output<outputs.containeranalysis.v1alpha1.BasisResponse>;
    /**
     * Build provenance type for a verifiable build.
     */
    public readonly buildType!: pulumi.Output<outputs.containeranalysis.v1alpha1.BuildTypeResponse>;
    /**
     * The time this note was created. This field can be used as a filter in list requests.
     */
    public readonly createTime!: pulumi.Output<string>;
    /**
     * A note describing something that can be deployed.
     */
    public readonly deployable!: pulumi.Output<outputs.containeranalysis.v1alpha1.DeployableResponse>;
    /**
     * A note describing a provider/analysis type.
     */
    public readonly discovery!: pulumi.Output<outputs.containeranalysis.v1alpha1.DiscoveryResponse>;
    /**
     * Time of expiration for this note, null if note does not expire.
     */
    public readonly expirationTime!: pulumi.Output<string>;
    /**
     * This explicitly denotes which kind of note is specified. This field can be used as a filter in list requests.
     */
    public readonly kind!: pulumi.Output<string>;
    /**
     * A detailed description of this `Note`.
     */
    public readonly longDescription!: pulumi.Output<string>;
    /**
     * The name of the note in the form "projects/{provider_project_id}/notes/{NOTE_ID}"
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A note describing a package hosted by various package managers.
     */
    public readonly package!: pulumi.Output<outputs.containeranalysis.v1alpha1.PackageResponse>;
    /**
     * URLs associated with this note
     */
    public readonly relatedUrl!: pulumi.Output<outputs.containeranalysis.v1alpha1.RelatedUrlResponse[]>;
    /**
     * A one sentence description of this `Note`.
     */
    public readonly shortDescription!: pulumi.Output<string>;
    /**
     * The time this note was last updated. This field can be used as a filter in list requests.
     */
    public readonly updateTime!: pulumi.Output<string>;
    /**
     * A note describing an upgrade.
     */
    public readonly upgrade!: pulumi.Output<outputs.containeranalysis.v1alpha1.UpgradeNoteResponse>;
    /**
     * A package vulnerability type of note.
     */
    public readonly vulnerabilityType!: pulumi.Output<outputs.containeranalysis.v1alpha1.VulnerabilityTypeResponse>;

    /**
     * Create a ProviderNote resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProviderNoteArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.notesId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'notesId'");
            }
            if ((!args || args.providersId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'providersId'");
            }
            inputs["attestationAuthority"] = args ? args.attestationAuthority : undefined;
            inputs["baseImage"] = args ? args.baseImage : undefined;
            inputs["buildType"] = args ? args.buildType : undefined;
            inputs["createTime"] = args ? args.createTime : undefined;
            inputs["deployable"] = args ? args.deployable : undefined;
            inputs["discovery"] = args ? args.discovery : undefined;
            inputs["expirationTime"] = args ? args.expirationTime : undefined;
            inputs["kind"] = args ? args.kind : undefined;
            inputs["longDescription"] = args ? args.longDescription : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["notesId"] = args ? args.notesId : undefined;
            inputs["package"] = args ? args.package : undefined;
            inputs["providersId"] = args ? args.providersId : undefined;
            inputs["relatedUrl"] = args ? args.relatedUrl : undefined;
            inputs["shortDescription"] = args ? args.shortDescription : undefined;
            inputs["updateTime"] = args ? args.updateTime : undefined;
            inputs["upgrade"] = args ? args.upgrade : undefined;
            inputs["vulnerabilityType"] = args ? args.vulnerabilityType : undefined;
        } else {
            inputs["attestationAuthority"] = undefined /*out*/;
            inputs["baseImage"] = undefined /*out*/;
            inputs["buildType"] = undefined /*out*/;
            inputs["createTime"] = undefined /*out*/;
            inputs["deployable"] = undefined /*out*/;
            inputs["discovery"] = undefined /*out*/;
            inputs["expirationTime"] = undefined /*out*/;
            inputs["kind"] = undefined /*out*/;
            inputs["longDescription"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["package"] = undefined /*out*/;
            inputs["relatedUrl"] = undefined /*out*/;
            inputs["shortDescription"] = undefined /*out*/;
            inputs["updateTime"] = undefined /*out*/;
            inputs["upgrade"] = undefined /*out*/;
            inputs["vulnerabilityType"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ProviderNote.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ProviderNote resource.
 */
export interface ProviderNoteArgs {
    /**
     * A note describing an attestation role.
     */
    readonly attestationAuthority?: pulumi.Input<inputs.containeranalysis.v1alpha1.AttestationAuthority>;
    /**
     * A note describing a base image.
     */
    readonly baseImage?: pulumi.Input<inputs.containeranalysis.v1alpha1.Basis>;
    /**
     * Build provenance type for a verifiable build.
     */
    readonly buildType?: pulumi.Input<inputs.containeranalysis.v1alpha1.BuildType>;
    /**
     * The time this note was created. This field can be used as a filter in list requests.
     */
    readonly createTime?: pulumi.Input<string>;
    /**
     * A note describing something that can be deployed.
     */
    readonly deployable?: pulumi.Input<inputs.containeranalysis.v1alpha1.Deployable>;
    /**
     * A note describing a provider/analysis type.
     */
    readonly discovery?: pulumi.Input<inputs.containeranalysis.v1alpha1.Discovery>;
    /**
     * Time of expiration for this note, null if note does not expire.
     */
    readonly expirationTime?: pulumi.Input<string>;
    /**
     * This explicitly denotes which kind of note is specified. This field can be used as a filter in list requests.
     */
    readonly kind?: pulumi.Input<string>;
    /**
     * A detailed description of this `Note`.
     */
    readonly longDescription?: pulumi.Input<string>;
    /**
     * The name of the note in the form "projects/{provider_project_id}/notes/{NOTE_ID}"
     */
    readonly name?: pulumi.Input<string>;
    readonly notesId: pulumi.Input<string>;
    /**
     * A note describing a package hosted by various package managers.
     */
    readonly package?: pulumi.Input<inputs.containeranalysis.v1alpha1.Package>;
    readonly providersId: pulumi.Input<string>;
    /**
     * URLs associated with this note
     */
    readonly relatedUrl?: pulumi.Input<pulumi.Input<inputs.containeranalysis.v1alpha1.RelatedUrl>[]>;
    /**
     * A one sentence description of this `Note`.
     */
    readonly shortDescription?: pulumi.Input<string>;
    /**
     * The time this note was last updated. This field can be used as a filter in list requests.
     */
    readonly updateTime?: pulumi.Input<string>;
    /**
     * A note describing an upgrade.
     */
    readonly upgrade?: pulumi.Input<inputs.containeranalysis.v1alpha1.UpgradeNote>;
    /**
     * A package vulnerability type of note.
     */
    readonly vulnerabilityType?: pulumi.Input<inputs.containeranalysis.v1alpha1.VulnerabilityType>;
}