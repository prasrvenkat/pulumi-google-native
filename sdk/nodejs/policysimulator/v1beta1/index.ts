// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export * from "./folderReplay";
export * from "./organizationReplay";
export * from "./replay";

// Import resources to register:
import { FolderReplay } from "./folderReplay";
import { OrganizationReplay } from "./organizationReplay";
import { Replay } from "./replay";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "google-cloud:policysimulator/v1beta1:FolderReplay":
                return new FolderReplay(name, <any>undefined, { urn })
            case "google-cloud:policysimulator/v1beta1:OrganizationReplay":
                return new OrganizationReplay(name, <any>undefined, { urn })
            case "google-cloud:policysimulator/v1beta1:Replay":
                return new Replay(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("google-cloud", "policysimulator/v1beta1", _module)