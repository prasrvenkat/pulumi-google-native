# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ConversationState',
    'DataStoreContentConfig',
    'DataStoreIndustryVertical',
    'DataStoreSolutionTypesItem',
    'EngineIndustryVertical',
    'EngineSolutionType',
    'GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigTrainingState',
    'GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigSearchAddOnsItem',
    'GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigSearchTier',
    'GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySummarySkippedReasonsItem',
]


class ConversationState(str, Enum):
    """
    The state of the Conversation.
    """
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    """
    Unknown.
    """
    IN_PROGRESS = "IN_PROGRESS"
    """
    Conversation is currently open.
    """
    COMPLETED = "COMPLETED"
    """
    Conversation has been completed.
    """


class DataStoreContentConfig(str, Enum):
    """
    Immutable. The content config of the data store. If this field is unset, the server behavior defaults to ContentConfig.NO_CONTENT.
    """
    CONTENT_CONFIG_UNSPECIFIED = "CONTENT_CONFIG_UNSPECIFIED"
    """
    Default value.
    """
    NO_CONTENT = "NO_CONTENT"
    """
    Only contains documents without any Document.content.
    """
    CONTENT_REQUIRED = "CONTENT_REQUIRED"
    """
    Only contains documents with Document.content.
    """
    PUBLIC_WEBSITE = "PUBLIC_WEBSITE"
    """
    The data store is used for public website search.
    """


class DataStoreIndustryVertical(str, Enum):
    """
    Immutable. The industry vertical that the data store registers.
    """
    INDUSTRY_VERTICAL_UNSPECIFIED = "INDUSTRY_VERTICAL_UNSPECIFIED"
    """
    Value used when unset.
    """
    GENERIC = "GENERIC"
    """
    The generic vertical for documents that are not specific to any industry vertical.
    """
    MEDIA = "MEDIA"
    """
    The media industry vertical.
    """


class DataStoreSolutionTypesItem(str, Enum):
    SOLUTION_TYPE_UNSPECIFIED = "SOLUTION_TYPE_UNSPECIFIED"
    """
    Default value.
    """
    SOLUTION_TYPE_RECOMMENDATION = "SOLUTION_TYPE_RECOMMENDATION"
    """
    Used for Recommendations AI.
    """
    SOLUTION_TYPE_SEARCH = "SOLUTION_TYPE_SEARCH"
    """
    Used for Discovery Search.
    """
    SOLUTION_TYPE_CHAT = "SOLUTION_TYPE_CHAT"
    """
    Used for use cases related to the Generative AI agent.
    """


class EngineIndustryVertical(str, Enum):
    """
    The industry vertical that the engine registers. The restriction of the Engine industry vertical is based on DataStore: If unspecified, default to `GENERIC`. Vertical on Engine has to match vertical of the DataStore liniked to the engine.
    """
    INDUSTRY_VERTICAL_UNSPECIFIED = "INDUSTRY_VERTICAL_UNSPECIFIED"
    """
    Value used when unset.
    """
    GENERIC = "GENERIC"
    """
    The generic vertical for documents that are not specific to any industry vertical.
    """
    MEDIA = "MEDIA"
    """
    The media industry vertical.
    """


class EngineSolutionType(str, Enum):
    """
    Required. The solutions of the engine.
    """
    SOLUTION_TYPE_UNSPECIFIED = "SOLUTION_TYPE_UNSPECIFIED"
    """
    Default value.
    """
    SOLUTION_TYPE_RECOMMENDATION = "SOLUTION_TYPE_RECOMMENDATION"
    """
    Used for Recommendations AI.
    """
    SOLUTION_TYPE_SEARCH = "SOLUTION_TYPE_SEARCH"
    """
    Used for Discovery Search.
    """
    SOLUTION_TYPE_CHAT = "SOLUTION_TYPE_CHAT"
    """
    Used for use cases related to the Generative AI agent.
    """


class GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigTrainingState(str, Enum):
    """
    The training state that the engine is in (e.g. `TRAINING` or `PAUSED`). Since part of the cost of running the service is frequency of training - this can be used to determine when to train engine in order to control cost. If not specified: the default value for `CreateEngine` method is `TRAINING`. The default value for `UpdateEngine` method is to keep the state the same as before.
    """
    TRAINING_STATE_UNSPECIFIED = "TRAINING_STATE_UNSPECIFIED"
    """
    Unspecified training state.
    """
    PAUSED = "PAUSED"
    """
    The engine training is paused.
    """
    TRAINING = "TRAINING"
    """
    The engine is training.
    """


class GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigSearchAddOnsItem(str, Enum):
    SEARCH_ADD_ON_UNSPECIFIED = "SEARCH_ADD_ON_UNSPECIFIED"
    """
    Default value when the enum is unspecified. This is invalid to use.
    """
    SEARCH_ADD_ON_LLM = "SEARCH_ADD_ON_LLM"
    """
    Large language model add-on.
    """


class GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigSearchTier(str, Enum):
    """
    The search feature tier of this engine. Different tiers might have different pricing. To learn more, please check the pricing documentation. Defaults to SearchTier.SEARCH_TIER_STANDARD if not specified.
    """
    SEARCH_TIER_UNSPECIFIED = "SEARCH_TIER_UNSPECIFIED"
    """
    Default value when the enum is unspecified. This is invalid to use.
    """
    SEARCH_TIER_STANDARD = "SEARCH_TIER_STANDARD"
    """
    Standard tier.
    """
    SEARCH_TIER_ENTERPRISE = "SEARCH_TIER_ENTERPRISE"
    """
    Enterprise tier.
    """


class GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySummarySkippedReasonsItem(str, Enum):
    SUMMARY_SKIPPED_REASON_UNSPECIFIED = "SUMMARY_SKIPPED_REASON_UNSPECIFIED"
    """
    Default value. The summary skipped reason is not specified.
    """
    ADVERSARIAL_QUERY_IGNORED = "ADVERSARIAL_QUERY_IGNORED"
    """
    The adversarial query ignored case. Only populated when SummarySpec.ignore_adversarial_query is set to `true`.
    """
    NON_SUMMARY_SEEKING_QUERY_IGNORED = "NON_SUMMARY_SEEKING_QUERY_IGNORED"
    """
    The non-summary seeking query ignored case. Only populated when SummarySpec.ignore_non_summary_seeking_query is set to `true`.
    """
    OUT_OF_DOMAIN_QUERY_IGNORED = "OUT_OF_DOMAIN_QUERY_IGNORED"
    """
    The out-of-domain query ignored case. Google skips the summary if there are no high-relevance search results. For example, the data store contains facts about company A but the user query is asking questions about company B.
    """
    POTENTIAL_POLICY_VIOLATION = "POTENTIAL_POLICY_VIOLATION"
    """
    The potential policy violation case. Google skips the summary if there is a potential policy violation detected. This includes content that may be violent or toxic.
    """
    LLM_ADDON_NOT_ENABLED = "LLM_ADDON_NOT_ENABLED"
    """
    The LLM addon not enabled case. Google skips the summary if the LLM addon is not enabled.
    """