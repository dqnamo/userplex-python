# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from userplex import Userplex, AsyncUserplex
from tests.utils import assert_matches_type
from userplex.types import EventNewResponse
from userplex._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_new(self, client: Userplex) -> None:
        event = client.events.new(
            name="name",
            user_id="user_id",
        )
        assert_matches_type(EventNewResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_new_with_all_params(self, client: Userplex) -> None:
        event = client.events.new(
            name="name",
            user_id="user_id",
            properties={"foo": "bar"},
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EventNewResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_new(self, client: Userplex) -> None:
        response = client.events.with_raw_response.new(
            name="name",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventNewResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_new(self, client: Userplex) -> None:
        with client.events.with_streaming_response.new(
            name="name",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventNewResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_new(self, async_client: AsyncUserplex) -> None:
        event = await async_client.events.new(
            name="name",
            user_id="user_id",
        )
        assert_matches_type(EventNewResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_new_with_all_params(self, async_client: AsyncUserplex) -> None:
        event = await async_client.events.new(
            name="name",
            user_id="user_id",
            properties={"foo": "bar"},
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EventNewResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_new(self, async_client: AsyncUserplex) -> None:
        response = await async_client.events.with_raw_response.new(
            name="name",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventNewResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_new(self, async_client: AsyncUserplex) -> None:
        async with async_client.events.with_streaming_response.new(
            name="name",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventNewResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True
