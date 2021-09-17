FROM python:3.8.2-alpine
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir Flask flask_prometheus_metrics
WORKDIR /
COPY . /
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
