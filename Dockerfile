FROM python:3.9

WORKDIR /app

RUN pip install fastapi
RUN pip install uvicorn
RUN pip install sqlalchemy
RUN pip install pydantic
RUN pip install python-multipart

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]