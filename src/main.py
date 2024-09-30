"""Text split microservice."""

import sentry_sdk
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App settings. Get from .env file, otherwise use predefined."""

    # TODO: Set your own environment variables

    greet: str = 'Hello'

    sentry_url: str = (
        'https://0000@sentry.domain.com/0'  # TODO: change sentry url
    )

    model_config = SettingsConfigDict(
        env_prefix='ms_template_',  # TODO: change service url
        env_file=['/build/.env'],
    )


settings: Settings = Settings()

sentry_sdk.init(dsn=settings.sentry_url, traces_sample_rate=1.0)


class RequestBody(BaseModel):
    """Request body."""

    # TODO: Set your own request body
    text: str
    model_config = ConfigDict(extra='forbid')


class ResponseBody(BaseModel):
    """Response body."""

    # TODO: Set your own response body
    text: str
    model_config = ConfigDict(extra='forbid')


class Service:
    """Main logic."""

    def process(self, request: RequestBody) -> ResponseBody:
        # TODO: Set your own logic
        """Process request.

        Args:
            request (RequestBody): request body.

        Returns:
            ResponseBody: response body
        """
        return ResponseBody(text=' '.join((settings.greet, request.text)))


service: Service = Service()
app: FastAPI = FastAPI()


@app.post('/')
async def text_split(request: RequestBody) -> ResponseBody:
    # TODO: write endpoint description.
    """Process endpoint.

    Args:
        request (RequestBody): Request body, details below.

    Returns:
        ResponseBody: Response body, details below.
    """
    return service.process(request)
