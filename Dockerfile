FROM alpine:3.5

# Update
RUN apk add --update python py-pip

# Install app dependencies
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Bundle app source
#COPY simpleapp.py /src/simpleapp.py

EXPOSE  8000
#CMD ["python", "/src/simpleapp.py", "-p 8000"]