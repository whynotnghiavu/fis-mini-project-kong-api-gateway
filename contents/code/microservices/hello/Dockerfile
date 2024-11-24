FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /services

COPY ./requirements.txt /services/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /services/requirements.txt

COPY . /services
CMD ["bash", "/services/start-service.sh"]
