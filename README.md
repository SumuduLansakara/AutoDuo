# AutoDuo

## Setting up

### Downloading web-drivers

Selenium web-driver files are not provided with the source package (as they are continuously being updated by the respective browser developers). Required web-drivers need to be added manually to make the program work.

The program is tested with only the following web-drivers.
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
### Updating user credentials
Valid Duolingo username/email and password must be defined in `settings.py` file inside `src` directory.

Corresponding entries will look as follows.

    email = "<Duolingo user email address>"
    password = "<Duoling user password>"

## Installing required python modules

> It is recommended to used a python virtual-environment for installing
> required python modules without installing them system-wide

Required python modules are listed in `requirements.txt`. 

Invoke following command from inside the project root directory to install all the requirements.

    pip install -r requirements.txt

