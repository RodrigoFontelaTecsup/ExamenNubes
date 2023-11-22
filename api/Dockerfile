FROM python:3.8

WORKDIR /app/api

COPY movies.csv /app/api

COPY ratings.csv /app/api

COPY main.py /app/api

COPY requirements.txt /app/api

RUN pip install -r requirements.txt

RUN chmod a+x main.py

RUN chmod +x main.py

ENTRYPOINT ["python", "main.py"]