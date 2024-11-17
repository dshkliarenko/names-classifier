FROM python:3.10.10-slim-buster

COPY requirements.txt .

RUN apt-get update -y \
&& pip install --upgrade pip \
&& pip install -r requirements.txt \
&& rm -rf /root/.cache/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . .

EXPOSE 8502
CMD ["uvicorn", "scripts.api:app", "--host", "0.0.0.0", "--port", "8502"]
