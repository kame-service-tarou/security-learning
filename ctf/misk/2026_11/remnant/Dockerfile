FROM python:3.15.2-slim-trixie
RUN apt-get update && apt-get -yq install socat
COPY server.py ./
CMD ["socat", "-T60", "TCP-L:1337,fork,reuseaddr", "EXEC:'python server.py',stderr"]
