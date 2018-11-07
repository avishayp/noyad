FROM python:3-alpine

WORKDIR /srv

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . server

EXPOSE 8888
CMD python -m server
