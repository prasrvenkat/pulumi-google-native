# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'GoogleFirestoreAdminV1DailyRecurrenceArgs',
    'GoogleFirestoreAdminV1FlatIndexArgs',
    'GoogleFirestoreAdminV1IndexFieldArgs',
    'GoogleFirestoreAdminV1VectorConfigArgs',
    'GoogleFirestoreAdminV1WeeklyRecurrenceArgs',
]

@pulumi.input_type
class GoogleFirestoreAdminV1DailyRecurrenceArgs:
    def __init__(__self__):
        """
        Represent a recurring schedule that runs at a specific time every day. The time zone is UTC.
        """
        pass


@pulumi.input_type
class GoogleFirestoreAdminV1FlatIndexArgs:
    def __init__(__self__):
        """
        An index that stores vectors in a flat data structure, and supports exhaustive search.
        """
        pass


@pulumi.input_type
class GoogleFirestoreAdminV1IndexFieldArgs:
    def __init__(__self__, *,
                 array_config: Optional[pulumi.Input['GoogleFirestoreAdminV1IndexFieldArrayConfig']] = None,
                 field_path: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input['GoogleFirestoreAdminV1IndexFieldOrder']] = None,
                 vector_config: Optional[pulumi.Input['GoogleFirestoreAdminV1VectorConfigArgs']] = None):
        """
        A field in an index. The field_path describes which field is indexed, the value_mode describes how the field value is indexed.
        :param pulumi.Input['GoogleFirestoreAdminV1IndexFieldArrayConfig'] array_config: Indicates that this field supports operations on `array_value`s.
        :param pulumi.Input[str] field_path: Can be __name__. For single field indexes, this must match the name of the field or may be omitted.
        :param pulumi.Input['GoogleFirestoreAdminV1IndexFieldOrder'] order: Indicates that this field supports ordering by the specified order or comparing using =, !=, <, <=, >, >=.
        :param pulumi.Input['GoogleFirestoreAdminV1VectorConfigArgs'] vector_config: Indicates that this field supports nearest neighbors and distance operations on vector.
        """
        if array_config is not None:
            pulumi.set(__self__, "array_config", array_config)
        if field_path is not None:
            pulumi.set(__self__, "field_path", field_path)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if vector_config is not None:
            pulumi.set(__self__, "vector_config", vector_config)

    @property
    @pulumi.getter(name="arrayConfig")
    def array_config(self) -> Optional[pulumi.Input['GoogleFirestoreAdminV1IndexFieldArrayConfig']]:
        """
        Indicates that this field supports operations on `array_value`s.
        """
        return pulumi.get(self, "array_config")

    @array_config.setter
    def array_config(self, value: Optional[pulumi.Input['GoogleFirestoreAdminV1IndexFieldArrayConfig']]):
        pulumi.set(self, "array_config", value)

    @property
    @pulumi.getter(name="fieldPath")
    def field_path(self) -> Optional[pulumi.Input[str]]:
        """
        Can be __name__. For single field indexes, this must match the name of the field or may be omitted.
        """
        return pulumi.get(self, "field_path")

    @field_path.setter
    def field_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field_path", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input['GoogleFirestoreAdminV1IndexFieldOrder']]:
        """
        Indicates that this field supports ordering by the specified order or comparing using =, !=, <, <=, >, >=.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input['GoogleFirestoreAdminV1IndexFieldOrder']]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter(name="vectorConfig")
    def vector_config(self) -> Optional[pulumi.Input['GoogleFirestoreAdminV1VectorConfigArgs']]:
        """
        Indicates that this field supports nearest neighbors and distance operations on vector.
        """
        return pulumi.get(self, "vector_config")

    @vector_config.setter
    def vector_config(self, value: Optional[pulumi.Input['GoogleFirestoreAdminV1VectorConfigArgs']]):
        pulumi.set(self, "vector_config", value)


@pulumi.input_type
class GoogleFirestoreAdminV1VectorConfigArgs:
    def __init__(__self__, *,
                 dimension: pulumi.Input[int],
                 flat: Optional[pulumi.Input['GoogleFirestoreAdminV1FlatIndexArgs']] = None):
        """
        The index configuration to support vector search operations
        :param pulumi.Input[int] dimension: The vector dimension this configuration applies to. The resulting index will only include vectors of this dimension, and can be used for vector search with the same dimension.
        :param pulumi.Input['GoogleFirestoreAdminV1FlatIndexArgs'] flat: Indicates the vector index is a flat index.
        """
        pulumi.set(__self__, "dimension", dimension)
        if flat is not None:
            pulumi.set(__self__, "flat", flat)

    @property
    @pulumi.getter
    def dimension(self) -> pulumi.Input[int]:
        """
        The vector dimension this configuration applies to. The resulting index will only include vectors of this dimension, and can be used for vector search with the same dimension.
        """
        return pulumi.get(self, "dimension")

    @dimension.setter
    def dimension(self, value: pulumi.Input[int]):
        pulumi.set(self, "dimension", value)

    @property
    @pulumi.getter
    def flat(self) -> Optional[pulumi.Input['GoogleFirestoreAdminV1FlatIndexArgs']]:
        """
        Indicates the vector index is a flat index.
        """
        return pulumi.get(self, "flat")

    @flat.setter
    def flat(self, value: Optional[pulumi.Input['GoogleFirestoreAdminV1FlatIndexArgs']]):
        pulumi.set(self, "flat", value)


@pulumi.input_type
class GoogleFirestoreAdminV1WeeklyRecurrenceArgs:
    def __init__(__self__, *,
                 day: Optional[pulumi.Input['GoogleFirestoreAdminV1WeeklyRecurrenceDay']] = None):
        """
        Represents a recurring schedule that runs on a specified day of the week. The time zone is UTC.
        :param pulumi.Input['GoogleFirestoreAdminV1WeeklyRecurrenceDay'] day: The day of week to run. DAY_OF_WEEK_UNSPECIFIED is not allowed.
        """
        if day is not None:
            pulumi.set(__self__, "day", day)

    @property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input['GoogleFirestoreAdminV1WeeklyRecurrenceDay']]:
        """
        The day of week to run. DAY_OF_WEEK_UNSPECIFIED is not allowed.
        """
        return pulumi.get(self, "day")

    @day.setter
    def day(self, value: Optional[pulumi.Input['GoogleFirestoreAdminV1WeeklyRecurrenceDay']]):
        pulumi.set(self, "day", value)


