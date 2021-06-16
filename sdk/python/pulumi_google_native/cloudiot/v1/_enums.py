# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DeviceLogLevel',
    'GatewayConfigGatewayAuthMethod',
    'GatewayConfigGatewayType',
    'HttpConfigHttpEnabledState',
    'MqttConfigMqttEnabledState',
    'PublicKeyCertificateFormat',
    'PublicKeyCredentialFormat',
    'RegistryLogLevel',
]


class DeviceLogLevel(str, Enum):
    """
    **Beta Feature** The logging verbosity for device activity. If unspecified, DeviceRegistry.log_level will be used.
    """
    LOG_LEVEL_UNSPECIFIED = "LOG_LEVEL_UNSPECIFIED"
    NONE = "NONE"
    ERROR = "ERROR"
    INFO = "INFO"
    DEBUG = "DEBUG"


class GatewayConfigGatewayAuthMethod(str, Enum):
    """
    Indicates how to authorize and/or authenticate devices to access the gateway.
    """
    GATEWAY_AUTH_METHOD_UNSPECIFIED = "GATEWAY_AUTH_METHOD_UNSPECIFIED"
    ASSOCIATION_ONLY = "ASSOCIATION_ONLY"
    DEVICE_AUTH_TOKEN_ONLY = "DEVICE_AUTH_TOKEN_ONLY"
    ASSOCIATION_AND_DEVICE_AUTH_TOKEN = "ASSOCIATION_AND_DEVICE_AUTH_TOKEN"


class GatewayConfigGatewayType(str, Enum):
    """
    Indicates whether the device is a gateway.
    """
    GATEWAY_TYPE_UNSPECIFIED = "GATEWAY_TYPE_UNSPECIFIED"
    GATEWAY = "GATEWAY"
    NON_GATEWAY = "NON_GATEWAY"


class HttpConfigHttpEnabledState(str, Enum):
    """
    If enabled, allows devices to use DeviceService via the HTTP protocol. Otherwise, any requests to DeviceService will fail for this registry.
    """
    HTTP_STATE_UNSPECIFIED = "HTTP_STATE_UNSPECIFIED"
    HTTP_ENABLED = "HTTP_ENABLED"
    HTTP_DISABLED = "HTTP_DISABLED"


class MqttConfigMqttEnabledState(str, Enum):
    """
    If enabled, allows connections using the MQTT protocol. Otherwise, MQTT connections to this registry will fail.
    """
    MQTT_STATE_UNSPECIFIED = "MQTT_STATE_UNSPECIFIED"
    MQTT_ENABLED = "MQTT_ENABLED"
    MQTT_DISABLED = "MQTT_DISABLED"


class PublicKeyCertificateFormat(str, Enum):
    """
    The certificate format.
    """
    UNSPECIFIED_PUBLIC_KEY_CERTIFICATE_FORMAT = "UNSPECIFIED_PUBLIC_KEY_CERTIFICATE_FORMAT"
    X509_CERTIFICATE_PEM = "X509_CERTIFICATE_PEM"


class PublicKeyCredentialFormat(str, Enum):
    """
    The format of the key.
    """
    UNSPECIFIED_PUBLIC_KEY_FORMAT = "UNSPECIFIED_PUBLIC_KEY_FORMAT"
    RSA_PEM = "RSA_PEM"
    RSA_X509_PEM = "RSA_X509_PEM"
    ES256_PEM = "ES256_PEM"
    ES256_X509_PEM = "ES256_X509_PEM"


class RegistryLogLevel(str, Enum):
    """
    **Beta Feature** The default logging verbosity for activity from devices in this registry. The verbosity level can be overridden by Device.log_level.
    """
    LOG_LEVEL_UNSPECIFIED = "LOG_LEVEL_UNSPECIFIED"
    NONE = "NONE"
    ERROR = "ERROR"
    INFO = "INFO"
    DEBUG = "DEBUG"