#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits import Streamer

# Create a Twit Streamer
twit = Streamer()

# Get Msgs from User 170
raw_json = twit.get_user_msgs("170")

# Get Status Code through nested dict
print(output['response']['status'])
