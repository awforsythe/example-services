import os
import pytest
import redis


@pytest.fixture(scope="module")
def redis_client():
    host = os.getenv("REDIS_HOST")
    if not host:
        raise RuntimeError("REDIS_HOST not set!")

    port = os.getenv("REDIS_PORT")
    if not port:
        raise RuntimeError("REDIS_PORT not set!")

    return redis.Redis(host=host, port=port, db=0, decode_responses=True)
