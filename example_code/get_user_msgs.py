from pystocktwits import Streamer

import json

#Create a Twit Streamer
twit = Streamer()

#Pass in all parameters to query search
output = twit.get_user_msgs(user_id = "180", since = 0, max = 30, limit = 30, callback = None, filter = "links")

print(output)

"""
Sample Output

{u'cursor': {u'max': None, u'since': None, u'more': False}, u'messages': [], u'response': {u'status': 200}, u'user': {u'username': u'StockTwits', u'name': u'StockTwits', u'classification': [u'suggested', u'official'], u'official': True, u'like_count': 49146, u'ideas': 74259, u'following': 10000, u'join_date': u'2009-08-31', u'avatar_url': u'https://avatars.stocktwits.com/production/170/thumb-1537898606.png', u'followers': 490006, u'watchlist_stocks_count': 17, u'avatar_url_ssl': u'https://avatars.stocktwits.com/production/170/thumb-1537898606.png', u'id': 170, u'identity': u'Official'}}
"""
