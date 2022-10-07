// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dataplex.V1.Outputs
{

    /// <summary>
    /// Config for running scheduled notebooks.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDataplexV1TaskNotebookTaskConfigResponse
    {
        /// <summary>
        /// Optional. GCS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip.
        /// </summary>
        public readonly ImmutableArray<string> ArchiveUris;
        /// <summary>
        /// Optional. GCS URIs of files to be placed in the working directory of each executor.
        /// </summary>
        public readonly ImmutableArray<string> FileUris;
        /// <summary>
        /// Optional. Infrastructure specification for the execution.
        /// </summary>
        public readonly Outputs.GoogleCloudDataplexV1TaskInfrastructureSpecResponse InfrastructureSpec;
        /// <summary>
        /// Path to input notebook. This can be the GCS URI of the notebook file or the path to a Notebook Content. The execution args are accessible as environment variables (TASK_key=value).
        /// </summary>
        public readonly string Notebook;

        [OutputConstructor]
        private GoogleCloudDataplexV1TaskNotebookTaskConfigResponse(
            ImmutableArray<string> archiveUris,

            ImmutableArray<string> fileUris,

            Outputs.GoogleCloudDataplexV1TaskInfrastructureSpecResponse infrastructureSpec,

            string notebook)
        {
            ArchiveUris = archiveUris;
            FileUris = fileUris;
            InfrastructureSpec = infrastructureSpec;
            Notebook = notebook;
        }
    }
}