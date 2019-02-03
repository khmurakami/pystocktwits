from pystocktwits import Streamer

import json

"""
Description and param's are from the documentation at stocktwits API

Returns the most recent 30 messages for the specified user. Includes user object in response.

param user_id (int) = User ID or Username of the stream's user you want to show (Required)
param since (int) = Returns results with an ID greater than (more recent than) the specified ID.
param max (int) = Returns results with an ID less than (older than) or equal to the specified ID.
param limit (int) = Default and max limit is 30. This limit must be a number under 30.
param callback = Define your own callback function name, add this parameter as the value.
param filter (string) = Filter messages by links, charts, or videos. (Optional)

return (dict) = raw json
"""

#Create a Twit Streamer
twit = Streamer()

#Get Msgs from User 170
test1 = twit.get_user_msgs("170")

#Pass in all parameters to query search
test2 = twit.get_user_msgs(user_id = "180", since = 0, max = 30, limit = 30, callback = None, filter = "links")

print(test2)

"""
Sample Output of Test 2

{u'cursor': {u'max': None, u'since': None, u'more': False}, u'messages': [], u'response': {u'status': 200}, u'user': {u'username': u'StockTwits', u'name': u'StockTwits', u'classification': [u'suggested', u'official'], u'official': True, u'like_count': 49146, u'ideas': 74259, u'following': 10000, u'join_date': u'2009-08-31', u'avatar_url': u'https://avatars.stocktwits.com/production/170/thumb-1537898606.png', u'followers': 490006, u'watchlist_stocks_count': 17, u'avatar_url_ssl': u'https://avatars.stocktwits.com/production/170/thumb-1537898606.png', u'id': 170, u'identity': u'Official'}}
"""
