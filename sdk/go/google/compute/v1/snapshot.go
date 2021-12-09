// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a snapshot in the specified project using the data included in the request.
type Snapshot struct {
	pulumi.CustomResourceState

	// Set to true if snapshots are automatically created by applying resource policy on the target disk.
	AutoCreated pulumi.BoolOutput `pulumi:"autoCreated"`
	// Creates the new snapshot in the snapshot chain labeled with the specified name. The chain name must be 1-63 characters long and comply with RFC1035. This is an uncommon option only for advanced service owners who needs to create separate snapshot chains, for example, for chargeback tracking. When you describe your snapshot resource, this field is visible only if it has a non-empty value.
	ChainName pulumi.StringOutput `pulumi:"chainName"`
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringOutput `pulumi:"creationTimestamp"`
	// An optional description of this resource. Provide this property when you create the resource.
	Description pulumi.StringOutput `pulumi:"description"`
	// Size of the source disk, specified in GB.
	DiskSizeGb pulumi.StringOutput `pulumi:"diskSizeGb"`
	// Number of bytes downloaded to restore a snapshot to a disk.
	DownloadBytes pulumi.StringOutput `pulumi:"downloadBytes"`
	// Type of the resource. Always compute#snapshot for Snapshot resources.
	Kind pulumi.StringOutput `pulumi:"kind"`
	// A fingerprint for the labels being applied to this snapshot, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a snapshot.
	LabelFingerprint pulumi.StringOutput `pulumi:"labelFingerprint"`
	// Labels to apply to this snapshot. These can be later modified by the setLabels method. Label values may be empty.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// Integer license codes indicating which licenses are attached to this snapshot.
	LicenseCodes pulumi.StringArrayOutput `pulumi:"licenseCodes"`
	// A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses attached (such as a Windows image).
	Licenses pulumi.StringArrayOutput `pulumi:"licenses"`
	// An opaque location hint used to place the snapshot close to other resources. This field is for use by internal tools that use the public API.
	LocationHint pulumi.StringOutput `pulumi:"locationHint"`
	// Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name pulumi.StringOutput `pulumi:"name"`
	// Reserved for future use.
	SatisfiesPzs pulumi.BoolOutput `pulumi:"satisfiesPzs"`
	// Server-defined URL for the resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// Encrypts the snapshot using a customer-supplied encryption key. After you encrypt a snapshot using a customer-supplied key, you must provide the same key if you use the snapshot later. For example, you must provide the encryption key when you create a disk from the encrypted snapshot in a future request. Customer-supplied encryption keys do not protect access to metadata of the snapshot. If you do not provide an encryption key when creating the snapshot, then the snapshot will be encrypted using an automatically generated key and you do not need to provide a key to use the snapshot later.
	SnapshotEncryptionKey CustomerEncryptionKeyResponseOutput `pulumi:"snapshotEncryptionKey"`
	// The source disk used to create this snapshot.
	SourceDisk pulumi.StringOutput `pulumi:"sourceDisk"`
	// The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.
	SourceDiskEncryptionKey CustomerEncryptionKeyResponseOutput `pulumi:"sourceDiskEncryptionKey"`
	// The ID value of the disk used to create this snapshot. This value may be used to determine whether the snapshot was taken from the current or a previous instance of a given disk name.
	SourceDiskId pulumi.StringOutput `pulumi:"sourceDiskId"`
	// The status of the snapshot. This can be CREATING, DELETING, FAILED, READY, or UPLOADING.
	Status pulumi.StringOutput `pulumi:"status"`
	// A size of the storage used by the snapshot. As snapshots share storage, this number is expected to change with snapshot creation/deletion.
	StorageBytes pulumi.StringOutput `pulumi:"storageBytes"`
	// An indicator whether storageBytes is in a stable state or it is being adjusted as a result of shared storage reallocation. This status can either be UPDATING, meaning the size of the snapshot is being updated, or UP_TO_DATE, meaning the size of the snapshot is up-to-date.
	StorageBytesStatus pulumi.StringOutput `pulumi:"storageBytesStatus"`
	// Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
	StorageLocations pulumi.StringArrayOutput `pulumi:"storageLocations"`
}

// NewSnapshot registers a new resource with the given unique name, arguments, and options.
func NewSnapshot(ctx *pulumi.Context,
	name string, args *SnapshotArgs, opts ...pulumi.ResourceOption) (*Snapshot, error) {
	if args == nil {
		args = &SnapshotArgs{}
	}

	var resource Snapshot
	err := ctx.RegisterResource("google-native:compute/v1:Snapshot", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSnapshot gets an existing Snapshot resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSnapshot(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SnapshotState, opts ...pulumi.ResourceOption) (*Snapshot, error) {
	var resource Snapshot
	err := ctx.ReadResource("google-native:compute/v1:Snapshot", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Snapshot resources.
type snapshotState struct {
}

type SnapshotState struct {
}

func (SnapshotState) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotState)(nil)).Elem()
}

type snapshotArgs struct {
	// Creates the new snapshot in the snapshot chain labeled with the specified name. The chain name must be 1-63 characters long and comply with RFC1035. This is an uncommon option only for advanced service owners who needs to create separate snapshot chains, for example, for chargeback tracking. When you describe your snapshot resource, this field is visible only if it has a non-empty value.
	ChainName *string `pulumi:"chainName"`
	// An optional description of this resource. Provide this property when you create the resource.
	Description *string `pulumi:"description"`
	// Labels to apply to this snapshot. These can be later modified by the setLabels method. Label values may be empty.
	Labels map[string]string `pulumi:"labels"`
	// An opaque location hint used to place the snapshot close to other resources. This field is for use by internal tools that use the public API.
	LocationHint *string `pulumi:"locationHint"`
	// Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name      *string `pulumi:"name"`
	Project   *string `pulumi:"project"`
	RequestId *string `pulumi:"requestId"`
	// Encrypts the snapshot using a customer-supplied encryption key. After you encrypt a snapshot using a customer-supplied key, you must provide the same key if you use the snapshot later. For example, you must provide the encryption key when you create a disk from the encrypted snapshot in a future request. Customer-supplied encryption keys do not protect access to metadata of the snapshot. If you do not provide an encryption key when creating the snapshot, then the snapshot will be encrypted using an automatically generated key and you do not need to provide a key to use the snapshot later.
	SnapshotEncryptionKey *CustomerEncryptionKey `pulumi:"snapshotEncryptionKey"`
	// The source disk used to create this snapshot.
	SourceDisk *string `pulumi:"sourceDisk"`
	// The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.
	SourceDiskEncryptionKey *CustomerEncryptionKey `pulumi:"sourceDiskEncryptionKey"`
	// Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
	StorageLocations []string `pulumi:"storageLocations"`
}

// The set of arguments for constructing a Snapshot resource.
type SnapshotArgs struct {
	// Creates the new snapshot in the snapshot chain labeled with the specified name. The chain name must be 1-63 characters long and comply with RFC1035. This is an uncommon option only for advanced service owners who needs to create separate snapshot chains, for example, for chargeback tracking. When you describe your snapshot resource, this field is visible only if it has a non-empty value.
	ChainName pulumi.StringPtrInput
	// An optional description of this resource. Provide this property when you create the resource.
	Description pulumi.StringPtrInput
	// Labels to apply to this snapshot. These can be later modified by the setLabels method. Label values may be empty.
	Labels pulumi.StringMapInput
	// An opaque location hint used to place the snapshot close to other resources. This field is for use by internal tools that use the public API.
	LocationHint pulumi.StringPtrInput
	// Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name      pulumi.StringPtrInput
	Project   pulumi.StringPtrInput
	RequestId pulumi.StringPtrInput
	// Encrypts the snapshot using a customer-supplied encryption key. After you encrypt a snapshot using a customer-supplied key, you must provide the same key if you use the snapshot later. For example, you must provide the encryption key when you create a disk from the encrypted snapshot in a future request. Customer-supplied encryption keys do not protect access to metadata of the snapshot. If you do not provide an encryption key when creating the snapshot, then the snapshot will be encrypted using an automatically generated key and you do not need to provide a key to use the snapshot later.
	SnapshotEncryptionKey CustomerEncryptionKeyPtrInput
	// The source disk used to create this snapshot.
	SourceDisk pulumi.StringPtrInput
	// The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.
	SourceDiskEncryptionKey CustomerEncryptionKeyPtrInput
	// Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
	StorageLocations pulumi.StringArrayInput
}

func (SnapshotArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotArgs)(nil)).Elem()
}

type SnapshotInput interface {
	pulumi.Input

	ToSnapshotOutput() SnapshotOutput
	ToSnapshotOutputWithContext(ctx context.Context) SnapshotOutput
}

func (*Snapshot) ElementType() reflect.Type {
	return reflect.TypeOf((*Snapshot)(nil))
}

func (i *Snapshot) ToSnapshotOutput() SnapshotOutput {
	return i.ToSnapshotOutputWithContext(context.Background())
}

func (i *Snapshot) ToSnapshotOutputWithContext(ctx context.Context) SnapshotOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SnapshotOutput)
}

type SnapshotOutput struct{ *pulumi.OutputState }

func (SnapshotOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Snapshot)(nil))
}

func (o SnapshotOutput) ToSnapshotOutput() SnapshotOutput {
	return o
}

func (o SnapshotOutput) ToSnapshotOutputWithContext(ctx context.Context) SnapshotOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SnapshotInput)(nil)).Elem(), &Snapshot{})
	pulumi.RegisterOutputType(SnapshotOutput{})
}