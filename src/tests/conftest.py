import os
import pytest
import redis


@pytest.fixture(scope="module")
def redis_client():
    url = os.getenv("REDIS_URL")
    if not url:
        raise RuntimeError("URL not set!")
    return redis.from_url(url, decode_responses=True)
