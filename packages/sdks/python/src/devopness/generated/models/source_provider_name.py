"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

import json
from enum import Enum
from typing import Literal, Self


class SourceProviderName(str, Enum):
    """
    The name of the source code provider
    """

    BITBUCKET = "bitbucket"
    GITHUB = "github"
    GITLAB = "gitlab"

    def __str__(self) -> str:
        """Return the string representation of the SourceProviderName"""
        return self.value

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SourceProviderName from a JSON string"""
        return cls(json.loads(json_str))


# The plain version of SourceProviderName
SourceProviderNamePlain = Literal[
    "bitbucket",
    "github",
    "gitlab",
]
