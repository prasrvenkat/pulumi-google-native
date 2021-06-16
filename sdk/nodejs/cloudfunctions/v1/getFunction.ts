// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../../types";
import * as utilities from "../../utilities";

/**
 * Returns a function with the given name from the requested project.
 */
export function getFunction(args: GetFunctionArgs, opts?: pulumi.InvokeOptions): Promise<GetFunctionResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("google-native:cloudfunctions/v1:getFunction", {
        "functionId": args.functionId,
        "location": args.location,
        "project": args.project,
    }, opts);
}

export interface GetFunctionArgs {
    functionId: string;
    location: string;
    project: string;
}

export interface GetFunctionResult {
    /**
     * The amount of memory in MB available for a function. Defaults to 256MB.
     */
    readonly availableMemoryMb: number;
    /**
     * Build environment variables that shall be available during build time.
     */
    readonly buildEnvironmentVariables: {[key: string]: string};
    /**
     * The Cloud Build ID of the latest successful deployment of the function.
     */
    readonly buildId: string;
    /**
     * Name of the Cloud Build Custom Worker Pool that should be used to build the function. The format of this field is `projects/{project}/locations/{region}/workerPools/{workerPool}` where {project} and {region} are the project id and region respectively where the worker pool is defined and {workerPool} is the short name of the worker pool. If the project id is not the same as the function, then the Cloud Functions Service Agent (service-@gcf-admin-robot.iam.gserviceaccount.com) must be granted the role Cloud Build Custom Workers Builder (roles/cloudbuild.customworkers.builder) in the project.
     */
    readonly buildWorkerPool: string;
    /**
     * User-provided description of a function.
     */
    readonly description: string;
    /**
     * The name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named "function". For Node.js this is name of a function exported by the module specified in `source_location`.
     */
    readonly entryPoint: string;
    /**
     * Environment variables that shall be available during function execution.
     */
    readonly environmentVariables: {[key: string]: string};
    /**
     * A source that fires events in response to a condition in another service.
     */
    readonly eventTrigger: outputs.cloudfunctions.v1.EventTriggerResponse;
    /**
     * An HTTPS endpoint type of source that can be triggered via URL.
     */
    readonly httpsTrigger: outputs.cloudfunctions.v1.HttpsTriggerResponse;
    /**
     * The ingress settings for the function, controlling what traffic can reach it.
     */
    readonly ingressSettings: string;
    /**
     * Labels associated with this Cloud Function.
     */
    readonly labels: {[key: string]: string};
    /**
     * The limit on the maximum number of function instances that may coexist at a given time. In some cases, such as rapid traffic surges, Cloud Functions may, for a short period of time, create more instances than the specified max instances limit. If your function cannot tolerate this temporary behavior, you may want to factor in a safety margin and set a lower max instances value than your function can tolerate. See the [Max Instances](https://cloud.google.com/functions/docs/max-instances) Guide for more details.
     */
    readonly maxInstances: number;
    /**
     * A user-defined name of the function. Function names must be unique globally and match pattern `projects/*&#47;locations/*&#47;functions/*`
     */
    readonly name: string;
    /**
     * The VPC Network that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network resource. If the short network name is used, the network must belong to the same project. Otherwise, it must belong to a project within the same organization. The format of this field is either `projects/{project}/global/networks/{network}` or `{network}`, where {project} is a project id where the network is defined, and {network} is the short name of the network. This field is mutually exclusive with `vpc_connector` and will be replaced by it. See [the VPC documentation](https://cloud.google.com/compute/docs/vpc) for more information on connecting Cloud projects.
     */
    readonly network: string;
    /**
     * The runtime in which to run the function. Required when deploying a new function, optional when updating an existing function. For a complete list of possible choices, see the [`gcloud` command reference](/sdk/gcloud/reference/functions/deploy#--runtime).
     */
    readonly runtime: string;
    /**
     * The email of the function's service account. If empty, defaults to `{project_id}@appspot.gserviceaccount.com`.
     */
    readonly serviceAccountEmail: string;
    /**
     * The Google Cloud Storage URL, starting with gs://, pointing to the zip archive which contains the function.
     */
    readonly sourceArchiveUrl: string;
    /**
     * **Beta Feature** The source repository where a function is hosted.
     */
    readonly sourceRepository: outputs.cloudfunctions.v1.SourceRepositoryResponse;
    /**
     * Input only. An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments.
     */
    readonly sourceToken: string;
    /**
     * The Google Cloud Storage signed URL used for source uploading, generated by google.cloud.functions.v1.GenerateUploadUrl
     */
    readonly sourceUploadUrl: string;
    /**
     * Status of the function deployment.
     */
    readonly status: string;
    /**
     * The function execution timeout. Execution is considered failed and can be terminated if the function is not completed at the end of the timeout period. Defaults to 60 seconds.
     */
    readonly timeout: string;
    /**
     * The last update timestamp of a Cloud Function.
     */
    readonly updateTime: string;
    /**
     * The version identifier of the Cloud Function. Each deployment attempt results in a new version of a function being created.
     */
    readonly versionId: string;
    /**
     * The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*&#47;locations/*&#47;connectors/*` This field is mutually exclusive with `network` field and will eventually replace it. See [the VPC documentation](https://cloud.google.com/compute/docs/vpc) for more information on connecting Cloud projects.
     */
    readonly vpcConnector: string;
    /**
     * The egress settings for the connector, controlling what traffic is diverted through it.
     */
    readonly vpcConnectorEgressSettings: string;
}