FROM python:3.7-slim as base

ENV PUID=${PUID:-1000}
ENV PGID=${PGID:-1000}
ENV APP_DIR="/code"
ENV PYTHONUNBUFFERED 1

# create user/group
RUN set -ex \
  && addgroup --gid $PGID python \
  && useradd -u $PUID -g $PGID python \
  && mkdir -p /env /home/python $APP_DIR

# create and activate our virtual env
RUN set -ex \
  && python3 -m venv /env \
  && cat /env/bin/activate > /home/python/.bashrc \
  && chown -R python.python /env /home/python $APP_DIR

# install dev dependencys
RUN set -ex \
 && apt-get update && apt-get install -y --no-install-recommends \
   git \
   vim \
   make \
 && rm -rf /var/lib/apt/lists/*

# install base python deps
USER python
COPY --chown=python:python requirements.txt $APP_DIR/requirements.txt
RUN set -ex &&  /env/bin/pip install -r $APP_DIR/requirements.txt

WORKDIR $APP_DIR

ENV PATH="/env/bin:/code:${PATH}"
USER python

CMD ["make", "build"]
