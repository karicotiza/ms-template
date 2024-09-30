"""FastAPI Tests."""

from fastapi.testclient import TestClient
from httpx import Response

from src.main import app

test_client: TestClient = TestClient(app)
url: str = '/'
success_code: int = 200

# TODO: write your own edge case tests.


def test_edge_case() -> None:
    """Test edge case.

    Raises:
        ValueError: on wrong status code.
        ValueError: on wrong response body.
    """
    payload: dict[str, str] = {'text': 'world!'}
    response: Response = test_client.post(url, json=payload)

    if response.status_code != success_code:
        raise ValueError('Wrong status code')

    if response.content.decode() != '{"text":"Hello world!"}':
        raise ValueError(response.content.decode())
