// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ContainerAnalysis.V1Beta1.Outputs
{

    /// <summary>
    /// Deprecated. Common Vulnerability Scoring System version 3. For details, see https://www.first.org/cvss/specification-document
    /// </summary>
    [OutputType]
    public sealed class CVSSv3Response
    {
        public readonly string AttackComplexity;
        /// <summary>
        /// Base Metrics Represents the intrinsic characteristics of a vulnerability that are constant over time and across user environments.
        /// </summary>
        public readonly string AttackVector;
        public readonly string AvailabilityImpact;
        /// <summary>
        /// The base score is a function of the base metric scores.
        /// </summary>
        public readonly double BaseScore;
        public readonly string ConfidentialityImpact;
        public readonly double ExploitabilityScore;
        public readonly double ImpactScore;
        public readonly string IntegrityImpact;
        public readonly string PrivilegesRequired;
        public readonly string Scope;
        public readonly string UserInteraction;

        [OutputConstructor]
        private CVSSv3Response(
            string attackComplexity,

            string attackVector,

            string availabilityImpact,

            double baseScore,

            string confidentialityImpact,

            double exploitabilityScore,

            double impactScore,

            string integrityImpact,

            string privilegesRequired,

            string scope,

            string userInteraction)
        {
            AttackComplexity = attackComplexity;
            AttackVector = attackVector;
            AvailabilityImpact = availabilityImpact;
            BaseScore = baseScore;
            ConfidentialityImpact = confidentialityImpact;
            ExploitabilityScore = exploitabilityScore;
            ImpactScore = impactScore;
            IntegrityImpact = integrityImpact;
            PrivilegesRequired = privilegesRequired;
            Scope = scope;
            UserInteraction = userInteraction;
        }
    }
}
