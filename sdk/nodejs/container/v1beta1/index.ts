// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export * from "./cluster";
export * from "./clusterNodePool";

// Import resources to register:
import { Cluster } from "./cluster";
import { ClusterNodePool } from "./clusterNodePool";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "google-cloud:container/v1beta1:Cluster":
                return new Cluster(name, <any>undefined, { urn })
            case "google-cloud:container/v1beta1:ClusterNodePool":
                return new ClusterNodePool(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("google-cloud", "container/v1beta1", _module)