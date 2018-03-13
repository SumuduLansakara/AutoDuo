import time


def dispatchKeyEvent(driver, name, options):
    options["type"] = name
    import json
    body = json.dumps({'cmd': 'Input.dispatchKeyEvent', 'params': options})
    resource = "/session/%s/chromium/send_command" % driver.session_id
    url = driver.command_executor._url + resource
    driver.command_executor._request('POST', url, body)


def hold_space(driver, duration):
    endtime = time.time() + duration
    options = {
        "code": "KeyW",
        "key": " ",
        "text": " ",
        "unmodifiedText": " ",
        "nativeVirtualKeyCode": ord(" "),
        "windowsVirtualKeyCode": ord(" ")
    }

    while True:
        dispatchKeyEvent(driver, "rawKeyDown", options)
        dispatchKeyEvent(driver, "char", options)

        if time.time() > endtime:
            dispatchKeyEvent(driver, "keyUp", options)
            break

        options["autoRepeat"] = True
        time.sleep(0.001)
