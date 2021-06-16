# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'VariableState',
]


class VariableState(str, Enum):
    """
    Output only. The current state of the variable. The variable state indicates the outcome of the `variables().watch` call and is visible through the `get` and `list` calls.
    """
    VARIABLE_STATE_UNSPECIFIED = "VARIABLE_STATE_UNSPECIFIED"
    UPDATED = "UPDATED"
    DELETED = "DELETED"