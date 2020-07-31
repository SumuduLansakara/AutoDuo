#!/usr/bin/env bash

cd "$(dirname "$0")/.." || exit

if ! type pipenv &>/dev/null; then
    echo "pipenv is not installed"
    exit 1
fi

pipenv install
./tools/download_chrome_driver.sh

echo "Setup complete !"
echo
echo "Run following in project root directory"
echo "  pipenv run python3 main.py"
