# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetTableResult',
    'AwaitableGetTableResult',
    'get_table',
    'get_table_output',
]

@pulumi.output_type
class GetTableResult:
    def __init__(__self__, create_time=None, delete_time=None, etag=None, expire_time=None, hive_options=None, name=None, type=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if delete_time and not isinstance(delete_time, str):
            raise TypeError("Expected argument 'delete_time' to be a str")
        pulumi.set(__self__, "delete_time", delete_time)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if expire_time and not isinstance(expire_time, str):
            raise TypeError("Expected argument 'expire_time' to be a str")
        pulumi.set(__self__, "expire_time", expire_time)
        if hive_options and not isinstance(hive_options, dict):
            raise TypeError("Expected argument 'hive_options' to be a dict")
        pulumi.set(__self__, "hive_options", hive_options)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The creation time of the table.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> str:
        """
        The deletion time of the table. Only set after the table is deleted.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        The checksum of a table object computed by the server based on the value of other fields. It may be sent on update requests to ensure the client has an up-to-date value before proceeding. It is only checked for update table operations.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> str:
        """
        The time when this table is considered expired. Only set after the table is deleted.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter(name="hiveOptions")
    def hive_options(self) -> 'outputs.HiveTableOptionsResponse':
        """
        Options of a Hive table.
        """
        return pulumi.get(self, "hive_options")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The table type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The last modification time of the table.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetTableResult(GetTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTableResult(
            create_time=self.create_time,
            delete_time=self.delete_time,
            etag=self.etag,
            expire_time=self.expire_time,
            hive_options=self.hive_options,
            name=self.name,
            type=self.type,
            update_time=self.update_time)


def get_table(catalog_id: Optional[str] = None,
              database_id: Optional[str] = None,
              location: Optional[str] = None,
              project: Optional[str] = None,
              table_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTableResult:
    """
    Gets the table specified by the resource name.
    """
    __args__ = dict()
    __args__['catalogId'] = catalog_id
    __args__['databaseId'] = database_id
    __args__['location'] = location
    __args__['project'] = project
    __args__['tableId'] = table_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:biglake/v1:getTable', __args__, opts=opts, typ=GetTableResult).value

    return AwaitableGetTableResult(
        create_time=pulumi.get(__ret__, 'create_time'),
        delete_time=pulumi.get(__ret__, 'delete_time'),
        etag=pulumi.get(__ret__, 'etag'),
        expire_time=pulumi.get(__ret__, 'expire_time'),
        hive_options=pulumi.get(__ret__, 'hive_options'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'),
        update_time=pulumi.get(__ret__, 'update_time'))


@_utilities.lift_output_func(get_table)
def get_table_output(catalog_id: Optional[pulumi.Input[str]] = None,
                     database_id: Optional[pulumi.Input[str]] = None,
                     location: Optional[pulumi.Input[str]] = None,
                     project: Optional[pulumi.Input[Optional[str]]] = None,
                     table_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTableResult]:
    """
    Gets the table specified by the resource name.
    """
    ...