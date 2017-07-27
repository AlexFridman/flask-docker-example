FROM ubuntu:latest
MAINTAINER Alexander Fridman "alexfridman@outlook.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
COPY . /packages
WORKDIR /app

# RUN pip install -r app/requirements.txt

RUN pip install packages/Flask-0.12.2-py2.py3-none-any.whl
RUN pip install packages/numpy-1.13.1-cp27-cp27mu-manylinux1_x86_64.whl
RUN pip install packages/pandas-0.18.1-cp27-cp27mu-manylinux1_x86_64.whl
RUN pip install packages/python_dateutil-2.6.1-py2.py3-none-any.whl
RUN pip install packages/pytz-2017.2-py2.py3-none-any.whl
RUN pip install packages/scikit_learn-0.19b2-cp27-cp27mu-manylinux1_x86_64.whl
RUN pip install packages/scipy-0.19.1-cp27-cp27mu-manylinux1_x86_64.whl

ENTRYPOINT ["python"]
CMD ["app/app.py"]