// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Returns the details of a fleet namespace.
 */
export function getNamespace(args: GetNamespaceArgs, opts?: pulumi.InvokeOptions): Promise<GetNamespaceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:gkehub/v1beta:getNamespace", {
        "location": args.location,
        "namespaceId": args.namespaceId,
        "project": args.project,
    }, opts);
}

export interface GetNamespaceArgs {
    location: string;
    namespaceId: string;
    project?: string;
}

export interface GetNamespaceResult {
    /**
     * When the namespace was created.
     */
    readonly createTime: string;
    /**
     * When the namespace was deleted.
     */
    readonly deleteTime: string;
    /**
     * The resource name for the namespace `projects/{project}/locations/{location}/namespaces/{namespace}`
     */
    readonly name: string;
    /**
     * Scope associated with the namespace
     */
    readonly scope: string;
    /**
     * State of the namespace resource.
     */
    readonly state: outputs.gkehub.v1beta.NamespaceLifecycleStateResponse;
    /**
     * Google-generated UUID for this resource. This is unique across all namespace resources. If a namespace resource is deleted and another resource with the same name is created, it gets a different uid.
     */
    readonly uid: string;
    /**
     * When the namespace was last updated.
     */
    readonly updateTime: string;
}
/**
 * Returns the details of a fleet namespace.
 */
export function getNamespaceOutput(args: GetNamespaceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetNamespaceResult> {
    return pulumi.output(args).apply((a: any) => getNamespace(a, opts))
}

export interface GetNamespaceOutputArgs {
    location: pulumi.Input<string>;
    namespaceId: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}