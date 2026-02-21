import pytest
from src.my_pkg import util

@pytest.mark.asyncio
async def test_async_fetch():
    result = await util.async_fetch('foo')
    assert result == 'fetched:foo'
