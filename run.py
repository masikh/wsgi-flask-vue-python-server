#!/usr/bin/env python
import time
import Configuration
import WSGIServer


if __name__ == "__main__":
    app = WSGIServer.APIServer(Configuration.environment['ip'],
                               Configuration.environment['port'],
                               Configuration.cwd,
                               Configuration.home_directory,
                               Configuration.username,
                               debug=False)

    try:
        while True:
            # Do anything you like here outside of the flask application...
            time.sleep(1)
    except KeyboardInterrupt:
        app.stop()
