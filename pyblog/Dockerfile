FROM python:3.8-alpine
WORKDIR /pyblog
COPY requirements.txt /pyblog/
COPY Dockerfile /pyblog/
COPY pyblog.py /pyblog/
RUN pip install -r ./requirements.txt
EXPOSE 8080
CMD python ./pyblog.py
