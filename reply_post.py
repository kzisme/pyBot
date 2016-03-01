import praw
import pdb
import re
import os
from config_bot import *

if not os.path.isfile("config_bot.py"):
    print "You must create a config file for user + pass"
    exit(1)

user_agent = ("PyFor Eng bot 0.1")
r = praw.Reddit(user_agent = user_agent)

r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning = True)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

subreddit = r.get_subreddit('EDC')
for submission in subreddit.get_new(limit = 25):

    if submission.id not in posts_replied_to:

        submission.add_comment("""I see you have made a new post!
        Please make sure you have added a list of items pictured""")

        posts_replied_to.append(submission.id)
        print "Bot replying to : ", submission.title

        # Store the current id into our list
        posts_replied_to.append(submission.id)
# Using "a" to append to .txt as opposed to "w" write
with open("posts_replied_to.txt", "a") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
