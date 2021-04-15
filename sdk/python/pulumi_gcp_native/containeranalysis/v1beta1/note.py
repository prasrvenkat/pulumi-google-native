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

__all__ = ['NoteArgs', 'Note']

@pulumi.input_type
class NoteArgs:
    def __init__(__self__, *,
                 notes_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 attestation_authority: Optional[pulumi.Input['AuthorityArgs']] = None,
                 base_image: Optional[pulumi.Input['BasisArgs']] = None,
                 build: Optional[pulumi.Input['BuildArgs']] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 deployable: Optional[pulumi.Input['DeployableArgs']] = None,
                 discovery: Optional[pulumi.Input['DiscoveryArgs']] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 intoto: Optional[pulumi.Input['InTotoArgs']] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 long_description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 package: Optional[pulumi.Input['PackageArgs']] = None,
                 related_note_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 related_url: Optional[pulumi.Input[Sequence[pulumi.Input['RelatedUrlArgs']]]] = None,
                 short_description: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 vulnerability: Optional[pulumi.Input['VulnerabilityArgs']] = None):
        """
        The set of arguments for constructing a Note resource.
        :param pulumi.Input['AuthorityArgs'] attestation_authority: A note describing an attestation role.
        :param pulumi.Input['BasisArgs'] base_image: A note describing a base image.
        :param pulumi.Input['BuildArgs'] build: A note describing build provenance for a verifiable build.
        :param pulumi.Input[str] create_time: The time this note was created. This field can be used as a filter in list requests.
        :param pulumi.Input['DeployableArgs'] deployable: A note describing something that can be deployed.
        :param pulumi.Input['DiscoveryArgs'] discovery: A note describing the initial analysis of a resource.
        :param pulumi.Input[str] expiration_time: Time of expiration for this note. Empty if note does not expire.
        :param pulumi.Input['InTotoArgs'] intoto: A note describing an in-toto link.
        :param pulumi.Input[str] kind: The type of analysis. This field can be used as a filter in list requests.
        :param pulumi.Input[str] long_description: A detailed description of this note.
        :param pulumi.Input[str] name: The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.
        :param pulumi.Input['PackageArgs'] package: A note describing a package hosted by various package managers.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] related_note_names: Other notes related to this note.
        :param pulumi.Input[Sequence[pulumi.Input['RelatedUrlArgs']]] related_url: URLs associated with this note.
        :param pulumi.Input[str] short_description: A one sentence description of this note.
        :param pulumi.Input[str] update_time: The time this note was last updated. This field can be used as a filter in list requests.
        :param pulumi.Input['VulnerabilityArgs'] vulnerability: A note describing a package vulnerability.
        """
        pulumi.set(__self__, "notes_id", notes_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if attestation_authority is not None:
            pulumi.set(__self__, "attestation_authority", attestation_authority)
        if base_image is not None:
            pulumi.set(__self__, "base_image", base_image)
        if build is not None:
            pulumi.set(__self__, "build", build)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if deployable is not None:
            pulumi.set(__self__, "deployable", deployable)
        if discovery is not None:
            pulumi.set(__self__, "discovery", discovery)
        if expiration_time is not None:
            pulumi.set(__self__, "expiration_time", expiration_time)
        if intoto is not None:
            pulumi.set(__self__, "intoto", intoto)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if long_description is not None:
            pulumi.set(__self__, "long_description", long_description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if package is not None:
            pulumi.set(__self__, "package", package)
        if related_note_names is not None:
            pulumi.set(__self__, "related_note_names", related_note_names)
        if related_url is not None:
            pulumi.set(__self__, "related_url", related_url)
        if short_description is not None:
            pulumi.set(__self__, "short_description", short_description)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)
        if vulnerability is not None:
            pulumi.set(__self__, "vulnerability", vulnerability)

    @property
    @pulumi.getter(name="notesId")
    def notes_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "notes_id")

    @notes_id.setter
    def notes_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "notes_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="attestationAuthority")
    def attestation_authority(self) -> Optional[pulumi.Input['AuthorityArgs']]:
        """
        A note describing an attestation role.
        """
        return pulumi.get(self, "attestation_authority")

    @attestation_authority.setter
    def attestation_authority(self, value: Optional[pulumi.Input['AuthorityArgs']]):
        pulumi.set(self, "attestation_authority", value)

    @property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> Optional[pulumi.Input['BasisArgs']]:
        """
        A note describing a base image.
        """
        return pulumi.get(self, "base_image")

    @base_image.setter
    def base_image(self, value: Optional[pulumi.Input['BasisArgs']]):
        pulumi.set(self, "base_image", value)

    @property
    @pulumi.getter
    def build(self) -> Optional[pulumi.Input['BuildArgs']]:
        """
        A note describing build provenance for a verifiable build.
        """
        return pulumi.get(self, "build")

    @build.setter
    def build(self, value: Optional[pulumi.Input['BuildArgs']]):
        pulumi.set(self, "build", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time this note was created. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def deployable(self) -> Optional[pulumi.Input['DeployableArgs']]:
        """
        A note describing something that can be deployed.
        """
        return pulumi.get(self, "deployable")

    @deployable.setter
    def deployable(self, value: Optional[pulumi.Input['DeployableArgs']]):
        pulumi.set(self, "deployable", value)

    @property
    @pulumi.getter
    def discovery(self) -> Optional[pulumi.Input['DiscoveryArgs']]:
        """
        A note describing the initial analysis of a resource.
        """
        return pulumi.get(self, "discovery")

    @discovery.setter
    def discovery(self, value: Optional[pulumi.Input['DiscoveryArgs']]):
        pulumi.set(self, "discovery", value)

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time of expiration for this note. Empty if note does not expire.
        """
        return pulumi.get(self, "expiration_time")

    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_time", value)

    @property
    @pulumi.getter
    def intoto(self) -> Optional[pulumi.Input['InTotoArgs']]:
        """
        A note describing an in-toto link.
        """
        return pulumi.get(self, "intoto")

    @intoto.setter
    def intoto(self, value: Optional[pulumi.Input['InTotoArgs']]):
        pulumi.set(self, "intoto", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The type of analysis. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> Optional[pulumi.Input[str]]:
        """
        A detailed description of this note.
        """
        return pulumi.get(self, "long_description")

    @long_description.setter
    def long_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "long_description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def package(self) -> Optional[pulumi.Input['PackageArgs']]:
        """
        A note describing a package hosted by various package managers.
        """
        return pulumi.get(self, "package")

    @package.setter
    def package(self, value: Optional[pulumi.Input['PackageArgs']]):
        pulumi.set(self, "package", value)

    @property
    @pulumi.getter(name="relatedNoteNames")
    def related_note_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Other notes related to this note.
        """
        return pulumi.get(self, "related_note_names")

    @related_note_names.setter
    def related_note_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "related_note_names", value)

    @property
    @pulumi.getter(name="relatedUrl")
    def related_url(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RelatedUrlArgs']]]]:
        """
        URLs associated with this note.
        """
        return pulumi.get(self, "related_url")

    @related_url.setter
    def related_url(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RelatedUrlArgs']]]]):
        pulumi.set(self, "related_url", value)

    @property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> Optional[pulumi.Input[str]]:
        """
        A one sentence description of this note.
        """
        return pulumi.get(self, "short_description")

    @short_description.setter
    def short_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "short_description", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time this note was last updated. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)

    @property
    @pulumi.getter
    def vulnerability(self) -> Optional[pulumi.Input['VulnerabilityArgs']]:
        """
        A note describing a package vulnerability.
        """
        return pulumi.get(self, "vulnerability")

    @vulnerability.setter
    def vulnerability(self, value: Optional[pulumi.Input['VulnerabilityArgs']]):
        pulumi.set(self, "vulnerability", value)


class Note(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attestation_authority: Optional[pulumi.Input[pulumi.InputType['AuthorityArgs']]] = None,
                 base_image: Optional[pulumi.Input[pulumi.InputType['BasisArgs']]] = None,
                 build: Optional[pulumi.Input[pulumi.InputType['BuildArgs']]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 deployable: Optional[pulumi.Input[pulumi.InputType['DeployableArgs']]] = None,
                 discovery: Optional[pulumi.Input[pulumi.InputType['DiscoveryArgs']]] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 intoto: Optional[pulumi.Input[pulumi.InputType['InTotoArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 long_description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes_id: Optional[pulumi.Input[str]] = None,
                 package: Optional[pulumi.Input[pulumi.InputType['PackageArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 related_note_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 related_url: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RelatedUrlArgs']]]]] = None,
                 short_description: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 vulnerability: Optional[pulumi.Input[pulumi.InputType['VulnerabilityArgs']]] = None,
                 __props__=None):
        """
        Creates a new note.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AuthorityArgs']] attestation_authority: A note describing an attestation role.
        :param pulumi.Input[pulumi.InputType['BasisArgs']] base_image: A note describing a base image.
        :param pulumi.Input[pulumi.InputType['BuildArgs']] build: A note describing build provenance for a verifiable build.
        :param pulumi.Input[str] create_time: The time this note was created. This field can be used as a filter in list requests.
        :param pulumi.Input[pulumi.InputType['DeployableArgs']] deployable: A note describing something that can be deployed.
        :param pulumi.Input[pulumi.InputType['DiscoveryArgs']] discovery: A note describing the initial analysis of a resource.
        :param pulumi.Input[str] expiration_time: Time of expiration for this note. Empty if note does not expire.
        :param pulumi.Input[pulumi.InputType['InTotoArgs']] intoto: A note describing an in-toto link.
        :param pulumi.Input[str] kind: The type of analysis. This field can be used as a filter in list requests.
        :param pulumi.Input[str] long_description: A detailed description of this note.
        :param pulumi.Input[str] name: The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.
        :param pulumi.Input[pulumi.InputType['PackageArgs']] package: A note describing a package hosted by various package managers.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] related_note_names: Other notes related to this note.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RelatedUrlArgs']]]] related_url: URLs associated with this note.
        :param pulumi.Input[str] short_description: A one sentence description of this note.
        :param pulumi.Input[str] update_time: The time this note was last updated. This field can be used as a filter in list requests.
        :param pulumi.Input[pulumi.InputType['VulnerabilityArgs']] vulnerability: A note describing a package vulnerability.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NoteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new note.

        :param str resource_name: The name of the resource.
        :param NoteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NoteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attestation_authority: Optional[pulumi.Input[pulumi.InputType['AuthorityArgs']]] = None,
                 base_image: Optional[pulumi.Input[pulumi.InputType['BasisArgs']]] = None,
                 build: Optional[pulumi.Input[pulumi.InputType['BuildArgs']]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 deployable: Optional[pulumi.Input[pulumi.InputType['DeployableArgs']]] = None,
                 discovery: Optional[pulumi.Input[pulumi.InputType['DiscoveryArgs']]] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 intoto: Optional[pulumi.Input[pulumi.InputType['InTotoArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 long_description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes_id: Optional[pulumi.Input[str]] = None,
                 package: Optional[pulumi.Input[pulumi.InputType['PackageArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 related_note_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 related_url: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RelatedUrlArgs']]]]] = None,
                 short_description: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 vulnerability: Optional[pulumi.Input[pulumi.InputType['VulnerabilityArgs']]] = None,
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
            __props__ = NoteArgs.__new__(NoteArgs)

            __props__.__dict__["attestation_authority"] = attestation_authority
            __props__.__dict__["base_image"] = base_image
            __props__.__dict__["build"] = build
            __props__.__dict__["create_time"] = create_time
            __props__.__dict__["deployable"] = deployable
            __props__.__dict__["discovery"] = discovery
            __props__.__dict__["expiration_time"] = expiration_time
            __props__.__dict__["intoto"] = intoto
            __props__.__dict__["kind"] = kind
            __props__.__dict__["long_description"] = long_description
            __props__.__dict__["name"] = name
            if notes_id is None and not opts.urn:
                raise TypeError("Missing required property 'notes_id'")
            __props__.__dict__["notes_id"] = notes_id
            __props__.__dict__["package"] = package
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["related_note_names"] = related_note_names
            __props__.__dict__["related_url"] = related_url
            __props__.__dict__["short_description"] = short_description
            __props__.__dict__["update_time"] = update_time
            __props__.__dict__["vulnerability"] = vulnerability
        super(Note, __self__).__init__(
            'gcp-native:containeranalysis/v1beta1:Note',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Note':
        """
        Get an existing Note resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NoteArgs.__new__(NoteArgs)

        __props__.__dict__["attestation_authority"] = None
        __props__.__dict__["base_image"] = None
        __props__.__dict__["build"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["deployable"] = None
        __props__.__dict__["discovery"] = None
        __props__.__dict__["expiration_time"] = None
        __props__.__dict__["intoto"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["long_description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["package"] = None
        __props__.__dict__["related_note_names"] = None
        __props__.__dict__["related_url"] = None
        __props__.__dict__["short_description"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["vulnerability"] = None
        return Note(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attestationAuthority")
    def attestation_authority(self) -> pulumi.Output['outputs.AuthorityResponse']:
        """
        A note describing an attestation role.
        """
        return pulumi.get(self, "attestation_authority")

    @property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> pulumi.Output['outputs.BasisResponse']:
        """
        A note describing a base image.
        """
        return pulumi.get(self, "base_image")

    @property
    @pulumi.getter
    def build(self) -> pulumi.Output['outputs.BuildResponse']:
        """
        A note describing build provenance for a verifiable build.
        """
        return pulumi.get(self, "build")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time this note was created. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def deployable(self) -> pulumi.Output['outputs.DeployableResponse']:
        """
        A note describing something that can be deployed.
        """
        return pulumi.get(self, "deployable")

    @property
    @pulumi.getter
    def discovery(self) -> pulumi.Output['outputs.DiscoveryResponse']:
        """
        A note describing the initial analysis of a resource.
        """
        return pulumi.get(self, "discovery")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[str]:
        """
        Time of expiration for this note. Empty if note does not expire.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter
    def intoto(self) -> pulumi.Output['outputs.InTotoResponse']:
        """
        A note describing an in-toto link.
        """
        return pulumi.get(self, "intoto")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The type of analysis. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> pulumi.Output[str]:
        """
        A detailed description of this note.
        """
        return pulumi.get(self, "long_description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def package(self) -> pulumi.Output['outputs.PackageResponse']:
        """
        A note describing a package hosted by various package managers.
        """
        return pulumi.get(self, "package")

    @property
    @pulumi.getter(name="relatedNoteNames")
    def related_note_names(self) -> pulumi.Output[Sequence[str]]:
        """
        Other notes related to this note.
        """
        return pulumi.get(self, "related_note_names")

    @property
    @pulumi.getter(name="relatedUrl")
    def related_url(self) -> pulumi.Output[Sequence['outputs.RelatedUrlResponse']]:
        """
        URLs associated with this note.
        """
        return pulumi.get(self, "related_url")

    @property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> pulumi.Output[str]:
        """
        A one sentence description of this note.
        """
        return pulumi.get(self, "short_description")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time this note was last updated. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def vulnerability(self) -> pulumi.Output['outputs.VulnerabilityResponse']:
        """
        A note describing a package vulnerability.
        """
        return pulumi.get(self, "vulnerability")
