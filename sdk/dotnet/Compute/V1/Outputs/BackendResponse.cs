// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Compute.V1.Outputs
{

    [OutputType]
    public sealed class BackendResponse
    {
        /// <summary>
        /// Specifies how to determine whether the backend of a load balancer can handle additional traffic or is fully loaded. For usage guidelines, see  Connection balancing mode.
        /// </summary>
        public readonly string BalancingMode;
        /// <summary>
        /// A multiplier applied to the backend's target capacity of its balancing mode. The default value is 1, which means the group serves up to 100% of its configured capacity (depending on balancingMode). A setting of 0 means the group is completely drained, offering 0% of its available capacity. The valid ranges are 0.0 and [0.1,1.0]. You cannot configure a setting larger than 0 and smaller than 0.1. You cannot configure a setting of 0 when there is only one backend attached to the backend service.
        /// 
        /// Not supported by:
        /// 
        /// - Internal TCP/UDP Load Balancing - Network Load Balancing
        /// </summary>
        public readonly double CapacityScaler;
        /// <summary>
        /// An optional description of this resource. Provide this property when you create the resource.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// This field designates whether this is a failover backend. More than one failover backend can be configured for a given BackendService.
        /// </summary>
        public readonly bool Failover;
        /// <summary>
        /// The fully-qualified URL of an instance group or network endpoint group (NEG) resource. The type of backend that a backend service supports depends on the backend service's loadBalancingScheme.
        /// 
        ///  
        /// - When the loadBalancingScheme for the backend service is EXTERNAL (except Network Load Balancing),  INTERNAL_SELF_MANAGED, or INTERNAL_MANAGED , the backend can be either an instance group or a NEG. The backends on the backend service must be either all instance groups or all NEGs. You cannot mix instance group and NEG backends on the same backend service. 
        /// 
        /// 
        /// - When the loadBalancingScheme for the backend service is EXTERNAL for Network Load Balancing or INTERNAL for Internal TCP/UDP Load Balancing, the backend must be an instance group. NEGs are not supported.  
        /// 
        /// For regional services, the backend must be in the same region as the backend service.
        /// 
        /// You must use the fully-qualified URL (starting with https://www.googleapis.com/) to specify the instance group or NEG. Partial URLs are not supported.
        /// </summary>
        public readonly string Group;
        /// <summary>
        /// Defines a target maximum number of simultaneous connections. For usage guidelines, see Connection balancing mode and Utilization balancing mode. Not available if the backend's balancingMode is RATE. Not supported by:
        /// 
        /// - Internal TCP/UDP Load Balancing - Network Load Balancing
        /// </summary>
        public readonly int MaxConnections;
        /// <summary>
        /// Defines a target maximum number of simultaneous connections. For usage guidelines, see Connection balancing mode and Utilization balancing mode.
        /// 
        /// Not available if the backend's balancingMode is RATE. Not supported by:
        /// 
        /// - Internal TCP/UDP Load Balancing - Network Load Balancing.
        /// </summary>
        public readonly int MaxConnectionsPerEndpoint;
        /// <summary>
        /// Defines a target maximum number of simultaneous connections. For usage guidelines, see Connection balancing mode and Utilization balancing mode.
        /// 
        /// Not available if the backend's balancingMode is RATE. Not supported by:
        /// 
        /// - Internal TCP/UDP Load Balancing - Network Load Balancing.
        /// </summary>
        public readonly int MaxConnectionsPerInstance;
        /// <summary>
        /// Defines a maximum number of HTTP requests per second (RPS). For usage guidelines, see Rate balancing mode and Utilization balancing mode.
        /// 
        /// Not available if the backend's balancingMode is CONNECTION.
        /// </summary>
        public readonly int MaxRate;
        /// <summary>
        /// Defines a maximum target for requests per second (RPS). For usage guidelines, see Rate balancing mode and Utilization balancing mode.
        /// 
        /// Not available if the backend's balancingMode is CONNECTION.
        /// </summary>
        public readonly double MaxRatePerEndpoint;
        /// <summary>
        /// Defines a maximum target for requests per second (RPS). For usage guidelines, see Rate balancing mode and Utilization balancing mode.
        /// 
        /// Not available if the backend's balancingMode is CONNECTION.
        /// </summary>
        public readonly double MaxRatePerInstance;
        public readonly double MaxUtilization;

        [OutputConstructor]
        private BackendResponse(
            string balancingMode,

            double capacityScaler,

            string description,

            bool failover,

            string group,

            int maxConnections,

            int maxConnectionsPerEndpoint,

            int maxConnectionsPerInstance,

            int maxRate,

            double maxRatePerEndpoint,

            double maxRatePerInstance,

            double maxUtilization)
        {
            BalancingMode = balancingMode;
            CapacityScaler = capacityScaler;
            Description = description;
            Failover = failover;
            Group = group;
            MaxConnections = maxConnections;
            MaxConnectionsPerEndpoint = maxConnectionsPerEndpoint;
            MaxConnectionsPerInstance = maxConnectionsPerInstance;
            MaxRate = maxRate;
            MaxRatePerEndpoint = maxRatePerEndpoint;
            MaxRatePerInstance = maxRatePerInstance;
            MaxUtilization = maxUtilization;
        }
    }
}