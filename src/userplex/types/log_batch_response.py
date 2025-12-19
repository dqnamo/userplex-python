# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["LogBatchResponse"]


class LogBatchResponse(BaseModel):
    count: float
    """Number of logs processed"""

    success: bool
    """Operation success status"""
