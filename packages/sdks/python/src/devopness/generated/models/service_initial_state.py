"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

import json
from enum import Enum
from typing import Literal, Self


class ServiceInitialState(str, Enum):
    """
    The expected initial state of the service after installed
    """

    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        """Return the string representation of the ServiceInitialState"""
        return self.value

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ServiceInitialState from a JSON string"""
        return cls(json.loads(json_str))


# The plain version of ServiceInitialState
ServiceInitialStatePlain = Literal[
    "started",
    "stopped",
]
