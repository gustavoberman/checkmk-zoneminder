#!/bin/python

import requests
import json

#This file goes into your host plugin dir (/usr/lib/check_mk_agent/plugins)
#Remember to change to your Zoneminder FQDN and you user/pass for accessing ZM API

req = requests.post("https://CHANGE_ME/zm/api/host/login.json", data={'user': 'CHANGE_ME', 'pass': 'CHANGE_ME'})
token_obtained = req.json()['access_token']
token_url_suffix = "?token="+token_obtained 
req = requests.request("get", "https://CHANGE_ME/zm/api/monitors.json" + token_url_suffix, data=None, cookies=None)

response=json.loads(req.text)
monitors=response.get("monitors")

print("<<<zoneminder_monitors>>>")
for monitor in monitors:
    monitorDef = monitor.get("Monitor")
    monitorID = monitorDef["Id"]
    monitorNameOrig = monitorDef["Name"]
    monitorName = monitorNameOrig.replace(' ', '_')

    statusDef = monitor.get("Monitor_Status")
    monitorStatus=statusDef["Status"]
    monitorCFPS=statusDef["CaptureFPS"]
    monitorAFPS=statusDef["AnalysisFPS"]
    monitorCB=statusDef["CaptureBandwidth"]

    print("{} {} {} {} {} {}".format(monitorID,monitorName,monitorStatus,monitorCFPS,monitorAFPS,monitorCB))
    
