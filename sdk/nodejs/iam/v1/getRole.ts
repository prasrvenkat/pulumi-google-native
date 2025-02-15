// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Gets the definition of a Role.
 */
export function getRole(args: GetRoleArgs, opts?: pulumi.InvokeOptions): Promise<GetRoleResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:iam/v1:getRole", {
        "project": args.project,
        "roleId": args.roleId,
    }, opts);
}

export interface GetRoleArgs {
    project?: string;
    roleId: string;
}

export interface GetRoleResult {
    /**
     * The current deleted state of the role. This field is read only. It will be ignored in calls to CreateRole and UpdateRole.
     */
    readonly deleted: boolean;
    /**
     * Optional. A human-readable description for the role.
     */
    readonly description: string;
    /**
     * Used to perform a consistent read-modify-write.
     */
    readonly etag: string;
    /**
     * The names of the permissions this role grants when bound in an IAM policy.
     */
    readonly includedPermissions: string[];
    /**
     * The name of the role. When `Role` is used in `CreateRole`, the role name must not be set. When `Role` is used in output and other input such as `UpdateRole`, the role name is the complete path. For example, `roles/logging.viewer` for predefined roles, `organizations/{ORGANIZATION_ID}/roles/my-role` for organization-level custom roles, and `projects/{PROJECT_ID}/roles/my-role` for project-level custom roles.
     */
    readonly name: string;
    /**
     * The current launch stage of the role. If the `ALPHA` launch stage has been selected for a role, the `stage` field will not be included in the returned definition for the role.
     */
    readonly stage: string;
    /**
     * Optional. A human-readable title for the role. Typically this is limited to 100 UTF-8 bytes.
     */
    readonly title: string;
}
/**
 * Gets the definition of a Role.
 */
export function getRoleOutput(args: GetRoleOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetRoleResult> {
    return pulumi.output(args).apply((a: any) => getRole(a, opts))
}

export interface GetRoleOutputArgs {
    project?: pulumi.Input<string>;
    roleId: pulumi.Input<string>;
}
