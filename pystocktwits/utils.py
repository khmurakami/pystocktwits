# Helper functions placed here for now

from pystocktwits import Streamer

import requests
import json
import csv
import pandas as pd
import numpy



def get_all_msgs_with_sentiment_by_user(raw_json):
    test = raw_json['messages']['entities']['sentiment']
    return test


#def get_all_msgs_with_sentiment_by_symbol(raw_json):

#def json_to_csv(raw_json, output_path):

#def json_to_dataframe(raw_json):


if __name__ == '__main__':
    twit = Streamer()
    output = twit.get_user_msgs("170")
    print(get_all_msgs_with_sentiment_by_user(output))
