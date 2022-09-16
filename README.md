# checkmk-zoneminder
A Checkmk plugin to get Zoneminder Monitor status

## About:
I needed something to warn me when a Zoneminder monitor was in error.

This plugin will use the Zoneminder API to get the list of monitors and their status. 

That means you need to enable Zoneminder API.

I followed https://docs.checkmk.com/latest/en/devel_check_plugins.html the best I could.

## Disclaimer: 
While coding, I'm a monkey with a keyboard. 

I'm a sysadmin, not a developer.

I'm sure this is not the best way to do it.


## Usage:
Copy plugin/zoneminder_monitors.py into a host's plugin directory.

Copy check/zoneminder_monitors.py into the checkmk check plugins directory.

Remember to modify plugin/zoneminder_monitors.py with your Zoneminder url/user/pass
