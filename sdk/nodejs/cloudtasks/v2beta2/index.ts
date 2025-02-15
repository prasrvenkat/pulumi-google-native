// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export { GetQueueArgs, GetQueueResult, GetQueueOutputArgs } from "./getQueue";
export const getQueue: typeof import("./getQueue").getQueue = null as any;
export const getQueueOutput: typeof import("./getQueue").getQueueOutput = null as any;
utilities.lazyLoad(exports, ["getQueue","getQueueOutput"], () => require("./getQueue"));

export { GetQueueIamPolicyArgs, GetQueueIamPolicyResult, GetQueueIamPolicyOutputArgs } from "./getQueueIamPolicy";
export const getQueueIamPolicy: typeof import("./getQueueIamPolicy").getQueueIamPolicy = null as any;
export const getQueueIamPolicyOutput: typeof import("./getQueueIamPolicy").getQueueIamPolicyOutput = null as any;
utilities.lazyLoad(exports, ["getQueueIamPolicy","getQueueIamPolicyOutput"], () => require("./getQueueIamPolicy"));

export { GetTaskArgs, GetTaskResult, GetTaskOutputArgs } from "./getTask";
export const getTask: typeof import("./getTask").getTask = null as any;
export const getTaskOutput: typeof import("./getTask").getTaskOutput = null as any;
utilities.lazyLoad(exports, ["getTask","getTaskOutput"], () => require("./getTask"));

export { QueueArgs } from "./queue";
export type Queue = import("./queue").Queue;
export const Queue: typeof import("./queue").Queue = null as any;
utilities.lazyLoad(exports, ["Queue"], () => require("./queue"));

export { QueueIamBindingArgs } from "./queueIamBinding";
export type QueueIamBinding = import("./queueIamBinding").QueueIamBinding;
export const QueueIamBinding: typeof import("./queueIamBinding").QueueIamBinding = null as any;
utilities.lazyLoad(exports, ["QueueIamBinding"], () => require("./queueIamBinding"));

export { QueueIamMemberArgs } from "./queueIamMember";
export type QueueIamMember = import("./queueIamMember").QueueIamMember;
export const QueueIamMember: typeof import("./queueIamMember").QueueIamMember = null as any;
utilities.lazyLoad(exports, ["QueueIamMember"], () => require("./queueIamMember"));

export { QueueIamPolicyArgs } from "./queueIamPolicy";
export type QueueIamPolicy = import("./queueIamPolicy").QueueIamPolicy;
export const QueueIamPolicy: typeof import("./queueIamPolicy").QueueIamPolicy = null as any;
utilities.lazyLoad(exports, ["QueueIamPolicy"], () => require("./queueIamPolicy"));

export { TaskArgs } from "./task";
export type Task = import("./task").Task;
export const Task: typeof import("./task").Task = null as any;
utilities.lazyLoad(exports, ["Task"], () => require("./task"));


// Export enums:
export * from "../../types/enums/cloudtasks/v2beta2";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "google-native:cloudtasks/v2beta2:Queue":
                return new Queue(name, <any>undefined, { urn })
            case "google-native:cloudtasks/v2beta2:QueueIamBinding":
                return new QueueIamBinding(name, <any>undefined, { urn })
            case "google-native:cloudtasks/v2beta2:QueueIamMember":
                return new QueueIamMember(name, <any>undefined, { urn })
            case "google-native:cloudtasks/v2beta2:QueueIamPolicy":
                return new QueueIamPolicy(name, <any>undefined, { urn })
            case "google-native:cloudtasks/v2beta2:Task":
                return new Task(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("google-native", "cloudtasks/v2beta2", _module)
