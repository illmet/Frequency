import os
import praw #install this
from praw.models import MoreComments
from datetime import datetime, timedelta
import json
import requests
import time

###CONFIG
#the time period for the scraping
campaign_end = int(datetime(2020, 11, 3).timestamp()) #election day
campaign_start = int(datetime(2020, 8, 18).timestamp()) #biden nomination by dnc
#print(f"End: {campaign_end}")
#print(f"Start: {campaign_start}")

#enviroments for connecting to reddit 
ci = os.getenv('cireddit')
cs = os.getenv('csreddit')
ua = os.getenv('uareddit')
#subsets of subreddits
subs = ["Politics", "uspolitics", "Conservative", "Liberal", "trump", "joebiden", "Libertarian", "DemocraticSocialism"]
#for the enviroment variables
reddit = praw.Reddit(
    client_id=ci,
    client_secret=cs,
    user_agent=ua
)
#dir
output = "data"
postsdir = os.path.join(output, "posts")
commsdir = os.path.join(output, "comments")
#+++limit the number of posts

###SCRAPE
def scrape_reddit_json(subreddit):
    n = 0
    fullposts = []
    fullcomms = []
    #for now, only gets the mention of either Biden or Trump in the specified period (or any other single word)
    for p in reddit.subreddit(subreddit).search('Election Biden Trump', sort='top', syntax='lucene', time_filter='all', limit=100):
        post_time = int(p.created_utc)
        #print(post_time)
        if (campaign_start <= post_time <= campaign_end) and (p.selftext != "") and (p.selftext != "[removed]") and (p.selftext != "[deleted]") and (len(p.selftext) < 4999):
            fullposts.append({
                "id": p.id,
                "title": p.title,
                "content": p.selftext,
                "upvotes": p.score,
                "author": str(p.author) if p.author else None,
                "flair": p.link_flair_text,
                "subreddit": str(p.subreddit),
                "date": post_time
            })
            
            p.comments.replace_more(limit=25)
            for comment in p.comments.list():
                fullcomms.append({
                    "body": comment.body,
                    "upvotes": comment.score,
                    "author": str(comment.author) if comment.author else None,
                    "date": datetime.fromtimestamp(comment.created_utc).isoformat(),
                    "post_id": p.id,
                    "parent_id": comment.parent_id
                })
            
            #full.append(info)
            print(f"Post {n} crawled")
            n+=1
            time.sleep(0.01)
    return fullposts, fullcomms
    
###FILE SAVE
all_posts = []
all_comms = []

for sub in subs:
    posts, comms = scrape_reddit_json(sub)
    all_posts.extend(posts)
    all_comms.extend(comms)

#save posts
pathpost = os.path.join(postsdir, f"posts.json")
with open(pathpost, 'w') as f:
    json.dump(all_posts, f, indent=4) 
#save comments
pathcomm = os.path.join(commsdir, f"comments.json")
with open(pathcomm, 'w') as f:
    json.dump(all_comms, f, indent=4)


#refactored txt file writing method (optional, obsolete), do not uncomment, do not delete! thanks.
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