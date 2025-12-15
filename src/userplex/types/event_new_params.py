# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventNewParams"]


class EventNewParams(TypedDict, total=False):
    name: Required[str]

    user_id: Required[str]
    """External user ID"""

    properties: Dict[str, Optional[object]]
    """Additional event properties"""

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Event timestamp (ISO 8601)"""
