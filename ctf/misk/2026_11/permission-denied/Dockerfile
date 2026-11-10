FROM python:3.14.4-slim-trixie
RUN apt-get update && apt-get install -yq socat
WORKDIR /app
COPY --chmod=400 chal.sh ./
CMD ["socat", "tcp-listen:1337,fork,reuseaddr", "exec:'bash chal.sh',stderr,pty,ctty,setsid,echo=0"]
