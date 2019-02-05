## pystocktwits

This is a Python 3.xx API Wrapper for PyStock Twits. This sadly doesn't include most of the API methods as they require a access token which redirect you to a uri which you can get around with a flask app, but I didn't want to develop on that part as it wasn't really needed for data

Also this API doesn't include bullish or bearish statements unless you sign up for the Partner level access. To get Partner level access to get such statements in your query you need to sign up go to <https://api.stocktwits.com/developers/contact> and sign up for a developers account.

This was mainly made to just parse for the sentiment in messages. The other functionality was not really needed.

## Requirements

Also listed in requirements.txt:

-   requests

## Install

#### Install Locally

This was only tested in Python 3.6

```shell
$ python3 setup.py install
```
#### Install inside a virtualenv
```shell
$ pip3 install virtualenv
$ python3 -m virutalenv env
$ source env/bin/activate
$ python3 setup.py install
```
## Using the Python Wrapper


Descriptions of files can be found inside pystocktwits.py

Get Messages from a User/User.id
```python
from pystocktwits import Streamer

twit = Streamer()

# Get User Messages by ID
print(twit.get_user_msgs("170", since=0, max=1, limit=1))


# Returns a Dictionary
output = twit.get_user_msgs("170", since=0, max=1, limit=1))
print(output['response']['status'])

# Output  = 200 if the call went through sucessfully
```
Response:
```json
{'response': {'status': 200}, 'user': {'id': 170, 'username': 'StockTwits', 'name': 'StockTwits', 'avatar_url': 'https://avatars.stocktwits.com/production/170/thumb-1537898606.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/170/thumb-1537898606.png', 'join_date': '2009-08-31', 'official': True, 'identity': 'Official', 'classification': ['suggested', 'official'], 'followers': 490004, 'following': 10000, 'ideas': 74259, 'watchlist_stocks_count': 17, 'like_count': 49146}, 'cursor': {'more': True, 'since': 152520810, 'max': 152520810}, 'messages': [{'id': 152520810, 'body': 'The rise of podcasts... $SPOT', 'created_at': '2019-02-02T00:10:26Z', 'user': {'id': 170, 'username': 'StockTwits', 'name': 'StockTwits', 'avatar_url': 'https://avatars.stocktwits.com/production/170/thumb-1537898606.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/170/thumb-1537898606.png', 'join_date': '2009-08-31', 'official': True, 'identity': 'Official', 'classification': ['suggested', 'official'], 'followers': 490004, 'following': 10000, 'ideas': 74259, 'watchlist_stocks_count': 17, 'like_count': 49146}, 'source': {'id': 2269, 'title': 'StockTwits Web', 'url': 'https://stocktwits.com'}, 'symbols': [{'id': 9076, 'symbol': 'SPOT', 'title': 'Spotify Technology S.A.', 'aliases': ['SPTF', 'SPOTIFY'], 'is_following': False, 'watchlist_count': 17405}], 'likes': {'total': 2, 'user_ids': [31814, 1325989]}, 'reshare_message': {'reshared_count': 1, 'reshared_deleted': False, 'reshared_user_deleted': False, 'parent_reshared_deleted': False, 'message': {'id': 152520718, 'body': 'Spotify is in talks to buy podcast startup Gimlet - Recode ... probably smart $spot https://www.recode.net/2019/2/1/18207198/spotify-gimlet-podcast-acquisition', 'created_at': '2019-02-02T00:08:45Z', 'user': {'id': 5, 'username': 'howardlindzon', 'name': 'Howard Lindzon', 'avatar_url': 'https://avatars.stocktwits.com/production/5/thumb-1503096790.png', 'avatar_url_ssl': 'https://avatars.stocktwits.com/production/5/thumb-1503096790.png', 'join_date': '2009-07-11', 'official': True, 'identity': 'Official', 'classification': ['suggested', 'official'], 'followers': 221231, 'following': 1689, 'ideas': 147145, 'watchlist_stocks_count': 137, 'like_count': 67007}, 'source': {'id': 1149, 'title': 'StockTwits for iOS', 'url': 'http://www.stocktwits.com/mobile'}, 'symbols': [{'id': 9076, 'symbol': 'SPOT', 'title': 'Spotify Technology S.A.', 'aliases': ['SPTF', 'SPOTIFY'], 'is_following': False, 'watchlist_count': 17405}], 'conversation': {'parent_message_id': 152520718, 'in_reply_to_message_id': None, 'parent': True, 'replies': 1}, 'links': [{'title': "Spotify is in talks to buy Gimlet. That's a big deal for the podcasting world.", 'url': 'https://www.recode.net/2019/2/1/18207198/spotify-gimlet-podcast-acquisition', 'shortened_url': 'https://www.recode.net/2019/2/1/18207198/spotify-gimlet-podcast-acquisition', 'shortened_expanded_url': 'recode.net/2019/2/1/1820719...', 'description': 'Spotify, which has been trying to branch out of the streaming music business, is getting ready to make its first big move into podcasting: It plans to buy Gimlet Media, the startup behind popular shows like Reply All.', 'image': 'https://cdn.vox-cdn.com/uploads/chorus_image/image/62977145/Gwyneth_Paltrow.0.jpg', 'created_at': '2019-02-02T00:08:45Z', 'video_url': None, 'source': {'name': 'Recode', 'website': 'https://www.recode.net'}}], 'likes': {'total': 3, 'user_ids': [170, 1325989, 1629492]}, 'mentioned_users': [], 'entities': {'sentiment': None}}}, 'mentioned_users': [], 'entities': {'sentiment': None}}]}
```

## Samples

Code samples can be found in example_code in "tests"

## Testing using Unit Tests

Run test script to test if it works properly

```shell
$ python unit_test/pystocktwits_test.py
```

## Using Curl Requests to Test

These curl requests are from the Stocktwits API site and are not mine. They can be found here: <https://api.stocktwits.com/developers/docs>

```
$ cd example_curl_requests
$ ./streams_user_curl.sh
```

## TODO

- Clean up example code
- Figure out how the callback part works in the functions when making the web call.
- Create Flask App for the redirect uri
- Clean up README.md
- Make better Unit Tests
- Fix __init__.py 
