FROM python:3.9-slim-buster
WORKDIR /app
COPY ./ /app
RUN pip install -r ./requirements.txt
RUN env
EXPOSE 5002
CMD [ "uvicorn", "--port", "5002", "--host", "0.0.0.0", "api:app" ]