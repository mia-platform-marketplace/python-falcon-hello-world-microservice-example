##########################################################################
FROM python:3

EXPOSE 3000
WORKDIR /app

ADD  . /app
RUN pip install falcon
RUN pip install uwsgi


ARG COMMIT_SHA=<not-specified>
RUN echo "%CUSTOM_PLUGIN_SERVICE_NAME%: $COMMIT_SHA" >> ./commit.sha


LABEL maintainer="%CUSTOM_PLUGIN_CREATOR_USERNAME%" \
      name="%CUSTOM_PLUGIN_SERVICE_NAME%" \
      description="%CUSTOM_PLUGIN_SERVICE_NAME%" \
      eu.mia-platform.url="https://www.mia-platform.eu" \
      eu.mia-platform.version="0.1.0" \
      eu.mia-platform.language="Python" \
      eu.mia-platform.framework="Falcon"

CMD ["python", "./app.py"]
