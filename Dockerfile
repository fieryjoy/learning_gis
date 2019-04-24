FROM ubuntu:18.04
RUN \
apt-get update && \
apt-get -y upgrade && \
apt-get install -y software-properties-common && \
add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable && \
apt-get update && \
apt-get -y upgrade && \
apt-get install -y gsl-bin libgsl-dev libgsl-dbg gsl-doc-info \
    python3.5 python3-pip curl vim devscripts build-essential libncurses5 \
    git debhelper libgeos-dev gdal-bin libgdal-dev python3-gdal libspatialindex-dev && \
apt-get -y autoremove && \
apt-get -y clean

ENV USER up42

RUN useradd -ms /bin/bash $USER
USER $USER

WORKDIR /home/$USER
