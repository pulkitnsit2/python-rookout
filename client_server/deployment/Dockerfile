FROM python:3.8

RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./client_server .

RUN chmod +x /app/deployment/entrypoint.sh

ENTRYPOINT [ "/usr/bin/dumb-init", "--" ]
CMD [ "/app/deployment/entrypoint.sh" ]
