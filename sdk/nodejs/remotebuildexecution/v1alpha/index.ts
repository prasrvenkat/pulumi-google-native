// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export * from "./instance";
export * from "./instanceWorkerpool";

// Import resources to register:
import { Instance } from "./instance";
import { InstanceWorkerpool } from "./instanceWorkerpool";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "google-cloud:remotebuildexecution/v1alpha:Instance":
                return new Instance(name, <any>undefined, { urn })
            case "google-cloud:remotebuildexecution/v1alpha:InstanceWorkerpool":
                return new InstanceWorkerpool(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("google-cloud", "remotebuildexecution/v1alpha", _module)