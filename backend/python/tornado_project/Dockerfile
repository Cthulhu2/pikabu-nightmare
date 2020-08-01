FROM python:3.7.8-alpine3.12

## install dependencies
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && apk add netcat-openbsd

## set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## set working directory
WORKDIR /usr/src/app

## add user
RUN adduser -D user
RUN chown -R user:user /usr/src/app && chmod -R 755 /usr/src/app


COPY requirements.txt /usr/src/app/

## add and install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

## switch to non-root user
USER user
COPY users/ /usr/src/app/

EXPOSE 5000

CMD [ "python", "/usr/src/app/__init__.py" ]
