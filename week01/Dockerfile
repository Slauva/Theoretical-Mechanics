FROM python:3.10-slim

WORKDIR /app

## Install Tkinter
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

RUN apt-get update -y
RUN apt-get install -y python3-tk

### Upgrade pip
RUN pip install --upgrade pip

COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 3000-8988

COPY task1.py /app/
COPY test.py /app/

RUN export DISPLAY=localhost:0.0

ENTRYPOINT [ "python3" ]
CMD [ "task1.py" ]