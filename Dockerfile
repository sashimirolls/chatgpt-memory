FROM python:3.10
WORKDIR /rest_api
COPY requirements.txt requirements.txt
RUN pip3 install poetry
COPY ./pyproject.toml ./poetry.lock*
RUN pip3 install -r requirements.txt
COPY / /rest_api
CMD ["poetry", "run","uvicorn", "rest_api:app", "--host", "0.0.0.0", "--port 8000"]