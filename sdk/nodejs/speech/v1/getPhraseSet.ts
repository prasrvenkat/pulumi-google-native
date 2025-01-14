// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Get a phrase set.
 */
export function getPhraseSet(args: GetPhraseSetArgs, opts?: pulumi.InvokeOptions): Promise<GetPhraseSetResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:speech/v1:getPhraseSet", {
        "location": args.location,
        "phraseSetId": args.phraseSetId,
        "project": args.project,
    }, opts);
}

export interface GetPhraseSetArgs {
    location: string;
    phraseSetId: string;
    project?: string;
}

export interface GetPhraseSetResult {
    /**
     * Allows users to store small amounts of arbitrary data. Both the key and the value must be 63 characters or less each. At most 100 annotations. This field is not used.
     */
    readonly annotations: {[key: string]: string};
    /**
     * Hint Boost. Positive value will increase the probability that a specific phrase will be recognized over other similar sounding phrases. The higher the boost, the higher the chance of false positive recognition as well. Negative boost values would correspond to anti-biasing. Anti-biasing is not enabled, so negative boost will simply be ignored. Though `boost` can accept a wide range of positive values, most use cases are best served with values between 0 (exclusive) and 20. We recommend using a binary search approach to finding the optimal value for your use case as well as adding phrases both with and without boost to your requests.
     */
    readonly boost: number;
    /**
     * The time at which this resource was requested for deletion. This field is not used.
     */
    readonly deleteTime: string;
    /**
     * User-settable, human-readable name for the PhraseSet. Must be 63 characters or less. This field is not used.
     */
    readonly displayName: string;
    /**
     * This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding. This field is not used.
     */
    readonly etag: string;
    /**
     * The time at which this resource will be purged. This field is not used.
     */
    readonly expireTime: string;
    /**
     * The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the PhraseSet is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.
     */
    readonly kmsKeyName: string;
    /**
     * The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the PhraseSet is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}`.
     */
    readonly kmsKeyVersionName: string;
    /**
     * The resource name of the phrase set.
     */
    readonly name: string;
    /**
     * A list of word and phrases.
     */
    readonly phrases: outputs.speech.v1.PhraseResponse[];
    /**
     * Whether or not this PhraseSet is in the process of being updated. This field is not used.
     */
    readonly reconciling: boolean;
    /**
     * The CustomClass lifecycle state. This field is not used.
     */
    readonly state: string;
    /**
     * System-assigned unique identifier for the PhraseSet. This field is not used.
     */
    readonly uid: string;
}
/**
 * Get a phrase set.
 */
export function getPhraseSetOutput(args: GetPhraseSetOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPhraseSetResult> {
    return pulumi.output(args).apply((a: any) => getPhraseSet(a, opts))
}

export interface GetPhraseSetOutputArgs {
    location: pulumi.Input<string>;
    phraseSetId: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
