"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from datetime import datetime
from typing import (
    List,
    Optional,
    Required,
    TypedDict,
    Union,
)

from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated

from .. import DevopnessBaseModel
from .action_status import ActionStatus, ActionStatusPlain
from .action_status_reason_code import (
    ActionStatusReasonCode,
    ActionStatusReasonCodePlain,
)
from .action_step import ActionStep, ActionStepPlain
from .action_target_data import ActionTargetData, ActionTargetDataPlain


class ActionTarget(DevopnessBaseModel):
    """
    ActionTarget

    Attributes:
        id (int): The ID of the action target
        resource_type (str): The type of the cloud resource on which the action must be performed
        resource_type_human_readable (str, optional): Human readable version of the resource type
        resource_id (int): The Id of the cloud resource on which the action must be performed
        status (ActionStatus):
        status_human_readable (str, optional): Human readable version of the action status
        status_reason_code (ActionStatusReasonCode):
        status_reason_human_readable (str, optional): Human readable version of the status reason code
        total_steps (int, optional, nullable): The total number of steps to complete the action
        current_step (ActionStep, optional, nullable):
        steps (List[ActionStep], optional): The list of action steps
        resource_data (ActionTargetData, optional, nullable):
        started_at (datetime, optional, nullable): The date and time when the action started execution (i.e., left the &#x60;pending/queued&#x60; status)
        completed_at (datetime, optional, nullable): The date and time when the action has finished execution
        created_at (datetime): The date and time when the record was created
        updated_at (datetime): The date and time when the record was last updated
    """

    id: StrictInt = Field(description="The ID of the action target")
    resource_type: StrictStr = Field(
        description="The type of the cloud resource on which the action must be performed"
    )
    resource_type_human_readable: Optional[StrictStr] = Field(
        default=None, description="Human readable version of the resource type"
    )
    resource_id: StrictInt = Field(
        description="The Id of the cloud resource on which the action must be performed"
    )
    status: ActionStatus
    status_human_readable: Optional[StrictStr] = Field(
        default=None, description="Human readable version of the action status"
    )
    status_reason_code: ActionStatusReasonCode
    status_reason_human_readable: Optional[StrictStr] = Field(
        default=None, description="Human readable version of the status reason code"
    )
    total_steps: Optional[Annotated[int, Field(le=127, strict=True, ge=0)]] = Field(
        description="The total number of steps to complete the action"
    )
    current_step: Optional[ActionStep]
    steps: Optional[List[Optional[ActionStep]]] = Field(
        default=None, description="The list of action steps"
    )
    resource_data: Optional[ActionTargetData]
    started_at: Optional[datetime] = Field(
        default=None,
        description="The date and time when the action started execution (i.e., left the `pending/queued` status)",
    )
    completed_at: Optional[datetime] = Field(
        default=None,
        description="The date and time when the action has finished execution",
    )
    created_at: datetime = Field(
        description="The date and time when the record was created"
    )
    updated_at: datetime = Field(
        description="The date and time when the record was last updated"
    )


class ActionTargetPlain(TypedDict, total=False):
    """
    Plain version of ActionTarget.
    """

    id: Required[int]
    resource_type: Required[str]
    resource_type_human_readable: Optional[str]
    resource_id: Required[int]
    status: Required[
        Union[
            ActionStatus,
            ActionStatusPlain,
        ]
    ]
    status_human_readable: Optional[str]
    status_reason_code: Required[
        Union[
            ActionStatusReasonCode,
            ActionStatusReasonCodePlain,
        ]
    ]
    status_reason_human_readable: Optional[str]
    total_steps: Optional[int]
    current_step: Optional[
        Union[
            ActionStep,
            ActionStepPlain,
        ]
    ]
    steps: Optional[
        List[
            Union[
                ActionStep,
                ActionStepPlain,
            ]
        ]
    ]
    resource_data: Optional[
        Union[
            ActionTargetData,
            ActionTargetDataPlain,
        ]
    ]
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    created_at: Required[datetime]
    updated_at: Required[datetime]
