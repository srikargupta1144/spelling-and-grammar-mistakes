FROM python:3.11-slim

WORKDIR /app

ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

#entrypoint
ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]