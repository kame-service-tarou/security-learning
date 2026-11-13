# NOTE: This hash is pinned to avoid version and environment differences.
FROM ubuntu:22.04@sha256:3ba65aa20f86a0fad9df2b2c259c613df006b2e6d0bfcc8a146afb8c525a9751

ENV DEBIAN_FRONTEND=noninteractive
ENV WINEDEBUG=-all

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wine64 \
        socat \
        ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* /tmp/*

RUN /usr/bin/wine64-stable wineboot --init

WORKDIR /app

COPY chall.exe .
COPY flag.txt .

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork \
    EXEC:"/usr/bin/wine64-stable ./chall.exe",stderr