#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits import Streamer
from pystocktwits.utils import *

# Create a Twit Streamer
twit = Streamer()

# Pass in all parameters to query search
raw_json = twit.get_symbol_msgs(user_id="APPL", since=0, max=30,
                                limit=30, callback=None, filter="links")

return_json_file(raw_json, "../sample_json_output/get_symbol_msgs.json")

print(raw_json)
