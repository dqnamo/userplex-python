# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from userplex import Userplex, AsyncUserplex
from tests.utils import assert_matches_type
from userplex.types import LogNewResponse, LogBatchResponse
from userplex._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch(self, client: Userplex) -> None:
        log = client.logs.batch(
            logs=[
                {
                    "name": "name",
                    "user_id": "user_id",
                }
            ],
        )
        assert_matches_type(LogBatchResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch(self, client: Userplex) -> None:
        response = client.logs.with_raw_response.batch(
            logs=[
                {
                    "name": "name",
                    "user_id": "user_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogBatchResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch(self, client: Userplex) -> None:
        with client.logs.with_streaming_response.batch(
            logs=[
                {
                    "name": "name",
                    "user_id": "user_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogBatchResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_new(self, client: Userplex) -> None:
        log = client.logs.new(
            name="name",
            user_id="user_id",
        )
        assert_matches_type(LogNewResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_new_with_all_params(self, client: Userplex) -> None:
        log = client.logs.new(
            name="name",
            user_id="user_id",
            data={"foo": "bar"},
            properties={"foo": "bar"},
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(LogNewResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_new(self, client: Userplex) -> None:
        response = client.logs.with_raw_response.new(
            name="name",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogNewResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_new(self, client: Userplex) -> None:
        with client.logs.with_streaming_response.new(
            name="name",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogNewResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch(self, async_client: AsyncUserplex) -> None:
        log = await async_client.logs.batch(
            logs=[
                {
                    "name": "name",
                    "user_id": "user_id",
                }
            ],
        )
        assert_matches_type(LogBatchResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncUserplex) -> None:
        response = await async_client.logs.with_raw_response.batch(
            logs=[
                {
                    "name": "name",
                    "user_id": "user_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogBatchResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncUserplex) -> None:
        async with async_client.logs.with_streaming_response.batch(
            logs=[
                {
                    "name": "name",
                    "user_id": "user_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogBatchResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_new(self, async_client: AsyncUserplex) -> None:
        log = await async_client.logs.new(
            name="name",
            user_id="user_id",
        )
        assert_matches_type(LogNewResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_new_with_all_params(self, async_client: AsyncUserplex) -> None:
        log = await async_client.logs.new(
            name="name",
            user_id="user_id",
            data={"foo": "bar"},
            properties={"foo": "bar"},
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(LogNewResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_new(self, async_client: AsyncUserplex) -> None:
        response = await async_client.logs.with_raw_response.new(
            name="name",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogNewResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_new(self, async_client: AsyncUserplex) -> None:
        async with async_client.logs.with_streaming_response.new(
            name="name",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogNewResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True
