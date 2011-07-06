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

    $ fab -R webservers -- tail /var/log/apache2/access.log

is directly equivalent to:

    def anonymous():
        run("tail /var/log/apache2/access.log")

followed by:

    $ fab -R webservers anonymous

No need for your own "one-off commands" task!

---

# Fabric 1.0 (2011-03)

---

# Interactivity

    $ fab -H code -- sudo -u postgres psql redmine
    [code] Executing task '<remainder>'
    [code] run: sudo -u postgres psql redmine
    [code] out: [sudo] password for jforcier:
    [code] out: Welcome to psql 8.3.8, the PostgreSQL interactive terminal
    [code] out:
    [code] out: redmine=# select subject from issues limit 5;
    [code] out:                    subject                    
    [code] out: ----------------------------------------------
    [code] out:  SSH key forwarding
    [code] out:  Make use of ssh_config where possible        
    [code] out:  Add timeout support
    [code] out:  Failover between IPv4/IPv6?
    [code] out:  Retry support for put, run, sudo
    [code] out: (5 rows)
    [code] out:
    [code] out: redmine=# \q
    [code] out:

    Done.
    Disconnecting from code... done.

---

# `put`/`get` enhancements

## Sudo-capable `put`

    !python
    put('apache2.conf', '/etc/apache2/', use_sudo=True)

<div style="height: 20px;"></div>

## Globbing

    !python
    get('/var/log/apache2/*.log', 'log_backups/')

<div style="height: 20px;"></div>

## File-like objects on the local end

    !python
    put(StringIO("127.0.0.1    server.com"), "/etc/hosts")

---

# The present

---

# Fabric 1.1 (2011-06)

---

# @task

    !python
    # This shows up in fab --list and may be called
    @task
    def foo():
        pass

    # This doesn't/can't
    def helper():
        pass

---

# Namespaces

`submodule.py`:

    !python
    @task
    def subtask():
        pass

`fabfile.py`:

    !python
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

# Namespace/task improvements (probably 1.2)

---

# Aliases 

Possible `fabfile.py` API:

    !python
    @task(alias="lt")
    def long_descriptive_task_name():
        pass

Possible result:

    $ fab --list
    Available commands:

        long_descriptive_task_name
        lt

---

# Default tasks

Possible `deploy.py` API:

    !python
    @task(default=True)
    def deploy_and_migrate():
        # deploy code
        # migrate database
        # etc

`fabfile.py`:

    !python
    import deploy

Possible result:

    $ fab --list
    Available commands:

        deploy # "fab deploy" now a valid invocation
        deploy.deploy_and_migrate # Same as just calling "fab deploy"

---

# Parallel execution, logging & UI
## (probably 1.3)

* Morgan's multiprocessing branch
* Integration with a logging module
* Prefix customization
* Colorized output by default

---

# Better SSH & networking behavior
## (possibly 1.4)

* Option to skip over unreachable/bad hosts
* Timeout control
* ProxyCommand support via paraproxy
* Option to detect SSH to localhost & replace with `local()`

---

# Much more

Including the previous, our tracker currently has:

* 60 open bug reports
* 70 open feature requests
* 28 open "support" todo items

The Github repository has 133 forks and over 700 watchers (!).

We're moving development entirely to Github soon.

---

# Thanks!

## Links

* **Presentation tool:** Landslide (`https://github.com/adamzap/landslide`)
* **Fabric:** `http://fabfile.org`
* **Changelogs:** `http://docs.fabfile.org/#changes-from-previous-versions`
* **Issues:** `http://code.fabfile.org` (soon: Github Issues)

## Contact

* **Email:** `jeff@bitprophet.org`
* **Google+:** `http://gplus.to/bitprophet`
* **Twitter:** `@bitprophet`
* **Web:** `http://bitprophet.org`
