# Python Flask WSGI skeleton

This example shows how to create a WSGI Flask server with APIDOCS (swagger) and routes splitted into separate files. In this example I made
the routes into separate files to show case how that can be done. Also I included some example class file to show how
to make use of it into your routes, get app data into blueprint routes and so on...

## Features:

- API Docs
- Dockerbuild
- threaded flask application so the main program can do something else
- Show case of multiple route directives (API/web/etc..)
- Show case of class files imported into routes
- Show case of configuration parameters shared across the program
- Show case of templates
- Show case of static files
- Show case of SSE (server side events)
- Show case of single page web application
- Show case of howto get app parameters in blueprint routes available
- Show case of flask template rendering
- Show case of base template
- Show case of javascript and flask
- Show case of tidy project structure
- Bootstrap

## Why???

Most examples are either highly detailed on a certain aspect of Flask/WSGI or to simple. It serves as a jumpstart into
a project. 

## Usage

    pip install -r requirements.txt
    python ./run.py

or build a Docker container

    ┌(robert@silverbird)-(jobs:0)-(/Users/.1./wsgi-flask-python-server)-(11 files,104b)
    └> 558 ● docker build .
    Sending build context to Docker daemon  540.2kB
    Step 1/10 : FROM ubuntu:17.10
     ---> e211a66937c6
    Step 2/10 : RUN mkdir /flask_app
     ---> Using cache
     ---> c25172fab5d3
    Step 3/10 : RUN apt-get update  && apt-get -y install python python-pip
     ---> Using cache
     ---> 618e9009f7a0
    Step 4/10 : COPY requirements.txt /requirements.txt
     ---> Using cache
     ---> 716b54db5221
    Step 5/10 : RUN pip install -r /requirements.txt
     ---> Using cache
     ---> 48c0e1d90b2e
    Step 6/10 : COPY . /flask_app/
     ---> cad06dbf7de8
    Step 7/10 : RUN chmod +x /flask_app/run.py
     ---> Running in 1835befbed56
    Removing intermediate container 1835befbed56
     ---> 15e2979466e6
    Step 8/10 : WORKDIR /flask_app
     ---> Running in ae550f1ee75d
    Removing intermediate container ae550f1ee75d
     ---> e77f52d932e0
    Step 9/10 : ENTRYPOINT /flask_app/run.py
     ---> Running in 9b5aaf0b1eed
    Removing intermediate container 9b5aaf0b1eed
     ---> 2e4b0d0dd610
    Step 10/10 : EXPOSE 5000
     ---> Running in b78b0fa59058
    Removing intermediate container b78b0fa59058
     ---> 120b56e156f7
    Successfully built 120b56e156f7
    ┌(robert@silverbird)-(jobs:0)-(/Users/.1./wsgi-flask-python-server)-(11 files,104b)
    └> 559 ● docker run -p 5000:5000 120b56e156f7 bash

Now open a webbrowser and go to http://localhost:5000

## Do you like it? 

It's nice to mention my name, or send me an email :)
