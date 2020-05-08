#USE PYTHON AS BASE IMAGE
FROM python:3.7-slim
#USE WORKING DIRECTORY /app
WORKDIR /
RUN apt-get update && apt-get -y install default-libmysqlclient-dev gcc
#COPT CONTENTS to /app
ADD . /app
WORKDIR /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
ENV NAME OpentoAll
CMD ["python","app.py"]