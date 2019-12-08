FROM ubuntu:latest
MAINTAINER Felipe Kermentz Ferraz Costa "felipekfcosta@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY ./ ./app
WORKDIR ./app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
