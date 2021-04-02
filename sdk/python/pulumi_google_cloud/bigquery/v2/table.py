# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Table']


class Table(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 clustering: Optional[pulumi.Input[pulumi.InputType['ClusteringArgs']]] = None,
                 creation_time: Optional[pulumi.Input[str]] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encryption_configuration: Optional[pulumi.Input[pulumi.InputType['EncryptionConfigurationArgs']]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 external_data_configuration: Optional[pulumi.Input[pulumi.InputType['ExternalDataConfigurationArgs']]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 last_modified_time: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 materialized_view: Optional[pulumi.Input[pulumi.InputType['MaterializedViewDefinitionArgs']]] = None,
                 model: Optional[pulumi.Input[pulumi.InputType['ModelDefinitionArgs']]] = None,
                 num_bytes: Optional[pulumi.Input[str]] = None,
                 num_long_term_bytes: Optional[pulumi.Input[str]] = None,
                 num_physical_bytes: Optional[pulumi.Input[str]] = None,
                 num_rows: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 range_partitioning: Optional[pulumi.Input[pulumi.InputType['RangePartitioningArgs']]] = None,
                 require_partition_filter: Optional[pulumi.Input[bool]] = None,
                 schema: Optional[pulumi.Input[pulumi.InputType['TableSchemaArgs']]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 snapshot_definition: Optional[pulumi.Input[pulumi.InputType['SnapshotDefinitionArgs']]] = None,
                 streaming_buffer: Optional[pulumi.Input[pulumi.InputType['StreamingbufferArgs']]] = None,
                 table_id: Optional[pulumi.Input[str]] = None,
                 table_reference: Optional[pulumi.Input[pulumi.InputType['TableReferenceArgs']]] = None,
                 time_partitioning: Optional[pulumi.Input[pulumi.InputType['TimePartitioningArgs']]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 view: Optional[pulumi.Input[pulumi.InputType['ViewDefinitionArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new, empty table in the dataset.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ClusteringArgs']] clustering: [Beta] Clustering specification for the table. Must be specified with partitioning, data in the table will be first partitioned and subsequently clustered.
        :param pulumi.Input[str] creation_time: [Output-only] The time when this table was created, in milliseconds since the epoch.
        :param pulumi.Input[str] description: [Optional] A user-friendly description of this table.
        :param pulumi.Input[pulumi.InputType['EncryptionConfigurationArgs']] encryption_configuration: Custom encryption configuration (e.g., Cloud KMS keys).
        :param pulumi.Input[str] etag: [Output-only] A hash of the table metadata. Used to ensure there were no concurrent modifications to the resource when attempting an update. Not guaranteed to change when the table contents or the fields numRows, numBytes, numLongTermBytes or lastModifiedTime change.
        :param pulumi.Input[str] expiration_time: [Optional] The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. The defaultTableExpirationMs property of the encapsulating dataset can be used to set a default expirationTime on newly created tables.
        :param pulumi.Input[pulumi.InputType['ExternalDataConfigurationArgs']] external_data_configuration: [Optional] Describes the data format, location, and other properties of a table stored outside of BigQuery. By defining these properties, the data source can then be queried as if it were a standard BigQuery table.
        :param pulumi.Input[str] friendly_name: [Optional] A descriptive name for this table.
        :param pulumi.Input[str] id: [Output-only] An opaque ID uniquely identifying the table.
        :param pulumi.Input[str] kind: [Output-only] The type of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels associated with this table. You can use these to organize and group your tables. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key.
        :param pulumi.Input[str] last_modified_time: [Output-only] The time when this table was last modified, in milliseconds since the epoch.
        :param pulumi.Input[str] location: [Output-only] The geographic location where the table resides. This value is inherited from the dataset.
        :param pulumi.Input[pulumi.InputType['MaterializedViewDefinitionArgs']] materialized_view: [Optional] Materialized view definition.
        :param pulumi.Input[pulumi.InputType['ModelDefinitionArgs']] model: [Output-only, Beta] Present iff this table represents a ML model. Describes the training information for the model, and it is required to run 'PREDICT' queries.
        :param pulumi.Input[str] num_bytes: [Output-only] The size of this table in bytes, excluding any data in the streaming buffer.
        :param pulumi.Input[str] num_long_term_bytes: [Output-only] The number of bytes in the table that are considered "long-term storage".
        :param pulumi.Input[str] num_physical_bytes: [Output-only] [TrustedTester] The physical size of this table in bytes, excluding any data in the streaming buffer. This includes compression and storage used for time travel.
        :param pulumi.Input[str] num_rows: [Output-only] The number of rows of data in this table, excluding any data in the streaming buffer.
        :param pulumi.Input[pulumi.InputType['RangePartitioningArgs']] range_partitioning: [TrustedTester] Range partitioning specification for this table. Only one of timePartitioning and rangePartitioning should be specified.
        :param pulumi.Input[bool] require_partition_filter: [Optional] If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified.
        :param pulumi.Input[pulumi.InputType['TableSchemaArgs']] schema: [Optional] Describes the schema of this table.
        :param pulumi.Input[str] self_link: [Output-only] A URL that can be used to access this resource again.
        :param pulumi.Input[pulumi.InputType['SnapshotDefinitionArgs']] snapshot_definition: [Output-only] Snapshot definition.
        :param pulumi.Input[pulumi.InputType['StreamingbufferArgs']] streaming_buffer: [Output-only] Contains information regarding this table's streaming buffer, if one is present. This field will be absent if the table is not being streamed to or if there is no data in the streaming buffer.
        :param pulumi.Input[pulumi.InputType['TableReferenceArgs']] table_reference: [Required] Reference describing the ID of this table.
        :param pulumi.Input[pulumi.InputType['TimePartitioningArgs']] time_partitioning: Time-based partitioning specification for this table. Only one of timePartitioning and rangePartitioning should be specified.
        :param pulumi.Input[str] type: [Output-only] Describes the table type. The following values are supported: TABLE: A normal BigQuery table. VIEW: A virtual table defined by a SQL query. SNAPSHOT: An immutable, read-only table that is a copy of another table. [TrustedTester] MATERIALIZED_VIEW: SQL query whose result is persisted. EXTERNAL: A table that references data stored in an external storage system, such as Google Cloud Storage. The default value is TABLE.
        :param pulumi.Input[pulumi.InputType['ViewDefinitionArgs']] view: [Optional] The view definition.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['clustering'] = clustering
            __props__['creation_time'] = creation_time
            if dataset_id is None and not opts.urn:
                raise TypeError("Missing required property 'dataset_id'")
            __props__['dataset_id'] = dataset_id
            __props__['description'] = description
            __props__['encryption_configuration'] = encryption_configuration
            __props__['etag'] = etag
            __props__['expiration_time'] = expiration_time
            __props__['external_data_configuration'] = external_data_configuration
            __props__['friendly_name'] = friendly_name
            __props__['id'] = id
            __props__['kind'] = kind
            __props__['labels'] = labels
            __props__['last_modified_time'] = last_modified_time
            __props__['location'] = location
            __props__['materialized_view'] = materialized_view
            __props__['model'] = model
            __props__['num_bytes'] = num_bytes
            __props__['num_long_term_bytes'] = num_long_term_bytes
            __props__['num_physical_bytes'] = num_physical_bytes
            __props__['num_rows'] = num_rows
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            __props__['range_partitioning'] = range_partitioning
            __props__['require_partition_filter'] = require_partition_filter
            __props__['schema'] = schema
            __props__['self_link'] = self_link
            __props__['snapshot_definition'] = snapshot_definition
            __props__['streaming_buffer'] = streaming_buffer
            if table_id is None and not opts.urn:
                raise TypeError("Missing required property 'table_id'")
            __props__['table_id'] = table_id
            __props__['table_reference'] = table_reference
            __props__['time_partitioning'] = time_partitioning
            __props__['type'] = type
            __props__['view'] = view
        super(Table, __self__).__init__(
            'google-cloud:bigquery/v2:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["clustering"] = None
        __props__["creation_time"] = None
        __props__["description"] = None
        __props__["encryption_configuration"] = None
        __props__["etag"] = None
        __props__["expiration_time"] = None
        __props__["external_data_configuration"] = None
        __props__["friendly_name"] = None
        __props__["kind"] = None
        __props__["labels"] = None
        __props__["last_modified_time"] = None
        __props__["location"] = None
        __props__["materialized_view"] = None
        __props__["model"] = None
        __props__["num_bytes"] = None
        __props__["num_long_term_bytes"] = None
        __props__["num_physical_bytes"] = None
        __props__["num_rows"] = None
        __props__["range_partitioning"] = None
        __props__["require_partition_filter"] = None
        __props__["schema"] = None
        __props__["self_link"] = None
        __props__["snapshot_definition"] = None
        __props__["streaming_buffer"] = None
        __props__["table_reference"] = None
        __props__["time_partitioning"] = None
        __props__["type"] = None
        __props__["view"] = None
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def clustering(self) -> pulumi.Output['outputs.ClusteringResponse']:
        """
        [Beta] Clustering specification for the table. Must be specified with partitioning, data in the table will be first partitioned and subsequently clustered.
        """
        return pulumi.get(self, "clustering")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        [Output-only] The time when this table was created, in milliseconds since the epoch.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        [Optional] A user-friendly description of this table.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> pulumi.Output['outputs.EncryptionConfigurationResponse']:
        """
        Custom encryption configuration (e.g., Cloud KMS keys).
        """
        return pulumi.get(self, "encryption_configuration")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        [Output-only] A hash of the table metadata. Used to ensure there were no concurrent modifications to the resource when attempting an update. Not guaranteed to change when the table contents or the fields numRows, numBytes, numLongTermBytes or lastModifiedTime change.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[str]:
        """
        [Optional] The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. The defaultTableExpirationMs property of the encapsulating dataset can be used to set a default expirationTime on newly created tables.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter(name="externalDataConfiguration")
    def external_data_configuration(self) -> pulumi.Output['outputs.ExternalDataConfigurationResponse']:
        """
        [Optional] Describes the data format, location, and other properties of a table stored outside of BigQuery. By defining these properties, the data source can then be queried as if it were a standard BigQuery table.
        """
        return pulumi.get(self, "external_data_configuration")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[str]:
        """
        [Optional] A descriptive name for this table.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output-only] The type of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The labels associated with this table. You can use these to organize and group your tables. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        """
        [Output-only] The time when this table was last modified, in milliseconds since the epoch.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        [Output-only] The geographic location where the table resides. This value is inherited from the dataset.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="materializedView")
    def materialized_view(self) -> pulumi.Output['outputs.MaterializedViewDefinitionResponse']:
        """
        [Optional] Materialized view definition.
        """
        return pulumi.get(self, "materialized_view")

    @property
    @pulumi.getter
    def model(self) -> pulumi.Output['outputs.ModelDefinitionResponse']:
        """
        [Output-only, Beta] Present iff this table represents a ML model. Describes the training information for the model, and it is required to run 'PREDICT' queries.
        """
        return pulumi.get(self, "model")

    @property
    @pulumi.getter(name="numBytes")
    def num_bytes(self) -> pulumi.Output[str]:
        """
        [Output-only] The size of this table in bytes, excluding any data in the streaming buffer.
        """
        return pulumi.get(self, "num_bytes")

    @property
    @pulumi.getter(name="numLongTermBytes")
    def num_long_term_bytes(self) -> pulumi.Output[str]:
        """
        [Output-only] The number of bytes in the table that are considered "long-term storage".
        """
        return pulumi.get(self, "num_long_term_bytes")

    @property
    @pulumi.getter(name="numPhysicalBytes")
    def num_physical_bytes(self) -> pulumi.Output[str]:
        """
        [Output-only] [TrustedTester] The physical size of this table in bytes, excluding any data in the streaming buffer. This includes compression and storage used for time travel.
        """
        return pulumi.get(self, "num_physical_bytes")

    @property
    @pulumi.getter(name="numRows")
    def num_rows(self) -> pulumi.Output[str]:
        """
        [Output-only] The number of rows of data in this table, excluding any data in the streaming buffer.
        """
        return pulumi.get(self, "num_rows")

    @property
    @pulumi.getter(name="rangePartitioning")
    def range_partitioning(self) -> pulumi.Output['outputs.RangePartitioningResponse']:
        """
        [TrustedTester] Range partitioning specification for this table. Only one of timePartitioning and rangePartitioning should be specified.
        """
        return pulumi.get(self, "range_partitioning")

    @property
    @pulumi.getter(name="requirePartitionFilter")
    def require_partition_filter(self) -> pulumi.Output[bool]:
        """
        [Optional] If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified.
        """
        return pulumi.get(self, "require_partition_filter")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output['outputs.TableSchemaResponse']:
        """
        [Optional] Describes the schema of this table.
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        [Output-only] A URL that can be used to access this resource again.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="snapshotDefinition")
    def snapshot_definition(self) -> pulumi.Output['outputs.SnapshotDefinitionResponse']:
        """
        [Output-only] Snapshot definition.
        """
        return pulumi.get(self, "snapshot_definition")

    @property
    @pulumi.getter(name="streamingBuffer")
    def streaming_buffer(self) -> pulumi.Output['outputs.StreamingbufferResponse']:
        """
        [Output-only] Contains information regarding this table's streaming buffer, if one is present. This field will be absent if the table is not being streamed to or if there is no data in the streaming buffer.
        """
        return pulumi.get(self, "streaming_buffer")

    @property
    @pulumi.getter(name="tableReference")
    def table_reference(self) -> pulumi.Output['outputs.TableReferenceResponse']:
        """
        [Required] Reference describing the ID of this table.
        """
        return pulumi.get(self, "table_reference")

    @property
    @pulumi.getter(name="timePartitioning")
    def time_partitioning(self) -> pulumi.Output['outputs.TimePartitioningResponse']:
        """
        Time-based partitioning specification for this table. Only one of timePartitioning and rangePartitioning should be specified.
        """
        return pulumi.get(self, "time_partitioning")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        [Output-only] Describes the table type. The following values are supported: TABLE: A normal BigQuery table. VIEW: A virtual table defined by a SQL query. SNAPSHOT: An immutable, read-only table that is a copy of another table. [TrustedTester] MATERIALIZED_VIEW: SQL query whose result is persisted. EXTERNAL: A table that references data stored in an external storage system, such as Google Cloud Storage. The default value is TABLE.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def view(self) -> pulumi.Output['outputs.ViewDefinitionResponse']:
        """
        [Optional] The view definition.
        """
        return pulumi.get(self, "view")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
