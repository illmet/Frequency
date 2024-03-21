import requests
from datetime import datetime
#take the data from the json and store in the list format, everything stored as t
t = "text"
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
    v2 = re.sub(r'r/\S+', '', v1)
    v3 = re.sub(r'u/\S+', '', v2)
    v4 = re.sub(r'n/\S+', '', v3)
    v5 = remove_emoji(v4)
    t[i] = v5
#full pipeline end with tokenisation
    