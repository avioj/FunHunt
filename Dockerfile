FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3-pip
ADD . /root
RUN chmod -R 777 /root
RUN python3 -m pip install -e /root/
