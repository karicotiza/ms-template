"""Schemathesis tests."""

from schemathesis import experimental, models
from schemathesis.specs.openapi import loaders, schemas

from src.main import app

experimental.OPEN_API_3_1.enable()

schema: schemas.BaseOpenAPISchema = loaders.from_asgi('/openapi.json', app)


@schema.parametrize()
async def test_schemathesis(case: models.Case) -> None:
    """Schemathesis tests.

    Args:
        case (models.Case): Schemathesis injection.
    """
    case.call_and_validate()
