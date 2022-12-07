FROM python:3.8-alpine
COPY . /pyblog
RUN apt update
RUN apt install -y python3 python3-pip
RUN pip install -r /app/requirements.txt
EXPOSE 8080
CMD python /pyblog/pyblog.py
