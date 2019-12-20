FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04
USER root 
RUN set -x \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends \
        wget \
        bzip2 \
        git \
        python3-dev \      
        unzip \
        gdal-bin libgdal-dev python3-gdal \
	python3-pip \
	libbz2-dev \
	liblzma-dev \
	libcurl4 \
	libcurl4-openssl-dev
	
#RUN rm /usr/bin/python
RUN ln -s /usr/bin/python3 /usr/bin/python
#RUN rm /usr/bin/pip
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN apt-get install -y python3-setuptools	
RUN which python
RUN python --version
RUN pip install wheel
RUN pip install keras==2.2.4 \
        opencv-python \
        tensorflow-gpu==1.14.0 \
	tables \
	tiledb==0.5.2 \
	psutil
RUN pip install pyBigWig
RUN apt-get install -y samtools
RUN pip install pysam
RUN rm /usr/bin/python
RUN ln -s /usr/bin/python3 /usr/bin/python
WORKDIR /root
RUN git clone https://github.com/kundajelab/atlas_resources.git
WORKDIR atlas_resources/train
RUN git pull
RUN chmod +x *sh

RUN git clone https://github.com/kundajelab/kerasAC.git
WORKDIR kerasAC
RUN python setup.py build
RUN python setup.py develop
WORKDIR /root
RUN mkdir /data
RUN mkdir /outputs
