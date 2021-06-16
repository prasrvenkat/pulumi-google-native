// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Ml.V1
{
    /// <summary>
    /// Adds a user provided trial to a study.
    /// </summary>
    [GoogleNativeResourceType("google-native:ml/v1:Trial")]
    public partial class Trial : Pulumi.CustomResource
    {
        /// <summary>
        /// The identifier of the client that originally requested this trial.
        /// </summary>
        [Output("clientId")]
        public Output<string> ClientId { get; private set; } = null!;

        /// <summary>
        /// Time at which the trial's status changed to COMPLETED.
        /// </summary>
        [Output("endTime")]
        public Output<string> EndTime { get; private set; } = null!;

        /// <summary>
        /// The final measurement containing the objective value.
        /// </summary>
        [Output("finalMeasurement")]
        public Output<Outputs.GoogleCloudMlV1__MeasurementResponse> FinalMeasurement { get; private set; } = null!;

        /// <summary>
        /// A human readable string describing why the trial is infeasible. This should only be set if trial_infeasible is true.
        /// </summary>
        [Output("infeasibleReason")]
        public Output<string> InfeasibleReason { get; private set; } = null!;

        /// <summary>
        /// A list of measurements that are strictly lexicographically ordered by their induced tuples (steps, elapsed_time). These are used for early stopping computations.
        /// </summary>
        [Output("measurements")]
        public Output<ImmutableArray<Outputs.GoogleCloudMlV1__MeasurementResponse>> Measurements { get; private set; } = null!;

        /// <summary>
        /// Name of the trial assigned by the service.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The parameters of the trial.
        /// </summary>
        [Output("parameters")]
        public Output<ImmutableArray<Outputs.GoogleCloudMlV1_Trial_ParameterResponse>> Parameters { get; private set; } = null!;

        /// <summary>
        /// Time at which the trial was started.
        /// </summary>
        [Output("startTime")]
        public Output<string> StartTime { get; private set; } = null!;

        /// <summary>
        /// The detailed state of a trial.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// If true, the parameters in this trial are not attempted again.
        /// </summary>
        [Output("trialInfeasible")]
        public Output<bool> TrialInfeasible { get; private set; } = null!;


        /// <summary>
        /// Create a Trial resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Trial(string name, TrialArgs args, CustomResourceOptions? options = null)
            : base("google-native:ml/v1:Trial", name, args ?? new TrialArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Trial(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:ml/v1:Trial", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Trial resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Trial Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Trial(name, id, options);
        }
    }

    public sealed class TrialArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The final measurement containing the objective value.
        /// </summary>
        [Input("finalMeasurement")]
        public Input<Inputs.GoogleCloudMlV1__MeasurementArgs>? FinalMeasurement { get; set; }

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("measurements")]
        private InputList<Inputs.GoogleCloudMlV1__MeasurementArgs>? _measurements;

        /// <summary>
        /// A list of measurements that are strictly lexicographically ordered by their induced tuples (steps, elapsed_time). These are used for early stopping computations.
        /// </summary>
        public InputList<Inputs.GoogleCloudMlV1__MeasurementArgs> Measurements
        {
            get => _measurements ?? (_measurements = new InputList<Inputs.GoogleCloudMlV1__MeasurementArgs>());
            set => _measurements = value;
        }

        [Input("parameters")]
        private InputList<Inputs.GoogleCloudMlV1_Trial_ParameterArgs>? _parameters;

        /// <summary>
        /// The parameters of the trial.
        /// </summary>
        public InputList<Inputs.GoogleCloudMlV1_Trial_ParameterArgs> Parameters
        {
            get => _parameters ?? (_parameters = new InputList<Inputs.GoogleCloudMlV1_Trial_ParameterArgs>());
            set => _parameters = value;
        }

        [Input("project", required: true)]
        public Input<string> Project { get; set; } = null!;

        /// <summary>
        /// The detailed state of a trial.
        /// </summary>
        [Input("state")]
        public Input<Pulumi.GoogleNative.Ml.V1.TrialState>? State { get; set; }

        [Input("studyId", required: true)]
        public Input<string> StudyId { get; set; } = null!;

        public TrialArgs()
        {
        }
    }
}