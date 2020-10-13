from alpine:latest

RUN apk add --no-cache python3-dev 

WORKDIR /app

COPY . /app

RUN set -xe \
    && apk add py3-pip 
    
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt


