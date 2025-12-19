# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LogNewParams"]


class LogNewParams(TypedDict, total=False):
    name: Required[str]

    user_id: Required[str]
    """External user ID"""

    data: Dict[str, Optional[object]]
    """Additional log data"""

    properties: Dict[str, Optional[object]]
    """Alias for data, for compatibility"""

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Log timestamp (ISO 8601)"""
