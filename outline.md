# Fabric - Past, Present & Future

---

# Who am I?

## Jeff Forcier

* Author of *Python Web Development with Django* (2008 / Django 1.0)
* Fabric contributor since 2008 / v0.1, maintainer since 2009 / v0.9
* Python/Ruby dev, Linux sysadmin
* Whiskey Media ops engineer

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

# What's this talk about?

---

# Features you may have missed

---

## 0.9.2
### Package fabfiles
### Lazy roledefs
### Arbitrary remote shell commands
## 1.0
### Interactivity
### put/get: sudo capable, globbing, file-like objs
## 1.1
### namespaces, @task
### exclude\_hosts

---

# Where we're going
## Faster, smaller releases
## Namespace/task improvements
### Aliases
### Default tasks
### Specify wrapper class in @task
## Parallel execution & UI improvements
### Morgan's multiprocessing branch
### Logging
### Prefix customization
### Colorizing output by default
## SSH & networking improvements
### Skip over unreachable hosts
### Timeout control
### ProxyCommand support via paraproxy
### ssh to localhost => local()

---

# Thanks!

## Links

* **Presentation tool:** Landslide (`https://github.com/adamzap/landslide`)
* **Fabric:** `http://fabfile.org`
* **Changelogs:** `http://docs.fabfile.org/#changes-from-previous-versions`

## Contact

* **Email:** `jeff@bitprophet.org`
* **Google+:** `bitprophet@gmail.com`
* **Twitter:** `@bitprophet`
* **Web:** `http://bitprophet.org`
