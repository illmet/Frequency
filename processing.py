import json
import os
import re
import requests
from datetime import datetime
#take the data from the json and store in the list format, everything stored as t
folder= 'data/posts'
t = []
for file in os.listdir(folder):
    if file.endswith('.json'):
        file_path = os.path.join(folder, file)
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        for item in data:
            content = item.get("content")
            if content is not None:
                t.append(content)
print(t[:10])
#function to remove emojis from individual strings
def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

#full processing pipeline for getting clean text
for i in range(len(t)):
    v1 = re.sub(r'http\S+', '', t[i], flags=re.MULTILINE)
    v2 = re.sub(r'(?:r|u|n)/\S+', '', v1) 
    v3 = re.sub(r'[^a-zA-Z0-9\s]', '', v2) #remove special characters
    v4 = re.sub(r'\s+', ' ', v3).strip()
    v5 = remove_emoji(v4)
    t[i] = v5
#full pipeline end with tokenisation
print(t[:10])
print(len(t))
    