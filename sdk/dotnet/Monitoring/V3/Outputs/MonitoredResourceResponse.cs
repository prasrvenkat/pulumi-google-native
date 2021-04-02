// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Monitoring.V3.Outputs
{

    [OutputType]
    public sealed class MonitoredResourceResponse
    {
        /// <summary>
        /// Required. Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels "project_id", "instance_id", and "zone".
        /// </summary>
        public readonly ImmutableDictionary<string, string> Labels;
        /// <summary>
        /// Required. The monitored resource type. This field must match the type field of a MonitoredResourceDescriptor object. For example, the type of a Compute Engine VM instance is gce_instance. For a list of types, see Monitoring resource types and Logging resource types.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private MonitoredResourceResponse(
            ImmutableDictionary<string, string> labels,

            string type)
        {
            Labels = labels;
            Type = type;
        }
    }
}