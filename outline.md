# Fabric - Past, Present & Future

---

# Who am I?

## Jeff Forcier

* Python/Ruby dev, Linux sysadmin
* Whiskey Media ops engineer
* Author of *Python Web Development with Django* (2008 / Django 1.0)
* Fabric contributor since 2008 / v0.1, maintainer since 2009 / v0.9

---

# What's Fabric?

---

# A Python task runner

`fabfile.py`:

    !python
    def hello(name=None):
        print("Hello %s!" % (name or "world"))

Execution:

    $ fab --list
    Available commands:

        hello

    $ fab hello
    Hello world!

    Done.

    $ fab hello:everybody
    Hello everybody!

    Done.

---

# A high level SSH library

`fabfile.py`:

    !python
    from fabric.api import run, puts, hide

    def stereotype():
        with hide('everything'):
            os_type = run("uname -s")
        if os_type == "Linux":
            puts("Gross, a neckbeard :(")
        elif os_type == "Darwin":
            puts("Hipster spotted!")

Execution:

    $ fab -H localhost,server stereotype
    [localhost] Executing task 'stereotype'
    [localhost] Hipster spotted!
    [server] Executing task 'stereotype'
    [server] Gross, a neckbeard :(

    Done.
    Disconnecting from localhost... done.
    Disconnecting from server... done.

---

# The past

---

# (Stuff you might have missed)

---

# Fabric 0.9.2 (2010-09)

---

# Package fabfiles

Filesystem:

    fabfile
    ├── __init__.py
    ├── submodule1.py
    └── submodule2.py

Contents of `fabfile/__init__.py`:

    !python
    from submodule1 import task2, task3
    from submodule2 import task4

    def task1():
        pass

Result:

    /folder/containing/fabfile/directory $ fab --list

    Available commands:

        task1
        task2
        task3
        task4

---

# Lazy roledefs

`fabfile.py`:

    !python
    import requests
    from fabric.api import env, run

    def _role(name):
        uri = "http://my/catalog/?role=%s" % name
        return requests.get(uri).content.splitlines()

    env.roledefs = {
        'web': lambda: _role('web'),
        'db': lambda: _role('database')
    }

    def mytask():
        ...

Execution:

    $ fab --role=web mytask
    # Looks up 'web' hosts only -- 1 HTTP request, not 2

---

# Arbitrary remote shell commands

Running the following:

    $ fab -H server -- rm /srv/rails/myapp/current/log/production.log

is directly equivalent to:

    def anonymous():
        run("rm /srv/rails/myapp/current/log/production.log")

followed by:

    $ fab -H server anonymous

---

# Fabric 1.0 (2011-03)

---

# Interactivity

How to show this? hrm

---

# Sudo-capable `put`

    put('foo', '/etc/apache2/sites-available/blah.conf', use_sudo=True)

---

# `put`/`get` globbing

    get('/srv/django/myproject/log/*.log', 'log_backups')

---

# File-like objects in `put`/`get`

    put(StringIO("127.0.0.1    server.com"), "/etc/hosts")

---

# The present

---

# Fabric 1.1 (2011-06)

---

# @task

    # This shows up in fab --list and may be called
    @task
    def foo():
        pass

    # This doesn't
    def helper():
        pass

---

# Namespaces

`submodule.py`:

    @task
    def subtask():
        pass

`fabfile.py`:

    import submodule

    @task
    def maintask():
        pass

Result:

    $ fab --list
    Available commands:

        maintask
        submodule.subtask

---

# Where we're going

---

# (Faster, smaller releases!)

---

# Namespace/task improvements

* Aliases
* Default tasks
* Specify wrapper class in @task

---

# Parallel execution, logging & UI

* Morgan's multiprocessing branch
* Logging
* Prefix customization
* Colorizing output by default

---

# Better SSH & networking behavior

* Skip over unreachable hosts
* Timeout control
* ProxyCommand support via paraproxy
* ssh to localhost => local()

---

# Thanks!

## Links

* **Presentation tool:** Landslide (`https://github.com/adamzap/landslide`)
* **Fabric:** `http://fabfile.org`
* **Changelogs:** `http://docs.fabfile.org/#changes-from-previous-versions`
* **Issues:** `http://code.fabfile.org` (soon: Github Issues)

## Contact

* **Email:** `jeff@bitprophet.org`
* **Google+:** `bitprophet@gmail.com`
* **Twitter:** `@bitprophet`
* **Web:** `http://bitprophet.org`
