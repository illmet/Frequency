import json
import os
import re

def clean_text(string):
    string = re.sub(r'http\S+', '', string, flags=re.MULTILINE)
    string = re.sub(r'(?:r|u|n)/\S+', '', string) 
    string = re.sub(r'[^a-zA-Z0-9\s.,\']', '', string)
    string = re.sub(r'\s+', ' ', string).strip()
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002500-\U00002BEF"
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
                               u"\ufe0f"
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def process_data(folder, id):
    texts = []
    for file in os.listdir(folder):
        if file.endswith('.json'):
            file_path = os.path.join(folder, file)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
            for item in data:
                content = item.get(id)
                if content:
                    texts.append(clean_text(content))
    combined_text = ' '.join(texts)
    return combined_text

def process_data_to_list(folder, id):
    texts = []
    for file in os.listdir(folder):
        if file.endswith('.json'):
            file_path = os.path.join(folder, file)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
            for item in data:
                content = item.get(id)
                if content:
                    texts.append(clean_text(content))
    print(f"Processing complete. Total posts and comments {len(texts)}")
    return texts
