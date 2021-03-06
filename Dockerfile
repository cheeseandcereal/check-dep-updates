FROM python:3.8-alpine AS base

WORKDIR /usr/src/app
# Install runtime dependencies
RUN apk --no-cache upgrade

FROM base AS builder
# Install build dependencies
# RUN apk --no-cache add make
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

FROM base AS release
# Copy the installed python dependencies from the builder
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
# Copy the app
COPY --chown=1000:1000 . .

USER 1000:1000
CMD [ "python", "-m", "check_dep_updates.cli" ]
