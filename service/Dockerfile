FROM python:3.11-slim as backend
COPY backend/ /backend/
WORKDIR /backend/

ENV SERVICE_HOST 0.0.0.0
ENV SERVICE_PORT 11111
ENV SERVER_HOST 0.0.0.0
ENV SERVER_PORT 11112
ENV LOG_LEVEL info

ENV TITLE TurnOff Commander
ENV VERSION 0.1
ENV DOCS_ENABLED true
ENV DOCS_URL api/docs

ENV POSTGRES_HOST 0.0.0.0
ENV POSTGRES_PORT 5432
ENV POSTGRES_DATABASE database
ENV POSTGRES_USER root
ENV POSTGRES_PASSWORD password

ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install -r requirements.txt

EXPOSE $SERVICE_PORT-$SERVER_PORT
CMD [ "bash", "start.sh" ]


FROM node:lts-alpine as frontend

COPY frontend/ /frontend/
WORKDIR /frontend/

RUN npm install @vue/cli@5.0.8 -g
RUN npm install

CMD ["npm", "run", "serve"]
