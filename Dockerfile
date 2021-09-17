FROM python:3.8.2-alpine
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir Flask flask_prometheus_metrics
WORKDIR /
COPY . /
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
