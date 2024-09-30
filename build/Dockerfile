FROM python:3.12.5-slim-bookworm AS build

WORKDIR /app

RUN apt update -y
RUN apt install curl -y

RUN python -m pip install fastapi==0.112.2
RUN python -m pip install pydantic-settings==2.5.2
RUN python -m pip install uvicorn==0.30.6
RUN python -m pip install uvloop==0.20.0

RUN python -m pip install sentry-sdk[fastapi]==2.14.0

RUN python -m pip install opentelemetry-distro==0.43b0
RUN python -m pip install opentelemetry-exporter-otlp==1.22.0

# TODO: Change service name
ENV OTEL_RESOURCE_ATTRIBUTES=service.name=ms-template
# TODO: Change signoz address
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://signoz:4317/
ENV OTEL_EXPORTER_OTLP_PROTOCOL=grpc
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

RUN opentelemetry-bootstrap --action=install

FROM build AS prod

COPY ./src/ ./src/

ENTRYPOINT [ "opentelemetry-instrument", "uvicorn", "src.main:app", "--host", "0.0.0.0" ]

FROM build AS test

RUN python -m pip install pytest==8.3.2
RUN python -m pip install schemathesis==3.35.2
RUN python -m pip install wemake-python-styleguide==0.19.2
RUN python -m pip install mypy==1.11.2

COPY ./src/ ./src/
COPY ./tests/ ./tests/