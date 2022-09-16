# checkmk-zoneminder
A Checkmk plugin to get Zoneminder Monitor status

Disclaimer: 
I'm a monkey with a keyboard while coding. 
I'm a sysadmin, not a developer.
I'm sure this is not the best way to do it.

I needed something to warn me when a Zoneminder monitor was in error
This plugin will use the Zoneminder API to get the list of monitors and their status.
I followed https://docs.checkmk.com/latest/en/devel_check_plugins.html the best I could.

Copy plugin/zoneminder_monitors.py into a host's plugin directory.
Copy agent/zoneminder_plugin.py into the checkmk agent_based directory.

Remember to modify plugin/zoneminder_monitors.py with your Zoneminder url/user/pass
