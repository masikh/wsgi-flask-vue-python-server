#!/bin/bash

function header {
    printf "\nInitializing environment\n"
}

function footer {
    printf "\n---------------------------------\n"
    env | grep -e HOSTNAME -e HOSTIP -e DB
    printf "\n---------------------------------\n"
    printf "Initializing environment done\n"
    printf "\n---------------------------------\n"
    printf "Starting: Server\n\n"
}

function SERVER {
  python3 /flask_app/run.py
}

function infinity_loop {
  export PYTHONPATH=/flask_app
  while true; do
    # Touch /flask_app/DEBUG, kill run.py and start run.py manually for debugging... :)
    if [[ ! -f "/flask_app/DEBUG" ]]
    then
	    SERVER;
    fi
    sleep 1
  done
}

header
footer
infinity_loop
