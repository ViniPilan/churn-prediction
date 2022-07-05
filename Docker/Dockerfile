# Image for: https://github.com/ViniPilan/churn-prediction

FROM ubuntu:22.04

RUN apt update -y
RUN apt install python3 -y
RUN apt install python3-pip -y

RUN pip3 install notebook

COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app
RUN pip3 install -r requirements.txt
COPY . /opt/app

WORKDIR /home

EXPOSE 8888

#docker run --rm -it --name container -p 8888:8888 -v $PWD/:/home/predict vinipilan/churn-predict-image
# jupyter notebook --allow-root --no-browser --ip 0.0.0.0 --port 8888