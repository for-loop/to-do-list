# Table of Contents
1. [Dependencies](README.md#dependencies)
2. [Run](README.md#run)
3. [Deploy](README.md#deploy)
4. [Setting up geckodriver on macOS Catalina](README.md#setting-up-geckodriver-on-macos-catalina)

# Dependencies

* Firefox (used 75.0+)
* geckodriver (used 0.26.0)
* Django 1.11.x
* Selenium 3.x
* [Bootstrap](https://getbootstrap.com/) 4.4.x
* Nginx 1.14.0
* Gunicorn 20.0.x
* Fabric3 1.14.post1
* [Qunit](https://qunitjs.com/) 2.9.2
* [jQuery](https://jquery.com/download/) 3.5.0

Coded in Python 3.6.x

> If setting up geckodriver 0.26.0 on macOS 10.15 (Catalina), [here is a step-by-step instruction](README.md#setting-up-geckodriver-on-macos-catalina).

# Run

### Local dev server

1. Run the server

    ```bash
    python manage.py runserver
    ```

2. Visit `http://localhost:8000`

3. To quit server, `CONTROL-C`

### Staging server

> [See provisioning notes](deploy_tools/provisioning_notes.md)

1. SSH onto a VM
2. cd into project directory
3. Run the server (Gunicorn config in Systemd service)

    ```bash
    sudo systemctl start nginx
    sudo systemctl start gunicorn-<staging server domain>
    ```

### Functional test

* Run all the tests locally:

    ```bash
    python manage.py test functional_tests
    ```

    > Run a specific test case, *e.g.*,
    > 
    > ```bash
    > python manage.py test functional_tests.test_list_item_validation
    > ```

* Run all the tests against staging server:

    ```bash
    STAGING_SERVER=<staging server domain> ./manage.py test functional_tests
    ```

    * optional: add `--failfast`

### Unit test

1. Run the test

    ```bash
    python manage.py test lists
    ```

2. For javascript test, enter the URL into the browser

    ```
    file://<path to project>/lists/static/tests/tests.html
    ```

# Deploy

1. Run fabfile.py (from a local shell)

    > If the server runs on Amazon EC2, add a path to the SSH key.

    ```bash
    cd deploy_tools/
    fab deploy:host=<username>@<server domain> [-i /path/to/key.pem]
    ```

2. Provision Nginx and Gunicorn (on the server)

    > Skip if not deploying for the first time

    Configure Nginx from template:

    ```bash
    cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/<server domain>/g" \
    | sudo tee /etc/nginx/sites-available/<server domain>
    ```

    Activate file with a symlink and delete default:

    ```bash
    sudo ln -s /etc/nginx/sites-available/<server domain> /etc/nginx/sites-enabled/<server domain>
    sudo rm /etc/nginx/sites-enabled/default
    ```

    Configure Systemd from template:
    
    ```bash
    cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/<server domain>/g" \
    | sudo tee /etc/systemd/system/gunicorn-<server domain>.service
    ```

3. Start the service (on the server)

    If deploying for the first time:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start nginx
    sudo systemctl enable gunicorn-<server domain>
    sudo systemctl start gunicorn-<server domain>
    ```

    Otherwise:

    ```bash
    sudo systemctl restart gunicorn-<server domain>
    ```

# Setting up geckodriver on macOS Catalina

This instruction is for users of geckodriver 0.26.0 on macOS 10.15 Catalina, which has a [known problem](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0) when downloaded from a browser like Firefox. Instead, use `wget` or `curl`.

1. Download the binary:

    ```bash
    cd /tmp
    curl -O -L https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz
    ```


2. Uncompress and unpack:

    ```bash
    tar -xvzf geckodriver-v0.26.0-macos.tar.gz
    ```


3. Move geckodriver to `/usr/local/bin` (requires `sudo`)

    ```bash
    sudo mv ./geckodriver /usr/local/bin/
    ```

4. Clean up (optional)

    ```bash
    rm geckodriver-v0.26.0-macos.tar.gz
    ```

---

*Test-Driven Development with Python*, 2nd edition, by Harry J.W. Percival (O’Reilly). Copyright 2017 Harry Percival, 978-1-491-95870-4.
