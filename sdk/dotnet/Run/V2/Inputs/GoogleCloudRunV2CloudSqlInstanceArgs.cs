// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Run.V2.Inputs
{

    /// <summary>
    /// Represents a set of Cloud SQL instances. Each one will be available under /cloudsql/[instance]. Visit https://cloud.google.com/sql/docs/mysql/connect-run for more information on how to connect Cloud SQL and Cloud Run.
    /// </summary>
    public sealed class GoogleCloudRunV2CloudSqlInstanceArgs : global::Pulumi.ResourceArgs
    {
        [Input("instances")]
        private InputList<string>? _instances;

        /// <summary>
        /// The Cloud SQL instance connection names, as can be found in https://console.cloud.google.com/sql/instances. Visit https://cloud.google.com/sql/docs/mysql/connect-run for more information on how to connect Cloud SQL and Cloud Run. Format: {project}:{location}:{instance}
        /// </summary>
        public InputList<string> Instances
        {
            get => _instances ?? (_instances = new InputList<string>());
            set => _instances = value;
        }

        public GoogleCloudRunV2CloudSqlInstanceArgs()
        {
        }
        public static new GoogleCloudRunV2CloudSqlInstanceArgs Empty => new GoogleCloudRunV2CloudSqlInstanceArgs();
    }
}
