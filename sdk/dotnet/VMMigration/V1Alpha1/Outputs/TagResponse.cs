// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.VMMigration.V1Alpha1.Outputs
{

    /// <summary>
    /// Tag is an AWS tag representation.
    /// </summary>
    [OutputType]
    public sealed class TagResponse
    {
        /// <summary>
        /// Key of tag.
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// Value of tag.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private TagResponse(
            string key,

            string value)
        {
            Key = key;
            Value = value;
        }
    }
}
