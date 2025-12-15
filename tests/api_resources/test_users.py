# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from userplex import Userplex, AsyncUserplex
from tests.utils import assert_matches_type
from userplex.types import UserIdentifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_identify(self, client: Userplex) -> None:
        user = client.users.identify(
            user_id="user_id",
        )
        assert_matches_type(UserIdentifyResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_identify_with_all_params(self, client: Userplex) -> None:
        user = client.users.identify(
            user_id="user_id",
            email="dev@stainless.com",
            name="name",
            properties={"foo": "bar"},
        )
        assert_matches_type(UserIdentifyResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_identify(self, client: Userplex) -> None:
        response = client.users.with_raw_response.identify(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserIdentifyResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_identify(self, client: Userplex) -> None:
        with client.users.with_streaming_response.identify(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserIdentifyResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_identify(self, async_client: AsyncUserplex) -> None:
        user = await async_client.users.identify(
            user_id="user_id",
        )
        assert_matches_type(UserIdentifyResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_identify_with_all_params(self, async_client: AsyncUserplex) -> None:
        user = await async_client.users.identify(
            user_id="user_id",
            email="dev@stainless.com",
            name="name",
            properties={"foo": "bar"},
        )
        assert_matches_type(UserIdentifyResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_identify(self, async_client: AsyncUserplex) -> None:
        response = await async_client.users.with_raw_response.identify(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserIdentifyResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_identify(self, async_client: AsyncUserplex) -> None:
        async with async_client.users.with_streaming_response.identify(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserIdentifyResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
