FROM python:3.7.12-alpine

RUN mkdir /src

COPY DigitalKlotski.py /src/DigitalKlotski.py
COPY app.py /src/app.py

CMD ["python", "./src/app.py"]
