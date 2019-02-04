from pystocktwits import Streamer

import requests
import json
import csv
import pandas as pd
import numpy

# Helper functions placed here for nowself.
# Need to optimize later once I figure out better programming

#Return only a msg
def get_most_recent_msg_by_user(user_id):
    twit = Streamer()
    raw_json = twit.get_user_msgs("100")
    recent_msg = raw_json['messages'][0]['body']
    return recent_msg

#Return only a msg
def get_most_recent_msg_by_symbol_id(symbol_id):
    twit = Streamer()
    raw_json = twit.get_symbol_msgs(symbol_id)
    recent_msg = raw_json['messages'][0]['body']
    return recent_msg

#Return only sentiment
def get_most_recent_sentiment_by_user(user_id):
    twit = Streamer()
    raw_json = twit.get_user_msgs(user_id)
    recent_sentiment = raw_json['messages'][0]['entities']
    return recent_sentiment

#Return only sentiment
def get_most_recent_sentiment_by_symbol_id(symbol_id):
    twit = Streamer()
    raw_json = twit.get_symbol_msgs(symbol_id)
    recent_sentiment =  raw_json['messages'][0]['entities']
    return recent_sentiment

#Return a dict with msg to senitment
def get_all_msgs_with_sentiment_by_symbol_id(symbol_id):
    msgs = []
    sentiment = []
    twit = Streamer()
    raw_json = twit.get_symbol_msgs(symbol_id = symbol_id, limit=2)
    messages_data = raw_json['messages']
    for message in messages_data:
        msgs.append(message.get("body"))
        sentiment.append(message.get("entities"))
    sentiment_dict = {msgs[i]: sentiment[i] for i in range(len(msgs))}
    return sentiment_dict

#Return a dict with msg to sentiment
def get_all_msgs_with_sentiment_by_user_id(user_id):
    msgs = []
    sentiment = []
    twit = Streamer()
    raw_json = twit.get_user_msgs(user_id = user_id, limit=1)
    messages_data = raw_json['messages']
    for message in messages_data:
        msgs.append(message.get("body"))
        sentiment.append(message.get("entities"))
    sentiment_dict = {msgs[i]: sentiment[i] for i in range(len(msgs))}
    return sentiment_dict

#Using this for temp use
def dict_to_dataframe(dict):
    dataframe = pd.DataFrame(dict)
    return dataframe

#Using this for temp use. Got it from here https://stackoverflow.com/questions/8685809/writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value
def dict_to_csv(dict, download_path):
    with open('{}'.format(download_path)) as csv_file:
        reader = csv.reader(csv_file)
        mydict = dict(reader)

def dataframe_to_csv(dataframe, download_path):
    dataframe.to_csv('{}'.format(download_path), index=False, header=False)

if __name__ == '__main__':
    twit = Streamer()
    #print(get_most_recent_msg_by_user("1190"))
    #print(get_most_recent_sentiment_by_user("190"))
    #print(get_most_recent_msg_by_symbol_id("AMZN"))
    #print(get_most_recent_sentiment_by_symbol_id("AMZN"))
    #output = twit.get_user_msgs("1190")
    #print(get_all_msgs_with_sentiment_by_user("190"))
    output = get_all_msgs_with_sentiment_by_symbol_id("AMZN")
    test = dict_to_dataframe(output)
    print(test)
    #dataframe_to_csv(test, 'test.csv')
