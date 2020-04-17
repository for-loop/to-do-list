# Table of Contents
1. [Dependencies](README.md#dependencies)
* [Run](README.md#run)
* [Setting up geckodriver on macOS Catalina](README.md#setting-up-geckodriver-on-macos-catalina)

# Dependencies

* Firefox (used 75.0+)
* geckodriver (used 0.26.0*)
* Django 1.11.x
* Selenium 3.x

Coded in Python 3.6.x

*If setting up geckodriver 0.26.0 on macOS 10.15 (Catalina), [here is a step-by-step instruction](README.md#setting-up-geckodriver-on-macos-catalina)

# Run

### Functional test

1. Start up the server:

    ```bash
    $ python manage.py runserver
    ```


2. Run the tests from another shell:

    ```bash
    $ python functional_tests.py
    ```
### Unit test

1. Run the test

    ```bash
    $ python manage.py test
    ```

# Setting up geckodriver on macOS Catalina

This instruction is for users of geckodriver 0.26.0 on macOS 10.15 Catalina, which has a [known problem](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0) when downloaded from a browser like Firefox. Instead, use `wget` or `curl`.

1. Download the binary:

    ```bash
    $ cd /tmp
    $ curl -O -L https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz
    ```


2. Uncompress and unpack:

    ```bash
    $ tar -xvzf geckodriver-v0.26.0-macos.tar.gz
    ```


3. Move geckodriver to `/usr/local/bin` (requires `sudo`)

    ```bash
    $ sudo mv ./geckodriver /usr/local/bin/.
    ```

4. Clean up (optional)

    ```bash
    $ rm geckodriver-v0.26.0-macos.tar.gz
    ```

---

*Test-Driven Development with Python*, 2nd edition, by Harry J.W. Percival (O’Reilly). Copyright 2017 Harry Percival, 978-1-491-95870-4.
