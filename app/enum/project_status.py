from enum import Enum

class ProjectStatus(Enum):
    IN_PROGRESS = 1
    INACTIVE = 2
    COMPLETED = 3
    UNPUBLISHED = 4
    PUBLISHED = 5
    APPLICATION_SUBMITTED = 6,
    CHURNED = 7,
    PENDING = 8,
    DRAFT = 9,
    ACTIVE = 10