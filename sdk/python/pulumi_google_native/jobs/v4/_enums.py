# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CompanySize',
    'CompensationEntryType',
    'CompensationEntryUnit',
    'JobDegreeTypesItem',
    'JobEmploymentTypesItem',
    'JobJobBenefitsItem',
    'JobJobLevel',
    'JobPostingRegion',
    'ProcessingOptionsHtmlSanitization',
]


class CompanySize(str, Enum):
    """
    The employer's company size.
    """
    COMPANY_SIZE_UNSPECIFIED = "COMPANY_SIZE_UNSPECIFIED"
    MINI = "MINI"
    SMALL = "SMALL"
    SMEDIUM = "SMEDIUM"
    MEDIUM = "MEDIUM"
    BIG = "BIG"
    BIGGER = "BIGGER"
    GIANT = "GIANT"


class CompensationEntryType(str, Enum):
    """
    Compensation type. Default is CompensationType.COMPENSATION_TYPE_UNSPECIFIED.
    """
    COMPENSATION_TYPE_UNSPECIFIED = "COMPENSATION_TYPE_UNSPECIFIED"
    BASE = "BASE"
    BONUS = "BONUS"
    SIGNING_BONUS = "SIGNING_BONUS"
    EQUITY = "EQUITY"
    PROFIT_SHARING = "PROFIT_SHARING"
    COMMISSIONS = "COMMISSIONS"
    TIPS = "TIPS"
    OTHER_COMPENSATION_TYPE = "OTHER_COMPENSATION_TYPE"


class CompensationEntryUnit(str, Enum):
    """
    Frequency of the specified amount. Default is CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED.
    """
    COMPENSATION_UNIT_UNSPECIFIED = "COMPENSATION_UNIT_UNSPECIFIED"
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"
    ONE_TIME = "ONE_TIME"
    OTHER_COMPENSATION_UNIT = "OTHER_COMPENSATION_UNIT"


class JobDegreeTypesItem(str, Enum):
    DEGREE_TYPE_UNSPECIFIED = "DEGREE_TYPE_UNSPECIFIED"
    PRIMARY_EDUCATION = "PRIMARY_EDUCATION"
    LOWER_SECONDARY_EDUCATION = "LOWER_SECONDARY_EDUCATION"
    UPPER_SECONDARY_EDUCATION = "UPPER_SECONDARY_EDUCATION"
    ADULT_REMEDIAL_EDUCATION = "ADULT_REMEDIAL_EDUCATION"
    ASSOCIATES_OR_EQUIVALENT = "ASSOCIATES_OR_EQUIVALENT"
    BACHELORS_OR_EQUIVALENT = "BACHELORS_OR_EQUIVALENT"
    MASTERS_OR_EQUIVALENT = "MASTERS_OR_EQUIVALENT"
    DOCTORAL_OR_EQUIVALENT = "DOCTORAL_OR_EQUIVALENT"


class JobEmploymentTypesItem(str, Enum):
    EMPLOYMENT_TYPE_UNSPECIFIED = "EMPLOYMENT_TYPE_UNSPECIFIED"
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACTOR = "CONTRACTOR"
    CONTRACT_TO_HIRE = "CONTRACT_TO_HIRE"
    TEMPORARY = "TEMPORARY"
    INTERN = "INTERN"
    VOLUNTEER = "VOLUNTEER"
    PER_DIEM = "PER_DIEM"
    FLY_IN_FLY_OUT = "FLY_IN_FLY_OUT"
    OTHER_EMPLOYMENT_TYPE = "OTHER_EMPLOYMENT_TYPE"


class JobJobBenefitsItem(str, Enum):
    JOB_BENEFIT_UNSPECIFIED = "JOB_BENEFIT_UNSPECIFIED"
    CHILD_CARE = "CHILD_CARE"
    DENTAL = "DENTAL"
    DOMESTIC_PARTNER = "DOMESTIC_PARTNER"
    FLEXIBLE_HOURS = "FLEXIBLE_HOURS"
    MEDICAL = "MEDICAL"
    LIFE_INSURANCE = "LIFE_INSURANCE"
    PARENTAL_LEAVE = "PARENTAL_LEAVE"
    RETIREMENT_PLAN = "RETIREMENT_PLAN"
    SICK_DAYS = "SICK_DAYS"
    VACATION = "VACATION"
    VISION = "VISION"


class JobJobLevel(str, Enum):
    """
    The experience level associated with the job, such as "Entry Level".
    """
    JOB_LEVEL_UNSPECIFIED = "JOB_LEVEL_UNSPECIFIED"
    ENTRY_LEVEL = "ENTRY_LEVEL"
    EXPERIENCED = "EXPERIENCED"
    MANAGER = "MANAGER"
    DIRECTOR = "DIRECTOR"
    EXECUTIVE = "EXECUTIVE"


class JobPostingRegion(str, Enum):
    """
    The job PostingRegion (for example, state, country) throughout which the job is available. If this field is set, a LocationFilter in a search query within the job region finds this job posting if an exact location match isn't specified. If this field is set to PostingRegion.NATION or PostingRegion.ADMINISTRATIVE_AREA, setting job Job.addresses to the same location level as this field is strongly recommended.
    """
    POSTING_REGION_UNSPECIFIED = "POSTING_REGION_UNSPECIFIED"
    ADMINISTRATIVE_AREA = "ADMINISTRATIVE_AREA"
    NATION = "NATION"
    TELECOMMUTE = "TELECOMMUTE"


class ProcessingOptionsHtmlSanitization(str, Enum):
    """
    Option for job HTML content sanitization. Applied fields are: * description * applicationInfo.instruction * incentives * qualifications * responsibilities HTML tags in these fields may be stripped if sanitiazation isn't disabled. Defaults to HtmlSanitization.SIMPLE_FORMATTING_ONLY.
    """
    HTML_SANITIZATION_UNSPECIFIED = "HTML_SANITIZATION_UNSPECIFIED"
    HTML_SANITIZATION_DISABLED = "HTML_SANITIZATION_DISABLED"
    SIMPLE_FORMATTING_ONLY = "SIMPLE_FORMATTING_ONLY"