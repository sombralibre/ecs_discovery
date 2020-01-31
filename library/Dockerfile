FROM python:3.7-alpine

COPY  requirements.txt /tmp/reqs.txt
COPY  app.py /app.py
RUN pip install -r /tmp/reqs.txt

EXPOSE 8080

CMD ["python", "/app.py"]