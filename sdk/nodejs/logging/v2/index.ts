// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export * from "./billingAccountBucket";
export * from "./billingAccountBucketView";
export * from "./billingAccountExclusion";
export * from "./billingAccountSink";
export * from "./bucket";
export * from "./bucketView";
export * from "./exclusion";
export * from "./folderBucket";
export * from "./folderBucketView";
export * from "./folderExclusion";
export * from "./folderSink";
export * from "./metric";
export * from "./organizationBucket";
export * from "./organizationBucketView";
export * from "./organizationExclusion";
export * from "./organizationSink";
export * from "./sink";

// Import resources to register:
import { BillingAccountBucket } from "./billingAccountBucket";
import { BillingAccountBucketView } from "./billingAccountBucketView";
import { BillingAccountExclusion } from "./billingAccountExclusion";
import { BillingAccountSink } from "./billingAccountSink";
import { Bucket } from "./bucket";
import { BucketView } from "./bucketView";
import { Exclusion } from "./exclusion";
import { FolderBucket } from "./folderBucket";
import { FolderBucketView } from "./folderBucketView";
import { FolderExclusion } from "./folderExclusion";
import { FolderSink } from "./folderSink";
import { Metric } from "./metric";
import { OrganizationBucket } from "./organizationBucket";
import { OrganizationBucketView } from "./organizationBucketView";
import { OrganizationExclusion } from "./organizationExclusion";
import { OrganizationSink } from "./organizationSink";
import { Sink } from "./sink";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "google-cloud:logging/v2:BillingAccountBucket":
                return new BillingAccountBucket(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:BillingAccountBucketView":
                return new BillingAccountBucketView(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:BillingAccountExclusion":
                return new BillingAccountExclusion(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:BillingAccountSink":
                return new BillingAccountSink(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:Bucket":
                return new Bucket(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:BucketView":
                return new BucketView(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:Exclusion":
                return new Exclusion(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:FolderBucket":
                return new FolderBucket(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:FolderBucketView":
                return new FolderBucketView(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:FolderExclusion":
                return new FolderExclusion(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:FolderSink":
                return new FolderSink(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:Metric":
                return new Metric(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:OrganizationBucket":
                return new OrganizationBucket(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:OrganizationBucketView":
                return new OrganizationBucketView(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:OrganizationExclusion":
                return new OrganizationExclusion(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:OrganizationSink":
                return new OrganizationSink(name, <any>undefined, { urn })
            case "google-cloud:logging/v2:Sink":
                return new Sink(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("google-cloud", "logging/v2", _module)