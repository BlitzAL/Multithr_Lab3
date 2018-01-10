# our base image
FROM frolvlad/alpine-gxx

#install GCC
#RUN apk add build-base

# Install python and pip
RUN apk add --update python python-dev py-pip   

# upgrade pip
RUN pip install --upgrade pip

# install Python modules needed by the Python app
COPY req.txt /usr/src/app/req.txt
RUN pip install --no-cache-dir -r /usr/src/app/req.txt

# copy files required for the app to run
COPY app.py /usr/src/app/

# tell the port number the container should expose
EXPOSE 5000
EXPOSE 5555

# run the application
CMD ["python", "/usr/src/app/app.py"]
