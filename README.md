[![License](https://img.shields.io/github/license/SumuduLansakara/AutoDuo)](https://github.com/SumuduLansakara/AutoDuo/blob/master/LICENSE)
[![Python version](https://img.shields.io/github/pipenv/locked/python-version/sumudulansakara/AutoDuo)](https://www.python.org/)
[![Selenium version](https://img.shields.io/github/pipenv/locked/dependency-version/SumuduLansakara/AutoDuo/selenium)](https://www.selenium.dev/)
[![Stars](https://img.shields.io/github/stars/SumuduLansakara/AutoDuo?style=social)](https://github.com/SumuduLansakara/AutoDuo/stargazers)

# AutoDuo

An attempt to automatically perform [Duolingo](https://www.duolingo.com/) exercises via browser automation.

## Setting up

### Requirements
- python 3.7
- selenium web-drivers

### Downloading Web-drivers

Selenium web-drivers need to be downloaded manually.
They are not provided with the source package as they are continuously being updated by the respective browser developers.

AutoDuo currently supports following web-drivers.
 - [Chrome-driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Download required web driver(s) and put them inside `drivers` directory.

> Provided downloader script in `tools` directory downloads the latest chrome-driver.
> However, if you are using an old chrome browser, you might have to manually download a compatible chrome-driver.

Final project hierarchy should be as follows.
```
AutoDuo (repository root directory)
├── drivers
│   └── chromedriver
├── tools
│   └── ...
├── LICENSE
├── README.md
└── ...
```

## Installing Required Python Modules

> It is recommended to use [`pipenv`](https://pypi.org/project/pipenv/) for installing required python modules.

Invoke following command from inside the project root directory to install all the requirements.

    pipenv install

## Usage
AutoDuo main script must be invoked with providing a valid Duolingo user-email and password as command-line arguments.

    pipenv run python3 main.py

In the very first run, you have to manually log into your Duolingo account.
This is not necessary in subsequent runs.

## ToDo

- Add support to play more levels (currently plays only the first level)
- Improve translations
- Support different web drivers

## Known Bugs and Workarounds

- The program can crash before starting a lesson. Ignore this and re-run.