#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/SSRFApp/")

from SSRFApp import app as application
application.secret_key = 'spEIeJL8wr9PCWMVT7As'
