// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const AuditLogConfigLogType = {
    /**
     * Default case. Should never be this.
     */
    LogTypeUnspecified: "LOG_TYPE_UNSPECIFIED",
    /**
     * Admin reads. Example: CloudIAM getIamPolicy
     */
    AdminRead: "ADMIN_READ",
    /**
     * Data writes. Example: CloudSQL Users create
     */
    DataWrite: "DATA_WRITE",
    /**
     * Data reads. Example: CloudSQL Users list
     */
    DataRead: "DATA_READ",
} as const;

/**
 * The log type that this config enables.
 */
export type AuditLogConfigLogType = (typeof AuditLogConfigLogType)[keyof typeof AuditLogConfigLogType];

export const InstanceType = {
    /**
     * No type specified. The instance creation will fail.
     */
    TypeUnspecified: "TYPE_UNSPECIFIED",
    /**
     * Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines using point and click UI. However, there are certain limitations, such as fewer number of concurrent pipelines, no support for streaming pipelines, etc.
     */
    Basic: "BASIC",
    /**
     * Enterprise Data Fusion instance. In Enterprise type, the user will have all features available, such as support for streaming pipelines, higher number of concurrent pipelines, etc.
     */
    Enterprise: "ENTERPRISE",
    /**
     * Developer Data Fusion instance. In Developer type, the user will have all features available but with restrictive capabilities. This is to help enterprises design and develop their data ingestion and integration pipelines at low cost.
     */
    Developer: "DEVELOPER",
} as const;

/**
 * Required. Instance type.
 */
export type InstanceType = (typeof InstanceType)[keyof typeof InstanceType];
