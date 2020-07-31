# AutoDuo

A program that automatically does Duolingo exercises. 

This currently does only the `basic-1` lesson of Duolingo `German` (in English) course.

## Setting up

### Downloading web-drivers

Selenium web-driver files are not provided with the source package (as they are continuously being updated by the respective browser developers).
Required web-drivers need to be added manually to make the program work.

AutoDuo currently supports following web-drivers.
 - [Chrome-driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Download required web driver(s) and put them inside `drivers` directory.

> Optionally, you can use the provided downloader script in `tools` directory.
> This downloads the latest chrome-driver.
> However, if you are using an old chrome browser, you might need to manually download a compatible chrome-driver.

Final project hierarchy should be as follows.
 - AutoDuo
	 + drivers
		 + [web driver file(s)]
	 + src
		 + [python source files]
	 - README.md
	 - LICENSE

## Installing required python modules

> It is recommended to use `pipenv` for installing required python modules.

Invoke following command from inside the project root directory to install all the requirements.

    pipenv install

## Usage
AutoDuo main script must be invoked with providing a valid Duolingo user-email and password as command-line arguments.

    python3 main.py

