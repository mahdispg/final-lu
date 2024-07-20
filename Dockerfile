FROM python:3.12.3

WORKDIR /fastapi

COPY ./requirements.txt /fastapi

RUN pip install -r requirements.txt

COPY . /fastapi

CMD ["fastapi", "run", "project/main.py"]
