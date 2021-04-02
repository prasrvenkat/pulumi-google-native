# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'BindingArgs',
    'ExprArgs',
    'GoogleCloudDatacatalogV1beta1BigQueryDateShardedSpecArgs',
    'GoogleCloudDatacatalogV1beta1BigQueryTableSpecArgs',
    'GoogleCloudDatacatalogV1beta1ColumnSchemaArgs',
    'GoogleCloudDatacatalogV1beta1FieldTypeArgs',
    'GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeArgs',
    'GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeEnumValueArgs',
    'GoogleCloudDatacatalogV1beta1GcsFilesetSpecArgs',
    'GoogleCloudDatacatalogV1beta1SchemaArgs',
    'GoogleCloudDatacatalogV1beta1TableSpecArgs',
    'GoogleCloudDatacatalogV1beta1ViewSpecArgs',
    'PolicyArgs',
]

@pulumi.input_type
class BindingArgs:
    def __init__(__self__, *,
                 condition: Optional[pulumi.Input['ExprArgs']] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None):
        """
        Associates `members` with a `role`.
        :param pulumi.Input['ExprArgs'] condition: The condition that is associated with this binding. If the condition evaluates to `true`, then this binding applies to the current request. If the condition evaluates to `false`, then this binding does not apply to the current request. However, a different role binding might grant the same role to one or more of the members in this binding. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: Specifies the identities requesting access for a Cloud Platform resource. `members` can have the following values: * `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account. * `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account. * `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@example.com` . * `serviceAccount:{emailid}`: An email address that represents a service account. For example, `my-other-app@appspot.gserviceaccount.com`. * `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`. * `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:{emailid}` and the recovered user retains the role in the binding. * `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:{emailid}` and the undeleted service account retains the role in the binding. * `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:{emailid}` and the recovered group retains the role in the binding. * `domain:{domain}`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`. 
        :param pulumi.Input[str] role: Role that is assigned to `members`. For example, `roles/viewer`, `roles/editor`, or `roles/owner`.
        """
        if condition is not None:
            pulumi.set(__self__, "condition", condition)
        if members is not None:
            pulumi.set(__self__, "members", members)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input['ExprArgs']]:
        """
        The condition that is associated with this binding. If the condition evaluates to `true`, then this binding applies to the current request. If the condition evaluates to `false`, then this binding does not apply to the current request. However, a different role binding might grant the same role to one or more of the members in this binding. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
        """
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input['ExprArgs']]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the identities requesting access for a Cloud Platform resource. `members` can have the following values: * `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account. * `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account. * `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@example.com` . * `serviceAccount:{emailid}`: An email address that represents a service account. For example, `my-other-app@appspot.gserviceaccount.com`. * `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`. * `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:{emailid}` and the recovered user retains the role in the binding. * `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:{emailid}` and the undeleted service account retains the role in the binding. * `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:{emailid}` and the recovered group retains the role in the binding. * `domain:{domain}`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`. 
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        Role that is assigned to `members`. For example, `roles/viewer`, `roles/editor`, or `roles/owner`.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)


@pulumi.input_type
class ExprArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at https://github.com/google/cel-spec. Example (Comparison): title: "Summary size limit" description: "Determines if a summary is less than 100 chars" expression: "document.summary.size() < 100" Example (Equality): title: "Requestor is owner" description: "Determines if requestor is the document owner" expression: "document.owner == request.auth.claims.email" Example (Logic): title: "Public documents" description: "Determine whether the document should be publicly visible" expression: "document.type != 'private' && document.type != 'internal'" Example (Data Manipulation): title: "Notification string" description: "Create a notification string with a timestamp." expression: "'New message received at ' + string(document.create_time)" The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information.
        :param pulumi.Input[str] description: Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
        :param pulumi.Input[str] expression: Textual representation of an expression in Common Expression Language syntax.
        :param pulumi.Input[str] location: Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.
        :param pulumi.Input[str] title: Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[str]]:
        """
        Textual representation of an expression in Common Expression Language syntax.
        """
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


@pulumi.input_type
class GoogleCloudDatacatalogV1beta1BigQueryDateShardedSpecArgs:
    def __init__(__self__):
        """
        Spec for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding
        """
        pass


@pulumi.input_type
class GoogleCloudDatacatalogV1beta1BigQueryTableSpecArgs:
    def __init__(__self__, *,
                 table_spec: Optional[pulumi.Input['GoogleCloudDatacatalogV1beta1TableSpecArgs']] = None,
                 view_spec: Optional[pulumi.Input['GoogleCloudDatacatalogV1beta1ViewSpecArgs']] = None):
        """
        Describes a BigQuery table.
        :param pulumi.Input['GoogleCloudDatacatalogV1beta1TableSpecArgs'] table_spec: Spec of a BigQuery table. This field should only be populated if `table_source_type` is `BIGQUERY_TABLE`.
        :param pulumi.Input['GoogleCloudDatacatalogV1beta1ViewSpecArgs'] view_spec: Table view specification. This field should only be populated if `table_source_type` is `BIGQUERY_VIEW`.
        """
        if table_spec is not None:
            pulumi.set(__self__, "table_spec", table_spec)
        if view_spec is not None:
            pulumi.set(__self__, "view_spec", view_spec)

    @property
    @pulumi.getter(name="tableSpec")
    def table_spec(self) -> Optional[pulumi.Input['GoogleCloudDatacatalogV1beta1TableSpecArgs']]:
        """
        Spec of a BigQuery table. This field should only be populated if `table_source_type` is `BIGQUERY_TABLE`.
        """
        return pulumi.get(self, "table_spec")

    @table_spec.setter
    def table_spec(self, value: Optional[pulumi.Input['GoogleCloudDatacatalogV1beta1TableSpecArgs']]):
        pulumi.set(self, "table_spec", value)

    @property
    @pulumi.getter(name="viewSpec")
    def view_spec(self) -> Optional[pulumi.Input['GoogleCloudDatacatalogV1beta1ViewSpecArgs']]:
        """
        Table view specification. This field should only be populated if `table_source_type` is `BIGQUERY_VIEW`.
        """
        return pulumi.get(self, "view_spec")

    @view_spec.setter
    def view_spec(self, value: Optional[pulumi.Input['GoogleCloudDatacatalogV1beta1ViewSpecArgs']]):
        pulumi.set(self, "view_spec", value)


@pulumi.input_type
class GoogleCloudDatacatalogV1beta1ColumnSchemaArgs:
    def __init__(__self__, *,
                 column: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 subcolumns: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDatacatalogV1beta1ColumnSchemaArgs']]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Representation of a column within a schema. Columns could be nested inside other columns.
        :param pulumi.Input[str] column: Required. Name of the column.
        :param pulumi.Input[str] description: Optional. Description of the column. Default value is an empty string.
        :param pulumi.Input[str] mode: Optional. A column's mode indicates whether the values in this column are required, nullable, etc. Only `NULLABLE`, `REQUIRED` and `REPEATED` are supported. Default mode is `NULLABLE`.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudDatacatalogV1beta1ColumnSchemaArgs']]] subcolumns: Optional. Schema of sub-columns. A column can have zero or more sub-columns.
        :param pulumi.Input[str] type: Required. Type of the column.
        """
        if column is not None:
            pulumi.set(__self__, "column", column)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if subcolumns is not None:
            pulumi.set(__self__, "subcolumns", subcolumns)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Name of the column.
        """
        return pulumi.get(self, "column")

    @column.setter
    def column(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "column", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Description of the column. Default value is an empty string.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A column's mode indicates whether the values in this column are required, nullable, etc. Only `NULLABLE`, `REQUIRED` and `REPEATED` are supported. Default mode is `NULLABLE`.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def subcolumns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDatacatalogV1beta1ColumnSchemaArgs']]]]:
        """
        Optional. Schema of sub-columns. A column can have zero or more sub-columns.
        """
        return pulumi.get(self, "subcolumns")

    @subcolumns.setter
    def subcolumns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDatacatalogV1beta1ColumnSchemaArgs']]]]):
        pulumi.set(self, "subcolumns", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Type of the column.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class GoogleCloudDatacatalogV1beta1FieldTypeArgs:
    def __init__(__self__, *,
                 enum_type: Optional[pulumi.Input['GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeArgs']] = None,
                 primitive_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input['GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeArgs'] enum_type: Represents an enum type.
        :param pulumi.Input[str] primitive_type: Represents primitive types - string, bool etc.
        """
        if enum_type is not None:
            pulumi.set(__self__, "enum_type", enum_type)
        if primitive_type is not None:
            pulumi.set(__self__, "primitive_type", primitive_type)

    @property
    @pulumi.getter(name="enumType")
    def enum_type(self) -> Optional[pulumi.Input['GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeArgs']]:
        """
        Represents an enum type.
        """
        return pulumi.get(self, "enum_type")

    @enum_type.setter
    def enum_type(self, value: Optional[pulumi.Input['GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeArgs']]):
        pulumi.set(self, "enum_type", value)

    @property
    @pulumi.getter(name="primitiveType")
    def primitive_type(self) -> Optional[pulumi.Input[str]]:
        """
        Represents primitive types - string, bool etc.
        """
        return pulumi.get(self, "primitive_type")

    @primitive_type.setter
    def primitive_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primitive_type", value)


@pulumi.input_type
class GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeArgs:
    def __init__(__self__, *,
                 allowed_values: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeEnumValueArgs']]]] = None):
        if allowed_values is not None:
            pulumi.set(__self__, "allowed_values", allowed_values)

    @property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeEnumValueArgs']]]]:
        return pulumi.get(self, "allowed_values")

    @allowed_values.setter
    def allowed_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeEnumValueArgs']]]]):
        pulumi.set(self, "allowed_values", value)


@pulumi.input_type
class GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeEnumValueArgs:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] display_name: Required. The display name of the enum value. Must not be an empty string.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The display name of the enum value. Must not be an empty string.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)


@pulumi.input_type
class GoogleCloudDatacatalogV1beta1GcsFilesetSpecArgs:
    def __init__(__self__, *,
                 file_patterns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Describes a Cloud Storage fileset entry.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] file_patterns: Required. Patterns to identify a set of files in Google Cloud Storage. See [Cloud Storage documentation](https://cloud.google.com/storage/docs/gsutil/addlhelp/WildcardNames) for more information. Note that bucket wildcards are currently not supported. Examples of valid file_patterns: * `gs://bucket_name/dir/*`: matches all files within `bucket_name/dir` directory. * `gs://bucket_name/dir/**`: matches all files in `bucket_name/dir` spanning all subdirectories. * `gs://bucket_name/file*`: matches files prefixed by `file` in `bucket_name` * `gs://bucket_name/??.txt`: matches files with two characters followed by `.txt` in `bucket_name` * `gs://bucket_name/[aeiou].txt`: matches files that contain a single vowel character followed by `.txt` in `bucket_name` * `gs://bucket_name/[a-m].txt`: matches files that contain `a`, `b`, ... or `m` followed by `.txt` in `bucket_name` * `gs://bucket_name/a/*/b`: matches all files in `bucket_name` that match `a/*/b` pattern, such as `a/c/b`, `a/d/b` * `gs://another_bucket/a.txt`: matches `gs://another_bucket/a.txt` You can combine wildcards to provide more powerful matches, for example: * `gs://bucket_name/[a-m]??.j*g`
        """
        if file_patterns is not None:
            pulumi.set(__self__, "file_patterns", file_patterns)

    @property
    @pulumi.getter(name="filePatterns")
    def file_patterns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Required. Patterns to identify a set of files in Google Cloud Storage. See [Cloud Storage documentation](https://cloud.google.com/storage/docs/gsutil/addlhelp/WildcardNames) for more information. Note that bucket wildcards are currently not supported. Examples of valid file_patterns: * `gs://bucket_name/dir/*`: matches all files within `bucket_name/dir` directory. * `gs://bucket_name/dir/**`: matches all files in `bucket_name/dir` spanning all subdirectories. * `gs://bucket_name/file*`: matches files prefixed by `file` in `bucket_name` * `gs://bucket_name/??.txt`: matches files with two characters followed by `.txt` in `bucket_name` * `gs://bucket_name/[aeiou].txt`: matches files that contain a single vowel character followed by `.txt` in `bucket_name` * `gs://bucket_name/[a-m].txt`: matches files that contain `a`, `b`, ... or `m` followed by `.txt` in `bucket_name` * `gs://bucket_name/a/*/b`: matches all files in `bucket_name` that match `a/*/b` pattern, such as `a/c/b`, `a/d/b` * `gs://another_bucket/a.txt`: matches `gs://another_bucket/a.txt` You can combine wildcards to provide more powerful matches, for example: * `gs://bucket_name/[a-m]??.j*g`
        """
        return pulumi.get(self, "file_patterns")

    @file_patterns.setter
    def file_patterns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "file_patterns", value)


@pulumi.input_type
class GoogleCloudDatacatalogV1beta1SchemaArgs:
    def __init__(__self__, *,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDatacatalogV1beta1ColumnSchemaArgs']]]] = None):
        """
        Represents a schema (e.g. BigQuery, GoogleSQL, Avro schema).
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudDatacatalogV1beta1ColumnSchemaArgs']]] columns: Required. Schema of columns. A maximum of 10,000 columns and sub-columns can be specified.
        """
        if columns is not None:
            pulumi.set(__self__, "columns", columns)

    @property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDatacatalogV1beta1ColumnSchemaArgs']]]]:
        """
        Required. Schema of columns. A maximum of 10,000 columns and sub-columns can be specified.
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDatacatalogV1beta1ColumnSchemaArgs']]]]):
        pulumi.set(self, "columns", value)


@pulumi.input_type
class GoogleCloudDatacatalogV1beta1TableSpecArgs:
    def __init__(__self__):
        """
        Normal BigQuery table spec.
        """
        pass


@pulumi.input_type
class GoogleCloudDatacatalogV1beta1ViewSpecArgs:
    def __init__(__self__):
        """
        Table view specification.
        """
        pass


@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *,
                 bindings: Optional[pulumi.Input[Sequence[pulumi.Input['BindingArgs']]]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions; each `role` can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a `binding` can also specify a `condition`, which is a logical expression that allows access to a resource only if the expression evaluates to `true`. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag": "BwWWja0YfJA=", "version": 3 } **YAML example:** bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01T00:00:00.000Z') - etag: BwWWja0YfJA= - version: 3 For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).
        :param pulumi.Input[Sequence[pulumi.Input['BindingArgs']]] bindings: Associates a list of `members` to a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one member.
        :param pulumi.Input[str] etag: `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy. **Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.
        :param pulumi.Input[int] version: Specifies the format of the policy. Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected. Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations: * Getting a policy that includes a conditional role binding * Adding a conditional role binding to a policy * Changing a conditional role binding in a policy * Removing any role binding, with or without a condition, from a policy that includes conditions **Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost. If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
        """
        if bindings is not None:
            pulumi.set(__self__, "bindings", bindings)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def bindings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BindingArgs']]]]:
        """
        Associates a list of `members` to a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one member.
        """
        return pulumi.get(self, "bindings")

    @bindings.setter
    def bindings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BindingArgs']]]]):
        pulumi.set(self, "bindings", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy. **Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the format of the policy. Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected. Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations: * Getting a policy that includes a conditional role binding * Adding a conditional role binding to a policy * Changing a conditional role binding in a policy * Removing any role binding, with or without a condition, from a policy that includes conditions **Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost. If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)

