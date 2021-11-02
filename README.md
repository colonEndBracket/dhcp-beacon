# dhcp-beacon

## About

Script that sends an email containing the local ip addresses of the machine that runs it.

Intended for headless computers that run on networks that use DHCP and you do not own.

For example, if the DHCP lease on a raspberry pi expires, this script can be used as a cronjob to send an email with the new ip address(es) and you can SSH into the new address instead of hooking up a display and keyboard to the pi

## Requirements

This python script requires the `netifaces` module. This can be installed with python's pip package manager:

```py
python3 -m pip install netifaces
```

## Usage

### Setting Credentials

Create a file named `creds.py` containing your credentials like so:

```py
str_username = ""
str_password = ""
list_recipients = ["someuser@examplemail.com"]
```

* `str_username` and `str_password` are the username and password of the email account you want to use to send emails with.

* `list_recipients` is a list of the email addresses of those who want to receive emails from the dhcp beacon.

### Automating the Script (Run Script at Boot)

On Linux systems with Cron installed, you can have your system automatically run this script using cronjobs.

Add the following to the `/etc/crontab` file, substituting `username` with your username
to have the script run when your computer reboots. This assumes you've cloned `dhcp-beacon`
to your `home` directory

`@reboot username /usr/bin/python3 /home/username/dhcp-beacon/beacon.py`

