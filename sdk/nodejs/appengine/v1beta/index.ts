// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export * from "./app";
export * from "./appAuthorizedCertificate";
export * from "./appDomainMapping";
export * from "./appFirewallIngressRule";
export * from "./appServiceVersion";

// Import resources to register:
import { App } from "./app";
import { AppAuthorizedCertificate } from "./appAuthorizedCertificate";
import { AppDomainMapping } from "./appDomainMapping";
import { AppFirewallIngressRule } from "./appFirewallIngressRule";
import { AppServiceVersion } from "./appServiceVersion";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "google-cloud:appengine/v1beta:App":
                return new App(name, <any>undefined, { urn })
            case "google-cloud:appengine/v1beta:AppAuthorizedCertificate":
                return new AppAuthorizedCertificate(name, <any>undefined, { urn })
            case "google-cloud:appengine/v1beta:AppDomainMapping":
                return new AppDomainMapping(name, <any>undefined, { urn })
            case "google-cloud:appengine/v1beta:AppFirewallIngressRule":
                return new AppFirewallIngressRule(name, <any>undefined, { urn })
            case "google-cloud:appengine/v1beta:AppServiceVersion":
                return new AppServiceVersion(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("google-cloud", "appengine/v1beta", _module)