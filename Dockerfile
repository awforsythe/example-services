FROM python:3.8-alpine
WORKDIR /usr/app
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
CMD pytest tests
