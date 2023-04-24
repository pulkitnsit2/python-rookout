FROM python:3.8.16-alpine3.17

RUN apk add --update --no-cache dumb-init git build-base python3-dev libc-dev libffi-dev
RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./client_server .

RUN chmod +x /app/deployment/entrypoint.sh

ENTRYPOINT [ "/usr/bin/dumb-init", "--" ]
CMD [ "/app/deployment/entrypoint.sh" ]