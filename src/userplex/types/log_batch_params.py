# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["LogBatchParams", "Log"]


class LogBatchParams(TypedDict, total=False):
    logs: Required[Iterable[Log]]
    """List of logs to track"""


class LogTyped(TypedDict, total=False):
    name: Required[str]

    user_id: Required[str]
    """External user ID"""

    data: Dict[str, Optional[object]]
    """Additional log data"""

    properties: Dict[str, Optional[object]]
    """Alias for data, for compatibility"""

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Log timestamp (ISO 8601)"""


Log: TypeAlias = Union[LogTyped, Dict[str, Optional[object]]]
