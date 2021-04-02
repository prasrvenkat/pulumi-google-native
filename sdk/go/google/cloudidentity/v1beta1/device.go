// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Creates a device. Only company-owned device may be created. **Note**: This method is available only to customers who have one of the following SKUs: Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity Premium
type Device struct {
	pulumi.CustomResourceState

	// Attributes specific to Android devices.
	AndroidSpecificAttributes AndroidAttributesResponseOutput `pulumi:"androidSpecificAttributes"`
	// Asset tag of the device.
	AssetTag pulumi.StringOutput `pulumi:"assetTag"`
	// Baseband version of the device.
	BasebandVersion pulumi.StringOutput `pulumi:"basebandVersion"`
	// Device bootloader version. Example: 0.6.7.
	BootloaderVersion pulumi.StringOutput `pulumi:"bootloaderVersion"`
	// Device brand. Example: Samsung.
	Brand pulumi.StringOutput `pulumi:"brand"`
	// Build number of the device.
	BuildNumber pulumi.StringOutput `pulumi:"buildNumber"`
	// Represents whether the Device is compromised.
	CompromisedState pulumi.StringOutput `pulumi:"compromisedState"`
	// When the Company-Owned device was imported. This field is empty for BYOD devices.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Type of device.
	DeviceType pulumi.StringOutput `pulumi:"deviceType"`
	// Whether developer options is enabled on device.
	EnabledDeveloperOptions pulumi.BoolOutput `pulumi:"enabledDeveloperOptions"`
	// Whether USB debugging is enabled on device.
	EnabledUsbDebugging pulumi.BoolOutput `pulumi:"enabledUsbDebugging"`
	// Device encryption state.
	EncryptionState pulumi.StringOutput `pulumi:"encryptionState"`
	// IMEI number of device if GSM device; empty otherwise.
	Imei pulumi.StringOutput `pulumi:"imei"`
	// Kernel version of the device.
	KernelVersion pulumi.StringOutput `pulumi:"kernelVersion"`
	// Most recent time when device synced with this service.
	LastSyncTime pulumi.StringOutput `pulumi:"lastSyncTime"`
	// Management state of the device
	ManagementState pulumi.StringOutput `pulumi:"managementState"`
	// Device manufacturer. Example: Motorola.
	Manufacturer pulumi.StringOutput `pulumi:"manufacturer"`
	// MEID number of device if CDMA device; empty otherwise.
	Meid pulumi.StringOutput `pulumi:"meid"`
	// Model name of device. Example: Pixel 3.
	Model pulumi.StringOutput `pulumi:"model"`
	// [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{device_id}`, where device_id is the unique id assigned to the Device.
	Name pulumi.StringOutput `pulumi:"name"`
	// Mobile or network operator of device, if available.
	NetworkOperator pulumi.StringOutput `pulumi:"networkOperator"`
	// OS version of the device. Example: Android 8.1.0.
	OsVersion pulumi.StringOutput `pulumi:"osVersion"`
	// Domain name for Google accounts on device. Type for other accounts on device. On Android, will only be populated if |ownership_privilege| is |PROFILE_OWNER| or |DEVICE_OWNER|. Does not include the account signed in to the device policy app if that account's domain has only one account. Examples: "com.example", "xyz.com".
	OtherAccounts pulumi.StringArrayOutput `pulumi:"otherAccounts"`
	// Whether the device is owned by the company or an individual
	OwnerType pulumi.StringOutput `pulumi:"ownerType"`
	// OS release version. Example: 6.0.
	ReleaseVersion pulumi.StringOutput `pulumi:"releaseVersion"`
	// OS security patch update time on device.
	SecurityPatchTime pulumi.StringOutput `pulumi:"securityPatchTime"`
	// Serial Number of device. Example: HT82V1A01076.
	SerialNumber pulumi.StringOutput `pulumi:"serialNumber"`
	// WiFi MAC addresses of device.
	WifiMacAddresses pulumi.StringArrayOutput `pulumi:"wifiMacAddresses"`
}

// NewDevice registers a new resource with the given unique name, arguments, and options.
func NewDevice(ctx *pulumi.Context,
	name string, args *DeviceArgs, opts ...pulumi.ResourceOption) (*Device, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DevicesId == nil {
		return nil, errors.New("invalid value for required argument 'DevicesId'")
	}
	var resource Device
	err := ctx.RegisterResource("google-cloud:cloudidentity/v1beta1:Device", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDevice gets an existing Device resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDevice(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeviceState, opts ...pulumi.ResourceOption) (*Device, error) {
	var resource Device
	err := ctx.ReadResource("google-cloud:cloudidentity/v1beta1:Device", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Device resources.
type deviceState struct {
	// Attributes specific to Android devices.
	AndroidSpecificAttributes *AndroidAttributesResponse `pulumi:"androidSpecificAttributes"`
	// Asset tag of the device.
	AssetTag *string `pulumi:"assetTag"`
	// Baseband version of the device.
	BasebandVersion *string `pulumi:"basebandVersion"`
	// Device bootloader version. Example: 0.6.7.
	BootloaderVersion *string `pulumi:"bootloaderVersion"`
	// Device brand. Example: Samsung.
	Brand *string `pulumi:"brand"`
	// Build number of the device.
	BuildNumber *string `pulumi:"buildNumber"`
	// Represents whether the Device is compromised.
	CompromisedState *string `pulumi:"compromisedState"`
	// When the Company-Owned device was imported. This field is empty for BYOD devices.
	CreateTime *string `pulumi:"createTime"`
	// Type of device.
	DeviceType *string `pulumi:"deviceType"`
	// Whether developer options is enabled on device.
	EnabledDeveloperOptions *bool `pulumi:"enabledDeveloperOptions"`
	// Whether USB debugging is enabled on device.
	EnabledUsbDebugging *bool `pulumi:"enabledUsbDebugging"`
	// Device encryption state.
	EncryptionState *string `pulumi:"encryptionState"`
	// IMEI number of device if GSM device; empty otherwise.
	Imei *string `pulumi:"imei"`
	// Kernel version of the device.
	KernelVersion *string `pulumi:"kernelVersion"`
	// Most recent time when device synced with this service.
	LastSyncTime *string `pulumi:"lastSyncTime"`
	// Management state of the device
	ManagementState *string `pulumi:"managementState"`
	// Device manufacturer. Example: Motorola.
	Manufacturer *string `pulumi:"manufacturer"`
	// MEID number of device if CDMA device; empty otherwise.
	Meid *string `pulumi:"meid"`
	// Model name of device. Example: Pixel 3.
	Model *string `pulumi:"model"`
	// [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{device_id}`, where device_id is the unique id assigned to the Device.
	Name *string `pulumi:"name"`
	// Mobile or network operator of device, if available.
	NetworkOperator *string `pulumi:"networkOperator"`
	// OS version of the device. Example: Android 8.1.0.
	OsVersion *string `pulumi:"osVersion"`
	// Domain name for Google accounts on device. Type for other accounts on device. On Android, will only be populated if |ownership_privilege| is |PROFILE_OWNER| or |DEVICE_OWNER|. Does not include the account signed in to the device policy app if that account's domain has only one account. Examples: "com.example", "xyz.com".
	OtherAccounts []string `pulumi:"otherAccounts"`
	// Whether the device is owned by the company or an individual
	OwnerType *string `pulumi:"ownerType"`
	// OS release version. Example: 6.0.
	ReleaseVersion *string `pulumi:"releaseVersion"`
	// OS security patch update time on device.
	SecurityPatchTime *string `pulumi:"securityPatchTime"`
	// Serial Number of device. Example: HT82V1A01076.
	SerialNumber *string `pulumi:"serialNumber"`
	// WiFi MAC addresses of device.
	WifiMacAddresses []string `pulumi:"wifiMacAddresses"`
}

type DeviceState struct {
	// Attributes specific to Android devices.
	AndroidSpecificAttributes AndroidAttributesResponsePtrInput
	// Asset tag of the device.
	AssetTag pulumi.StringPtrInput
	// Baseband version of the device.
	BasebandVersion pulumi.StringPtrInput
	// Device bootloader version. Example: 0.6.7.
	BootloaderVersion pulumi.StringPtrInput
	// Device brand. Example: Samsung.
	Brand pulumi.StringPtrInput
	// Build number of the device.
	BuildNumber pulumi.StringPtrInput
	// Represents whether the Device is compromised.
	CompromisedState pulumi.StringPtrInput
	// When the Company-Owned device was imported. This field is empty for BYOD devices.
	CreateTime pulumi.StringPtrInput
	// Type of device.
	DeviceType pulumi.StringPtrInput
	// Whether developer options is enabled on device.
	EnabledDeveloperOptions pulumi.BoolPtrInput
	// Whether USB debugging is enabled on device.
	EnabledUsbDebugging pulumi.BoolPtrInput
	// Device encryption state.
	EncryptionState pulumi.StringPtrInput
	// IMEI number of device if GSM device; empty otherwise.
	Imei pulumi.StringPtrInput
	// Kernel version of the device.
	KernelVersion pulumi.StringPtrInput
	// Most recent time when device synced with this service.
	LastSyncTime pulumi.StringPtrInput
	// Management state of the device
	ManagementState pulumi.StringPtrInput
	// Device manufacturer. Example: Motorola.
	Manufacturer pulumi.StringPtrInput
	// MEID number of device if CDMA device; empty otherwise.
	Meid pulumi.StringPtrInput
	// Model name of device. Example: Pixel 3.
	Model pulumi.StringPtrInput
	// [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{device_id}`, where device_id is the unique id assigned to the Device.
	Name pulumi.StringPtrInput
	// Mobile or network operator of device, if available.
	NetworkOperator pulumi.StringPtrInput
	// OS version of the device. Example: Android 8.1.0.
	OsVersion pulumi.StringPtrInput
	// Domain name for Google accounts on device. Type for other accounts on device. On Android, will only be populated if |ownership_privilege| is |PROFILE_OWNER| or |DEVICE_OWNER|. Does not include the account signed in to the device policy app if that account's domain has only one account. Examples: "com.example", "xyz.com".
	OtherAccounts pulumi.StringArrayInput
	// Whether the device is owned by the company or an individual
	OwnerType pulumi.StringPtrInput
	// OS release version. Example: 6.0.
	ReleaseVersion pulumi.StringPtrInput
	// OS security patch update time on device.
	SecurityPatchTime pulumi.StringPtrInput
	// Serial Number of device. Example: HT82V1A01076.
	SerialNumber pulumi.StringPtrInput
	// WiFi MAC addresses of device.
	WifiMacAddresses pulumi.StringArrayInput
}

func (DeviceState) ElementType() reflect.Type {
	return reflect.TypeOf((*deviceState)(nil)).Elem()
}

type deviceArgs struct {
	// Required. The device to be created. The name field within this device is ignored in the create method. A new name is created by the method, and returned within the response. Only the fields `device_type`, `serial_number` and `asset_tag` (if present) are used to create the device. All other fields are ignored. The `device_type` and `serial_number` fields are required.
	Device    *DeviceType `pulumi:"device"`
	DevicesId string      `pulumi:"devicesId"`
}

// The set of arguments for constructing a Device resource.
type DeviceArgs struct {
	// Required. The device to be created. The name field within this device is ignored in the create method. A new name is created by the method, and returned within the response. Only the fields `device_type`, `serial_number` and `asset_tag` (if present) are used to create the device. All other fields are ignored. The `device_type` and `serial_number` fields are required.
	Device    DeviceTypePtrInput
	DevicesId pulumi.StringInput
}

func (DeviceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deviceArgs)(nil)).Elem()
}

type DeviceInput interface {
	pulumi.Input

	ToDeviceOutput() DeviceOutput
	ToDeviceOutputWithContext(ctx context.Context) DeviceOutput
}

func (*Device) ElementType() reflect.Type {
	return reflect.TypeOf((*Device)(nil))
}

func (i *Device) ToDeviceOutput() DeviceOutput {
	return i.ToDeviceOutputWithContext(context.Background())
}

func (i *Device) ToDeviceOutputWithContext(ctx context.Context) DeviceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeviceOutput)
}

type DeviceOutput struct {
	*pulumi.OutputState
}

func (DeviceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Device)(nil))
}

func (o DeviceOutput) ToDeviceOutput() DeviceOutput {
	return o
}

func (o DeviceOutput) ToDeviceOutputWithContext(ctx context.Context) DeviceOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DeviceOutput{})
}