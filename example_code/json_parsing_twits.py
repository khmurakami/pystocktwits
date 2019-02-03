from pystocktwits import Streamer
import json

twit = Streamer()
output = twit.get_user_msgs("170")
print(output['response']['status'])
