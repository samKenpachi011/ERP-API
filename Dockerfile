FROM python:3.9-alpine3.13
LABEL maintenance="samKenpachi011"

ENV PYTHONNUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /pyerp && \
    /pyerp/bin/pip install --upgrade pip && \
    /pyerp/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /pyerp/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        erp-user

ENV PATH="/pyerp/bin:$PATH"

USER erp-user
