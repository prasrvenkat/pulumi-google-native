// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.StorageTransfer.V1.Inputs
{

    /// <summary>
    /// Conditions that determine which objects are transferred. Applies only to Cloud Data Sources such as S3, Azure, and Cloud Storage. The "last modification time" refers to the time of the last change to the object's content or metadata — specifically, this is the `updated` property of Cloud Storage objects, the `LastModified` field of S3 objects, and the `Last-Modified` header of Azure blobs. Transfers with a PosixFilesystem source or destination don't support `ObjectConditions`.
    /// </summary>
    public sealed class ObjectConditionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("excludePrefixes")]
        private InputList<string>? _excludePrefixes;

        /// <summary>
        /// If you specify `exclude_prefixes`, Storage Transfer Service uses the items in the `exclude_prefixes` array to determine which objects to exclude from a transfer. Objects must not start with one of the matching `exclude_prefixes` for inclusion in a transfer. The following are requirements of `exclude_prefixes`: * Each exclude-prefix can contain any sequence of Unicode characters, to a max length of 1024 bytes when UTF8-encoded, and must not contain Carriage Return or Line Feed characters. Wildcard matching and regular expression matching are not supported. * Each exclude-prefix must omit the leading slash. For example, to exclude the object `s3://my-aws-bucket/logs/y=2015/requests.gz`, specify the exclude-prefix as `logs/y=2015/requests.gz`. * None of the exclude-prefix values can be empty, if specified. * Each exclude-prefix must exclude a distinct portion of the object namespace. No exclude-prefix may be a prefix of another exclude-prefix. * If include_prefixes is specified, then each exclude-prefix must start with the value of a path explicitly included by `include_prefixes`. The max size of `exclude_prefixes` is 1000. For more information, see [Filtering objects from transfers](/storage-transfer/docs/filtering-objects-from-transfers).
        /// </summary>
        public InputList<string> ExcludePrefixes
        {
            get => _excludePrefixes ?? (_excludePrefixes = new InputList<string>());
            set => _excludePrefixes = value;
        }

        [Input("includePrefixes")]
        private InputList<string>? _includePrefixes;

        /// <summary>
        /// If you specify `include_prefixes`, Storage Transfer Service uses the items in the `include_prefixes` array to determine which objects to include in a transfer. Objects must start with one of the matching `include_prefixes` for inclusion in the transfer. If exclude_prefixes is specified, objects must not start with any of the `exclude_prefixes` specified for inclusion in the transfer. The following are requirements of `include_prefixes`: * Each include-prefix can contain any sequence of Unicode characters, to a max length of 1024 bytes when UTF8-encoded, and must not contain Carriage Return or Line Feed characters. Wildcard matching and regular expression matching are not supported. * Each include-prefix must omit the leading slash. For example, to include the object `s3://my-aws-bucket/logs/y=2015/requests.gz`, specify the include-prefix as `logs/y=2015/requests.gz`. * None of the include-prefix values can be empty, if specified. * Each include-prefix must include a distinct portion of the object namespace. No include-prefix may be a prefix of another include-prefix. The max size of `include_prefixes` is 1000. For more information, see [Filtering objects from transfers](/storage-transfer/docs/filtering-objects-from-transfers).
        /// </summary>
        public InputList<string> IncludePrefixes
        {
            get => _includePrefixes ?? (_includePrefixes = new InputList<string>());
            set => _includePrefixes = value;
        }

        /// <summary>
        /// If specified, only objects with a "last modification time" before this timestamp and objects that don't have a "last modification time" are transferred.
        /// </summary>
        [Input("lastModifiedBefore")]
        public Input<string>? LastModifiedBefore { get; set; }

        /// <summary>
        /// If specified, only objects with a "last modification time" on or after this timestamp and objects that don't have a "last modification time" are transferred. The `last_modified_since` and `last_modified_before` fields can be used together for chunked data processing. For example, consider a script that processes each day's worth of data at a time. For that you'd set each of the fields as follows: * `last_modified_since` to the start of the day * `last_modified_before` to the end of the day
        /// </summary>
        [Input("lastModifiedSince")]
        public Input<string>? LastModifiedSince { get; set; }

        /// <summary>
        /// Ensures that objects are not transferred if a specific maximum time has elapsed since the "last modification time". When a TransferOperation begins, objects with a "last modification time" are transferred only if the elapsed time between the start_time of the `TransferOperation`and the "last modification time" of the object is less than the value of max_time_elapsed_since_last_modification`. Objects that do not have a "last modification time" are also transferred.
        /// </summary>
        [Input("maxTimeElapsedSinceLastModification")]
        public Input<string>? MaxTimeElapsedSinceLastModification { get; set; }

        /// <summary>
        /// Ensures that objects are not transferred until a specific minimum time has elapsed after the "last modification time". When a TransferOperation begins, objects with a "last modification time" are transferred only if the elapsed time between the start_time of the `TransferOperation` and the "last modification time" of the object is equal to or greater than the value of min_time_elapsed_since_last_modification`. Objects that do not have a "last modification time" are also transferred.
        /// </summary>
        [Input("minTimeElapsedSinceLastModification")]
        public Input<string>? MinTimeElapsedSinceLastModification { get; set; }

        public ObjectConditionsArgs()
        {
        }
        public static new ObjectConditionsArgs Empty => new ObjectConditionsArgs();
    }
}
