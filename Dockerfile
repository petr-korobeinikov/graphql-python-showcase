FROM python:3.9-alpine as base


FROM base as builder

RUN mkdir /requirements
WORKDIR /requirements
COPY requirements.txt /requirements.txt
RUN pip install --prefix=/requirements -r /requirements.txt


FROM base

COPY --from=builder /requirements /usr/local
COPY app /app
WORKDIR /
CMD ["python", "-m", "app"]
