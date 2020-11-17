FROM debian:jessie
  
RUN apt-get update && apt-get install -y \
    git \
    curl \
    jq    \
    python2.7

WORKDIR /root
RUN ["/bin/bash", "-c", "mkdir data && cd data && while read i; do git clone $i; done < <(curl -s https://api.github.com/orgs/datasets/repos?per_page=100 | jq -r '.[].clone_url')"]

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python2.7 get-pip.py
RUN pip install numpy pandas sqlalchemy pymysql
