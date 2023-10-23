FROM python:3.11-slim
COPY . /backend/
WORKDIR /backend

ENV SERVER_HOST 0.0.0.0
ENV SERVER_PORT 11111
ENV LOG_LEVEL info

ENV TITLE TurnOff Commander
ENV VERSION 0.1
ENV DOCS_ENABLED true
ENV DOCS_URL api/docs
ENV ROOT_LOGIN root
ENV ROOT_PASSWORD password

ENV POSTGRES_HOST 0.0.0.0
ENV POSTGRES_PORT 5432
ENV POSTGRES_DATABASE database
ENV POSTGRES_USER root
ENV POSTGRES_PASSWORD password

ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install -r requirements.txt

EXPOSE $SERVER_PORT
CMD [ "bash", "start.sh" ]