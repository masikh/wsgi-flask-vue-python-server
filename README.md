## Documentation
This template server is based on Python (3.x), Flask, WSGI, Vue and MongoDB.

This example shows how to create a WSGI Flask server with APIDOCS (swagger) and routes splitted into separate files. In this example I made the routes into separate files to show case how that can be done. Also I included some example class file to show how to make use of it into your routes, get app data into blueprint routes and so on...

#### Features:

- API Docs
- Dockerbuild
- Vue
- Flask
- WSGI
- MongoDB
- Bootstrap
- Single page web-application
- Threaded application, main program can do something else...
- Show case of class files imported into routes
- Show case of configuration parameters shared across the program
- Show case of tidy project structure

#### Why???

Most examples are either highly detailed on a certain aspect of Flask/WSGI or to simple. It serves as a jumpstart into
a project. 

#### Database setup
This template server will use a  mongodb with authentication enabled. Open a mongo shell to your database server and execute the 
following statements. Replace the username and password with your appropriate settings, also reflect the settings in
the file Configuration/server.py. It uses the default database: 'wsgi_flask_vue_template'

```
use admin
db.createUser({user: 'admin', pwd: 'secret', roles: [{role: 'root', db: 'admin'}]})
```

Now change the mongodb.conf to enable authentication. This is a minimal sample configuration 

```
dbpath=/var/lib/mongodb
logpath=/var/log/mongodb/mongodb.log
logappend=true
bind_ip = 127.0.0.1
journal=true
auth = true
```

### Install python requirements
```
sudo python3 -m pip install -r requirements.txt
```


### Compile VUE
change directory to 'vue_web_code' and run:
```
npm install
npm run build
npm run build_dev (*)
```
\* used for during development


### Lints and fixes files
```
npm run lint
```

### Customize Vue configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

#### Default user
At first startup a default login user will be created
```
username: admin
password: admin
```

#### Docker build and execution

```
┌(masikh@garthim.masikh.org)-(jobs:0)-(/Users/.3./flask_wsgi_vue)-(11 files,48b)
└> 560 ● docker build .
Sending build context to Docker daemon    163MB
Step 1/12 : FROM ubuntu:20.04
 ---> d70eaf7277ea
Step 2/12 : RUN mkdir /flask_app
 ---> Using cache
 ---> 10531c67484b
Step 3/12 : COPY requirements.txt /requirements.txt
 ---> Using cache
 ---> b25383677884
Step 4/12 : ENV TZ=Europa/Amsterdam
 ---> Using cache
 ---> e38cbb328799
Step 5/12 : RUN DEBIAN_FRONTEND="noninteractive"  && apt-get update  && apt-get -y install --no-install-recommends tzdata python3 python3-pip python3-crypto npm  && pip3 install -r /requirements.txt
 ---> Using cache
 ---> d83d6c9d6809
Step 6/12 : COPY . /flask_app/
 ---> Using cache
 ---> 33e629d3d176
Step 7/12 : RUN chmod +x /flask_app/init.sh
 ---> Using cache
 ---> 2b5bd3379089
Step 8/12 : RUN cd /flask_app/vue_web_code  && npm install  && npm run build
 ---> Using cache
 ---> 96cd78df5769
Step 9/12 : RUN chmod +x /flask_app/run.py
 ---> Using cache
 ---> 037549ec96a0
Step 10/12 : WORKDIR /flask_app
 ---> Using cache
 ---> 44cc7e0a3b2b
Step 11/12 : ENTRYPOINT /flask_app/init.sh
 ---> Using cache
 ---> b7d0dc18851b
Step 12/12 : EXPOSE 8888
 ---> Using cache
 ---> 25843143d6f5
Successfully built 25843143d6f5

┌(masikh@garthim.masikh.org)-(jobs:0)-(/Users/.3./flask_wsgi_vue)-(11 files,48b)
└> 561 ● docker run -p 8888:8888 -e DB=darkcrystal.masikh.org 25843143d6f5 bash

Initializing environment

---------------------------------
HOSTNAME=9509c5f261ee
DB=darkcrystal.masikh.org

---------------------------------
Initializing environment done

---------------------------------
Starting: Server
```