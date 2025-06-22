import os 
from dotenv import load_dotenv
import praw
import re 
import time
import ai_backend

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD")
)
subreddit_name = 'TestingGroundBot'
subreddit = reddit.subreddit(subreddit_name)

def get_posts(subreddit):
    while True:
        try:
            for submission in subreddit.stream.submissions(skip_existing=True):
                title = submission.title 
                body = submission.selftext or ""

                NEET_POST_APPROVE = ai_backend.Moderate_Sub(title, body)
                if NEET_POST_APPROVE == 'no':
                     print(f"Flagging for mod review: {submission.id}")
                     submission.report("Off-topic for r/NEET (Indian exam content).")
                     submission.mod.flair(text="🚧 Under Mod Review. Suspected as Indian NEET exam post")
                     submission.mod.remove()

                else:
                     print('NEET post')

                     

        except (praw.exceptions.PRAWException, 
                praw.exceptions.APIException, 
                praw.exceptions.ClientException) as e:
                print(f"An error occurred: {e}")
                time.sleep(10)
                continue 
            
# def accept_mod_invite():
#     reddit.subreddit(subreddit_name).mod.accept_invite()


# def filter_posts():
#      print("🔍 Monitoring modqueue…")
#      while True:
#           try:
#                for submisstestbotsubreddition in subreddit.mod.stream.modqueue(skip_existing=True):
#                     print(f'Mod Queue title {submission.title}')
#                     print(f'Mod Queue Items {submission.selftext}')
#           except:
#                print('Error')

get_posts(subreddit)              
               