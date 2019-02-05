from pystocktwits import Streamer

import json

#Create a Twit Streamer
twit = Streamer()

#Pass in all parameters to query search
output = twit.get_specified_conversation_msgs(conversation_id = "102919", since = 0, max = 30, limit = 30, callback = None, filter = "links")

print(output)
