#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits import Streamer
from pystocktwits.utils import *

# Create a Twit Streamer
twit = Streamer()

# Pass in all parameters to query search
raw_json = twit.get_specified_conversation_msgs(conversation_id="10349526", since=1, max=30, limit=30, callback=None)

# Return the raw_json as a JSON file
return_json_file(raw_json,
                 "../sample_json_output/get_specified_conversation_msgs.json")

print(raw_json)
