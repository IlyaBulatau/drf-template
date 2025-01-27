FROM python:3.11.9-slim-bullseye as builder

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /install

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
    gcc \
    python3-dev \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .

RUN pip install poetry && poetry export -o req.txt --without-hashes --dev

RUN --mount=type=cache,target=/root/.cache/pip/ \
    pip install --upgrade pip && \
    pip install --prefix=/install -r req.txt

FROM python:3.11.9-slim-bullseye

COPY --from=builder /install /usr/local

WORKDIR /home/code

COPY src/ .

RUN groupadd -r app && \
    useradd -r -g app app && \
    chmod 775 -R /home/code

USER app