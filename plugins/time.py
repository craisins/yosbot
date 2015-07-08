import re
import time

from util import hook, http

@hook.command("swatch")
@hook.command
def beats(inp):
        utc_time = time.gmtime()
        beats = int((utc_time.tm_sec+1 + (utc_time.tm_min+1)*60 + (utc_time.tm_hour+1)*3600) / 86.4)
        return "The Swatch Internet Time is " + str(beats) + ".beats! Fuck your time zones!"
