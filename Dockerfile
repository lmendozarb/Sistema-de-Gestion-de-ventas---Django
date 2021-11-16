FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code

RUN apk add --update \
    python3 \
    python3-dev \
    gcc \
    py-pip \
    build-base \
    git \
    wget \
    libxslt-dev \
    xmlsec-dev \
    mariadb-dev \
    libressl-dev \
    libffi \
    cairo-dev \
    pango-dev \
    gdk-pixbuf \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    fontconfig \
    ttf-dejavu

ADD requirements.txt /code/
RUN pip3 install -r requirements.txt

ADD . /code/
