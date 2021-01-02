FROM ubuntu:20.04

# Create some base directories
RUN mkdir /flask_app

COPY requirements.txt /requirements.txt

# Set TZ-data environment
ENV TZ=Europa/Amsterdam

# Install base utils
RUN DEBIAN_FRONTEND="noninteractive" \
 && apt-get update \
 && apt-get -y install --no-install-recommends tzdata python3 python3-pip python3-crypto npm \
 && pip3 install -r /requirements.txt

# Add source
COPY . /flask_app/
RUN chmod +x /flask_app/init.sh

# Compile vue
RUN cd /flask_app/vue_web_code \
 && npm install \
 && npm run build

# Entrypoint for this docker
RUN chmod +x /flask_app/run.py
WORKDIR /flask_app
ENTRYPOINT /flask_app/init.sh
EXPOSE 8888
