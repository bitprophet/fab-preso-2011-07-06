def hello(name=None):
    print("Hello %s!" % (name or "world"))

from fabric.api import run, puts, hide

def stereotype():
    with hide('everything'):
        os_type = run("uname -s")
    if os_type == "Linux":
        puts("Gross, a neckbeard :(")
    elif os_type == "Darwin":
        puts("Hipster spotted!")



import requests
from fabric.api import env, run

def _fetch_role(name):
    uri = "http://my/catalog/?role=%s" % name
    return requests.get(uri).content.splitlines()

env.roledefs = {
    'web': lambda: _fetch_role('web'),
    'db': lambda: _role('database')
}

def mytask():
    run("command")
