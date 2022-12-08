FROM python:3.8-alpine
COPY . /nfiapp
RUN pip3 install -r /nfiapp/requirements.txt
ENTRYPOINT ["python3", "pyblog.py"]