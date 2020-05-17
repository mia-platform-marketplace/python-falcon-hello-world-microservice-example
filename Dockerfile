##########################################################################
FROM python:3

EXPOSE 3000
WORKDIR /app

ADD  . /app
RUN pip install falcon
RUN pip install uwsgi


ARG COMMIT_SHA=<not-specified>
RUN echo assa: $COMMIT_SHA >> ./commit.sha



CMD ["python", "./app.py"]
