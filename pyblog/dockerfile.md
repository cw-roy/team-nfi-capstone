FROM python:3.8-alpine
copy . /nfiapp
Run pip3 install -r /nfiapp/requirements.txt
ENTRYPOINT ["python3", "pyblog.py"]