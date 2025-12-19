# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime

import httpx

from ..types import log_new_params, log_batch_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.log_new_response import LogNewResponse
from ..types.log_batch_response import LogBatchResponse

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dqnamo/userplex-python#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dqnamo/userplex-python#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)

    def batch(
        self,
        *,
        logs: Iterable[log_batch_params.Log],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogBatchResponse:
        """Records multiple log occurrences in a single request.

        Requires a valid API key
        for authentication.

        Args:
          logs: List of logs to track

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/logs/batch",
            body=maybe_transform({"logs": logs}, log_batch_params.LogBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogBatchResponse,
        )

    def new(
        self,
        *,
        name: str,
        user_id: str,
        data: Dict[str, Optional[object]] | Omit = omit,
        properties: Dict[str, Optional[object]] | Omit = omit,
        timestamp: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogNewResponse:
        """
        Creates or uses an existing log and records a log occurrence for an end user.
        Requires a valid API key for authentication.

        Args:
          user_id: External user ID

          data: Additional log data

          properties: Alias for data, for compatibility

          timestamp: Log timestamp (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/log",
            body=maybe_transform(
                {
                    "name": name,
                    "user_id": user_id,
                    "data": data,
                    "properties": properties,
                    "timestamp": timestamp,
                },
                log_new_params.LogNewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogNewResponse,
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dqnamo/userplex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dqnamo/userplex-python#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)

    async def batch(
        self,
        *,
        logs: Iterable[log_batch_params.Log],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogBatchResponse:
        """Records multiple log occurrences in a single request.

        Requires a valid API key
        for authentication.

        Args:
          logs: List of logs to track

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/logs/batch",
            body=await async_maybe_transform({"logs": logs}, log_batch_params.LogBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogBatchResponse,
        )

    async def new(
        self,
        *,
        name: str,
        user_id: str,
        data: Dict[str, Optional[object]] | Omit = omit,
        properties: Dict[str, Optional[object]] | Omit = omit,
        timestamp: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogNewResponse:
        """
        Creates or uses an existing log and records a log occurrence for an end user.
        Requires a valid API key for authentication.

        Args:
          user_id: External user ID

          data: Additional log data

          properties: Alias for data, for compatibility

          timestamp: Log timestamp (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/log",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "user_id": user_id,
                    "data": data,
                    "properties": properties,
                    "timestamp": timestamp,
                },
                log_new_params.LogNewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogNewResponse,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.batch = to_raw_response_wrapper(
            logs.batch,
        )
        self.new = to_raw_response_wrapper(
            logs.new,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.batch = async_to_raw_response_wrapper(
            logs.batch,
        )
        self.new = async_to_raw_response_wrapper(
            logs.new,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.batch = to_streamed_response_wrapper(
            logs.batch,
        )
        self.new = to_streamed_response_wrapper(
            logs.new,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.batch = async_to_streamed_response_wrapper(
            logs.batch,
        )
        self.new = async_to_streamed_response_wrapper(
            logs.new,
        )
