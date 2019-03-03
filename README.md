## pystocktwits
[![Build Status](https://travis-ci.com/khmurakami/pystocktwits.svg?branch=master)](https://travis-ci.com/khmurakami/pystocktwits)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub All Releases](https://img.shields.io/github/downloads/khmurakami/pystocktwits/total.svg)
[![HitCount](http://hits.dwyl.com/khmurakami/pystocktwits.svg)](http://hits.dwyl.com/khmurakami/pystocktwits)

This is a Python Client for Stock Twits.

This sadly doesn't include most of the API methods as they require a access token which redirect you to a uri which you can get around with a flask app, but I didn't want to develop on that part as it wasn't really needed for data.

This was mainly made to just parse for the sentiment in messages. The other functionality was not really needed.

## Requirements

Also listed in requirements.txt:

-   requests

## Install

#### Install Locally

This was only tested in Python 3.6

```shell
$ git clone https://github.com/khmurakami/pystocktwits
$ cd pystocktwits
$ python setup.py install
```

#### Install inside a virtualenv

```shell
$ pip3 install virtualenv
$ python3 -m virutalenv env
$ source env/bin/activate
$ git clone https://github.com/khmurakami/pystocktwits
$ cd pystocktwits
$ python3 setup.py install
```

## Using the Python Wrapper

Descriptions of files can be found inside pystocktwits.py

Get Messages from a User/User.id

```python
from pystocktwits import Streamer

twit = Streamer()

# Get User Messages by ID
raw_json = twit.get_user_msgs("170", since=0, max=1, limit=1))

return_json_file(raw_json, 'result.json')
```

Response (This JSON was shortened because it was too long):

```json

{
    "cursor": {
        "max": 2607768,
        "more": false,
        "since": 14895004
    },
    "messages": [
        {
            "body": "$wbmd",
            "created_at": "2013-07-31T14:37:02Z",
            "entities": {
                "sentiment": null
            },
            "id": 14895004,
            "mentioned_users": [],
            "source": {
                "id": 1,
                "title": "StockTwits",
                "url": "http://stocktwits.com"
            },
            "symbols": [
                {
                    "aliases": [],
                    "id": 4077,
                    "is_following": false,
                    "symbol": "WBMD",
                    "title": "WebMD Health Corp.",
                    "watchlist_count": 476
                }
            ],
            "user": {
                "avatar_url": "https://avatars.stocktwits.com/production/180/thumb-1271178935.png",
                "avatar_url_ssl": "https://avatars.stocktwits.com/production/180/thumb-1271178935.png",
                "classification": [],
                "followers": 5,
                "following": 8,
                "id": 180,
                "ideas": 5,
                "identity": "User",
                "join_date": "2009-09-01",
                "like_count": 0,
                "name": "Martin Bourgeois",
                "official": false,
                "username": "montrealrocket",
                "watchlist_stocks_count": 1
            }
        },
        {
            "body": "$yhoo",
            "created_at": "2013-02-26T18:43:16Z",
            "entities": {
                "sentiment": null
            }
        }
      ]
  }
```

Get Messages from a Company/Symbol.id

```python
from pystocktwits import Streamer

twit = Streamer()

# Get User Messages by ID
raw_json = twit.get_symbol_msgs(symbol_id="AAPL", since=0, max=0, limit=30, callback=None, filter=None)

# Return raw json as JSON file
return_json_file(raw_json, 'result.json')
```


Response (This JSON was shortened because it was too long):

```json
"cursor": {
    "max": 155604916,
    "more": true,
    "since": 155614013
},
"messages": [
    {
        "body": "@sonicmerlin short term $SPY will oscillate around her NAV from momentum &amp; FOMO. But over a few quarters SPY will follow $MSFT $AAPL $AMZN",
        "conversation": {
            "in_reply_to_message_id": 155613895,
            "parent": false,
            "parent_message_id": 155613408,
            "replies": 5
        },
        "created_at": "2019-03-03T05:38:09Z",
        "entities": {
            "sentiment": null
        },
        "id": 155614013,
        "mentioned_users": [
            "@sonicmerlin"
        ],
        "source": {
            "id": 2095,
            "title": "StockTwits For Android ",
            "url": "http://www.stocktwits.com/mobile"
        },

    }
]

```

## Samples

Code samples can be found in example_code/python_scripts
JSON sample outputs can be found in example_code/sample_json_output

## Testing using Unit Tests

Run test script to test if it works properly

```shell
$ python tests/pystocktwits_test.py
```

## Using Curl Requests to Test

These curl requests are from the Stocktwits API site and are not mine. They can be found here: <https://api.stocktwits.com/developers/docs>

```shell
$ cd example_curl_requests
$ ./streams_user_curl.sh
```

## TODO

- Figure out how the callback part works in the functions when making the web call.
- Create Flask App for the redirect uri
- Clean up README.md
- Fix __init__.py

## Links/Credits

- Git Ignore Used in this Repo: https://github.com/github/gitignore/blob/master/Python.gitignore
- Stocktwits Official Site: https://stocktwits.com/
- Stocktwits Developer Sign Up: https://api.stocktwits.com/developers/contact
- Stocktwits Official APU Documentation: https://api.stocktwits.com/developers/docs
