FROM python:3.7.12-slim

RUN pip install flask && \
    groupadd -r flask && useradd -r -g flask flask && \
    mkdir /src && \
    chown -R flask:flask /src

COPY static/ /src/static/
COPY templates/ /src/templates/

COPY DigitalKlotski.py /src/DigitalKlotski.py
COPY app.py /src/app.py
COPY config.py /src/config.py

WORKDIR /src
ENV FLASK=app.py
EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]
