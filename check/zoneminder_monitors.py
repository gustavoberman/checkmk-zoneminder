from .agent_based_api.v1 import *

#This file goes into your Checkmk site 'check plugins' directory (local/lib/check_mk/base/plugins/agent_based)

def discover_zoneminder_monitors(section):
    for monID, _name, _status, _cfps, _afps, _cb in section:
        yield Service(item=monID)

def check_zoneminder_monitors(item, section):
    for monID, name, status, cfps, afps, cb in section:
        if monID == item:
            if status != "Connected":
                s = State.CRIT
            else:
                s = State.OK
            yield Result(state=s, summary=f"Monitor {monID}, {name} is {status}")
            return

register.check_plugin(
    name="zoneminder_monitors",
    service_name="Zoneminder Monitor %s Status",
    discovery_function=discover_zoneminder_monitors,
    check_function=check_zoneminder_monitors,
)
