"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import (
    Optional,
    Required,
    TypedDict,
    Union,
)

from pydantic import Field, StrictBool, StrictInt, StrictStr

from .. import DevopnessBaseModel
from .action_relation_shallow import ActionRelationShallow, ActionRelationShallowPlain
from .service_initial_state import ServiceInitialState, ServiceInitialStatePlain


class ServiceRelation(DevopnessBaseModel):
    """
    ServiceRelation

    Attributes:
        id (int): The unique ID of the given service
        name (str): The human readable service name
        type (str): The service type
        type_human_readable (str): Formatted/human readable version of the service type
        version (str, optional, nullable): The service current installed version
        is_auto_generated (bool): Indicates if the service was auto_generated by &#x60;Devopness&#x60; itself
        auto_start (bool): Indicates if the service will start automatically on operating system boot
        initial_state (ServiceInitialState):
        description (str, optional, nullable): A text describing the service, provided by the service author
        last_action (ActionRelationShallow, optional, nullable):
        created_at (str, optional): The date and time when the record was created
        updated_at (str, optional): The date and time when the record was last updated
    """

    id: StrictInt = Field(description="The unique ID of the given service")
    name: StrictStr = Field(description="The human readable service name")
    type: StrictStr = Field(description="The service type")
    type_human_readable: StrictStr = Field(
        description="Formatted/human readable version of the service type"
    )
    version: Optional[StrictStr] = Field(
        description="The service current installed version"
    )
    is_auto_generated: StrictBool = Field(
        description="Indicates if the service was auto_generated by `Devopness` itself"
    )
    auto_start: StrictBool = Field(
        description="Indicates if the service will start automatically on operating system boot"
    )
    initial_state: ServiceInitialState
    description: Optional[StrictStr] = Field(
        description="A text describing the service, provided by the service author"
    )
    last_action: Optional[ActionRelationShallow] = None
    created_at: Optional[StrictStr] = Field(
        default=None, description="The date and time when the record was created"
    )
    updated_at: Optional[StrictStr] = Field(
        default=None, description="The date and time when the record was last updated"
    )


class ServiceRelationPlain(TypedDict, total=False):
    """
    Plain version of ServiceRelation.
    """

    id: Required[int]
    name: Required[str]
    type: Required[str]
    type_human_readable: Required[str]
    version: Optional[str]
    is_auto_generated: Required[bool]
    auto_start: Required[bool]
    initial_state: Required[
        Union[
            ServiceInitialState,
            ServiceInitialStatePlain,
        ]
    ]
    description: Optional[str]
    last_action: Optional[
        Union[
            ActionRelationShallow,
            ActionRelationShallowPlain,
        ]
    ]
    created_at: Optional[str]
    updated_at: Optional[str]
