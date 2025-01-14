// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const AuditLogConfigLogType = {
    /**
     * Default case. Should never be this.
     */
    LogTypeUnspecified: "LOG_TYPE_UNSPECIFIED",
    /**
     * Admin reads. Example: CloudIAM getIamPolicy
     */
    AdminRead: "ADMIN_READ",
    /**
     * Data writes. Example: CloudSQL Users create
     */
    DataWrite: "DATA_WRITE",
    /**
     * Data reads. Example: CloudSQL Users list
     */
    DataRead: "DATA_READ",
} as const;

/**
 * The log type that this config enables.
 */
export type AuditLogConfigLogType = (typeof AuditLogConfigLogType)[keyof typeof AuditLogConfigLogType];

export const AuthConfigAuthType = {
    /**
     * Authentication type not specified.
     */
    AuthTypeUnspecified: "AUTH_TYPE_UNSPECIFIED",
    /**
     * Username and Password Authentication.
     */
    UserPassword: "USER_PASSWORD",
    /**
     * JSON Web Token (JWT) Profile for Oauth 2.0 Authorization Grant based authentication
     */
    Oauth2JwtBearer: "OAUTH2_JWT_BEARER",
    /**
     * Oauth 2.0 Client Credentials Grant Authentication
     */
    Oauth2ClientCredentials: "OAUTH2_CLIENT_CREDENTIALS",
    /**
     * SSH Public Key Authentication
     */
    SshPublicKey: "SSH_PUBLIC_KEY",
    /**
     * Oauth 2.0 Authorization Code Flow
     */
    Oauth2AuthCodeFlow: "OAUTH2_AUTH_CODE_FLOW",
} as const;

/**
 * The type of authentication configured.
 */
export type AuthConfigAuthType = (typeof AuthConfigAuthType)[keyof typeof AuthConfigAuthType];

export const ConnectionEventingEnablementType = {
    /**
     * Eventing Enablement Type Unspecifeied.
     */
    EventingEnablementTypeUnspecified: "EVENTING_ENABLEMENT_TYPE_UNSPECIFIED",
    /**
     * Both connection and eventing.
     */
    EventingAndConnection: "EVENTING_AND_CONNECTION",
    /**
     * Only Eventing.
     */
    OnlyEventing: "ONLY_EVENTING",
} as const;

/**
 * Optional. Eventing enablement type. Will be nil if eventing is not enabled.
 */
export type ConnectionEventingEnablementType = (typeof ConnectionEventingEnablementType)[keyof typeof ConnectionEventingEnablementType];

export const CustomConnectorCustomConnectorType = {
    /**
     * Connector type is not specified.
     */
    CustomConnectorTypeUnspecified: "CUSTOM_CONNECTOR_TYPE_UNSPECIFIED",
    /**
     * OpenAPI connector.
     */
    OpenApi: "OPEN_API",
    /**
     * Proto connector.
     */
    Proto: "PROTO",
} as const;

/**
 * Required. Type of the custom connector.
 */
export type CustomConnectorCustomConnectorType = (typeof CustomConnectorCustomConnectorType)[keyof typeof CustomConnectorCustomConnectorType];

export const CustomConnectorVersionType = {
    /**
     * Connector type is not specified.
     */
    CustomConnectorTypeUnspecified: "CUSTOM_CONNECTOR_TYPE_UNSPECIFIED",
    /**
     * OpenAPI connector.
     */
    OpenApi: "OPEN_API",
    /**
     * Proto connector.
     */
    Proto: "PROTO",
} as const;

/**
 * Required. Type of the customConnector.
 */
export type CustomConnectorVersionType = (typeof CustomConnectorVersionType)[keyof typeof CustomConnectorVersionType];

export const EncryptionKeyType = {
    /**
     * Value type is not specified.
     */
    TypeUnspecified: "TYPE_UNSPECIFIED",
    /**
     * Google Managed.
     */
    GoogleManaged: "GOOGLE_MANAGED",
    /**
     * Customer Managed.
     */
    CustomerManaged: "CUSTOMER_MANAGED",
} as const;

/**
 * Type.
 */
export type EncryptionKeyType = (typeof EncryptionKeyType)[keyof typeof EncryptionKeyType];

export const EventSubscriptionDestinationType = {
    /**
     * Default state.
     */
    TypeUnspecified: "TYPE_UNSPECIFIED",
    /**
     * Endpoint - Hit the value of endpoint when event is received
     */
    Endpoint: "ENDPOINT",
} as const;

/**
 * type of the destination
 */
export type EventSubscriptionDestinationType = (typeof EventSubscriptionDestinationType)[keyof typeof EventSubscriptionDestinationType];

export const JMSType = {
    /**
     * Default state.
     */
    TypeUnspecified: "TYPE_UNSPECIFIED",
    /**
     * JMS Queue.
     */
    Queue: "QUEUE",
    /**
     * JMS Topic.
     */
    Topic: "TOPIC",
} as const;

/**
 * Optional. Type of the JMS Source. i.e. Queue or Topic
 */
export type JMSType = (typeof JMSType)[keyof typeof JMSType];

export const SslConfigClientCertType = {
    /**
     * Cert type unspecified.
     */
    CertTypeUnspecified: "CERT_TYPE_UNSPECIFIED",
    /**
     * Privacy Enhanced Mail (PEM) Type
     */
    Pem: "PEM",
} as const;

/**
 * Type of Client Cert (PEM/JKS/.. etc.)
 */
export type SslConfigClientCertType = (typeof SslConfigClientCertType)[keyof typeof SslConfigClientCertType];

export const SslConfigServerCertType = {
    /**
     * Cert type unspecified.
     */
    CertTypeUnspecified: "CERT_TYPE_UNSPECIFIED",
    /**
     * Privacy Enhanced Mail (PEM) Type
     */
    Pem: "PEM",
} as const;

/**
 * Type of Server Cert (PEM/JKS/.. etc.)
 */
export type SslConfigServerCertType = (typeof SslConfigServerCertType)[keyof typeof SslConfigServerCertType];

export const SslConfigTrustModel = {
    /**
     * Public Trust Model. Takes the Default Java trust store.
     */
    Public: "PUBLIC",
    /**
     * Private Trust Model. Takes custom/private trust store.
     */
    Private: "PRIVATE",
    /**
     * Insecure Trust Model. Accept all certificates.
     */
    Insecure: "INSECURE",
} as const;

/**
 * Trust Model of the SSL connection
 */
export type SslConfigTrustModel = (typeof SslConfigTrustModel)[keyof typeof SslConfigTrustModel];

export const SslConfigType = {
    /**
     * No SSL configuration required.
     */
    SslTypeUnspecified: "SSL_TYPE_UNSPECIFIED",
    /**
     * TLS Handshake
     */
    Tls: "TLS",
    /**
     * mutual TLS (MTLS) Handshake
     */
    Mtls: "MTLS",
} as const;

/**
 * Controls the ssl type for the given connector version.
 */
export type SslConfigType = (typeof SslConfigType)[keyof typeof SslConfigType];
