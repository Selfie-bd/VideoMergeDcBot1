FROM ubuntu:20.04

RUN mkdir /app
RUN chmod 777 /app


RUN apt -qq update
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata
RUN apt -qq install -y git python3 python3-pip

RUN git clone https://github.com/Selfie-bd/VideoMergeDcBot1.git /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash","run.sh"]
