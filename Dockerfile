FROM python:3.9

WORKDIR /app

RUN apt update
RUN apt install -y telnet

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY script.py .

CMD [ "python", "./script.py" ]
