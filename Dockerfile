FROM python:3.10

WORKDIR /usr/src/app

# dont write pyc files
# dont buffer to stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV OPENAI_API_KEY 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

COPY ./requirements.txt /usr/src/app/requirements.txt

# dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY ./ /usr/src/app
