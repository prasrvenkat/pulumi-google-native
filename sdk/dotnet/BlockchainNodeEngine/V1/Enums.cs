// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.GoogleNative.BlockchainNodeEngine.V1
{
    /// <summary>
    /// Immutable. The blockchain type of the node.
    /// </summary>
    [EnumType]
    public readonly struct BlockchainNodeBlockchainType : IEquatable<BlockchainNodeBlockchainType>
    {
        private readonly string _value;

        private BlockchainNodeBlockchainType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Blockchain type has not been specified, but should be.
        /// </summary>
        public static BlockchainNodeBlockchainType BlockchainTypeUnspecified { get; } = new BlockchainNodeBlockchainType("BLOCKCHAIN_TYPE_UNSPECIFIED");
        /// <summary>
        /// The blockchain type is Ethereum.
        /// </summary>
        public static BlockchainNodeBlockchainType Ethereum { get; } = new BlockchainNodeBlockchainType("ETHEREUM");

        public static bool operator ==(BlockchainNodeBlockchainType left, BlockchainNodeBlockchainType right) => left.Equals(right);
        public static bool operator !=(BlockchainNodeBlockchainType left, BlockchainNodeBlockchainType right) => !left.Equals(right);

        public static explicit operator string(BlockchainNodeBlockchainType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is BlockchainNodeBlockchainType other && Equals(other);
        public bool Equals(BlockchainNodeBlockchainType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Immutable. The consensus client.
    /// </summary>
    [EnumType]
    public readonly struct EthereumDetailsConsensusClient : IEquatable<EthereumDetailsConsensusClient>
    {
        private readonly string _value;

        private EthereumDetailsConsensusClient(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Consensus client has not been specified, but should be.
        /// </summary>
        public static EthereumDetailsConsensusClient ConsensusClientUnspecified { get; } = new EthereumDetailsConsensusClient("CONSENSUS_CLIENT_UNSPECIFIED");
        /// <summary>
        /// Consensus client implementation written in Rust, maintained by Sigma Prime. See [Lighthouse - Sigma Prime](https://lighthouse.sigmaprime.io/) for details.
        /// </summary>
        public static EthereumDetailsConsensusClient Lighthouse { get; } = new EthereumDetailsConsensusClient("LIGHTHOUSE");
        /// <summary>
        /// Erigon's embedded consensus client embedded in the execution client. Note this option is not currently available when creating new blockchain nodes. See [Erigon on GitHub](https://github.com/ledgerwatch/erigon#embedded-consensus-layer) for details.
        /// </summary>
        public static EthereumDetailsConsensusClient ErigonEmbeddedConsensusLayer { get; } = new EthereumDetailsConsensusClient("ERIGON_EMBEDDED_CONSENSUS_LAYER");

        public static bool operator ==(EthereumDetailsConsensusClient left, EthereumDetailsConsensusClient right) => left.Equals(right);
        public static bool operator !=(EthereumDetailsConsensusClient left, EthereumDetailsConsensusClient right) => !left.Equals(right);

        public static explicit operator string(EthereumDetailsConsensusClient value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EthereumDetailsConsensusClient other && Equals(other);
        public bool Equals(EthereumDetailsConsensusClient other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Immutable. The execution client
    /// </summary>
    [EnumType]
    public readonly struct EthereumDetailsExecutionClient : IEquatable<EthereumDetailsExecutionClient>
    {
        private readonly string _value;

        private EthereumDetailsExecutionClient(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Execution client has not been specified, but should be.
        /// </summary>
        public static EthereumDetailsExecutionClient ExecutionClientUnspecified { get; } = new EthereumDetailsExecutionClient("EXECUTION_CLIENT_UNSPECIFIED");
        /// <summary>
        /// Official Go implementation of the Ethereum protocol. See [go-ethereum](https://geth.ethereum.org/) for details.
        /// </summary>
        public static EthereumDetailsExecutionClient Geth { get; } = new EthereumDetailsExecutionClient("GETH");
        /// <summary>
        /// An implementation of Ethereum (execution client), on the efficiency frontier, written in Go. See [Erigon on GitHub](https://github.com/ledgerwatch/erigon) for details.
        /// </summary>
        public static EthereumDetailsExecutionClient Erigon { get; } = new EthereumDetailsExecutionClient("ERIGON");

        public static bool operator ==(EthereumDetailsExecutionClient left, EthereumDetailsExecutionClient right) => left.Equals(right);
        public static bool operator !=(EthereumDetailsExecutionClient left, EthereumDetailsExecutionClient right) => !left.Equals(right);

        public static explicit operator string(EthereumDetailsExecutionClient value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EthereumDetailsExecutionClient other && Equals(other);
        public bool Equals(EthereumDetailsExecutionClient other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Immutable. The Ethereum environment being accessed.
    /// </summary>
    [EnumType]
    public readonly struct EthereumDetailsNetwork : IEquatable<EthereumDetailsNetwork>
    {
        private readonly string _value;

        private EthereumDetailsNetwork(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// The network has not been specified, but should be.
        /// </summary>
        public static EthereumDetailsNetwork NetworkUnspecified { get; } = new EthereumDetailsNetwork("NETWORK_UNSPECIFIED");
        /// <summary>
        /// The Ethereum Mainnet.
        /// </summary>
        public static EthereumDetailsNetwork Mainnet { get; } = new EthereumDetailsNetwork("MAINNET");
        /// <summary>
        /// The Ethereum Testnet based on Goerli protocol.
        /// </summary>
        public static EthereumDetailsNetwork TestnetGoerliPrater { get; } = new EthereumDetailsNetwork("TESTNET_GOERLI_PRATER");
        /// <summary>
        /// The Ethereum Testnet based on Sepolia/Bepolia protocol. See https://github.com/eth-clients/sepolia.
        /// </summary>
        public static EthereumDetailsNetwork TestnetSepolia { get; } = new EthereumDetailsNetwork("TESTNET_SEPOLIA");
        /// <summary>
        /// The Ethereum Testnet based on Holesky specification. See https://github.com/eth-clients/holesky.
        /// </summary>
        public static EthereumDetailsNetwork TestnetHolesky { get; } = new EthereumDetailsNetwork("TESTNET_HOLESKY");

        public static bool operator ==(EthereumDetailsNetwork left, EthereumDetailsNetwork right) => left.Equals(right);
        public static bool operator !=(EthereumDetailsNetwork left, EthereumDetailsNetwork right) => !left.Equals(right);

        public static explicit operator string(EthereumDetailsNetwork value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EthereumDetailsNetwork other && Equals(other);
        public bool Equals(EthereumDetailsNetwork other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Immutable. The type of Ethereum node.
    /// </summary>
    [EnumType]
    public readonly struct EthereumDetailsNodeType : IEquatable<EthereumDetailsNodeType>
    {
        private readonly string _value;

        private EthereumDetailsNodeType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Node type has not been specified, but should be.
        /// </summary>
        public static EthereumDetailsNodeType NodeTypeUnspecified { get; } = new EthereumDetailsNodeType("NODE_TYPE_UNSPECIFIED");
        /// <summary>
        /// An Ethereum node that only downloads Ethereum block headers.
        /// </summary>
        public static EthereumDetailsNodeType Light { get; } = new EthereumDetailsNodeType("LIGHT");
        /// <summary>
        /// Keeps a complete copy of the blockchain data, and contributes to the network by receiving, validating, and forwarding transactions.
        /// </summary>
        public static EthereumDetailsNodeType Full { get; } = new EthereumDetailsNodeType("FULL");
        /// <summary>
        /// Holds the same data as full node as well as all of the blockchain's history state data dating back to the Genesis Block.
        /// </summary>
        public static EthereumDetailsNodeType Archive { get; } = new EthereumDetailsNodeType("ARCHIVE");

        public static bool operator ==(EthereumDetailsNodeType left, EthereumDetailsNodeType right) => left.Equals(right);
        public static bool operator !=(EthereumDetailsNodeType left, EthereumDetailsNodeType right) => !left.Equals(right);

        public static explicit operator string(EthereumDetailsNodeType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EthereumDetailsNodeType other && Equals(other);
        public bool Equals(EthereumDetailsNodeType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Immutable. Blockchain garbage collection mode.
    /// </summary>
    [EnumType]
    public readonly struct GethDetailsGarbageCollectionMode : IEquatable<GethDetailsGarbageCollectionMode>
    {
        private readonly string _value;

        private GethDetailsGarbageCollectionMode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// The garbage collection has not been specified.
        /// </summary>
        public static GethDetailsGarbageCollectionMode GarbageCollectionModeUnspecified { get; } = new GethDetailsGarbageCollectionMode("GARBAGE_COLLECTION_MODE_UNSPECIFIED");
        /// <summary>
        /// Configures Geth's garbage collection so that older data not needed for a full node is deleted. This is the default mode when creating a full node.
        /// </summary>
        public static GethDetailsGarbageCollectionMode Full { get; } = new GethDetailsGarbageCollectionMode("FULL");
        /// <summary>
        /// Configures Geth's garbage collection so that old data is never deleted. This is the default mode when creating an archive node. This value can also be chosen when creating a full node in order to create a partial/recent archive node. See [Sync modes](https://geth.ethereum.org/docs/fundamentals/sync-modes) for more details.
        /// </summary>
        public static GethDetailsGarbageCollectionMode Archive { get; } = new GethDetailsGarbageCollectionMode("ARCHIVE");

        public static bool operator ==(GethDetailsGarbageCollectionMode left, GethDetailsGarbageCollectionMode right) => left.Equals(right);
        public static bool operator !=(GethDetailsGarbageCollectionMode left, GethDetailsGarbageCollectionMode right) => !left.Equals(right);

        public static explicit operator string(GethDetailsGarbageCollectionMode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is GethDetailsGarbageCollectionMode other && Equals(other);
        public bool Equals(GethDetailsGarbageCollectionMode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}