FROM python:3.10.9-slim

RUN pip install -U pip & pip install pipenv

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY [ "model.bin", "model.bin" ]
COPY [ "batch.py", "batch.py" ]

ENTRYPOINT [ "python", "batch.py" ]