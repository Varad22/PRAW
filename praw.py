"""Importing Libraries"""
import praw
from transformers import pipeline
import re

"""Defining Pipeline"""

#steps to find client_id and client_secret are mentioned here: https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
sentiment_pipeline = pipeline("sentiment-analysis")
reddit = praw.Reddit(
    client_id="",   #enter your client_id
    client_secret="",   #enter your client_secret
    user_agent="",   #enter your user_agent
)

print(reddit.read_only)

import pandas as pd
# Create sub-reddit instance
subreddit_name = "clinicaltrials"
subreddit = reddit.subreddit(subreddit_name)

# creating lists for storing scraped data
titles=[]
scores=[]
ids=[]
urls = []

# looping over posts and scraping it
for submission in subreddit.top(limit=21):
    titles.append(submission.title)
    scores.append(submission.score) #upvotes
    ids.append(submission.id)
    urls.append("https://www.reddit.com/r/"+subreddit_name+'/comments/'+str(submission.id)+"/"+str(submission.title).replace(" ","_")+"/")

#extracting comments and authors
comments={}
for i in urls:
  submission = reddit.submission(url=i)
  top_level_comments = list(submission.comments)
  all_comments = submission.comments.replace_more()
  for comment in submission.comments:
    res1 = " ".join(re.findall("[a-zA-Z0-9.,!;]+", comment.body))
    if res1.count('.')>1:
      res1 = res1.split('.')
      comments[comment.author]=res1
    else:
      comments[comment.author]=[res1]
print(comments)

#creating a table for comments and analyzing author's sentiments
df = pd.DataFrame()
authors=[]
comments_lst=[]
sentiments=[]
for i in comments:
  for j in comments[i]:
    authors.append(str(i))
    comments_lst.append(str(j))
    sentiments.append(str(sentiment_pipeline(j)[0]['label']))

df['Author'] = authors
df['Comment'] = comments_lst
df['Sentiment'] = sentiments
df

#generating personalized message for authors who are interested
for i in range(len(df)):
  if df['Sentiment'][i]=="POSITIVE":
    message = "Hello "+str(df['Author'][i])+" ! Your interest in staying informed about healthcare options is admirable. Participating in a clinical trial might provide access to treatments not yet available to the public. If you're interested, I'm here to guide you through the process and address any questions you may have."
    print(message)

