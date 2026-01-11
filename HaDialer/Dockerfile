FROM python:3.12-alpine

COPY run.py requirements.txt /
RUN apk add --no-cache usbutils android-tools
RUN pip instqll -r requirements.txt

CMD [ "python", "/run.sh" ]
