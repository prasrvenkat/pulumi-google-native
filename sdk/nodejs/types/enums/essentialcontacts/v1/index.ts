// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const ContactNotificationCategorySubscriptionsItem = {
    /**
     * Notification category is unrecognized or unspecified.
     */
    NotificationCategoryUnspecified: "NOTIFICATION_CATEGORY_UNSPECIFIED",
    /**
     * All notifications related to the resource, including notifications pertaining to categories added in the future.
     */
    All: "ALL",
    /**
     * Notifications related to imminent account suspension.
     */
    Suspension: "SUSPENSION",
    /**
     * Notifications related to security/privacy incidents, notifications, and vulnerabilities.
     */
    Security: "SECURITY",
    /**
     * Notifications related to technical events and issues such as outages, errors, or bugs.
     */
    Technical: "TECHNICAL",
    /**
     * Notifications related to billing and payments notifications, price updates, errors, or credits.
     */
    Billing: "BILLING",
    /**
     * Notifications related to enforcement actions, regulatory compliance, or government notices.
     */
    Legal: "LEGAL",
    /**
     * Notifications related to new versions, product terms updates, or deprecations.
     */
    ProductUpdates: "PRODUCT_UPDATES",
    /**
     * Child category of TECHNICAL. If assigned, technical incident notifications will go to these contacts instead of TECHNICAL.
     */
    TechnicalIncidents: "TECHNICAL_INCIDENTS",
} as const;

export type ContactNotificationCategorySubscriptionsItem = (typeof ContactNotificationCategorySubscriptionsItem)[keyof typeof ContactNotificationCategorySubscriptionsItem];

export const ContactValidationState = {
    /**
     * The validation state is unknown or unspecified.
     */
    ValidationStateUnspecified: "VALIDATION_STATE_UNSPECIFIED",
    /**
     * The contact is marked as valid. This is usually done manually by the contact admin. All new contacts begin in the valid state.
     */
    Valid: "VALID",
    /**
     * The contact is considered invalid. This may become the state if the contact's email is found to be unreachable.
     */
    Invalid: "INVALID",
} as const;

/**
 * The validity of the contact. A contact is considered valid if it is the correct recipient for notifications for a particular resource.
 */
export type ContactValidationState = (typeof ContactValidationState)[keyof typeof ContactValidationState];

export const FolderContactNotificationCategorySubscriptionsItem = {
    /**
     * Notification category is unrecognized or unspecified.
     */
    NotificationCategoryUnspecified: "NOTIFICATION_CATEGORY_UNSPECIFIED",
    /**
     * All notifications related to the resource, including notifications pertaining to categories added in the future.
     */
    All: "ALL",
    /**
     * Notifications related to imminent account suspension.
     */
    Suspension: "SUSPENSION",
    /**
     * Notifications related to security/privacy incidents, notifications, and vulnerabilities.
     */
    Security: "SECURITY",
    /**
     * Notifications related to technical events and issues such as outages, errors, or bugs.
     */
    Technical: "TECHNICAL",
    /**
     * Notifications related to billing and payments notifications, price updates, errors, or credits.
     */
    Billing: "BILLING",
    /**
     * Notifications related to enforcement actions, regulatory compliance, or government notices.
     */
    Legal: "LEGAL",
    /**
     * Notifications related to new versions, product terms updates, or deprecations.
     */
    ProductUpdates: "PRODUCT_UPDATES",
    /**
     * Child category of TECHNICAL. If assigned, technical incident notifications will go to these contacts instead of TECHNICAL.
     */
    TechnicalIncidents: "TECHNICAL_INCIDENTS",
} as const;

export type FolderContactNotificationCategorySubscriptionsItem = (typeof FolderContactNotificationCategorySubscriptionsItem)[keyof typeof FolderContactNotificationCategorySubscriptionsItem];

export const FolderContactValidationState = {
    /**
     * The validation state is unknown or unspecified.
     */
    ValidationStateUnspecified: "VALIDATION_STATE_UNSPECIFIED",
    /**
     * The contact is marked as valid. This is usually done manually by the contact admin. All new contacts begin in the valid state.
     */
    Valid: "VALID",
    /**
     * The contact is considered invalid. This may become the state if the contact's email is found to be unreachable.
     */
    Invalid: "INVALID",
} as const;

/**
 * The validity of the contact. A contact is considered valid if it is the correct recipient for notifications for a particular resource.
 */
export type FolderContactValidationState = (typeof FolderContactValidationState)[keyof typeof FolderContactValidationState];

export const OrganizationContactNotificationCategorySubscriptionsItem = {
    /**
     * Notification category is unrecognized or unspecified.
     */
    NotificationCategoryUnspecified: "NOTIFICATION_CATEGORY_UNSPECIFIED",
    /**
     * All notifications related to the resource, including notifications pertaining to categories added in the future.
     */
    All: "ALL",
    /**
     * Notifications related to imminent account suspension.
     */
    Suspension: "SUSPENSION",
    /**
     * Notifications related to security/privacy incidents, notifications, and vulnerabilities.
     */
    Security: "SECURITY",
    /**
     * Notifications related to technical events and issues such as outages, errors, or bugs.
     */
    Technical: "TECHNICAL",
    /**
     * Notifications related to billing and payments notifications, price updates, errors, or credits.
     */
    Billing: "BILLING",
    /**
     * Notifications related to enforcement actions, regulatory compliance, or government notices.
     */
    Legal: "LEGAL",
    /**
     * Notifications related to new versions, product terms updates, or deprecations.
     */
    ProductUpdates: "PRODUCT_UPDATES",
    /**
     * Child category of TECHNICAL. If assigned, technical incident notifications will go to these contacts instead of TECHNICAL.
     */
    TechnicalIncidents: "TECHNICAL_INCIDENTS",
} as const;

export type OrganizationContactNotificationCategorySubscriptionsItem = (typeof OrganizationContactNotificationCategorySubscriptionsItem)[keyof typeof OrganizationContactNotificationCategorySubscriptionsItem];

export const OrganizationContactValidationState = {
    /**
     * The validation state is unknown or unspecified.
     */
    ValidationStateUnspecified: "VALIDATION_STATE_UNSPECIFIED",
    /**
     * The contact is marked as valid. This is usually done manually by the contact admin. All new contacts begin in the valid state.
     */
    Valid: "VALID",
    /**
     * The contact is considered invalid. This may become the state if the contact's email is found to be unreachable.
     */
    Invalid: "INVALID",
} as const;

/**
 * The validity of the contact. A contact is considered valid if it is the correct recipient for notifications for a particular resource.
 */
export type OrganizationContactValidationState = (typeof OrganizationContactValidationState)[keyof typeof OrganizationContactValidationState];
