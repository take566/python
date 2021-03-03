#!/home/take566.com/.pyenv/shims/python3.7
from wsgiref.handlers import CGIHandler
from test import app
CGIHandler().run(app)