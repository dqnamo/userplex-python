# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["UserIdentifyParams"]


class UserIdentifyParams(TypedDict, total=False):
    user_id: Required[str]
    """Unique identifier for the user"""

    email: str
    """User email address"""

    name: str
    """User full name"""

    properties: Dict[str, Optional[object]]
    """Additional user properties"""
