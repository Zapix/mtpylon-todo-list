# -*- coding: utf-8 -*-
import pytest

from schema import sum


@pytest.mark.asyncio
async def test_sum():
    result = await sum(3, 5)
    assert result == 8
