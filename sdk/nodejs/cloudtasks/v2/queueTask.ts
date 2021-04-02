// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../../types";
import * as utilities from "../../utilities";

/**
 * Creates a task and adds it to a queue. Tasks cannot be updated after creation; there is no UpdateTask command. * The maximum task size is 100KB.
 */
export class QueueTask extends pulumi.CustomResource {
    /**
     * Get an existing QueueTask resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): QueueTask {
        return new QueueTask(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-cloud:cloudtasks/v2:QueueTask';

    /**
     * Returns true if the given object is an instance of QueueTask.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is QueueTask {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === QueueTask.__pulumiType;
    }

    /**
     * HTTP request that is sent to the App Engine app handler. An App Engine task is a task that has AppEngineHttpRequest set.
     */
    public /*out*/ readonly appEngineHttpRequest!: pulumi.Output<outputs.cloudtasks.v2.AppEngineHttpRequestResponse>;
    /**
     * The time that the task was created. `create_time` will be truncated to the nearest second.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * The number of attempts dispatched. This count includes attempts which have been dispatched but haven't received a response.
     */
    public /*out*/ readonly dispatchCount!: pulumi.Output<number>;
    /**
     * The deadline for requests sent to the worker. If the worker does not respond by this deadline then the request is cancelled and the attempt is marked as a `DEADLINE_EXCEEDED` failure. Cloud Tasks will retry the task according to the RetryConfig. Note that when the request is cancelled, Cloud Tasks will stop listening for the response, but whether the worker stops processing depends on the worker. For example, if the worker is stuck, it may not react to cancelled requests. The default and maximum values depend on the type of request: * For HTTP tasks, the default is 10 minutes. The deadline must be in the interval [15 seconds, 30 minutes]. * For App Engine tasks, 0 indicates that the request has the default deadline. The default deadline depends on the [scaling type](https://cloud.google.com/appengine/docs/standard/go/how-instances-are-managed#instance_scaling) of the service: 10 minutes for standard apps with automatic scaling, 24 hours for standard apps with manual and basic scaling, and 60 minutes for flex apps. If the request deadline is set, it must be in the interval [15 seconds, 24 hours 15 seconds]. Regardless of the task's `dispatch_deadline`, the app handler will not run for longer than than the service's timeout. We recommend setting the `dispatch_deadline` to at most a few seconds more than the app handler's timeout. For more information see [Timeouts](https://cloud.google.com/tasks/docs/creating-appengine-handlers#timeouts). `dispatch_deadline` will be truncated to the nearest millisecond. The deadline is an approximate deadline.
     */
    public /*out*/ readonly dispatchDeadline!: pulumi.Output<string>;
    /**
     * The status of the task's first attempt. Only dispatch_time will be set. The other Attempt information is not retained by Cloud Tasks.
     */
    public /*out*/ readonly firstAttempt!: pulumi.Output<outputs.cloudtasks.v2.AttemptResponse>;
    /**
     * HTTP request that is sent to the worker. An HTTP task is a task that has HttpRequest set.
     */
    public /*out*/ readonly httpRequest!: pulumi.Output<outputs.cloudtasks.v2.HttpRequestResponse>;
    /**
     * The status of the task's last attempt.
     */
    public /*out*/ readonly lastAttempt!: pulumi.Output<outputs.cloudtasks.v2.AttemptResponse>;
    /**
     * Optionally caller-specified in CreateTask. The task name. The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters. * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The number of attempts which have received a response.
     */
    public /*out*/ readonly responseCount!: pulumi.Output<number>;
    /**
     * The time when the task is scheduled to be attempted or retried. `schedule_time` will be truncated to the nearest microsecond.
     */
    public /*out*/ readonly scheduleTime!: pulumi.Output<string>;
    /**
     * The view specifies which subset of the Task has been returned.
     */
    public /*out*/ readonly view!: pulumi.Output<string>;

    /**
     * Create a QueueTask resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: QueueTaskArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.locationsId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'locationsId'");
            }
            if ((!args || args.projectsId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectsId'");
            }
            if ((!args || args.queuesId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'queuesId'");
            }
            if ((!args || args.tasksId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tasksId'");
            }
            inputs["locationsId"] = args ? args.locationsId : undefined;
            inputs["projectsId"] = args ? args.projectsId : undefined;
            inputs["queuesId"] = args ? args.queuesId : undefined;
            inputs["responseView"] = args ? args.responseView : undefined;
            inputs["task"] = args ? args.task : undefined;
            inputs["tasksId"] = args ? args.tasksId : undefined;
            inputs["appEngineHttpRequest"] = undefined /*out*/;
            inputs["createTime"] = undefined /*out*/;
            inputs["dispatchCount"] = undefined /*out*/;
            inputs["dispatchDeadline"] = undefined /*out*/;
            inputs["firstAttempt"] = undefined /*out*/;
            inputs["httpRequest"] = undefined /*out*/;
            inputs["lastAttempt"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["responseCount"] = undefined /*out*/;
            inputs["scheduleTime"] = undefined /*out*/;
            inputs["view"] = undefined /*out*/;
        } else {
            inputs["appEngineHttpRequest"] = undefined /*out*/;
            inputs["createTime"] = undefined /*out*/;
            inputs["dispatchCount"] = undefined /*out*/;
            inputs["dispatchDeadline"] = undefined /*out*/;
            inputs["firstAttempt"] = undefined /*out*/;
            inputs["httpRequest"] = undefined /*out*/;
            inputs["lastAttempt"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["responseCount"] = undefined /*out*/;
            inputs["scheduleTime"] = undefined /*out*/;
            inputs["view"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(QueueTask.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a QueueTask resource.
 */
export interface QueueTaskArgs {
    readonly locationsId: pulumi.Input<string>;
    readonly projectsId: pulumi.Input<string>;
    readonly queuesId: pulumi.Input<string>;
    /**
     * The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the Task resource.
     */
    readonly responseView?: pulumi.Input<string>;
    /**
     * Required. The task to add. Task names have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The user can optionally specify a task name. If a name is not specified then the system will generate a random unique task id, which will be set in the task returned in the response. If schedule_time is not set or is in the past then Cloud Tasks will set it to the current time. Task De-duplication: Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or executed recently then the call will fail with ALREADY_EXISTS. If the task's queue was created using Cloud Tasks, then another task with the same name can't be created for ~1hour after the original task was deleted or executed. If the task's queue was created using queue.yaml or queue.xml, then another task with the same name can't be created for ~9days after the original task was deleted or executed. Because there is an extra lookup cost to identify duplicate task names, these CreateTask calls have significantly increased latency. Using hashed strings for the task id or for the prefix of the task id is recommended. Choosing task ids that are sequential or have sequential prefixes, for example using a timestamp, causes an increase in latency and error rates in all task commands. The infrastructure relies on an approximately uniform distribution of task ids to store and serve tasks efficiently.
     */
    readonly task?: pulumi.Input<inputs.cloudtasks.v2.Task>;
    readonly tasksId: pulumi.Input<string>;
}