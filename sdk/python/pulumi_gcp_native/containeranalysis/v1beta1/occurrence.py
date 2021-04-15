# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['OccurrenceArgs', 'Occurrence']

@pulumi.input_type
class OccurrenceArgs:
    def __init__(__self__, *,
                 occurrences_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 attestation: Optional[pulumi.Input['DetailsArgs']] = None,
                 build: Optional[pulumi.Input['GrafeasV1beta1BuildDetailsArgs']] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 deployment: Optional[pulumi.Input['GrafeasV1beta1DeploymentDetailsArgs']] = None,
                 derived_image: Optional[pulumi.Input['GrafeasV1beta1ImageDetailsArgs']] = None,
                 discovered: Optional[pulumi.Input['GrafeasV1beta1DiscoveryDetailsArgs']] = None,
                 installation: Optional[pulumi.Input['GrafeasV1beta1PackageDetailsArgs']] = None,
                 intoto: Optional[pulumi.Input['GrafeasV1beta1IntotoDetailsArgs']] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 note_name: Optional[pulumi.Input[str]] = None,
                 remediation: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input['ResourceArgs']] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 vulnerability: Optional[pulumi.Input['GrafeasV1beta1VulnerabilityDetailsArgs']] = None):
        """
        The set of arguments for constructing a Occurrence resource.
        :param pulumi.Input['DetailsArgs'] attestation: Describes an attestation of an artifact.
        :param pulumi.Input['GrafeasV1beta1BuildDetailsArgs'] build: Describes a verifiable build.
        :param pulumi.Input[str] create_time: The time this occurrence was created.
        :param pulumi.Input['GrafeasV1beta1DeploymentDetailsArgs'] deployment: Describes the deployment of an artifact on a runtime.
        :param pulumi.Input['GrafeasV1beta1ImageDetailsArgs'] derived_image: Describes how this resource derives from the basis in the associated note.
        :param pulumi.Input['GrafeasV1beta1DiscoveryDetailsArgs'] discovered: Describes when a resource was discovered.
        :param pulumi.Input['GrafeasV1beta1PackageDetailsArgs'] installation: Describes the installation of a package on the linked resource.
        :param pulumi.Input['GrafeasV1beta1IntotoDetailsArgs'] intoto: Describes a specific in-toto link.
        :param pulumi.Input[str] kind: This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests.
        :param pulumi.Input[str] name: The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.
        :param pulumi.Input[str] note_name: Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests.
        :param pulumi.Input[str] remediation: A description of actions that can be taken to remedy the note.
        :param pulumi.Input['ResourceArgs'] resource: Required. Immutable. The resource for which the occurrence applies.
        :param pulumi.Input[str] update_time: The time this occurrence was last updated.
        :param pulumi.Input['GrafeasV1beta1VulnerabilityDetailsArgs'] vulnerability: Describes a security vulnerability.
        """
        pulumi.set(__self__, "occurrences_id", occurrences_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if attestation is not None:
            pulumi.set(__self__, "attestation", attestation)
        if build is not None:
            pulumi.set(__self__, "build", build)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if deployment is not None:
            pulumi.set(__self__, "deployment", deployment)
        if derived_image is not None:
            pulumi.set(__self__, "derived_image", derived_image)
        if discovered is not None:
            pulumi.set(__self__, "discovered", discovered)
        if installation is not None:
            pulumi.set(__self__, "installation", installation)
        if intoto is not None:
            pulumi.set(__self__, "intoto", intoto)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if note_name is not None:
            pulumi.set(__self__, "note_name", note_name)
        if remediation is not None:
            pulumi.set(__self__, "remediation", remediation)
        if resource is not None:
            pulumi.set(__self__, "resource", resource)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)
        if vulnerability is not None:
            pulumi.set(__self__, "vulnerability", vulnerability)

    @property
    @pulumi.getter(name="occurrencesId")
    def occurrences_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "occurrences_id")

    @occurrences_id.setter
    def occurrences_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "occurrences_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter
    def attestation(self) -> Optional[pulumi.Input['DetailsArgs']]:
        """
        Describes an attestation of an artifact.
        """
        return pulumi.get(self, "attestation")

    @attestation.setter
    def attestation(self, value: Optional[pulumi.Input['DetailsArgs']]):
        pulumi.set(self, "attestation", value)

    @property
    @pulumi.getter
    def build(self) -> Optional[pulumi.Input['GrafeasV1beta1BuildDetailsArgs']]:
        """
        Describes a verifiable build.
        """
        return pulumi.get(self, "build")

    @build.setter
    def build(self, value: Optional[pulumi.Input['GrafeasV1beta1BuildDetailsArgs']]):
        pulumi.set(self, "build", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time this occurrence was created.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def deployment(self) -> Optional[pulumi.Input['GrafeasV1beta1DeploymentDetailsArgs']]:
        """
        Describes the deployment of an artifact on a runtime.
        """
        return pulumi.get(self, "deployment")

    @deployment.setter
    def deployment(self, value: Optional[pulumi.Input['GrafeasV1beta1DeploymentDetailsArgs']]):
        pulumi.set(self, "deployment", value)

    @property
    @pulumi.getter(name="derivedImage")
    def derived_image(self) -> Optional[pulumi.Input['GrafeasV1beta1ImageDetailsArgs']]:
        """
        Describes how this resource derives from the basis in the associated note.
        """
        return pulumi.get(self, "derived_image")

    @derived_image.setter
    def derived_image(self, value: Optional[pulumi.Input['GrafeasV1beta1ImageDetailsArgs']]):
        pulumi.set(self, "derived_image", value)

    @property
    @pulumi.getter
    def discovered(self) -> Optional[pulumi.Input['GrafeasV1beta1DiscoveryDetailsArgs']]:
        """
        Describes when a resource was discovered.
        """
        return pulumi.get(self, "discovered")

    @discovered.setter
    def discovered(self, value: Optional[pulumi.Input['GrafeasV1beta1DiscoveryDetailsArgs']]):
        pulumi.set(self, "discovered", value)

    @property
    @pulumi.getter
    def installation(self) -> Optional[pulumi.Input['GrafeasV1beta1PackageDetailsArgs']]:
        """
        Describes the installation of a package on the linked resource.
        """
        return pulumi.get(self, "installation")

    @installation.setter
    def installation(self, value: Optional[pulumi.Input['GrafeasV1beta1PackageDetailsArgs']]):
        pulumi.set(self, "installation", value)

    @property
    @pulumi.getter
    def intoto(self) -> Optional[pulumi.Input['GrafeasV1beta1IntotoDetailsArgs']]:
        """
        Describes a specific in-toto link.
        """
        return pulumi.get(self, "intoto")

    @intoto.setter
    def intoto(self, value: Optional[pulumi.Input['GrafeasV1beta1IntotoDetailsArgs']]):
        pulumi.set(self, "intoto", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="noteName")
    def note_name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "note_name")

    @note_name.setter
    def note_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "note_name", value)

    @property
    @pulumi.getter
    def remediation(self) -> Optional[pulumi.Input[str]]:
        """
        A description of actions that can be taken to remedy the note.
        """
        return pulumi.get(self, "remediation")

    @remediation.setter
    def remediation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remediation", value)

    @property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input['ResourceArgs']]:
        """
        Required. Immutable. The resource for which the occurrence applies.
        """
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: Optional[pulumi.Input['ResourceArgs']]):
        pulumi.set(self, "resource", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time this occurrence was last updated.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)

    @property
    @pulumi.getter
    def vulnerability(self) -> Optional[pulumi.Input['GrafeasV1beta1VulnerabilityDetailsArgs']]:
        """
        Describes a security vulnerability.
        """
        return pulumi.get(self, "vulnerability")

    @vulnerability.setter
    def vulnerability(self, value: Optional[pulumi.Input['GrafeasV1beta1VulnerabilityDetailsArgs']]):
        pulumi.set(self, "vulnerability", value)


class Occurrence(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attestation: Optional[pulumi.Input[pulumi.InputType['DetailsArgs']]] = None,
                 build: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1BuildDetailsArgs']]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 deployment: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1DeploymentDetailsArgs']]] = None,
                 derived_image: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1ImageDetailsArgs']]] = None,
                 discovered: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1DiscoveryDetailsArgs']]] = None,
                 installation: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1PackageDetailsArgs']]] = None,
                 intoto: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1IntotoDetailsArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 note_name: Optional[pulumi.Input[str]] = None,
                 occurrences_id: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 remediation: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['ResourceArgs']]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 vulnerability: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1VulnerabilityDetailsArgs']]] = None,
                 __props__=None):
        """
        Creates a new occurrence.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DetailsArgs']] attestation: Describes an attestation of an artifact.
        :param pulumi.Input[pulumi.InputType['GrafeasV1beta1BuildDetailsArgs']] build: Describes a verifiable build.
        :param pulumi.Input[str] create_time: The time this occurrence was created.
        :param pulumi.Input[pulumi.InputType['GrafeasV1beta1DeploymentDetailsArgs']] deployment: Describes the deployment of an artifact on a runtime.
        :param pulumi.Input[pulumi.InputType['GrafeasV1beta1ImageDetailsArgs']] derived_image: Describes how this resource derives from the basis in the associated note.
        :param pulumi.Input[pulumi.InputType['GrafeasV1beta1DiscoveryDetailsArgs']] discovered: Describes when a resource was discovered.
        :param pulumi.Input[pulumi.InputType['GrafeasV1beta1PackageDetailsArgs']] installation: Describes the installation of a package on the linked resource.
        :param pulumi.Input[pulumi.InputType['GrafeasV1beta1IntotoDetailsArgs']] intoto: Describes a specific in-toto link.
        :param pulumi.Input[str] kind: This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests.
        :param pulumi.Input[str] name: The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.
        :param pulumi.Input[str] note_name: Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests.
        :param pulumi.Input[str] remediation: A description of actions that can be taken to remedy the note.
        :param pulumi.Input[pulumi.InputType['ResourceArgs']] resource: Required. Immutable. The resource for which the occurrence applies.
        :param pulumi.Input[str] update_time: The time this occurrence was last updated.
        :param pulumi.Input[pulumi.InputType['GrafeasV1beta1VulnerabilityDetailsArgs']] vulnerability: Describes a security vulnerability.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OccurrenceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new occurrence.

        :param str resource_name: The name of the resource.
        :param OccurrenceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OccurrenceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attestation: Optional[pulumi.Input[pulumi.InputType['DetailsArgs']]] = None,
                 build: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1BuildDetailsArgs']]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 deployment: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1DeploymentDetailsArgs']]] = None,
                 derived_image: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1ImageDetailsArgs']]] = None,
                 discovered: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1DiscoveryDetailsArgs']]] = None,
                 installation: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1PackageDetailsArgs']]] = None,
                 intoto: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1IntotoDetailsArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 note_name: Optional[pulumi.Input[str]] = None,
                 occurrences_id: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 remediation: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['ResourceArgs']]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 vulnerability: Optional[pulumi.Input[pulumi.InputType['GrafeasV1beta1VulnerabilityDetailsArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OccurrenceArgs.__new__(OccurrenceArgs)

            __props__.__dict__["attestation"] = attestation
            __props__.__dict__["build"] = build
            __props__.__dict__["create_time"] = create_time
            __props__.__dict__["deployment"] = deployment
            __props__.__dict__["derived_image"] = derived_image
            __props__.__dict__["discovered"] = discovered
            __props__.__dict__["installation"] = installation
            __props__.__dict__["intoto"] = intoto
            __props__.__dict__["kind"] = kind
            __props__.__dict__["name"] = name
            __props__.__dict__["note_name"] = note_name
            if occurrences_id is None and not opts.urn:
                raise TypeError("Missing required property 'occurrences_id'")
            __props__.__dict__["occurrences_id"] = occurrences_id
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["remediation"] = remediation
            __props__.__dict__["resource"] = resource
            __props__.__dict__["update_time"] = update_time
            __props__.__dict__["vulnerability"] = vulnerability
        super(Occurrence, __self__).__init__(
            'gcp-native:containeranalysis/v1beta1:Occurrence',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Occurrence':
        """
        Get an existing Occurrence resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OccurrenceArgs.__new__(OccurrenceArgs)

        __props__.__dict__["attestation"] = None
        __props__.__dict__["build"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["deployment"] = None
        __props__.__dict__["derived_image"] = None
        __props__.__dict__["discovered"] = None
        __props__.__dict__["installation"] = None
        __props__.__dict__["intoto"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["note_name"] = None
        __props__.__dict__["remediation"] = None
        __props__.__dict__["resource"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["vulnerability"] = None
        return Occurrence(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attestation(self) -> pulumi.Output['outputs.DetailsResponse']:
        """
        Describes an attestation of an artifact.
        """
        return pulumi.get(self, "attestation")

    @property
    @pulumi.getter
    def build(self) -> pulumi.Output['outputs.GrafeasV1beta1BuildDetailsResponse']:
        """
        Describes a verifiable build.
        """
        return pulumi.get(self, "build")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time this occurrence was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def deployment(self) -> pulumi.Output['outputs.GrafeasV1beta1DeploymentDetailsResponse']:
        """
        Describes the deployment of an artifact on a runtime.
        """
        return pulumi.get(self, "deployment")

    @property
    @pulumi.getter(name="derivedImage")
    def derived_image(self) -> pulumi.Output['outputs.GrafeasV1beta1ImageDetailsResponse']:
        """
        Describes how this resource derives from the basis in the associated note.
        """
        return pulumi.get(self, "derived_image")

    @property
    @pulumi.getter
    def discovered(self) -> pulumi.Output['outputs.GrafeasV1beta1DiscoveryDetailsResponse']:
        """
        Describes when a resource was discovered.
        """
        return pulumi.get(self, "discovered")

    @property
    @pulumi.getter
    def installation(self) -> pulumi.Output['outputs.GrafeasV1beta1PackageDetailsResponse']:
        """
        Describes the installation of a package on the linked resource.
        """
        return pulumi.get(self, "installation")

    @property
    @pulumi.getter
    def intoto(self) -> pulumi.Output['outputs.GrafeasV1beta1IntotoDetailsResponse']:
        """
        Describes a specific in-toto link.
        """
        return pulumi.get(self, "intoto")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="noteName")
    def note_name(self) -> pulumi.Output[str]:
        """
        Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "note_name")

    @property
    @pulumi.getter
    def remediation(self) -> pulumi.Output[str]:
        """
        A description of actions that can be taken to remedy the note.
        """
        return pulumi.get(self, "remediation")

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Output['outputs.ResourceResponse']:
        """
        Required. Immutable. The resource for which the occurrence applies.
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time this occurrence was last updated.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def vulnerability(self) -> pulumi.Output['outputs.GrafeasV1beta1VulnerabilityDetailsResponse']:
        """
        Describes a security vulnerability.
        """
        return pulumi.get(self, "vulnerability")
