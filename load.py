"""
Plugin for "Bounty"
"""
import json
import urllib
import requests
import time

import Tkinter as tk
import myNotebook as nb
from config import config

from EDMCOverlay import edmcoverlay


TARGET_BOUNTY_VERSION = "0.0.1"
DEFAULT_OVERLAY_MESSAGE_DURATION = 10

PREFNAME_OVERLAY_DURATION = "BountyOverlayDuration"

OVERLAY_MESSAGE_DURATION = tk.StringVar(value=config.get(PREFNAME_OVERLAY_DURATION))
_overlay = None


def get_display_ttl():
    try:
        # return int(OVERLAY_MESSAGE_DURATION.get())
        return int(DEFAULT_OVERLAY_MESSAGE_DURATION.get())
    except:
        return DEFAULT_OVERLAY_MESSAGE_DURATION


def plugin_start():
    """
    Start up our EDMC Plugin
    :return:
    """
    global _overlay
    _overlay = edmcoverlay.Overlay()
    time.sleep(2)
    notify("ED:Target Bounty Plugin Loaded")

    if not OVERLAY_MESSAGE_DURATION.get():
        OVERLAY_MESSAGE_DURATION.set(str(DEFAULT_OVERLAY_MESSAGE_DURATION))
        config.set(PREFNAME_OVERLAY_DURATION, str(DEFAULT_OVERLAY_MESSAGE_DURATION))


def plugin_stop():
    """
    Edmc is going to exit.
    :return:
    """
    _overlay.send_raw({
        "command": "exit"
    })


HEADER = 380
INFO = 420
DETAIL1 = INFO + 25
DETAIL2 = DETAIL1 + 25
DETAIL3 = DETAIL2 + 25


def display(text, row=HEADER, col=80, color="yellow", size="large"):
    try:
        _overlay.send_message("bounty_{}_{}".format(row, col),
                              text,
                              color,
                              80, row, ttl=get_display_ttl(), size=size)
    except:
        pass


def header(text):
    display(text, row=HEADER, size="normal")


def notify(text):
    display(text, row=INFO, color="#00ff00", col=95)


def warn(text):
    display(text, row=INFO, color="red", col=95)


def info(line1, line2=None, line3=None):
    if line1:
        display(line1, row=DETAIL1, col=95, size="normal")
    if line2:
        display(line2, row=DETAIL2, col=95, size="normal")
    if line3:
        display(line3, row=DETAIL3, col=95, size="normal")


def pretty_number(bountyValue):
    readable = ""
    if bountyValue >= 10000000000:
        # Translators: this is a short representation for a bounty >= 10 000 000 000 credits (b stands for billion)
        readable = _(u"{} b").format(bountyValue / 1000000000)
    elif bountyValue >= 1000000000:
        # Translators: this is a short representation for a bounty >= 1 000 000 000 credits (b stands for billion)
        readable = _(u"{:.1f} b").format(bountyValue / 1000000000.0)
    elif bountyValue >= 10000000:
        # Translators: this is a short representation for a bounty >= 10 000 000 credits (m stands for million)
        readable = _(u"{} m").format(bountyValue / 1000000)
    elif bountyValue > 1000000:
        # Translators: this is a short representation for a bounty >= 1 000 000 credits (m stands for million)
        readable = _(u"{:.1f} m").format(bountyValue / 1000000.0)
    elif bountyValue >= 10000:
        # Translators: this is a short representation for a bounty >= 10 000 credits (k stands for kilo, i.e. thousand)
        readable = _(u"{} k").format(bountyValue / 1000)
    elif bountyValue >= 1000:
        # Translators: this is a short representation for a bounty >= 1000 credits (k stands for kilo, i.e. thousand)
        readable = _(u"{:.1f} k").format(bountyValue / 1000.0)
    else:
        # Translators: this is a short representation for a bounty < 1000 credits (i.e. shows the whole bounty, unabbreviated)
        readable = _(u"{}").format(bountyValue)
    return readable


def journal_entry(cmdr, system, station, entry, state):
    """
    Check a system for advice
    :param cmdr:
    :param system:
    :param station:
    :param entry:
    :param state:
    :return:
    """

    try:
        if entry["event"] in ["ShipTargeted"] and "TargetLocked" in entry and entry["TargetLocked"]:
            shipType = entry["Ship"]
            if "Ship_Localised" in entry:
                shipType = entry["Ship_Localised"]

            if "LegalStatus" in entry:
                pilotName = entry["PilotName"][len("$npc_name_decorate:#name="):-1]
                pilotRank = entry["PilotRank"]
                shieldHealth = entry["ShieldHealth"]
                legalStatus = entry["LegalStatus"]

                if "PilotName_Localised" in entry:
                    pilotName = entry["PilotName_Localised"]

                header("{} - {}, {}".format(pilotRank, shipType, pilotName))
                info(None, line2="Shield: {}".format(pretty_number(shieldHealth)))

                if entry["LegalStatus"] == "Wanted":
                    bountyValue = entry["Bounty"]
                    warn("Bounty: {}".format(pretty_number(bountyValue)))
                else:
                    notify("Status: {}".format(legalStatus))

    except Exception as err:
        info(None, line3="Error.. {} {}".format(type(err), err.message))


