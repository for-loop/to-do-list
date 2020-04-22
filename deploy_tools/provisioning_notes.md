Provisioning a new site
=======================

## Required packages

* nginx
* Python 3.6
* virtualenv + pip
* Git

*e.g.*, on Ubuntu:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install nginx git python36 python3.6-venv
```

## Nginx Virtual Host config

* See nginx.template.conf
* Replace DOMAIN with, *e.g.*, staging.my-domain.com

## Systemd service

* See gunicorn-systemd.template.service
* Replace DOMAIN with, *e.g.*, staging.my-domain.com

## Folder structure

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc
