import os.path
from datetime import datetime,timedelta

import praw

backup_subreddit_name = os.environ.get("BACKUP_SUBREDDIT_NAME")
backup_file_ids = []

def backup():

    bot_name = os.environ.get("REDDIT_USER_NAME")  # 账号名称
    password = os.environ.get("REDDIT_PASSWORD")  # 账号密码
    client_id = os.environ.get("CLIENT_ID")  # 账号密码
    client_secret = os.environ.get("CLIENT_SECRET")  # 账号密码
    print(f"{backup_subreddit_name},{client_id}")


    user_agent = "autoreply bot created by u/Chinese_Dictator."  # 这一项可以随意填写
    reddit = praw.Reddit(client_id=client_id,
                              client_secret=client_secret,
                              user_agent=user_agent,
                              username=bot_name,
                              password=password)
    backup_subreddit =  reddit.subreddit(backup_subreddit_name)
    now = datetime.utcnow()
    one_hour_ago = now - timedelta(hours=1)
    # 获取新贴文
    for submission in backup_subreddit.new(limit=None):
        # post_time = datetime.utcfromtimestamp(submission.created_utc)
        # if post_time > one_hour_ago:
        backup_post(submission)
        # else:
        #     break
def get_post_content(submission):
    content = '''
OP: u/{author}  
原始地址: {url}  
正文:  
{content}
'''
    content = content.replace("{author}",f"{submission.author}")
    content = content.replace("{url}", submission.permalink)
    content = content.replace("{content}", submission.selftext)
    return content

def get_post_title(submission):
    title = submission.title.replace("\\", " ")
    title = title.replace("/", " ")
    return f"{submission.id}_{title}"

def check_is_backup(submission):
    if submission.id not in backup_file_ids:
        return False
    return True
def init_backup_file_ids():
    global backup_file_ids
    if not os.path.isdir(backup_subreddit_name):
        os.mkdir(backup_subreddit_name)
    ids = []
    for root, dirs, files in os.walk(backup_subreddit_name):
        for file in files:
            ids.append(file.split("_")[0])
    backup_file_ids = ids

def backup_post(submission):
    if check_is_backup(submission):
       return
    title = get_post_title(submission)
    body = get_post_content(submission)
    with open(f"{backup_subreddit_name}/{title}.md", "w",encoding="utf-8") as f:
        f.write(body)



if __name__ == "__main__":
    init_backup_file_ids()
    backup()
