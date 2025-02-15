// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export { ConnectionArgs } from "./connection";
export type Connection = import("./connection").Connection;
export const Connection: typeof import("./connection").Connection = null as any;
utilities.lazyLoad(exports, ["Connection"], () => require("./connection"));

export { ConnectionIamBindingArgs } from "./connectionIamBinding";
export type ConnectionIamBinding = import("./connectionIamBinding").ConnectionIamBinding;
export const ConnectionIamBinding: typeof import("./connectionIamBinding").ConnectionIamBinding = null as any;
utilities.lazyLoad(exports, ["ConnectionIamBinding"], () => require("./connectionIamBinding"));

export { ConnectionIamMemberArgs } from "./connectionIamMember";
export type ConnectionIamMember = import("./connectionIamMember").ConnectionIamMember;
export const ConnectionIamMember: typeof import("./connectionIamMember").ConnectionIamMember = null as any;
utilities.lazyLoad(exports, ["ConnectionIamMember"], () => require("./connectionIamMember"));

export { ConnectionIamPolicyArgs } from "./connectionIamPolicy";
export type ConnectionIamPolicy = import("./connectionIamPolicy").ConnectionIamPolicy;
export const ConnectionIamPolicy: typeof import("./connectionIamPolicy").ConnectionIamPolicy = null as any;
utilities.lazyLoad(exports, ["ConnectionIamPolicy"], () => require("./connectionIamPolicy"));

export { GetConnectionArgs, GetConnectionResult, GetConnectionOutputArgs } from "./getConnection";
export const getConnection: typeof import("./getConnection").getConnection = null as any;
export const getConnectionOutput: typeof import("./getConnection").getConnectionOutput = null as any;
utilities.lazyLoad(exports, ["getConnection","getConnectionOutput"], () => require("./getConnection"));

export { GetConnectionIamPolicyArgs, GetConnectionIamPolicyResult, GetConnectionIamPolicyOutputArgs } from "./getConnectionIamPolicy";
export const getConnectionIamPolicy: typeof import("./getConnectionIamPolicy").getConnectionIamPolicy = null as any;
export const getConnectionIamPolicyOutput: typeof import("./getConnectionIamPolicy").getConnectionIamPolicyOutput = null as any;
utilities.lazyLoad(exports, ["getConnectionIamPolicy","getConnectionIamPolicyOutput"], () => require("./getConnectionIamPolicy"));

export { GetRepositoryArgs, GetRepositoryResult, GetRepositoryOutputArgs } from "./getRepository";
export const getRepository: typeof import("./getRepository").getRepository = null as any;
export const getRepositoryOutput: typeof import("./getRepository").getRepositoryOutput = null as any;
utilities.lazyLoad(exports, ["getRepository","getRepositoryOutput"], () => require("./getRepository"));

export { RepositoryArgs } from "./repository";
export type Repository = import("./repository").Repository;
export const Repository: typeof import("./repository").Repository = null as any;
utilities.lazyLoad(exports, ["Repository"], () => require("./repository"));


// Export enums:
export * from "../../types/enums/cloudbuild/v2";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "google-native:cloudbuild/v2:Connection":
                return new Connection(name, <any>undefined, { urn })
            case "google-native:cloudbuild/v2:ConnectionIamBinding":
                return new ConnectionIamBinding(name, <any>undefined, { urn })
            case "google-native:cloudbuild/v2:ConnectionIamMember":
                return new ConnectionIamMember(name, <any>undefined, { urn })
            case "google-native:cloudbuild/v2:ConnectionIamPolicy":
                return new ConnectionIamPolicy(name, <any>undefined, { urn })
            case "google-native:cloudbuild/v2:Repository":
                return new Repository(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("google-native", "cloudbuild/v2", _module)
