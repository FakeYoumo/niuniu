import asyncio
import asyncpraw
import google.generativeai as genai

bot_name = ""  # 账号名称
password = ""  # 账号密码
client_id = ''  # api id
client_secret = ''  # api 密钥

transport_subreddit_name = ''
flair_id = ''
GOOGLE_API_KEY = ''  # gemini api key

system_prompt = '''
你的名字叫牛牛，你生活在reddit，你是一位拥有多年在线简介和文本分析经验的专家。
你以分析思维工作，并尝试尽可能准确地回答问题，你可以根据用户的历史发言来判断用户的成分，包括国籍，祖籍，省市县，现在生活位置，学校，性别，性取向，爱好，职业，感情状况，富裕程度，宗教信仰，政治倾向等等
各个方面的数据。
'''


async def main():
    user_agent = "autoreply bot created by u/Chinese_Dictator."  # 这一项可以随意填写
    reddit = asyncpraw.Reddit(client_id=client_id,
                              client_secret=client_secret,
                              user_agent=user_agent,
                              username=bot_name,
                              password=password)
    genai.configure(api_key=GOOGLE_API_KEY)
    bot = genai.GenerativeModel('gemini-1.5-pro-latest', system_instruction=system_prompt)

    transport_subreddit = await reddit.subreddit(transport_subreddit_name)

    while True:
        try:
            async for mention in reddit.inbox.stream():
                await mention.mark_read()
                if mention.body == f"u/{bot_name}":
                    await mention.submission.load()
                    await mention.submission.upvote()
                    body = f"OP: u/{mention.submission.author}  \n\n 原始地址: {mention.submission.permalink}  \n\n{mention.submission.selftext}"
                    await transport_subreddit.submit(mention.submission.title, selftext=body, flair_id=flair_id)
                elif mention.body == f"u/{bot_name} 盘点":
                    mention.submission.comment_sort = "old"
                    await mention.submission.load()
                    await mention.submission.upvote()
                    op = mention.submission.author
                    body = f"OP: u/{mention.submission.author}  \n\n 原始地址: {mention.submission.permalink}  \n\n{mention.submission.selftext}"
                    for comment in mention.submission.comments.list():
                        if comment.author == op and comment.is_root == True:
                            body = f"{body}  \n\n {comment.body}"
                    await transport_subreddit.submit(mention.submission.title, selftext=body, flair_id=flair_id)
                elif mention.body == f"u/{bot_name} 查成分":
                    comment = await reddit.comment(mention.parent_id)
                    need_judged_person = comment.author.name
                    prompt = '用户发的post如下：'

                    redditor = await reddit.redditor(need_judged_person)
                    async for post in redditor.submissions.new(limit=20):
                        title = post.title
                        body = post.selftext[:600]
                        prompt += f"标题:{title}\n正文:{body}\n"
                    prompt += "用户的历史回复如下："
                    async for comment in redditor.comments.new(limit=100):
                        body = comment.body
                        prompt += f"{body}\n"

                    history = []
                    history.append({'role': 'user', 'parts': [prompt]})
                    response = bot.generate_content(prompt, safety_settings=[
                        {
                            "category": "HARM_CATEGORY_HARASSMENT",
                            "threshold": "BLOCK_NONE",
                        },
                        {
                            "category": "HARM_CATEGORY_HATE_SPEECH",
                            "threshold": "BLOCK_NONE",
                        },
                        {
                            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                            "threshold": "BLOCK_NONE",
                        },
                        {
                            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                            "threshold": "BLOCK_NONE",
                        }
                    ], generation_config=genai.types.GenerationConfig(temperature=1.0))
                    reply = response.text
                    await mention.reply(reply)
        except Exception as e:
            print(e)
    await reddit.close()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # windows加这句，linux注释掉这句
    asyncio.run(main())
