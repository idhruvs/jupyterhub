FROM ubuntu:18.04
LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

# install nodejs, utf8 locale, set CDN because default httpredir is unreliable
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install wget git bzip2 && \
    apt-get -y install npm nodejs
ENV LANG C.UTF-8

# install Python + NodeJS with conda
RUN wget -q https://repo.continuum.io/miniconda/Miniconda3-4.5.1-Linux-x86_64.sh -O /tmp/miniconda.sh  && \
    echo '0c28787e3126238df24c5d4858bd0744 */tmp/miniconda.sh' | md5sum -c - && \
    bash /tmp/miniconda.sh -f -b -p /opt/conda && \
    /opt/conda/bin/conda install --yes -c conda-forge \
      python=3.6 sqlalchemy tornado jinja2 traitlets requests pip pycurl \
      nodejs configurable-http-proxy && \
    /opt/conda/bin/pip install --upgrade pip && \
    rm /tmp/miniconda.sh
ENV PATH=/opt/conda/bin:$PATH

# Adding Users to the Image Container
#RUN useradd -ms /bin/bash idhruvs
#RUN mkdir -p /home/idhruvs/notebooks
#RUN ls -la /home/idhruvs/notebooks 

ADD ./config/jupyterhub-custom-auth /src/jupyterhub-custom-auth
WORKDIR /src/jupyterhub-custom-auth

RUN pip install . 

ADD . /src/jupyterhub
WORKDIR /src/jupyterhub

RUN pip install . && \
    rm -rf $PWD ~/.cache ~/.npm
RUN pip install oauthenticator
RUN pip install --upgrade notebook

RUN mkdir -p /srv/jupyterhub/ 
WORKDIR /srv/jupyterhub/ 
EXPOSE 8000

LABEL org.jupyter.service="jupyterhub"
COPY ./config/jupyterhub_config.py jupyterhub_config.py
CMD ["jupyterhub"]
