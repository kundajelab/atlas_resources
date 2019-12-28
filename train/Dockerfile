FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04
USER root
RUN apt-get update -y
RUN apt-get install apt-utils -y 
RUN apt-get install -y \
	cmake \
        bzip2 \
        git \
        python3.7-dev \      
        unzip \
        gdal-bin libgdal-dev python3-gdal \
	python3-pip \
	libbz2-dev \
	liblzma-dev \
	libcurl4 \
	libcurl4-openssl-dev

RUN rm /usr/bin/python3
#RUN rm /usr/bin/python
RUN ln -s /usr/bin/python3.7 /usr/bin/python3
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN apt-get install -y python3-setuptools	
RUN which python
RUN python --version
RUN pip install numpy==1.15.0 \
        keras==2.2.4 \
        opencv-python \
        tensorflow-gpu==1.14.0 \
	tables \
	s3fs \
	boto3
RUN pip install pyBigWig
RUN apt-get install -y samtools
RUN pip install pysam

RUN rm /usr/bin/python
RUN rm /usr/bin/python3
RUN ln -s /usr/bin/python3.7 /usr/bin/python3
RUN ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /root
RUN git clone https://github.com/TileDB-Inc/TileDB-Py.git
WORKDIR TileDB-Py
RUN git checkout release-0.5.3
RUN python setup.py build
RUN python setup.py develop
WORKDIR /root
RUN git clone https://github.com/kundajelab/kerasAC.git
WORKDIR kerasAC
RUN python setup.py build
RUN python setup.py develop

WORKDIR /root
COPY scripts/ scripts/
RUN chmod -R +x scripts
