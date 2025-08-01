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
)

from pydantic import Field, StrictInt, StrictStr

from .. import DevopnessBaseModel


class TeamRelation(DevopnessBaseModel):
    """
    TeamRelation

    Attributes:
        id (int): The unique ID of the given team
        name (str): The name of the given team
        photo_url (str, optional, nullable): The URL to team&#39;s image
        created_at (str): The date and time when the record was created
        updated_at (str): The date and time when the record was last updated
    """

    id: StrictInt = Field(description="The unique ID of the given team")
    name: StrictStr = Field(description="The name of the given team")
    photo_url: Optional[StrictStr] = Field(description="The URL to team's image")
    created_at: StrictStr = Field(
        description="The date and time when the record was created"
    )
    updated_at: StrictStr = Field(
        description="The date and time when the record was last updated"
    )


class TeamRelationPlain(TypedDict, total=False):
    """
    Plain version of TeamRelation.
    """

    id: Required[int]
    name: Required[str]
    photo_url: Optional[str]
    created_at: Required[str]
    updated_at: Required[str]
