FROM python:3.5.4-slim-jessie

# Update
RUN pip install --upgrade pip

# Install app dependencies
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
