// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Creates a snapshot from the requested subscription. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. If the snapshot already exists, returns `ALREADY_EXISTS`. If the requested subscription doesn't exist, returns `NOT_FOUND`. If the backlog in the subscription is too old -- and the resulting snapshot would expire in less than 1 hour -- then `FAILED_PRECONDITION` is returned. See also the `Snapshot.expire_time` field. If the name is not provided in the request, the server will assign a random name for this snapshot on the same project as the subscription, conforming to the [resource name format] (https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names). The generated name is populated in the returned Snapshot object. Note that for REST API requests, you must specify a name in the request.
 * Auto-naming is currently not supported for this resource.
 */
export class Snapshot extends pulumi.CustomResource {
    /**
     * Get an existing Snapshot resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Snapshot {
        return new Snapshot(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:pubsub/v1:Snapshot';

    /**
     * Returns true if the given object is an instance of Snapshot.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Snapshot {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Snapshot.__pulumiType;
    }

    /**
     * Optional. The snapshot is guaranteed to exist up until this time. A newly-created snapshot expires no later than 7 days from the time of its creation. Its exact lifetime is determined at creation by the existing backlog in the source subscription. Specifically, the lifetime of the snapshot is `7 days - (age of oldest unacked message in the subscription)`. For example, consider a subscription whose oldest unacked message is 3 days old. If a snapshot is created from this subscription, the snapshot -- which will always capture this 3-day-old backlog as long as the snapshot exists -- will expire in 4 days. The service will refuse to create a snapshot that would expire in less than 1 hour after creation.
     */
    public /*out*/ readonly expireTime!: pulumi.Output<string>;
    /**
     * Optional. See [Creating and managing labels] (https://cloud.google.com/pubsub/docs/labels).
     */
    public readonly labels!: pulumi.Output<{[key: string]: string}>;
    /**
     * Optional. The name of the snapshot.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    public readonly snapshotId!: pulumi.Output<string>;
    /**
     * Optional. The name of the topic from which this snapshot is retaining messages.
     */
    public /*out*/ readonly topic!: pulumi.Output<string>;

    /**
     * Create a Snapshot resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SnapshotArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.snapshotId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'snapshotId'");
            }
            if ((!args || args.subscription === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subscription'");
            }
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["snapshotId"] = args ? args.snapshotId : undefined;
            resourceInputs["subscription"] = args ? args.subscription : undefined;
            resourceInputs["expireTime"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["topic"] = undefined /*out*/;
        } else {
            resourceInputs["expireTime"] = undefined /*out*/;
            resourceInputs["labels"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["snapshotId"] = undefined /*out*/;
            resourceInputs["topic"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["project", "snapshotId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Snapshot.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Snapshot resource.
 */
export interface SnapshotArgs {
    /**
     * Optional. See [Creating and managing labels](https://cloud.google.com/pubsub/docs/labels).
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    project?: pulumi.Input<string>;
    snapshotId: pulumi.Input<string>;
    /**
     * The subscription whose backlog the snapshot retains. Specifically, the created snapshot is guaranteed to retain: (a) The existing backlog on the subscription. More precisely, this is defined as the messages in the subscription's backlog that are unacknowledged upon the successful completion of the `CreateSnapshot` request; as well as: (b) Any messages published to the subscription's topic following the successful completion of the CreateSnapshot request. Format is `projects/{project}/subscriptions/{sub}`.
     */
    subscription: pulumi.Input<string>;
}
