FROM python:3.10-slim

WORKDIR /app

## Install Tkinter
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

RUN apt-get update -y
RUN apt-get install -y python3-tk

### Upgrade pip
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8988

COPY . .
ENTRYPOINT [ "python3" ]
CMD [ "test.py" ]
