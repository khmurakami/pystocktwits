from pystocktwits import Streamer

import json

#Create a Twit Streamer
twit = Streamer()

#Get Msgs from User 170
output = twit.get_user_msgs("170")

#Get Status Code through nested dict
print(output['response']['status'])

"""
Sample Output

200

"""
