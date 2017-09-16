# mybot.py
# Author: MelBrooksKA (Daniel Tweedy)
# Simple bot that replies with links to GIFs of Kazuma Kiryu from Yakuza
# to popular phases he's said, i.e. "That's rad" will be replied to with
# a link to a GIF zooming in on Kiryu saying "that's rad"
#

import praw
import os

radGif="i0.kym-cdn.com/photos/images/original/001/239/018/19d.gif"

bot = praw.Reddit(user_agent=os.environ["USER_AGENT"],
                  client_id=os.environ["CLIENT_ID"],
                  client_secret=os.environ["CLIENT_SECRET"],
                  username=os.environ["USERNAME"],
                  password=os.environ["USER_PASSWORD"])

subreddit = bot.subreddit('TwoBestFriendsPlay')
comments = subreddit.stream.comments()

print("[That's rad!]({0})".format(radGif))

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if 'that\'s rad' in text.lower():
        # Generate a message
        message = "[That's rad!]({0})".format(radGif)

        comment.reply(message)
