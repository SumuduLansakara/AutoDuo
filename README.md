# AutoDuo

A program that automatically does Duolingo exercises. 

This currently does only the `basic-1` lesson of Duolingo `German` (in English) course.

## Setting up

### Downloading web-drivers

Selenium web-driver files are not provided with the source package (as they are continuously being updated by the respective browser developers). Required web-drivers need to be added manually to make the program work.

AutoDuo currently supports following web-drivers.
 - [Chrome-driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
 - [Firefox-driver (geckodriver)](https://github.com/mozilla/geckodriver/releases)

Simply, download required web driver(s) and put them inside `drivers` directory.

Final project hierarchy should look as follows.
 - AutoDuo
	 + drivers
		 + [web driver file(s)]
	 + src
		 + [python source files]
	 + venv [optional python virtual environment]
	 - requirements.txt
	 - README.md
	 - LICENSE

## Installing required python modules

> It is recommended to use a python virtual-environment for installing
> required python modules without installing them system-wide

Required python modules are listed in `requirements.txt`. 

Invoke following command from inside the project root directory to install all the requirements.

    pip install -r requirements.txt

## Usage
AutoDuo main script must be invoked with providing a valid Duolingo user-email and password as command-line arguments.

    python main.py -e <user_email> -p <password>

