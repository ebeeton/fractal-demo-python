# syntax=docker/dockerfile:1
FROM python:3.10-alpine

WORKDIR /app
COPY requirements.txt requirements.txt

# Install requirements for Pillow, and temporarily include gcc and musl libc.
# Create a system user so the app does not run as root.
RUN apk add zlib-dev jpeg-dev && \
    apk add --virtual .pillow-reqs gcc musl-dev && \
    pip install -r requirements.txt && \
    apk del .pillow-reqs && \
    adduser -S notroot

COPY fractal/ .

USER notroot

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
