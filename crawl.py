import os
import praw #install this
from praw.models import MoreComments
from datetime import datetime, timedelta
import json
import requests

###CONFIG
#the time period for the scraping
#CHANGE THESE TO BE UNIX EPOCHS FROM THE START
campaign_end = int(datetime(2020, 11, 3).timestamp()) #election day
campaign_start = int(datetime(2020, 8, 18).timestamp()) #biden nomination by dnc
print(f"End: {campaign_end}")
print(f"Start: {campaign_start}")

#enviroments for connecting to reddit 
ci = os.getenv('cireddit')
cs = os.getenv('csreddit')
ua = os.getenv('uareddit')
#subsets of subreddits
subs = ["Politics", "uspolitics"]
#for the enviroment variables
reddit = praw.Reddit(
    client_id=ci,
    client_secret=cs,
    user_agent=ua
)
#dir
output_dir = "data"
#separate lists for titles, posts and comments
titles = []
posts = []
comments = []
#comment counter, but I had it in the wrong place
#comm = 1
#+++limit the number of posts
###SCRAPE
def scrape_reddit_json(subreddit):
    n = 0
    fullposts = []
    #fullcomms = []
    for p in reddit.subreddit(subreddit).search('"Biden" OR "Trump"', time_filter="all"):
    #for p in reddit.subreddit(subreddit).new(limit=10):
        time = p.created_utc
        g = int(p.created_utc)
        print(time)
        if campaign_start <= g <= campaign_end:
            fullposts.append({
                "id": p.id,
                "title": p.title,
                "content": p.selftext,
                "upvotes": p.score,
                "author": str(p.author) if p.author else None,
                "flair": p.link_flair_text,
                "subreddit": str(p.subreddit),
                "date": time
            })
            
            #p.comments.replace_more(limit=10)
            #for comment in p.comments.list():
                #fullcomms.append({
                    #"body": comment.body,
                    #"upvotes": comment.score,
                    #"author": str(comment.author) if comment.author else None,
                    #"date": datetime.fromtimestamp(comment.created_utc),
                    #"parent_id": comment.parent_id
                #})
            
            #full.append(info)
            print(f"Post {n} crawled")
            n+=1
    return fullposts
###FILE SAVE
for sub in subs:
    info = scrape_reddit_json(sub)
    #print(info)
    filename = f"{sub}.json"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        json.dump(info, f, indent=4) 

#refactored txt file writing method (optional, obsolete)
#def scrape_reddit_txt():
    #with open(file_name, "w") as f:
        #for post in reddit.subreddit(subreddit).submissions(campaign_start.timestamp(), campaign_end.timestamp()):
            #f.write("Post title: " + post.title + "\n")
            #f.write("Post content: " + post.selftext + "\n\n")
            #for comment in post.comments:
                #if isinstance(comment, MoreComments):
                    #continue
                #if len(comment.body) < 1024:
                    #f.write("Comment " + str(comm) + ": " + comment.body + "\n")