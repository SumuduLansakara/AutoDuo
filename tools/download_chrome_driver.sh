#!/usr/bin/env bash

# get latest driver version
version_url="https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
driver_version="$(curl -s "$version_url")"
echo "Latest chrome web-driver version: [$driver_version]"

# go to driver directory
driver_dir="$(dirname "$0")/../drivers"
mkdir -p "${driver_dir}"
cd "${driver_dir}"

# download web driver
driver_url="https://chromedriver.storage.googleapis.com/${driver_version}/chromedriver_linux64.zip"
curl -s "$driver_url" --output 'driver.zip'
unzip -q 'driver.zip'
rm 'driver.zip'
