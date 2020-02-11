FROM python:3.7

WORKDIR /var/app
COPY . /var/app
COPY .env /var/app/.env

RUN pip install -r requirements.txt
RUN pip install python-dotenv boto3

EXPOSE 8000

CMD flask run -p 8000 --host=0.0.0.0