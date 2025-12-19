# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["LogNewResponse"]


class LogNewResponse(BaseModel):
    success: bool
    """Operation success status"""
