FROM ubuntu:17.10

# Create some base directories
RUN mkdir /flask_app

# Install base utils
RUN apt-get update \ 
 && apt-get -y install python python-pip
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Add source 
COPY . /flask_app/

# Entrypoint for this docker
RUN chmod +x /flask_app/run.py
WORKDIR /flask_app
ENTRYPOINT /flask_app/run.py

# Expose the ports
EXPOSE 5000


