# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'GoogleCloudDatalabelingV1beta1ImageClassificationConfigAnswerAggregationType',
    'GoogleCloudDatalabelingV1beta1InputConfigAnnotationType',
    'GoogleCloudDatalabelingV1beta1InputConfigDataType',
    'InstructionDataType',
]


class GoogleCloudDatalabelingV1beta1ImageClassificationConfigAnswerAggregationType(str, Enum):
    """
    Optional. The type of how to aggregate answers.
    """
    STRING_AGGREGATION_TYPE_UNSPECIFIED = "STRING_AGGREGATION_TYPE_UNSPECIFIED"
    MAJORITY_VOTE = "MAJORITY_VOTE"
    """
    Majority vote to aggregate answers.
    """
    UNANIMOUS_VOTE = "UNANIMOUS_VOTE"
    """
    Unanimous answers will be adopted.
    """
    NO_AGGREGATION = "NO_AGGREGATION"
    """
    Preserve all answers by crowd compute.
    """


class GoogleCloudDatalabelingV1beta1InputConfigAnnotationType(str, Enum):
    """
    Optional. The type of annotation to be performed on this data. You must specify this field if you are using this InputConfig in an EvaluationJob.
    """
    ANNOTATION_TYPE_UNSPECIFIED = "ANNOTATION_TYPE_UNSPECIFIED"
    IMAGE_CLASSIFICATION_ANNOTATION = "IMAGE_CLASSIFICATION_ANNOTATION"
    """
    Classification annotations in an image. Allowed for continuous evaluation.
    """
    IMAGE_BOUNDING_BOX_ANNOTATION = "IMAGE_BOUNDING_BOX_ANNOTATION"
    """
    Bounding box annotations in an image. A form of image object detection. Allowed for continuous evaluation.
    """
    IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION = "IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION"
    """
    Oriented bounding box. The box does not have to be parallel to horizontal line.
    """
    IMAGE_BOUNDING_POLY_ANNOTATION = "IMAGE_BOUNDING_POLY_ANNOTATION"
    """
    Bounding poly annotations in an image.
    """
    IMAGE_POLYLINE_ANNOTATION = "IMAGE_POLYLINE_ANNOTATION"
    """
    Polyline annotations in an image.
    """
    IMAGE_SEGMENTATION_ANNOTATION = "IMAGE_SEGMENTATION_ANNOTATION"
    """
    Segmentation annotations in an image.
    """
    VIDEO_SHOTS_CLASSIFICATION_ANNOTATION = "VIDEO_SHOTS_CLASSIFICATION_ANNOTATION"
    """
    Classification annotations in video shots.
    """
    VIDEO_OBJECT_TRACKING_ANNOTATION = "VIDEO_OBJECT_TRACKING_ANNOTATION"
    """
    Video object tracking annotation.
    """
    VIDEO_OBJECT_DETECTION_ANNOTATION = "VIDEO_OBJECT_DETECTION_ANNOTATION"
    """
    Video object detection annotation.
    """
    VIDEO_EVENT_ANNOTATION = "VIDEO_EVENT_ANNOTATION"
    """
    Video event annotation.
    """
    TEXT_CLASSIFICATION_ANNOTATION = "TEXT_CLASSIFICATION_ANNOTATION"
    """
    Classification for text. Allowed for continuous evaluation.
    """
    TEXT_ENTITY_EXTRACTION_ANNOTATION = "TEXT_ENTITY_EXTRACTION_ANNOTATION"
    """
    Entity extraction for text.
    """
    GENERAL_CLASSIFICATION_ANNOTATION = "GENERAL_CLASSIFICATION_ANNOTATION"
    """
    General classification. Allowed for continuous evaluation.
    """


class GoogleCloudDatalabelingV1beta1InputConfigDataType(str, Enum):
    """
    Required. Data type must be specifed when user tries to import data.
    """
    DATA_TYPE_UNSPECIFIED = "DATA_TYPE_UNSPECIFIED"
    """
    Data type is unspecified.
    """
    IMAGE = "IMAGE"
    """
    Allowed for continuous evaluation.
    """
    VIDEO = "VIDEO"
    """
    Video data type.
    """
    TEXT = "TEXT"
    """
    Allowed for continuous evaluation.
    """
    GENERAL_DATA = "GENERAL_DATA"
    """
    Allowed for continuous evaluation.
    """


class InstructionDataType(str, Enum):
    """
    Required. The data type of this instruction.
    """
    DATA_TYPE_UNSPECIFIED = "DATA_TYPE_UNSPECIFIED"
    """
    Data type is unspecified.
    """
    IMAGE = "IMAGE"
    """
    Allowed for continuous evaluation.
    """
    VIDEO = "VIDEO"
    """
    Video data type.
    """
    TEXT = "TEXT"
    """
    Allowed for continuous evaluation.
    """
    GENERAL_DATA = "GENERAL_DATA"
    """
    Allowed for continuous evaluation.
    """
