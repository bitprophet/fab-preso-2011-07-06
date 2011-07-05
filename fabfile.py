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
