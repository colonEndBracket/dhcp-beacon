# dhcp-beacon
Script that sends an email containing the local ip addresses of the machine that runs it.

Intended for headless computers that run on networks that use DHCP and you do not own.

For example, if the DHCP lease on a raspberry pi expires, this script can be used as a cronjob to send an email with the new ip address(es) and you can SSH into the new address instead of hooking up a display and keyboard to the pi
